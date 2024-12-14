import mysql.connector as mysql
def conectar():
    conexao = mysql.connect(
    host='127.0.0.1',
    port=3306,
    user='root',
    password='',
    database='sistema_chamado'
    )
    return conexao

def executar_sql(sql):
    try:
        con = conectar()
        cursor = con.cursor()
        cursor.execute(sql)
        if sql.strip().upper().startswith("SELECT"):
            resultado = cursor.fetchall()
            return resultado
        return resultado
    except mysql.Error as err:
        print(f"Erro: {err}")
        con.rollback()
        return None
    finally:
        cursor.close()
        con.close()


# sql = "select usuario.login, setor.nome_setor from setor inner join usuario on usuario.setor_idSetor = setor.idSetor"
# # sql = "select * from usuario"
# resultados = executar_sql(sql)
#
# print(resultados)