import sys
from PySide6 import QtWidgets
from Telas.ui_Login import Ui_login
from Conexao import executar_sql
from main_menu_usuario import Main_usuario
from main_menu_tecnico import Main_tecnico

class Main_login(QtWidgets.QMainWindow, Ui_login):
    def __init__(self):
        super(Main_login,self).__init__()
        self.setupUi(self)
        self.BtnEntrar.clicked.connect(self.valida_login)

    def valida_login(self):
        senha = self.edtSenha.text()
        usuario = self.edtUsuario.text()
        sql = f"select login,senha,cargo_idcargo from usuario where login = '{usuario}' and senha = '{senha}'"
        quarry = executar_sql(sql)
        print(quarry)
        print(quarry[0][2])
        if quarry:
            if quarry[0][2] == 1:
                self.validou.setStyleSheet("color: rgb(100, 243, 29);")
                self.validou.setText("Logado com sucesso")
                self.tecnico = Main_tecnico()
                self.tecnico.show()
                self.close()
            else:
                self.validou.setStyleSheet("color: rgb(100, 243, 29);")
                self.validou.setText("Logado com sucesso")
                self.usuario = Main_usuario()
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