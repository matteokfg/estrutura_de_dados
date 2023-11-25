# Trabalho de Estrutura de Dados - Prof. Garcia

## Necessário fazer:

  1. Cadastro de Clientes;
  2. Cadastro de Agências;
  3. Cadstro de Contas, com opção de consulta de saldo e extrato;
  4. Cadastro de Movimento, entradas, saídas e saldos, anterior e atual;
  5. Menu.

## JSON

  Explicação de JSON: https://www.json.org/json-en.html

  Validador de JSON: https://jsonlint.com/

  O Banco de Dados vai ser um arquivo JSON, assim, ele terá um objeto chamado "BD". Dentro de "BD" terá quatro objetos: "Cliente", "Agencia", "Conta" e "Movimento". Cada um desses objetos guardará um array com vários obejtos daquele tipo. Exemplo:
  ```
  {
    "BD":{
            "Cliente": [],
            "Agencia": [],
            "Banco": [],
            "Conta": [],
            "Movimento": []
        }
  }
  ```