# Processamento Interrompido de Pedidos

## 📝 Enunciado
Dada a seguinte lista de pedidos em formato de dicionário:

```python
pedidos = [
    {"id": 1, "valor": 100, "status": "pago"},
    {"id": 2, "valor": 50,  "status": "cancelado"},
    {"id": 3, "valor": 80,  "status": "pago"},
    {"id": 4, "valor": 30,  "status": "pago"},
]
```

Desenvolva um código que processe a lista seguindo estas regras de negócio:
1.  **Iteração:** Percorra a lista `pedidos` utilizando um laço `for`.
2.  **Soma de Pagos:** Acumule o valor apenas dos pedidos que possuem o status `"pago"`.
3.  **Interrupção Crítica:** Se encontrar qualquer pedido com o status `"cancelado"`, o processamento deve ser interrompido imediatamente (utilize `break`).
4.  **Filtro Adicional:** Utilize a estrutura de controle `continue` para pular qualquer lógica extra caso o status não seja o esperado antes de somar.
5.  **Resultado:** Exiba o valor total somado até o momento da interrupção ou do fim da lista.

## 🎯 Objetivo
Praticar o gerenciamento de erros ou estados críticos em fluxos de dados, utilizando interrupções forçadas para garantir a integridade do processamento.
* **Categoria:** Lógica de Programação.
* **Nível:** Iniciante / Intermediário.

## 🛠️ Tecnologias e Conceitos
* **Iteração:** Laço `for` para percorrer dicionários em listas.
* **Controle de Fluxo:** `break` para parar o sistema em caso de pedido cancelado.
* **Controle de Fluxo:** `continue` para filtragem lógica.
* **Lógica Condicional:** Verificação de strings (status).
* **Acumuladores:** Soma de valores monetários.