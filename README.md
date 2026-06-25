# Sistema de Gestão de Farmácia - Trabalho Final de PED 2026.1

Este é um trabalho desenvolvido para a finalização da cadeira de Programação e Estrutura de Dados da turma de 2026.1. Desenvolvemos um sistema em Python e integrado com banco de dados MySQL para gerenciamento de clientes, controle de estoque e fluxo de pedidos de medicamentos. 

---

## Funcionalidades Principais

* *Gestão de Clientes:* Cadastro, consulta, edição e exclusão de contas de usuários.
* *Fluxo de Pedidos:* Menu interativo para pedido e visualização do estoque de medicamentos como Dipirona, Paracetamol, Ibuprofeno, Loratadina e Ambroxol.
* *Persistência de Dados:* Integração completa com banco de dados relacional para controle de usuários e pedidos.

---

## Tecnologias Utilizadas

* *Linguagem:* Python 3
* *Banco de Dados:* MySQL
* *Editor:* Visual Studio Code

---

## Estrutura do Repositório

* farmacia.py — Arquivo principal que gerencia os menus de navegação e a interface do terminal.
* bdfarmacia.py — Camada que executa os comandos SQL diretamente no banco de dados.
* pedido.py — Classe responsável pela estrutura dos objetos de pedidos.
* cliente.py e cliente_atualizar.py — Classes responsáveis por gerenciar as operações de usuários.

---

## Como Executar o Projeto

1. Certifique-se de ter o MySQL ativo na sua máquina.
2. Instale o conector do banco de dados no terminal:
   ```bash
   pip install mysql-connector-python
3. Clone o repositório
    ```bash
    git clone https://github.com/dimmitriarruda/prog-estru-dados-2026.1    
4. Execute o arquivo principal para iniciar o sistema:
   ```bash
   python farmacia.py
 
