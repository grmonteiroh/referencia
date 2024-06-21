# Curva de Decaimento

## Introdução

Este modelo visa calcular a curva de decaimento dos saldos de contas e poupanças de pessoas físicas (PF) e jurídicas (PJ), considerando os saques realizados. A abordagem utilizada baseia-se em métodos de autorregressão e incorpora a sensibilidade dos depósitos às taxas de juros.
   
## Metodologia
1. **Coleta e Limpeza de Dados**

   Os dados foram coletados e organizados nas seguintes colunas:
   - Data: Data da transação.
   - Número da Conta: Identificador da conta.
   - Saldo: Saldo atual da conta.
   - Saldo Anterior: Saldo da conta no dia anterior.
   - Diferença: Variação no saldo (Saldo Atual - Saldo Anterior).
   - Filtramos os dados para incluir apenas linhas com diferença negativa, representando os saques realizados.

2. **Definição de Saldos Estáveis e Não Estáveis**
   
   - Saldos Estáveis: Parte do saldo que permanece constante ou apresenta pouca variação.
   - Saldos Não Estáveis: Parte do saldo que é suscetível a grandes variações devido a saques.
   - Saldos Core: Fração dos saldos estáveis que representam um fundo estável e de longo prazo.
   - Saldos Não Core: Fração dos saldos que não se enquadram na categoria core.
  
3. **Modelagem do Decaimento**

      Para modelar o decaimento dos saldos, consideramos a equação de decaimento discreta e autorregressiva, incorporando a sensibilidade às taxas de juros.

### Equação de Decaimento:
![a](https://latex.codecogs.com/svg.image?{\color{White}S_t=S_{t-1}\cdot&space;e^{-\lambda\Delta&space;t}&plus;\epsilon_t})

Onde:
   - ![a](https://latex.codecogs.com/svg.image?{\color{White}S_t}) é o saldo no tempo 
   - λ é a taxa de decaimento.
   - Δt é o intervalo de tempo (número de dias úteis).
   - ϵt é o termo de erro (ruído estocástico).

A taxa de decaimento λ pode ser ajustada considerando a sensibilidade às taxas de juros e outros fatores macroeconômicos:

![a](https://latex.codecogs.com/svg.image?{\color{White}\lambda=\alpha&plus;\beta\cdot(r_{CDB}-r_{poupanca})&plus;\gamma\cdot&space;X_t})

Onde:
   - α é um termo constante.
   - β representa a sensibilidade dos saldos à diferença de taxas de juros entre CDB e poupança.
   - rCDB é a taxa de juros do CDB.
   - rpoupanca é a taxa de juros da poupança.
   - γ são os coeficientes de sensibilidade a outras variáveis macroeconômicas Xt.
   
## Implementação
**Passo 1: Coleta dos Dados:** Os dados históricos de saldos e transações foram coletados e organizados. Os saques foram filtrados para análise.

**Passo 2: Estimativa de Parâmetros:** Utilizamos técnicas econométricas para estimar os parâmetros α, β e γ. Modelos de regressão linear e séries temporais são aplicados para entender a relação entre os saques e as variáveis macroeconômicas.

**Passo 3: Simulação do Decaimento:** Com os parâmetros estimados, simulamos a curva de decaimento dos saldos ao longo de um período específico. Utilizamos métodos de Monte Carlo para incorporar o termo de erro ϵt e obter diferentes trajetórias possíveis dos saldos.

## Resultados Esperados
Os resultados incluem uma curva de decaimento que mostra a porcentagem de saldo restante ao longo do tempo. Essa curva pode ser utilizada para prever o comportamento dos saldos sob diferentes cenários de taxas de juros e condições macroeconômicas.

## Conclusão
Este modelo oferece uma abordagem quantitativa robusta para analisar o decaimento dos saldos de contas e poupanças. A inclusão de variáveis macroeconômicas e a sensibilidade às taxas de juros permite uma compreensão detalhada dos fatores que influenciam os saques e o comportamento dos depositantes.
