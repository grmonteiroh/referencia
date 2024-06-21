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

**Equação de Decaimento:**
![a](https://latex.codecogs.com/svg.image?{\color{White}S_t=S_{t-1}\cdot&space;e^{-\lambda\Delta&space;t}&plus;\epsilon_t})

onde:
   - ![a](https://latex.codecogs.com/svg.image?{\color{White}S_t}) é o saldo no tempo 
   - λ é a taxa de decaimento.
   - Δt é o intervalo de tempo (número de dias úteis).
   - ϵt é o termo de erro (ruído estocástico).

A taxa de decaimento λ pode ser ajustada considerando a sensibilidade às taxas de juros e outros fatores macroeconômicos:

![a](https://latex.codecogs.com/svg.image?{\color{White}\lambda=\alpha&plus;\beta\cdot(r_{CDB}-r_{poupanca})&plus;\gamma\cdot&space;X_t})

onde:

�
α é um termo constante.
�
β representa a sensibilidade dos saldos à diferença de taxas de juros entre CDB e poupança.
�
�
�
�
r 
CDB
​
  é a taxa de juros do CDB.
�
�
�
�
�
�
�
�
\c
�
r 
poupan 
c
\c
​
 a
​
  é a taxa de juros da poupança.
�
γ são os coeficientes de sensibilidade a outras variáveis macroeconômicas 
�
�
X 
t
​
 .
   
3. **Resultados Esperados**:
   - Resultados antecipados e como eles serão medidos.
   - Impacto esperado e possíveis aplicações.

4. **Conclusão**:
   - Resumo dos principais pontos discutidos.
   - Considerações finais e próximos passos.

### Equações Matemáticas

Neste projeto, utilizamos várias equações matemáticas para modelar e resolver o problema proposto.

#### Equação de Exemplo 1

A primeira equação utilizada é a equação quadrática, que é expressa como:

![Equação Quadrática](https://latex.codecogs.com/png.latex?ax^2%20+%20bx%20+%20c%20=%200)

onde:
- \(a\), \(b\), e \(c\) são coeficientes constantes.
- \(x\) representa as variáveis.

#### Equação de Exemplo 2

Outra equação importante é a fórmula da área de um círculo, dada por:

\[ A = \pi r^2 \]

onde:
- \(A\) é a área do círculo.
- \(\pi\) é uma constante aproximadamente igual a 3.14159.
- \(r\) é o raio do círculo.
