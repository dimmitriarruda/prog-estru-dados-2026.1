import bdfarmacia
from cliente import Cliente
from cliente_atualizar import Cliente_Atualizar
from pedido import Pedido

while True:
    
    print("\n-----MENU DA FARMÁCIA-----")
    print("1.Lista de Clientes")
    print("2.Acesse sua Conta")
    print("3.Cadastre-se")
    print("4.Editar Cadastro")
    print("5.Excluir Cadastro")
    print("6.Sair\n")
    
    
    x = input("Digite o número da operação que você deseja executar: ")
    
    if x == '1':
        print("")
        dados = bdfarmacia.listar_todos()
        i = 0
        for cliente in dados:
            i = i + 1
            print(f"{i}.{cliente["nome"]}")
    
    if x == '2':
        while True:
            cpf_busca = input("Digite o seu cpf: ")
            dados = bdfarmacia.verificar_por_cpf(cpf_busca)
            if dados is None:
                print("\nEsse cpf não está cadastrado.")
            
            else:
                cliente_obj = Cliente_Atualizar(
                    dados["id_cliente"],
                    dados["nome"],
                    dados["idade"],
                    dados["cpf"],
                    dados["senha"]
                )
                 
                senha_busca = input("Digite a sua senha: ")
                if (cliente_obj.senha == senha_busca):
                    while True:
                        print("\n---MENU DO CLIENTE---")
                        print("1.Realizar Pedido")
                        print("2.Exibir Histórico de Pedidos")
                        print("3.Sair\n")
                        z = input("Escolha uma opção: ")
                        
                        data = bdfarmacia.tb_pedido(cliente_obj.id_cliente)
                        pedido_obj = Pedido(
                            data["dipirona"],
                            data["paracetamol"],
                            data["ibuprofeno"],
                            data["loratadina"],
                            data["ambroxol"],
                            data["id_cliente"]
                        ) 
      
                        if z == '1':
                            while True:
                                print("\n--MENU DE PEDIDO--")
                                print("1.Continuar Pedido")
                                print("2.Voltar")
                                y = input("Escolha uma opção: ")
                                
                                if y == '1':
                                    produto = input("\nInforme o item que você deseja pedir:\n(Dipirona, Paracetamol, Ibuprofeno, Loratadina, Ambroxol)\n").lower()
                                    
                                    nao_conseguiu = True
                                    for campo in data.keys():
                                        if produto == campo:
                                            nao_conseguiu = False
                                            quantidade_pedido = int(input(f"\nInforme a quantidade de {produto} que você quer pedir: "))
                                            estoque = getattr(pedido_obj, produto, 0)
                                            if estoque is None:
                                                estoque = 0
                                                
                                            setattr(
                                                pedido_obj,
                                                produto,
                                                estoque + quantidade_pedido
                                            )
                                            bdfarmacia.atualizar_pedido(pedido_obj)
                                            break
                                            
                                        else:
                                            continue
                                        
                                    if nao_conseguiu:
                                        print("Item Inválido.")
                                            
                                elif y == '2':
                                    break   
                                
                                else:
                                    print("Opção Inválida")
                                        
                        elif z == '2':
                            print("\n---RESUMO DE PEDIDOS---\n")
                            for campo, valor in data.items():
                                if campo == "id_cliente" or valor == 0 or campo == "id_pedido":
                                    continue
                                else:    
                                    print(f"Você já pediu {campo}: {valor} vezes")

                        elif z == '3':
                            break 
                        
                        else:
                            print("Opção Inválida")
                    break                                 
                else:
                    print("Senha Incorreta!")
                    break      
               
    if x == '3':
        nome = input("Digite seu nome: ")
        idade = int(input("Digite sua idade: "))
        
        while True:
            cpf = input("Digite seu cpf: ")
            dados = bdfarmacia.verificar_por_cpf(cpf)
            if dados is not None:
                print("\nEsse cpf já está cadastrado.")
                continue
                
            else:
                break
        
        senha = (input("Digite sua senha: "))
        
        cadastro = Cliente(nome, idade, cpf, senha)
        bdfarmacia.cadastrar_cliente(cadastro)
        
    if x == '4':
        while True:
            cpf_edit = input("Digite o cpf do usuário que você deseja editar: ")
            dados = bdfarmacia.verificar_por_cpf(cpf_edit)
            if dados is None:
                print("\nEsse cpf não está cadastrado.")
                continue
            
            else:
                break
            
        cliente_obj2 = Cliente_Atualizar(
                    dados["id_cliente"],
                    dados["nome"],
                    dados["idade"],
                    dados["cpf"],
                    dados["senha"]
                )  
        
        while True:
            r0 = input("Deseja editar seu nome?(sim ou não) ")
            
            if r0 == 'sim': 
                cliente_obj2.nome = input("Digite seu nome: ")
                break
                
            elif r0 == 'não':
                break
            
            else:
                print("\nDigite Novamente.")
                continue
            
        while True:
            r1 = input("Deseja editar sua idade?(sim ou não) ")
            
            if r1 == 'sim': 
                cliente_obj2.idade = int(input("Digite sua idade: "))
                break
                
            elif r1 == 'não':
                break
            
            else:
                print("\nDigite Novamente.")
                continue
           
        while True:
            r2 = input("Deseja editar seu cpf?(sim ou não) ")
            
            if r2 == 'sim': 
                while True:
                    cpf_novo = input("Digite seu novo cpf: ")
                    dados = bdfarmacia.verificar_por_cpf(cpf_novo)
                    if dados is not None:
                        print("\nEsse cpf já está cadastrado.")
                        continue
                    
                    else:
                        break
                    
                cliente_obj2.cpf = cpf_novo
                break
                           
            elif r2 == 'não':
                break
            
            else:
                print("\nDigite Novamente.")
                continue
        
        while True:
            r3 = input("Deseja editar sua senha?(sim ou não) ")
            
            if r3 == 'sim': 
                cliente_obj2.senha = input("Digite sua senha: ")
                break
                
            elif r3 == 'não':
                break
            
            else:
                print("\nDigite Novamente.")
                continue
            
        bdfarmacia.atualizar_cadastro(cliente_obj2)    
            
    if x == '5':
        while True:
            cpf_exclui = input("Digite o cpf do usuário que você deseja excluir: ")
            dados = bdfarmacia.verificar_por_cpf(cpf_exclui)
            if dados is None:
                print("\nEsse cpf não está cadastrado.")
                continue
            
            else:
                break
        
        senha_exclui = input("Digite a sua senha: ")
        if senha_exclui == dados["senha"]:
            bdfarmacia.excluir(cpf_exclui, dados["id_cliente"])
            
        else:
            print("Senha Incorreta.")  
        
    if x == '6':
        break