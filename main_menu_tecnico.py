import sys
from PySide6 import QtWidgets
from Telas.ui_menu_tecnico import Ui_tecnico
from Entities.Chamados import Chamado
from Entities.Usuario import Usuario
from Entities.Setor import Setor
from Entities.Cargo import Cargo
from main_alterar_chamado import Main_alterar
from main_fechar_chamado import Main_fechar
from main_abrir_chamado import Main_Abrir
from main_cadastro_usuario import Main_cadastro_usuario
from PySide6.QtWidgets import QMessageBox
from Conexao import executar_sql

class Main_tecnico(QtWidgets.QMainWindow, Ui_tecnico):
    def __init__(self, user = None):
        super(Main_tecnico,self).__init__()
        self.user = user
        self.setupUi(self)
        self.stackedWidget.setCurrentIndex(0)
        self.listaChamados = []
        self.listaUsuarios = []
        self.chamadoSelecionado = None

        self.btn_perfil_aberto.setChecked(True)
        self.btn_perfil_aberto.clicked.connect(self.quandoBotaoPerfilPressionado)
        self.btn_chamados_aberto.clicked.connect(self.quandoBotaoChamadoPresionado)
        self.btn_usuarios.clicked.connect(self.quandoBotaoUsuariopressionado)

        self.BtnAlterarChamado.clicked.connect(self.quandoBotaoAlterarPresionado)
        self.BtnFecharChamado.clicked.connect(self.quandoBotaoFecharPresionado)
        self.BtnAbrirChamado.clicked.connect(self.quandoBotaoAbrirPresionado)
        self.BtnCadastrarUsuario.clicked.connect(self.quandoBotaoCadastrarUsuario)
        self.BtnEditar.clicked.connect(self.quandoBotaoEditarUsuarioPressionado)
        self.BtnLogoff.clicked.connect(self.quandoBotaLogoffPresionado)
        self.BtnAtualizarUsuario.clicked.connect(self.quandoBotaoAtualizarUsuarioPressionado)

        self.montarTabelaChamados()
        self.montarTabelaUsuarios()
        self.montarPerfil()

    def montarPerfil(self):
        self.LB_login.setText(self.user.login)
        self.LB_email_2.setText(self.user.nome)
        self.LB_email.setText(self.user.email)
        self.LB_cargo.setText(self.user.cargo.cargo)
        self.LB_setor.setText(self.user.setor.nome_setor)

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
            self.TB_Chamados_usuario.setItem(linha, 3, QtWidgets.QTableWidgetItem(str(chamado.buscarPorServico(chamado.servico_idServico))))
            self.TB_Chamados_usuario.setItem(linha, 4, QtWidgets.QTableWidgetItem(str(chamado.titulo)))
            self.TB_Chamados_usuario.setItem(linha, 5, QtWidgets.QTableWidgetItem(str(chamado.descricao)))
            self.TB_Chamados_usuario.setItem(linha, 6, QtWidgets.QTableWidgetItem(str(Usuario.buscarPorUsuario(chamado.usuario_abertura))))
            self.TB_Chamados_usuario.setItem(linha, 7, QtWidgets.QTableWidgetItem(str(Usuario.buscarPorUsuario(chamado.usuario_atendimento))))
            self.TB_Chamados_usuario.setItem(linha, 8, QtWidgets.QTableWidgetItem(str(chamado.dataAbertura)))
            self.TB_Chamados_usuario.setItem(linha, 9, QtWidgets.QTableWidgetItem(str(chamado.dataDeFechamento)))
            linha+=1


    def quandoBotaoPerfilPressionado(self):
        self.stackedWidget.setCurrentIndex(0)

    def quandoBotaoUsuariopressionado(self):
        self.stackedWidget.setCurrentIndex(1)

    def quandoBotaoChamadoPresionado(self):
        self.stackedWidget.setCurrentIndex(2)

    def quandoBotaoCadastrarUsuario(self):
        self.cadastrar = Main_cadastro_usuario()
        self.cadastrar.show()
        self.cadastrar.closed.connect(self.montarTabelaUsuarios)

    def quandoBotaoEditarUsuarioPressionado(self):
        self.editar = Main_cadastro_usuario(self.user)
        self.editar.show()
        self.editar.closed.connect(self.montarTabelaUsuarios)

    def quandoBotaoAlterarPresionado(self):
        if self.TB_Chamados_usuario.currentRow() < 0:
            QMessageBox.warning(self, "Erro", "nenhum item selecionado")
        else:
            item = self.TB_Chamados_usuario.currentRow()
            self.chamadoSelecionado = self.listaChamados[item]
            chamado = self.chamadoSelecionado
            self.alterar = Main_alterar(chamado)
            self.alterar.show()
            self.alterar.closed.connect(self.montarTabelaChamados)

    def quandoBotaoFecharPresionado(self):
        if self.TB_Chamados_usuario.currentRow() < 0:
            QMessageBox.warning(self, "Erro", "nenhum item selecionado")
        else:
            item = self.TB_Chamados_usuario.currentRow()
            self.chamadoSelecionado = self.listaChamados[item]
            chamado = self.chamadoSelecionado
            self.fechar = Main_fechar(chamado,self.user)
            self.fechar.show()
            self.fechar.closed.connect(self.montarTabelaChamados)

    def quandoBotaoAtualizarUsuarioPressionado(self):
        if self.tableWidget.currentRow() < 0:
            QMessageBox.warning(self, "Erro", "nenhum item selecionado")
        else:
            item = self.tableWidget.currentRow()
            usuarioSelecionado = self.listaUsuarios[item]
            setor = Setor.buscarUm(usuarioSelecionado.setor)
            cargo = Cargo.buscarUm(usuarioSelecionado.cargo)
            usuarioSelecionado.setor = setor
            usuarioSelecionado.cargo = cargo
            self.atualizarUsuario = Main_cadastro_usuario(usuarioSelecionado)
            self.atualizarUsuario.show()
            self.atualizarUsuario.closed.connect(self.montarTabelaUsuarios)

    def quandoBotaoAbrirPresionado(self):
            self.abrir = Main_Abrir(self.user)
            self.abrir.show()
            self.abrir.closed.connect(self.montarTabelaChamados)
    def quandoBotaLogoffPresionado(self):
        from Entities.teste.Teste_usuario import Main_login
        self.login = Main_login()
        self.login.show()
        self.close()



if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    with open(r"Telas\scr\style\Style.qss","r") as style_file:
        style_str = style_file.read()
    app.setStyleSheet(style_str)
    window = Main_tecnico()
    window.show()
    app.exec()