# Refinamento com Continue

## 📝 Enunciado
Reescreva a lógica de validação de usuários do `ex003`, focando em um código mais limpo e utilizando desvios de fluxo para ignorar dados irrelevantes.

Dada a lista de usuários:
```python
usuarios = [
    {"nome": "Lucas", "ativo": True,  "idade": 25},
    {"nome": "Ana",   "ativo": False, "idade": 30},
    {"nome": "João",  "ativo": True,  "idade": 17},
    {"nome": "Maria", "ativo": True,  "idade": 40}
]
```

**Regras da função:**
1.  **Nome:** Mantenha o nome `contar_usuarios_validos(lista)`.
2.  **Uso de `continue`:** Utilize o comando `continue` para pular imediatamente os usuários que:
    *   **Não** estão ativos.
    *   Possuem idade **menor** que 18 anos.
3.  **Estrutura Clean:** Não utilize a cláusula `else`. O incremento do contador deve acontecer naturalmente após as verificações de `continue`.
4.  **Retorno único:** Utilize o `return` apenas uma vez, ao final da função, para retornar a quantidade total.

## 🎯 Objetivo
Praticar o padrão de projeto "Guard Clauses" (Cláusulas de Guarda), onde as condições inválidas são tratadas primeiro para manter o fluxo principal do código mais limpo e legível.
* **Categoria:** Lógica de Programação / Refatoração.
* **Nível:** Intermediário.

## 🛠️ Tecnologias e Conceitos
* **Cláusulas de Guarda:** Uso de `if` com `continue` para eliminar casos indesejados precocemente.
* **Lógica Negativa:** Verificação de condições de exclusão (`not ativo`, `idade < 18`).
* **Sintaxe Pythonica:** Redução de indentação aninhada ao evitar o uso de `else`.
* **Acumulação Limpa:** Incremento de variáveis em um fluxo linear.