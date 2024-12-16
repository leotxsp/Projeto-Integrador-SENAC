import sys
from PySide6 import QtWidgets

from Entities.Cargo import Cargo
from Telas.ui_menu_usuario import Ui_Usuario
from Entities.Usuario import Usuario
from Entities.Chamados import Chamado
from Conexao import executar_sql

class Main_usuario(QtWidgets.QMainWindow, Ui_Usuario):
    def __init__(self,user = None):
        super(Main_usuario,self).__init__()
        self.setupUi(self)
        self.user = user
        self.listaChamados = []
        self.stackedWidget.setCurrentIndex(0)
        self.btn_perfil_aberto.setChecked(True)
        self.btn_perfil_aberto.clicked.connect(self.quandoBotaoPerfilPressionado)
        self.btn_chamados_aberto.clicked.connect(self.quandoBotaoChamadoPresionado)
        self.montarPerfil()
        self.montarTabelaChamados()

    def montarPerfil(self):
        self.LB_login.setText(self.user.login)
        self.LB_email_2.setText(self.user.nome)
        self.LB_email.setText(self.user.email)
        self.LB_cargo.setText(self.user.cargo.cargo)
        self.LB_setor.setText(self.user.setor.nome_setor)

    def quandoBotaoPerfilPressionado(self):
        self.stackedWidget.setCurrentIndex(0)
    def quandoBotaoChamadoPresionado(self):
        self.stackedWidget.setCurrentIndex(1)




    def buscarChamados(self):
        try:
            chamados = Chamado()
            self.listaChamados = chamados.buscarPorUsuario(self.user.IDusuario)
            print("Busca realizada com sucesso")
        except Exception as erro:
            print("Erro ao buscar alunos")
            print(erro)

    def montarTabelaChamados(self):
        self.buscarChamados()
        linha = 0
        self.TB_Chamados_usuario.setRowCount(len(self.listaChamados))
        for chamado in self.listaChamados:
            self.TB_Chamados_usuario.setItem(linha, 0, QtWidgets.QTableWidgetItem(str(chamado.status)))
            self.TB_Chamados_usuario.setItem(linha, 1, QtWidgets.QTableWidgetItem(str(chamado.prioridade)))
            self.TB_Chamados_usuario.setItem(linha, 2, QtWidgets.QTableWidgetItem(str(chamado.titulo)))
            self.TB_Chamados_usuario.setItem(linha, 3, QtWidgets.QTableWidgetItem(str(chamado.descricao)))
            self.TB_Chamados_usuario.setItem(linha, 4, QtWidgets.QTableWidgetItem(str(user.nome)))
            self.TB_Chamados_usuario.setItem(linha, 6, QtWidgets.QTableWidgetItem(str(chamado.dataAbertura)))
            self.TB_Chamados_usuario.setItem(linha, 7, QtWidgets.QTableWidgetItem(str(chamado.dataDeFechamento)))
            linha+=1


















    
if __name__ == '__main__':
    login = "paulo.gomes"
    senha = "senha123"
    user = Usuario.buscar_por_email_senha(login, senha)
    print(user)
    if user:
        print("Usuário encontrado:")
        print(f"ID: {user.IDusuario}")
        print(f"Login: {user.login}")
        print(f"Nome: {user.nome}")
        print(f"Email: {user.email}")
        print(f"Setor: {user.setor.idsetor}")  # Acessando o atributo 'nome' do objeto Setor
        print(f"Cargo: {user.cargo.idCargo}")  # Acessando o atributo 'nome' do objeto Cargo
    else:
        print("Usuário não encontrado ou credenciais inválidas.")


    app = QtWidgets.QApplication(sys.argv)
    with open(r"Telas\scr\style\Style.qss","r") as style_file:
        style_str = style_file.read()
    app.setStyleSheet(style_str)
    window = Main_usuario(user)
    window.show()
    app.exec()