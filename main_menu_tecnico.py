import sys
from PySide6 import QtWidgets
from Telas.ui_menu_tecnico import Ui_tecnico
from Entities.Chamados import Chamado
from Entities.Usuario import Usuario
from Conexao import executar_sql

class Main_tecnico(QtWidgets.QMainWindow, Ui_tecnico):
    def __init__(self):
        super(Main_tecnico,self).__init__()
        self.setupUi(self)
        self.stackedWidget.setCurrentIndex(0)
        self.listaChamados = []
        self.listaUsuarios = []


        self.btn_perfil_aberto.setChecked(True)
        self.btn_perfil_aberto.clicked.connect(self.quandoBotaoPerfilPressionado)
        self.btn_chamados_aberto.clicked.connect(self.quandoBotaoChamadoPresionado)
        self.btn_usuarios.clicked.connect(self.quandoBotaoUsuariopressionado)

        self.montarTabelaChamados()
        self.montarTabelaUsuarios()


    def buscarUsuarios(self):
        try:
            usuario = Usuario()
            self.listaUsuarios = usuario.buscar()
            print("Busca realizada com sucesso")
        except Exception as erro:
            print("Erro ao buscar alunos")
            print(erro)

    def montarTabelaUsuarios(self):
        self.buscarUsuarios()
        linha = 0
        self.tableWidget.setRowCount(len(self.listaUsuarios))
        for usuario in self.listaUsuarios:
            self.tableWidget.setItem(linha, 0, QtWidgets.QTableWidgetItem(str(usuario.IDusuario)))
            self.tableWidget.setItem(linha, 1, QtWidgets.QTableWidgetItem(str(usuario.login)))
            self.tableWidget.setItem(linha, 2, QtWidgets.QTableWidgetItem(str(usuario.email)))
            self.tableWidget.setItem(linha, 3, QtWidgets.QTableWidgetItem(str(usuario.senha)))
            self.tableWidget.setItem(linha, 4, QtWidgets.QTableWidgetItem(str(usuario.nome)))
            self.tableWidget.setItem(linha, 5, QtWidgets.QTableWidgetItem(str(usuario.setor)))
            self.tableWidget.setItem(linha, 6, QtWidgets.QTableWidgetItem(str(usuario.cargo)))
            linha += 1



    def buscarChamados(self):
        try:
            chamados = Chamado()
            self.listaChamados = chamados.buscar()
            print("Busca realizada com sucesso")
        except Exception as erro:
            print("Erro ao buscar alunos")
            print(erro)

    def montarTabelaChamados(self):
        self.buscarChamados()
        linha = 0
        self.TB_Chamados_usuario.setRowCount(len(self.listaChamados))
        for chamado in self.listaChamados:
            self.TB_Chamados_usuario.setItem(linha, 0, QtWidgets.QTableWidgetItem(str(chamado.idchamado)))
            self.TB_Chamados_usuario.setItem(linha, 1, QtWidgets.QTableWidgetItem(str(chamado.status)))
            self.TB_Chamados_usuario.setItem(linha, 2, QtWidgets.QTableWidgetItem(str(chamado.prioridade)))
            self.TB_Chamados_usuario.setItem(linha, 3, QtWidgets.QTableWidgetItem(str(chamado.titulo)))
            self.TB_Chamados_usuario.setItem(linha, 4, QtWidgets.QTableWidgetItem(str(chamado.descricao)))
            self.TB_Chamados_usuario.setItem(linha, 5, QtWidgets.QTableWidgetItem(str(chamado.usuario_abertura)))
            self.TB_Chamados_usuario.setItem(linha, 6, QtWidgets.QTableWidgetItem(str(chamado.usuario_atendimento)))
            self.TB_Chamados_usuario.setItem(linha, 7, QtWidgets.QTableWidgetItem(str(chamado.dataAbertura)))
            self.TB_Chamados_usuario.setItem(linha, 8, QtWidgets.QTableWidgetItem(str(chamado.dataDeFechamento)))
            linha+=1


    def quandoBotaoPerfilPressionado(self):
        self.stackedWidget.setCurrentIndex(0)

    def quandoBotaoUsuariopressionado(self):
        self.stackedWidget.setCurrentIndex(1)

    def quandoBotaoChamadoPresionado(self):
        self.stackedWidget.setCurrentIndex(2)

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    with open(r"Telas\scr\style\Style.qss","r") as style_file:
        style_str = style_file.read()
    app.setStyleSheet(style_str)
    window = Main_tecnico()
    window.show()
    app.exec()