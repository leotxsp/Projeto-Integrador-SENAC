from Conexao import conectar

class Cargo:
    def __init__(self, idCargo:int = None, cargo = None):
        self.idCargo = idCargo
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

    def buscarUm(idCargo):
        conexao = conectar()
        cursor = conexao.cursor()
        sql = f'SELECT * FROM cargo WHERE idcargo = {idCargo}'
        cursor.execute(sql)
        resultado = cursor.fetchone()
        conexao.close()
        if resultado:
            return Cargo(resultado[0], resultado[1])
        return None