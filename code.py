import pandas as pd
import numpy as np
from statsmodels.tsa.ar_model import AutoReg
import matplotlib.pyplot as plt

# Supondo que os dados estejam em um DataFrame chamado `df`
df = pd.read_csv('dados.csv')

# Filtrando diferenças negativas
df_negative = df[df['diferença'] < 0]

# Calculando o desvio padrão dos saldos por conta
saldo_std = df_negative.groupby('numero da conta')['saldo'].std()

# Definindo limiar para saldo estável (core) e instável (non-core)
limiar_estavel = saldo_std.median()

# Classificando contas
df_negative['categoria'] = df_negative['numero da conta'].apply(lambda x: 'core' if saldo_std[x] < limiar_estavel else 'non-core')

# Modelo de autorregressão com mudança na taxa de juros
df_negative['delta_taxa_juros'] = df_negative['taxa_juros'].diff()

# Separando os dados em treino e teste
treino = df_negative[df_negative['data'] < '2023-01-01']
teste = df_negative[df_negative['data'] >= '2023-01-01']

# Ajustando o modelo
model = AutoReg(treino['saldo'], lags=1, exog=treino[['delta_taxa_juros']])
model_fit = model.fit()

# Previsão
previsao = model_fit.predict(start=len(treino), end=len(treino)+len(teste)-1, exog_oos=teste[['delta_taxa_juros']])

plt.figure(figsize=(12, 6))
plt.plot(treino['data'], treino['saldo'], label='Treino')
plt.plot(teste['data'], teste['saldo'], label='Teste')
plt.plot(teste['data'], previsao, label='Previsão', linestyle='--')
plt.xlabel('Data')
plt.ylabel('Saldo')
plt.legend()
plt.show()
