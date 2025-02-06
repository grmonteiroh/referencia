WITH saldos_filtrados AS (
    SELECT 
        conta, 
        data, 
        saldo, 
        MIN(CASE WHEN saldo = 0 THEN data END) 
            OVER (PARTITION BY conta) AS primeira_vez_zero
    FROM transacoes
    WHERE data BETWEEN '@start_date' AND '@end_date'
      AND conta IN ('@lista_contas')
)
SELECT conta, data, saldo
FROM saldos_filtrados
WHERE data <= primeira_vez_zero OR primeira_vez_zero IS NULL
ORDER BY conta, data;

---
WITH saldos_filtrados AS (
    SELECT 
        conta, 
        data, 
        saldo, 
        MIN(data) FILTER (WHERE saldo = 0) 
            OVER (PARTITION BY conta) AS primeira_vez_zero
    FROM transacoes
    WHERE data BETWEEN DATE '@start_date' AND DATE '@end_date'
      AND conta IN ('@lista_contas')
)
SELECT conta, data, saldo
FROM saldos_filtrados
WHERE data <= primeira_vez_zero OR primeira_vez_zero IS NULL
ORDER BY conta, data;
