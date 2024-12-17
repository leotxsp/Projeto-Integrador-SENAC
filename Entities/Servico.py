from Conexao import conectar

class Servico:
    def __init__(self, idServico:int = None, tipoServico = None):
        self.idServico = idServico
        self.tipoServico = tipoServico

    def buscar(self):
        conexao = conectar()
        cursor = conexao.cursor()
        sql = 'select * from servico'
        cursor.execute(sql)
        resultado = cursor.fetchall()
        lista = []
        for item in resultado:
            servico = Servico(item[0], item[1])
            lista.append(servico)
        conexao.close()
        return lista

    def buscarUm(idServico):
        conexao = conectar()
        cursor = conexao.cursor()
        sql = f'SELECT * FROM servico WHERE idServico = {idServico}'
        cursor.execute(sql)
        resultado = cursor.fetchone()
        conexao.close()
        if resultado:
            return Servico(resultado[0], resultado[1])
        return None