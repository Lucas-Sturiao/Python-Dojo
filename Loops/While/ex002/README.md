# Sistema de Segurança com Break

## 📝 Enunciado
Desenvolva um script que simule a validação de segurança de um sistema com limite de tentativas, utilizando obrigatoriamente a instrução de interrupção de laço.

**Configurações:**
*   **PIN correto:** `"9999"`
*   **Limite de tentativas:** `5`

**Regras:**
1. O programa deve utilizar um laço `while` para gerenciar as tentativas.
2. A cada tentativa incorreta, o contador deve ser atualizado.
3. Se o usuário acertar o PIN, o programa deve exibir `"Acesso liberado"` e parar imediatamente utilizando o comando `break`.
4. Se o limite de 5 tentativas for atingido sem sucesso, o programa deve exibir `"Acesso bloqueado"`.

## 🎯 Objetivo
Entender o funcionamento da instrução `break` para interromper fluxos de repetição de forma imediata quando uma condição específica é atendida.
* **Categoria:** Lógica de Programação.
* **Nível:** Iniciante.

## 🛠️ Tecnologias e Conceitos
* **Controle de Fluxo:** Laço `while`.
* **Interrupção de Fluxo:** Comando `break`.
* **Entrada de Dados:** Função `input()`.
* **Contadores:** Gerenciamento de tentativas restantes.
* **Lógica Condicional:** Estrutura `if/else` para validação do PIN.