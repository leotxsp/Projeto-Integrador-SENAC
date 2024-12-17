import sys
import datetime
from cgi import print_environ_usage

from PySide6.QtCore import QDate
from Entities.Chamados import *
from Entities.Servico import Servico
from PySide6 import QtWidgets
from Telas.ui_Tela_fechar_chamado import Ui_fecharCadastro
from main_menu_tecnico import Main_tecnico as tecnico
tecnico.test()

class Main_fechar(QtWidgets.QMainWindow, Ui_fecharCadastro):
    def __init__(self, chamado = None):
        super(Main_fechar, self).__init__()
        self.setupUi(self)
        self.chamado = chamado
        self.pushButton.clicked.connect(self.alterandoChamado)
        self.preencher()


    def preencher(self):
        self.TEdescricao.setText(self.chamado.descricao)
        self.LBtitulo.setText(self.chamado.titulo)
        self.LBstatus.setText(self.chamado.status)
        self.LBPrioridade.setText(self.chamado.prioridade)
        servico = Servico.buscarUm(self.chamado.servico_idServico).tipoServico
        self.LBservico.setText(servico)
        data_entrada = self.chamado.dataAbertura
        string_data=data_entrada.strftime("%Y-%m-%d")
        self.LBdataAbertura.setText(string_data)


    def tratamentoTexto(self, texto:tuple):
        tratado = f"{texto[0]}-{texto[1]}-{texto[2]}"
        return tratado

    def alterandoChamado(self):

        data_fechamento_bruta = self.dateEdit_2.date().getDate()
        data_fechamento = self.tratamentoTexto(data_fechamento_bruta)
        self.chamado.dataDeFechamento = data_fechamento
        self.chamado.alterar()
        tecnico.montarTabelaChamados()
        self.close()



if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = Main_fechar()
    window.show()
    app.exec()