import pandas as pd
import trino
from concurrent.futures import ThreadPoolExecutor

# Configurações do Trino
DB_CONFIG = {
    "host": "seu_host",
    "port": 8080,  # Porta padrão do Trino
    "user": "seu_usuario",
    "catalog": "seu_catalogo",
    "schema": "seu_esquema"
}

# Número de threads (não exagere, pois o Trino já paraleliza consultas)
NUM_THREADS = 4  # Ajuste dependendo da carga do servidor

# Função para obter a lista de contas a serem monitoradas
def obter_contas():
    conn = trino.dbapi.connect(
        host=DB_CONFIG["host"],
        port=DB_CONFIG["port"],
        user=DB_CONFIG["user"],
        catalog=DB_CONFIG["catalog"],
        schema=DB_CONFIG["schema"]
    )
    cursor = conn.cursor()
    query = "SELECT conta FROM contas_monitoradas"
    cursor.execute(query)
    contas = [row[0] for row in cursor.fetchall()]
    conn.close()
    return contas

# Consulta SQL para um subconjunto de contas
def consulta_saldo(contas):
    conn = trino.dbapi.connect(
        host=DB_CONFIG["host"],
        port=DB_CONFIG["port"],
        user=DB_CONFIG["user"],
        catalog=DB_CONFIG["catalog"],
        schema=DB_CONFIG["schema"]
    )
    cursor = conn.cursor()

    # Criando um filtro para as contas deste lote
    contas_str = ",".join([f"'{conta}'" for conta in contas])
    
    query = f"""
    WITH saldos_filtrados AS (
        SELECT 
            conta, 
            data, 
            saldo, 
            MIN(data) FILTER (WHERE saldo = 0) 
                OVER (PARTITION BY conta) AS primeira_vez_zero
        FROM transacoes
        WHERE data BETWEEN DATE '2022-01-01' AND DATE '2024-12-31'
          AND conta IN ({contas_str})
    )
    SELECT conta, data, saldo
    FROM saldos_filtrados
    WHERE data <= primeira_vez_zero OR primeira_vez_zero IS NULL
    ORDER BY conta, data;
    """

    cursor.execute(query)
    df = pd.DataFrame(cursor.fetchall(), columns=["conta", "data", "saldo"])
    conn.close()
    return df

# Função para dividir a lista de contas em partes menores
def dividir_lista(lista, n):
    """Divide a lista de contas em n partes aproximadamente iguais."""
    tamanho = len(lista) // n + (len(lista) % n > 0)
    return [lista[i * tamanho:(i + 1) * tamanho] for i in range(n)]

# Rodar consultas em paralelo
def rodar_consultas():
    contas = obter_contas()
    blocos = dividir_lista(contas, NUM_THREADS)

    with ThreadPoolExecutor(max_workers=NUM_THREADS) as executor:
        resultados = list(executor.map(consulta_saldo, blocos))

    # Concatenar os resultados
    df_final = pd.concat(resultados, ignore_index=True)
    return df_final

# Executar e exibir os resultados
df_resultado = rodar_consultas()
import ace_tools as tools
tools.display_dataframe_to_user(name="Saldos Filtrados", dataframe=df_resultado)
