import sys
from PySide6.QtCore import QDate
from PySide6.QtCore import Signal
from PySide6 import QtWidgets
from Entities.Chamados import *
from Entities.Servico import Servico
from Telas.ui_Tela_abrir_chamado import Ui_AbrirChamado

class Main_Abrir(QtWidgets.QMainWindow, Ui_AbrirChamado):
    closed = Signal()
    def __init__(self, user = None):
        super(Main_Abrir, self).__init__()
        self.setupUi(self)
        self.user = user
        self.chamado = Chamado()
        self.comboServico = []
        self.listaServicos = []
        self.preencher()
        self.pushButton.clicked.connect(self.inserindoChamado)



    def buscarServicos(self):
        try:
            servico = Servico()
            self.listaServicos = servico.buscar()
            for item in self.listaServicos:
                self.comboServico.append(item.tipoServico)
            print("Busca dos cursos realizada com sucesso")
        except Exception as erro:
            print("Erro ao buscar")
            print(erro)


    def preencherComboBox(self):
        self.buscarServicos()
        for status in Status:
            self.CBStatus.addItem(status.description, status)
        for prioridade in Prioridade:
            self.CBprioridade.addItem(prioridade.description, prioridade)
        self.CBservico_3.addItems(self.comboServico)


        self.CBStatus.setCurrentIndex(0)
        self.CBprioridade.setCurrentIndex(0)
        self.CBservico_3.setCurrentIndex(0)




    def preencher(self):
        self.preencherComboBox()
        self.edtTitulo.setText(self.chamado.titulo)
        self.dateEdit.setDate(self.chamado.dataAbertura)
        self.TEdescricao.setText(self.chamado.descricao)



    def tratamentoTexto(self, texto:tuple):
        tratado = f"{texto[0]}-{texto[1]}-{texto[2]}"
        return tratado

    def inserindoChamado(self):
        servico = self.listaServicos[self.CBservico_3.currentIndex()].idServico
        titulo = self.edtTitulo.text()
        descricao = self.TEdescricao.toPlainText()
        status = self.CBStatus.currentData().name
        prioridade = self.CBprioridade.currentData().name
        data_abertura_bruta = self.dateEdit.date().getDate()
        data_abertura = self.tratamentoTexto(data_abertura_bruta)

        usuarioAbertura = self.user.IDusuario
        chamado = Chamado(None,servico,titulo,descricao,prioridade,status,data_abertura,None,usuarioAbertura,None)
        print(chamado.__dict__)
        chamado.incluir()
        self.close()

    def closeEvent(self, event):
        self.closed.emit()
        super().closeEvent(event)

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = Main_Abrir()
    window.show()
    app.exec()