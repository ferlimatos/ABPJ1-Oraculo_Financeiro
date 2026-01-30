# Oráculo Financeiro

## Descrição do projeto
O **Oráculo Financeiro** é uma aplicação em Python desenvolvida para auxiliar no planejamento financeiro doméstico. O programa permite que o usuário registre sua renda mensal e categorize seus principais gastos (água, energia, aluguel e cartão), fornecendo um diagnóstico sobre a saúde financeira do mês.

## Como começar a usar
1.  **Pré-requisitos:** Certifique-se de ter o **Python 3.x** instalado.
2.  **Instalação:**
    * Faça o download ou clone este repositório.
    * Navegue até a pasta do projeto.
4.  **Execução:**
    * No terminal, execute: `python main.py`

## Lógica e Variáveis
O sistema utiliza as seguintes variáveis para o processamento:
| Variável | Descrição | Tipo de Dado |
| :--- | :--- | :--- |
| `renda_mensal` | Salário ou ganhos totais do mês | `float` |
| `total_agua` | Gasto com fatura de água | `float` |
| `total_energia` | Gasto com fatura de luz | `float` |
| `total_aluguel` | Valor fixo de moradia | `float` |
| `total_cartao` | Despesas variadas no crédito | `float` |
| `gastos_total` | A soma de todas as despesas acima | `float` |
| `saldo_final` | O que sobra após o pagamento das contas | `float` |

### Fórmulas de Processamento:
* **Cálculo de Despesas:** `gastos_total = total_agua + total_energia + total_aluguel + total_cartao`
* **Cálculo de Saldo:** `saldo_final = renda_mensal - gastos_total`

### Regras de Decisão:
* **Se** `saldo_final >= 0`: Exibir que o orçamento está positivo.
* **Se** `saldo_final < 0`: Exibir alerta de orçamento estourado.

### Regras de Decisão (Fluxo Lógico):
1. O programa recebe as entradas via teclado.
2. Realiza a soma das despesas e a subtração da renda.
3. **Se** `saldo_final >= 0`: Exibe mensagem de saldo positivo.
4. **Se** `saldo_final < 0`: Exibe alerta de saldo negativo.

[Fluxograma](https://www.canva.com/design/DAG_2O8ZvsE/4rQsAB8IlXAzr6dTXcYrwQ/edit?utm_content=DAG_2O8ZvsE&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton)

## Ajuda e Contribuições
Para obter ajuda, abra uma *Issue* neste repositório.

**Mantido por:** Fernanda Matos

