import sys
from PySide6 import QtWidgets
from Telas.ui_Login import Ui_login
from Conexao import executar_sql
from Entities.Usuario import Usuario
class Main_login(QtWidgets.QMainWindow, Ui_login):
    def __init__(self):
        super(Main_login,self).__init__()
        self.setupUi(self)
        self.BtnEntrar.clicked.connect(self.valida_login)
        self.usuario = None
        self.edtSenha.setText("senha123")
        self.edtUsuario.setText("daniel.oliveira ")

    def valida_login(self):
        senha = self.edtSenha.text()
        login = self.edtUsuario.text()
        usuario = Usuario.buscar_por_email_senha(login,senha)
        if usuario:
            if usuario.cargo.idCargo == 1:
                from main_menu_tecnico import Main_tecnico
                self.validou.setStyleSheet("color: rgb(100, 243, 29);")
                self.validou.setText("Logado com sucesso")
                self.tecnico = Main_tecnico(usuario)
                self.tecnico.show()
                self.close()
            else:
                from main_menu_usuario import Main_usuario
                self.validou.setStyleSheet("color: rgb(100, 243, 29);")
                self.validou.setText("Logado com sucesso")
                self.usuario = Main_usuario(usuario)
                self.usuario.show()
                self.close()
        else:
            self.validou.setStyleSheet("color: rgb(243, 232, 228);")
            self.validou.setText("Usuario ou senha incorretos")

if __name__ == '__main__':

    app = QtWidgets.QApplication(sys.argv)
    window = Main_login()
    window.show()
    app.exec()