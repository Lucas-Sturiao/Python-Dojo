# Contagem de Produtos em Estoque

## 📝 Enunciado
Dada a seguinte lista de dicionários representando o inventário de uma loja:

```python
produtos = [
    {"nome": "Teclado", "estoque": 10},
    {"nome": "Mouse",   "estoque": 0},
    {"nome": "Monitor", "estoque": 5},
    {"nome": "Cabo",    "estoque": 0}
]
```

Desenvolva uma função que siga estas especificações:
1.  **Nome da Função:** `contar_produtos_disponiveis(lista)`.
2.  **Lógica de Filtragem:** A função deve percorrer a lista de produtos.
3.  **Uso de `continue`:** Se o produto tiver estoque igual a 0, utilize o comando `continue` para pular para o próximo item.
4.  **Contagem:** Incremente um contador apenas para os produtos que possuem estoque maior que 0.
5.  **Retorno:** A função deve retornar o total de produtos disponíveis.

## 🎯 Objetivo
Praticar a manipulação de listas de dicionários e o uso do comando `continue` para simplificar a lógica de filtragem dentro de uma função.
* **Categoria:** Lógica de Programação / Funções.
* **Nível:** Iniciante / Intermediário.

## 🛠️ Tecnologias e Conceitos
* **Dicionários:** Acesso a valores por chaves (`produto["estoque"]`).
* **Controle de Fluxo:** Uso de `continue` para desvio de execução.
* **Modularização:** Criação de funções com parâmetros e retorno.
* **Operadores Relacionais:** Verificação de disponibilidade (`> 0`).