from Conexao import conectar

class Setor:
    def __init__(self,idsetor = None, nome_setor = None ):
        self.idsetor = idsetor
        self.nome_setor = nome_setor

    def buscar(self):
        conexao = conectar()
        cursor = conexao.cursor()
        sql = 'select * from setor'
        cursor.execute(sql)
        resultado = cursor.fetchall()
        lista = []
        for item in resultado:
            setor = Setor(item[0], item[1])
            lista.append(setor)
        conexao.close()
        return lista