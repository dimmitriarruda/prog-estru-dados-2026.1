import bdfarmacia
from cliente import Cliente
cedulas = {"DIPIRONA":2, "PARACETAMOL":5, "IBUPROFENO":3, "LOROTADINA":2 , "AMBROXOL":1}#banco de dados
cedulas_usadas = []
senha = "123"

lista_cadastro = []
j = 0

while True:
    
    print("\n-----MENU DA FARMÁCIA-----")
    print("1.Listar Clientes")
    print("2.Acesse sua Conta")
    print("3.Cadastre-se")
    print("4.Editar Cadastro")
    print("5.Sair\n")
    
    
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
            dados = bdfarmacia.buscar_por_cpf(cpf_busca)
            if dados is None:
                print("\nEsse cpf não está cadastrado.")
            
            else:
                cliente_obj = Cliente(
                    dados["nome"],
                    dados["cpf"],
                    dados["senha"],
                    dados["idade"]
                )
                 
                senha_busca = input("Digite a sua senha: ")
                if (cliente_obj.senha == senha_busca):
                    while True:
                        print("\n---MENU DO CLIENTE---")
                        print("1.Realizar Compra")
                        print("2.Exibir Histórico")
                        print("3.Excluir Histórico")
                        print("4.Sair\n")
                        x = input("Escolha uma opção: ") 
                                
                        if x == '1':
                            while True:
                                print("\n--MENU DE COMPRA--")
                                print("1.Continuar Compra")
                                print("2.Voltar")
                                y = input("Escolha uma opção: ")
                                
                                if y == '1':
                                    produto = input("\nInforme o item que você deseja comprar:\n(Dipirona, Paracetamol, Ibuprofeno, Lorotadina, Ambroxol\n").lower()
                                    for i in cedulas:
                                        if produto not in cedulas:
                                            print("Item Inválido.")
                                            break
                                            
                                        if produto == i:
                                            quantidade_cedula = int(input("\nInforme a quantidade que você quer comprar: "))
                                            if quantidade_cedula > 0:
                                                cedulas[i] += quantidade_cedula
                                                print("Compra realizada com sucesso.")
                                            else:
                                                print("Não temos essa quantidade disponível no estoque.\nCompra Inválida")        
                                elif y == '2':
                                    break   
                                
                                else:
                                    print("Opção Inválida")
                                        
                        elif x == '2':
                            print("Resumo do Caixa")
                            j = 0
                            for i in cedulas:
                                print(f"Cédulas de R${i}: {cedulas[i]}")
                                z = int(i)
                                j = j + z * cedulas[i]
                            print(f"Total Disponível: R${j},00")
                                
                                
                        elif x == '4':
                            break 
                        
                        else:
                            print("Opção Inválida")
                                                 
                else:
                    print("Senha Incorreta!")
                    break
                  
               
    if x == '3':
        nome = input("Digite seu nome: ")
        
        while True:
            cpf = input("Digite seu cpf: ")
            j = 0
            for i in range(len(lista_cadastro)): 
                if (lista_cadastro[i]["cpf"] == cpf):
                    print("\nEsse cpf já está cadastrado.")
                    j = 1
                    break
                
                else:
                    continue
            
            if j == 1:
                continue
            
            else:
                break    
            
        idade = int(input("Digite sua idade: "))
        
        novo_cadastro = {
            "nome" : nome,
            "cpf" : cpf,
            "idade" : idade
        }
        
        lista_cadastro.append(novo_cadastro)
        print("\nCadastro incluido com sucesso.")
        
    if x == '4':
        while True:
            if len(lista_cadastro) >= 1:
                cpf_edit = input("Digite o cpf do usuário que você deseja editar: ")
                for i in range(len(lista_cadastro)): 
                    if (lista_cadastro[i]["cpf"] == cpf_edit):
                        
                        nome = lista_cadastro[i]["nome"]
                        cpf = lista_cadastro[i]["cpf"]
                        idade = lista_cadastro[i]["idade"]
                        
                        lista_cadastro.remove(lista_cadastro[i])
                        
                        while True:
                            r0 = input("Deseja editar seu nome?(sim ou não) ")
                            
                            if r0 == 'sim': 
                                nome = input("Digite seu nome: ")
                                break
                                
                            elif r0 == 'não':
                                break
                            
                            else:
                                print("\nDigite Novamente.")
                                continue
                        
                        while True:
                            r1 = input("Deseja editar seu cpf?(sim ou não) ")
                            
                            if r1 == 'sim': 
                                while True:
                                    cpf = input("Digite seu cpf: ")
                                    j = 0
                                    for i in range(len(lista_cadastro)): 
                                        if (lista_cadastro[i]["cpf"] == cpf):
                                            print("\nEsse cpf já está cadastrado.")
                                            j = 1
                                            break
                                        
                                        else:
                                            continue
                                    
                                    if j == 1:
                                        continue
                                    
                                    else:
                                        break
                                break
                                
                            elif r1 == 'não':
                                break
                            
                            else:
                                print("\nDigite Novamente.")
                                continue    
                        
                        while True:
                            r2 = input("Deseja editar sua idade?(sim ou não) ")
                            
                            if r2 == 'sim': 
                                idade = int(input("Digite sua idade: "))
                                break
                                
                            elif r2 == 'não':
                                break
                            
                            else:
                                print("\nDigite Novamente.")
                                continue 
                        
                        edit_cadastro = {
                            "nome" : nome,
                            "cpf" : cpf,
                            "idade" : idade
                        }
                        
                        lista_cadastro.append(edit_cadastro)
                        print("\nCadastro editado com sucesso.")
                        j = 1
                        break
                    else:
                        if (i == len(lista_cadastro) - 1):
                            print("\nEsse cpf não está cadastrado.")
                            j = 0
                        else:
                            continue
                if (j == 1):
                    break
                
                else:
                    continue
            else:
                print("\nA lista ainda não possui nenhum cadastro.")
                break
                        
    if x == '5':
        while True:
            if len(lista_cadastro) >= 1:
                cpf_exclui = input("Digite o cpf do usuário que você deseja excluir: ")
                for i in range(len(lista_cadastro)): 
                    if (lista_cadastro[i]["cpf"] == cpf_exclui):
                        lista_cadastro.remove(lista_cadastro[i])
                        print("\nCadastro excluido com sucesso.")
                        j = 1
                        break
                    else:
                        if (i == len(lista_cadastro) - 1):
                            print("\nEsse cpf não está cadastrado.")
                            j = 0
                        else:
                            continue
                if (j == 1):
                    break
                
                else:
                    continue
            else:
                print("\nA lista ainda não possui nenhum cadastro.")
                break    
        
    if x == '6':
        break

