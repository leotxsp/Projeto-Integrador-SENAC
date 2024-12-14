import sys
from PySide6 import QtWidgets
from Telas.ui_menu_tecnico import Ui_tecnico 
from Conexao import executar_sql

class Main_tecnico(QtWidgets.QMainWindow, Ui_tecnico):
    def __init__(self):
        super(Main_tecnico,self).__init__()
        self.setupUi(self)
        self.stackedWidget.setCurrentIndex(0)
        self.btn_perfil_aberto.setChecked(True)
        self.btn_perfil_aberto.clicked.connect(self.quandoBotaoPerfilPressionado)
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
    window = Main_tecnico()
    window.show()
    app.exec()