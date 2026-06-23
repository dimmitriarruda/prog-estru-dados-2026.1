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

def buscar_por_cpf(cpf):
    conn = None
    cursor = None
    try:
        conn = conectar_mysql()
        cursor = conn.cursor(dictionary=True)
        sql = "SELECT * FROM tb_cliente WHERE cpf = %s"
        cursor.execute(sql, (cpf,))
        return cursor.fetchone()

    except Error as e:
        print(f"Erro ao buscar CPF: {e}")
        return None

    finally:
        if cursor is not None:
            cursor.close()
        if conn is not None:
            conn.close()


def inserir_aluno(aluno):
    conn = None
    cursor = None
    try:
        conn = conectar_mysql()
        cursor = conn.cursor()
        sql = """
        INSERT INTO tb_aluno 
        (
            nome,
            cpf, 
            idade,
            bolsa_monitoria,
            bolsa_estagio
        )
            VALUES (%s, %s, %s, %s, %s)
        """
        
        valores = (
            aluno.nome,
            aluno.cpf,
            aluno.idade,
            aluno.bolsa_estagio,
            aluno.bolsa_monitoria
        )
        
        cursor.execute(sql, valores)
        
        conn.commit()
        
        #return cursor.lastrowid
    
        print("Aluno cadastrado com sucesso!")

    except Error as e:
        print(f"Erro ao inserir aluno: {e}")
        return None

    finally:
        if cursor is not None:
            cursor.close()
        if conn is not None:
            conn.close()

def atualizar(aluno_id, nome, cpf, idade, bolsa_monitoria, bolsa_estagio):
    conn = None
    cursor = None
    try:
        conn = conectar_mysql()
        cursor = conn.cursor()
        sql = """""
            UPDATE tb_aluno
            SET nome = %s,
                cpf = %s,
                idade = %s,
                bolsa_monitoria = %s,
                bolsa_estagio = %s
            WHERE id = %s
        """""
        cursor.execute(sql, (nome, cpf, idade, bolsa_monitoria, bolsa_estagio, aluno_id))
        conn.commit()
        return cursor.rowcount
    except Error as e:
        print(f"Erro ao atualizar aluno: {e}")
        return 0

    finally:
        if cursor is not None:
            cursor.close()
        if conn is not None:
            conn.close()

def excluir(aluno_id):
    conn = None
    cursor = None
    try:
        conn = conectar_mysql()
        cursor = conn.cursor()
        sql = "DELETE FROM tb_aluno WHERE aluno_id = %s"
        cursor.execute(sql, (aluno_id,))
        conn.commit()
        return cursor.rowcount

    except Error as e:
        print(f"Erro ao excluir aluno: {e}")
        return 0

    finally:
        if cursor is not None:
            cursor.close()
        if conn is not None:
            conn.close()
