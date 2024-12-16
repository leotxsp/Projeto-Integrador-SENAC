from Conexao import conectar


class Chamado:
    def __init__(self,
                 idchamado: int = None,
                 servico_idServico: int = None,
                 titulo: str = None,
                 descricao: str = None,
                 prioridade: str = None,
                 status: str = None,
                 dataAbertura: str = None,
                 dataDeFechamento: str = None,
                 usuario_abertura: int = None,
                 usuario_atendimento: int = None):

        self.idchamado = idchamado
        self.servico_idServico = servico_idServico
        self.titulo = titulo
        self.descricao = descricao
        self.prioridade = prioridade
        self.status = status
        self.dataAbertura = dataAbertura
        self.dataDeFechamento = dataDeFechamento
        self.usuario_abertura = usuario_abertura
        self.usuario_atendimento = usuario_atendimento

    def incluir(self):
        con = conectar()
        cursor = con.cursor()
        sql = (
            'INSERT INTO `chamado` (`servico_idServico`, `titulo`, `descricao`, `prioridade`, '
            '`status`, `dataAbertura`, `dataDechamento`, `usuario_abertura`, `usuario_atendimento`) '
            'VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)'
        )
        values = (self.servico_idServico, self.titulo, self.descricao, self.prioridade,
                  self.status, self.dataAbertura, self.dataDeFechamento,
                  self.usuario_abertura, self.usuario_atendimento)
        try:
            cursor.execute(sql, values)
            con.commit()
            print("Chamado inserido com sucesso.")
        except Exception as e:
            print("Erro ao inserir chamado:", e)
        finally:
            cursor.close()
            con.close()

    def excluir(self):
        con = conectar()
        cursor = con.cursor()
        sql = f'DELETE FROM chamado WHERE idchamado = {self.idchamado}'
        try:
            cursor.execute(sql)
            con.commit()
            print("Chamado excluído com sucesso.")
        except Exception as e:
            print("Erro ao excluir chamado:", e)
        finally:
            cursor.close()
            con.close()

    def alterar(self):
        con = conectar()
        cursor = con.cursor()
        sql = (
            'UPDATE chamado SET servico_idServico=%s, titulo=%s, descricao=%s, prioridade=%s, '
            'status=%s, dataAbertura=%s, dataDechamento=%s, usuario_abertura=%s, '
            'usuario_atendimento=%s WHERE idchamado=%s'
        )
        values = (self.servico_idServico, self.titulo, self.descricao, self.prioridade,
                  self.status, self.dataAbertura, self.dataDeFechamento,
                  self.usuario_abertura, self.usuario_atendimento, self.idchamado)
        try:
            cursor.execute(sql, values)
            con.commit()
            print("Chamado alterado com sucesso.")
        except Exception as e:
            print("Erro ao alterar chamado:", e)
        finally:
            cursor.close()
            con.close()

    def buscar(self):
        con = conectar()
        cursor = con.cursor()
        sql = 'SELECT * chamado'
        try:
            cursor.execute(sql)
            resultado = cursor.fetchall()
            lista = []
            for item in resultado:
                chamado = Chamado(item[0], item[1], item[2], item[3], item[4],
                                  item[5], item[6], item[7], item[8], item[9])
                lista.append(chamado)
            return lista
        except Exception as e:
            print("Erro ao buscar chamados:", e)
            return []
        finally:
            cursor.close()
            con.close()


    def buscarPorUsuario(self,usuario_abertura):
        con = conectar()
        cursor = con.cursor()
        sql = f'SELECT chamado.*, usuario.nome FROM chamado JOIN usuario ON chamado.usuario_abertura = usuario.idusuario WHERE chamado.usuario_abertura = {usuario_abertura};'
        try:
            cursor.execute(sql)
            resultado = cursor.fetchall()
            lista = []
            for item in resultado:
                print(item)
                chamado = Chamado(item[0], item[1], item[2], item[3], item[4],
                                  item[5], item[6], item[7], item[8], item[9])
                lista.append(chamado)
            return lista
        except Exception as e:
            print("Erro ao buscar a:", e)
            return []
        finally:
            cursor.close()
            con.close()


if __name__ == '__main__':
    lista_chamados = Chamado().buscar()
    for chamado in lista_chamados:
        print(chamado)
