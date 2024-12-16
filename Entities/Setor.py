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

    def buscarUm(idsetor):
        conexao = conectar()
        cursor = conexao.cursor()
        sql = f'select * from setor where idsetor = {idsetor}'
        print(sql)
        cursor.execute(sql)
        resultado = cursor.fetchone()
        if resultado is None:
            print("Nenhum setor encontrado com o idsetor fornecido.")
            conexao.close()
            return None
        if len(resultado) < 2:
            print("Resultado inesperado da consulta.")
            conexao.close()
            return None
        setor = Setor(resultado[0], resultado[1])
        conexao.close()
        return setor