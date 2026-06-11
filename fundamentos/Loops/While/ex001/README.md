# 🧩 Tentativas de Acesso

## 📝 Enunciado
Desenvolva um sistema de validação de segurança que simule o acesso de um usuário por meio de um PIN. O código deve seguir estas especificações:

**Configurações Iniciais:**
*   PIN correto: `"4321"`
*   Limite de tentativas: `3`

**Regras de Negócio:**
1. Use uma estrutura de repetição para solicitar o PIN ao usuário enquanto ele ainda tiver tentativas disponíveis.
2. Se o usuário digitar o PIN correto:
    *   Exiba: `"Acesso liberado"`
    *   Encerre a execução.
3. Se o usuário digitar o PIN incorreto:
    *   Diminua o número de tentativas restantes.
4. Caso as tentativas cheguem a zero sem o acerto:
    *   Exiba: `"Acesso bloqueado"`

**Restrição Técnica:** O desafio deve ser resolvido obrigatoriamente usando `while`, `if/else` e variáveis de controle, sem o uso de `for`.

## 🎯 Objetivo
Praticar o controle de fluxo com laços de repetição baseados em condições dinâmicas e gerenciamento de estado de variáveis.
* **Categoria:** Lógica de Programação.
* **Nível:** Iniciante / Intermediário.

## 🛠️ Tecnologias e Conceitos
* **Controle de Fluxo:** Laço `while` para repetições indeterminadas.
* **Entrada de Dados:** Função `input()` para interação com o usuário.
* **Lógica Condicional:** Verificação de igualdade e controle de parada (`break` ou flag).
* **Variáveis de Controle:** Decremento de contadores para limite de tentativas.