import sys
from PySide6 import QtWidgets
from Telas.ui_menu_usuario import Ui_Usuario
from Conexao import executar_sql

class Main_usuario(QtWidgets.QMainWindow, Ui_Usuario):
    def __init__(self):
        super(Main_usuario,self).__init__()
        self.setupUi(self)
        self.apenasIcone.hide()
        self.stackedWidget.setCurrentIndex(0)
        self.btn_perfil.setChecked(True)
        self.btn_perfil.clicked.connect(self.quandoBotaoPerfilPressionado)
        self.btn_perfil_aberto.clicked.connect(self.quandoBotaoPerfilPressionado)
        self.btn_chamado.clicked.connect(self.quandoBotaoChamadoPresionado)
        self.btn_chamados_aberto.clicked.connect(self.quandoBotaoChamadoPresionado)

        
    def quandoBotaoPerfilPressionado(self):
        self.stackedWidget.setCurrentIndex(0)
    def quandoBotaoChamadoPresionado(self):
        self.stackedWidget.setCurrentIndex(1)
    
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    with open(r"Telas\scr\style\Style.qss","r") as style_file:
        style_str = style_file.read()
    app.setStyleSheet(style_str)
    window = Main_usuario()
    window.show()
    app.exec()