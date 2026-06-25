#pip install mysql-connector-python
import mysql.connector
from mysql.connector import Error

def conectar_mysql():
    try:
        conexao = mysql.connector.connect(
            host="localhost",
            port=3306,
            user="root",
            password="Dimmitri*2004",
            database="bd_poli"
        )

        if conexao.is_connected():
            return conexao
        else:
            print(f"Falha na conexão: {conexao.get_server_info()}")
            return None

    except Error as e:
        print(f"Erro ao conectar ao MySQL: {e}")
        return None

def listar_todos():
    conn = None
    cursor = None
    try:
        conn = conectar_mysql()
        cursor = conn.cursor(dictionary=True)
        sql = """
            SELECT *
            FROM tb_cliente
            ORDER BY id_cliente
        """
        cursor.execute(sql)
        return cursor.fetchall()

    except Error as e:
        print(f"Erro ao listar clientes: {e}")
        return []

    finally:
        if cursor is not None:
            cursor.close()
        if conn is not None:
            conn.close()

def verificar_por_cpf(cpf):
    conn = None
    cursor = None
    try:
        conn = conectar_mysql()
        cursor = conn.cursor(dictionary=True)
        sql = "SELECT * FROM tb_cliente WHERE cpf = %s"
        cursor.execute(sql, (cpf,))
        return cursor.fetchone()

    except Error as e:
        print(f"\nErro ao verificar CPF: {e}")
        return None

    finally:
        if cursor is not None:
            cursor.close()
        if conn is not None:
            conn.close()
            
def cadastrar_cliente(cadastro):
    conn = None
    cursor = None
    try:
        conn = conectar_mysql()
        cursor = conn.cursor(dictionary=True)
        sql = """
        INSERT INTO tb_cliente 
        (nome, idade, cpf, senha)
        VALUES (%s, %s, %s, %s)
        """
        valores = (
            cadastro.nome,
            cadastro.idade,
            cadastro.cpf,
            cadastro.senha
        )
        
        cursor.execute(sql, valores)
        
        conn.commit()
        
        novo_id = cursor.lastrowid
        
        sql_pedido = """
        INSERT INTO tb_pedidos
        (
            id_cliente,
            dipirona,
            paracetamol,
            ibuprofeno,
            loratadina,
            ambroxol
        )
        
        VALUES
        (
            %s,
            0,
            0,
            0,
            0,
            0
        )
        """
        cursor.execute(sql_pedido, (novo_id,))
        conn.commit()
        print("\nCliente cadastrado com sucesso!")
        
    except Error as e:
        print(f"\nErro ao cadastrar cliente: {e}")
        return None
    
    finally:
        if cursor is not None:
            cursor.close()
        if conn is not None:
            conn.close()

def atualizar_cadastro(cadastro):
    conn = None
    cursor = None
    try:
        conn = conectar_mysql()
        cursor = conn.cursor()
        sql = """
            UPDATE tb_cliente
            SET nome = %s,
                idade = %s,
                cpf = %s,
                senha = %s
            WHERE id_cliente = %s
        """
        
        valores = (
            cadastro.nome,
            cadastro.idade,
            cadastro.cpf,
            cadastro.senha,
            cadastro.id_cliente
        )
        
        cursor.execute(sql, valores)
        
        conn.commit()
        
        print("\nCadastro atualizado com sucesso!")
        return cursor.rowcount
    except Error as e:
        print(f"\nErro ao atualizar cadastro: {e}")
        return 0

    finally:
        if cursor is not None:
            cursor.close()
        if conn is not None:
            conn.close()

def excluir(cpf, id_cliente):
    conn = None
    cursor = None
    try:
        conn = conectar_mysql()
        cursor = conn.cursor()
        
        sql = "DELETE FROM tb_pedidos WHERE id_cliente = %s"
        
        cursor.execute(sql, (id_cliente,))
        conn.commit()
        
        sql = "DELETE FROM tb_cliente WHERE cpf = %s"
        
        cursor.execute(sql, (cpf,))
        conn.commit()
        
        print("\nCadastrado excluido com sucesso!")
        return cursor.rowcount

    except Error as e:
        print(f"\nErro ao excluir cadastro: {e}")
        return 0

    finally:
        if cursor is not None:
            cursor.close()
        if conn is not None:
            conn.close()

def tb_pedido(id_cliente):
    conn = None
    cursor = None
    try:
        conn = conectar_mysql()
        cursor = conn.cursor(dictionary=True)
        sql = "SELECT * FROM tb_pedidos WHERE id_cliente = %s"
        cursor.execute(sql, (id_cliente,))
        return cursor.fetchone()

    except Error as e:
        print(f"Erro ao buscar Tabela: {e}")
        return None

    finally:
        if cursor is not None:
            cursor.close()
        if conn is not None:
            conn.close()
            