from Conexao import conectar
from enum import Enum

class Status(Enum):
    ABERTO = (0, "ABERTO")
    EM_PROGRESSO = (1, "EM PROGRESSO")
    FECHADO = (2, "FECHADO")

    def __init__(self, index, description):
        self.index = index
        self.description = description

    def procurarStatusPorIndex(index):
        if 0 <= index < len(Status):
            return list(Status)[index]
        raise ValueError("Valor de index invalido")

class Prioridade(Enum):
    BAIXA = (0, "BAIXA")
    MEDIA = (1, "MEDIA")
    ALTA = (2, "ALTA")

    def __init__(self, index, description):
        self.index = index
        self.description = description

    def procurarPrioridadePorIndex(index):
        if 0 <= index < len(Prioridade):
            return list(Prioridade)[index]
        raise ValueError("Valor de index invalido")


class Chamado:
    def __init__(self,
                 idchamado: int = None,
                 servico_idServico: int = None,
                 titulo: str = None,
                 descricao: str = None,
                 prioridade: Prioridade = None,
                 status: Status = None,
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
            '`status`, `dataAbertura`, `dataDeFechamento`, `usuario_abertura`, `usuario_atendimento`) '
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
            'status=%s, dataAbertura=%s, dataDeFechamento=%s, usuario_abertura=%s, '
            'usuario_atendimento=%s WHERE idchamado=%s'
        )
        values = (self.servico_idServico, self.titulo, self.descricao, self.prioridade,
                  self.status, self.dataAbertura, self.dataDeFechamento,
                  self.usuario_abertura, self.usuario_atendimento, self.idchamado)
        print(sql, values)
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
        sql = 'SELECT * FROM `chamado`'
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

    def buscarPorServico(self,servico):
        con = conectar()
        cursor = con.cursor()
        sql = f'select tipoServico from servico where idServico = {servico};'
        cursor.execute(sql)
        resultado = cursor.fetchall()
        resultado = (resultado[0][0]).upper()
        cursor.close()
        con.close()
        return resultado

    def fecharChamado(dataDeFechamento , idchamado):
        con = conectar()
        cursor = con.cursor()
        print(dataDeFechamento,idchamado)
        sql = 'UPDATE chamado SET dataDeFechamento = %s WHERE idchamado = %s'
        print(sql, (dataDeFechamento, idchamado))
        cursor.execute(sql, (dataDeFechamento, idchamado))
        cursor.close()
        con.close()
        print("Chamado fechardo com sucesso.")

if __name__ == '__main__':
    lista_chamados = Chamado().buscar()
    for chamado in lista_chamados:
        print(chamado)
