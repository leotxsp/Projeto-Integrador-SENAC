import sys
from PySide6.QtCore import QDate
from Entities.Chamados import *
from Entities.Servico import Servico
from PySide6 import QtWidgets
from Telas.ui_Tela_alterar_chamado import Ui_AlterarChamado

class Main_alterar(QtWidgets.QMainWindow, Ui_AlterarChamado):
    def __init__(self, chamado = None):
        super(Main_alterar, self).__init__()
        self.setupUi(self)
        self.chamado = chamado
        self.comboServico = []
        self.listaServicos = []
        self.preencher()
        self.pushButton.clicked.connect(self.alterandoChamado)
        print(chamado.__dict__)



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
        self.CBservico.addItems(self.comboServico)


        self.CBStatus.setCurrentIndex(0)
        self.CBprioridade.setCurrentIndex(0)
        self.CBservico.setCurrentIndex(0)




    def preencher(self):
        self.preencherComboBox()
        status_enum = Status[self.chamado.status]
        prioridade_enum = Prioridade[self.chamado.prioridade]
        self.edtTitulo.setText(self.chamado.titulo)
        self.CBStatus.setCurrentIndex(status_enum.index)
        self.CBprioridade.setCurrentIndex(prioridade_enum.index)
        self.dateEdit.setDate(self.chamado.dataAbertura)
        self.dateEdit_2.setDate(self.chamado.dataDeFechamento)
        self.TEdescricao.setText(self.chamado.descricao)



    def tratamentoTexto(self, texto:tuple):
        tratado = f"{texto[0]}-{texto[1]}-{texto[2]}"
        return tratado

    def alterandoChamado(self):
        idchamado = self.chamado.idchamado
        servico = self.listaServicos[self.CBservico.currentIndex()].idServico
        titulo = self.edtTitulo.text()
        descricao = self.TEdescricao.toPlainText()
        status = self.CBStatus.currentData().name
        prioridade = self.CBprioridade.currentData().name
        data_abertura_bruta = self.dateEdit.date().getDate()
        data_fechamento_bruta = self.dateEdit_2.date().getDate()
        data_abertura = self.tratamentoTexto(data_abertura_bruta)
        data_fechamento = self.tratamentoTexto(data_fechamento_bruta)

        usuarioAbertura = self.chamado.usuario_abertura
        usuarioFechamento = self.chamado.usuario_atendimento
        chamado = Chamado(idchamado,servico,titulo,descricao,prioridade,status,data_abertura,data_fechamento,usuarioAbertura,usuarioFechamento)
        print(chamado.__dict__)
        chamado.alterar()

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = Main_alterar()
    window.show()
    app.exec()