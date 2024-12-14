import sys
from PySide6 import QtWidgets, QtCore
from Telas.ui_menu_cadastro_usuario import Ui_MainWindow
from Entities.Cargo import Cargo
from Entities.Setor import Setor

from Conexao import executar_sql

class Main_usuario(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(Main_usuario,self).__init__()
        self.setupUi(self)
        self.lista_cargo = []
        self.cargo_combo = []  # só pra exibir o combo
        self.lista_setor = []
        self.setor_combo = []
        self.montar_combo_boxes()

    def buscar_cargo(self):
        try:
            cargo = Cargo()
            self.lista_cargo = Cargo.buscar(cargo)
            for item in self.lista_cargo:
                self.cargo_combo.append(item.cargo)
            print("Busca dos cursos realizada com sucesso")
        except Exception as erro:
            print("Erro ao buscar")
            print(erro)

    def buscar_setor(self):
        try:
            setor = Setor()
            self.lista_setor = Setor.buscar(setor)
            for item in self.lista_setor:
                self.setor_combo.append(item.nome_setor)
            print("Busca dos cursos realizada com sucesso")
        except Exception as erro:
            print("Erro ao buscar")
            print(erro)

    def montar_combo_boxes(self):
        self.buscar_cargo()
        self.buscar_setor()
        self.CB_Cargo.addItems(self.cargo_combo)
        self.CB_Setor.addItems(self.setor_combo)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    with open(r"Telas\scr\style\Style.qss","r") as style_file:
        style_str = style_file.read()
    app.setStyleSheet(style_str)
    window = Main_usuario()
    window.show()
    app.exec()