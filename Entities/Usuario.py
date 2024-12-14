from Conexao import conectar
from Entities.Cargo import Cargo
from Entities.Setor import Setor

class Usuario:
    def __init__(self,IDusuario:int = None,login:str = None,senha= None,nome= None,email= None,cargo= None,setor = None):
        self.IDusuario = IDusuario
        self.login = login
        self.senha = senha
        self.nome = nome
        self.email = email
        self.setor = setor
        self.cargo = cargo

    def incluir(self):
        con = conectar()
        cursor = con.cursor()
        sql = (
            'INSERT INTO `usuario` (`login`, `senha`, `nome`, `email`, `setor_idsetor`, `cargo_idcargo`) '
            'VALUES (%s, %s, %s, %s, %s, %s)'
        )
        values = (self.login, self.senha, self.nome, self.email, self.setor.idsetor, self.cargo.idCargo)
        try:
            cursor.execute(sql, values)
            con.commit()
            print("Usuário inserido com sucesso.")
        except Exception as e:
            print("Erro ao inserir usuário:", e)
        finally:
            cursor.close()



    def excluir(self):
        con = conectar()
        cursor = con.cursor()
        sql = f'delete from curso where idcurso = {self.idcurso}'
        cursor.execute(sql)
        con.commit()
        con.close()

    def alterar(self):
        con = conectar()
        cursor = con.cursor()
        sql = f'updete curso set nome = "{self.nome}", ch= {self.ch} where idcurso{self.idcurso}'
        cursor.execute(sql)
        con.commit()
        con.close()

    def buscar(self):
        con = conectar()
        cursor = con.cursor()
        sql = 'select * from usuario'
        cursor.execute(sql)
        resultado = cursor.fetchall()
        lista = []
        for item in resultado:
            print(item)
            usuario = Usuario(item[0], item[1], item[2], item[3], item[4], item[5], item[6])
            lista.append(usuario)
        con.close()
        return lista

# if __name__ == '__main__':
#     lista = (Usuario().buscar())
#     for i in lista:
#         print(i.IDusuario)