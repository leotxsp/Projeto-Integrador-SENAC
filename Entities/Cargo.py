from Conexao import conectar

class Cargo:
    def __init__(self,idcurso = None, cargo = None):
        self.idcurso = idcurso
        self.cargo = cargo

    def buscar(self):
        conexao = conectar()
        cursor = conexao.cursor()
        sql = 'select * from cargo'
        cursor.execute(sql)
        resultado = cursor.fetchall()
        lista = []
        for item in resultado:
            cargo = Cargo(item[0], item[1])
            lista.append(cargo)
        conexao.close()
        return lista