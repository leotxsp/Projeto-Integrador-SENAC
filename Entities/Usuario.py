from Conexao import conectar
class Usuario:
    def __init__(self,usuario = None,senha= None,nome= None,email= None,cargo= None,setor = None):
        self.usuario = usuario
        self.senha = senha
        self.nome = nome
        self.email = email
        self.setor = setor
        self.cargo = cargo




    def incluir(self):
        con = conectar()
        cursor = con.cursor()
        sql = (f'INSERT INTO `usuario`(`login`, `senha`, `nome`, `email`, `setor_idsetor`, `cargo_idcargo`) '
               f'VALUES ({self.usuario},{self.senha},{self.nome},{self.email},{self.setor},{self.cargo})')
        cursor.execute(sql)
        con.commit()
        con.close()

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
        sql = 'select * from curso'
        cursor.execute(sql)
        resultado = cursor.fetchall()
        lista = []
        for item in resultado:
            curso = Curso(item[0], item[1], item[2])
            lista.append(curso)
        con.close()
        return lista
