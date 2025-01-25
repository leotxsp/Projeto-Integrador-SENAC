import sys
from PySide6.QtCore import Signal
from PySide6.QtCore import QDate
from Entities.Chamados import Status
from Entities.Servico import Servico
from PySide6 import QtWidgets
from Telas.ui_Tela_fechar_chamado import Ui_fecharCadastro


class Main_fechar(QtWidgets.QMainWindow, Ui_fecharCadastro):
    closed = Signal()
    def __init__(self, chamado = None,user = None):
        super(Main_fechar, self).__init__()
        self.setupUi(self)
        self.user = user
        self.chamado = chamado
        self.pushButton.clicked.connect(self.alterandoChamado)
        self.preencher()


    def preencher(self):
        self.TEdescricao.setText(self.chamado.descricao)
        self.LBtitulo.setText(self.chamado.titulo)
        self.LBstatus.setText("FECHADO")
        self.LBPrioridade.setText(self.chamado.prioridade)
        servico = Servico.buscarUm(self.chamado.servico_idServico).tipoServico
        self.LBservico.setText(servico)
        data_entrada = self.chamado.dataAbertura
        data=data_entrada.strftime("%Y-%m-%d")
        self.LBdataAbertura.setText(data)
        self.dateEdit_2.setDate(QDate.currentDate())


    def tratamentoTexto(self, texto:tuple):
        tratado = f"{texto[0]}-{texto[1]}-{texto[2]}"
        return tratado

    def alterandoChamado(self):
        data_fechamento_bruta = self.dateEdit_2.date().getDate()
        data_fechamento = self.tratamentoTexto(data_fechamento_bruta)
        self.chamado.usuario_atendimento = self.user.IDusuario
        self.chamado.dataDeFechamento = data_fechamento
        status = Status.procurarStatusPorIndex(2)
        self.chamado.status = status.description
        self.chamado.alterar()
        self.close()

    def closeEvent(self, event):
        self.closed.emit()
        super().closeEvent(event)

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = Main_fechar()
    window.show()
    app.exec()