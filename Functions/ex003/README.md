# Função com Dicionários

## 📝 Enunciado
Simule o processamento de dados de uma API que retorna uma lista de usuários. O objetivo é criar uma lógica de filtragem para validar quais usuários estão aptos a acessar um serviço.

Dada a seguinte lista:
```python
usuarios = [
    {"nome": "Lucas", "ativo": True,  "idade": 25},
    {"nome": "Ana",   "ativo": False, "idade": 30},
    {"nome": "João",  "ativo": True,  "idade": 17},
    {"nome": "Maria", "ativo": True,  "idade": 40}
]
```

**Regras da função:**
1.  **Nome:** A função deve se chamar `contar_usuarios_validos(lista)`.
2.  **Filtros:** Conte apenas os usuários que atenderem a **ambos** os critérios:
    *   Estar ativo (`"ativo": True`).
    *   Ter idade maior ou igual a 18 anos (`"idade" >= 18`).
3.  **Retorno:** A função deve retornar o número total (inteiro) de usuários que passaram nos filtros.

## 🎯 Objetivo
Praticar a manipulação de estruturas de dados compostas (listas de dicionários) e a aplicação de lógica booleana dentro de funções.
* **Categoria:** Lógica de Programação / Manipulação de Dados.
* **Nível:** Intermediário (Nível API).

## 🛠️ Tecnologias e Conceitos
* **Dicionários:** Acesso a chaves específicas (`user["ativo"]`, `user["idade"]`).
* **Funções com Parâmetros:** Passagem de listas para processamento modular.
* **Operadores Lógicos:** Uso de `and` para combinar múltiplas condições de filtragem.
* **Contadores:** Variável de incremento para armazenar a quantidade de itens válidos.
* **Retorno de Função:** Uso do `return` para disponibilizar o resultado do processamento.