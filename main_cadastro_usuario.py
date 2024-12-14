import sys
from PySide6 import QtWidgets, QtCore
from Telas.ui_menu_cadastro_usuario import Ui_cadastroUsuario
from Entities.Cargo import Cargo
from Entities.Setor import Setor
from Entities.Usuario import Usuario
from PySide6.QtWidgets import QMessageBox
from main_login import Main_login
from Conexao import executar_sql

class Main_usuario(QtWidgets.QMainWindow, Ui_cadastroUsuario):
    def __init__(self):
        super(Main_usuario,self).__init__()
        self.setupUi(self)
        self.lista_cargo = []
        self.cargo_combo = []
        self.lista_setor = []
        self.setor_combo = []
        self.montar_combo_boxes()
        self.BTcadastrar.clicked.connect(self.incluir)

    def incluir(self):
        try:
            if not self.validar_campos():
                return
            login = self.LElogin.text()
            nome = self.LEnome.text()
            email = self.LEemail.text()
            senha = self.LEsenha.text()
            index_cargo = self.CB_Cargo.currentIndex()
            index_setor = self.CB_Setor.currentIndex()
            cargo = self.lista_cargo[index_cargo]
            setor = self.lista_setor[index_setor]
            usuario = Usuario(0,login=login,nome=nome,email=email,senha=senha,setor=setor,cargo=cargo)
            usuario.incluir()
            QMessageBox.warning(self, "SUCESSO", "Usuario cadastrado com sucesso.")
            self.login = Main_login()
            self.login.show()
            self.close()
        except Exception as erro:
            print("Erro ao inserir")
            print(erro)

    def validar_campos(self):
        if not self.LElogin.text():
            QMessageBox.warning(self, "Erro de Validação", "O campo 'login' deve ser preenchido.")
            return False
        if not self.LEnome.text():
            QMessageBox.warning(self, "Erro de Validação", "O campo 'nome' deve ser preenchido.")
            return False
        if not self.LEsenha.text():
            QMessageBox.warning(self, "Erro de Validação", "O campo 'senha' deve ser preenchido.")
            return False
        if not self.LEconfirmarSenha.text():
            QMessageBox.warning(self, "Erro de Validação", "O campo 'confirmar senha' deve ser preenchido.")
            return False
        if not self.LEemail.text():
            QMessageBox.warning(self, "Erro de Validação", "O campo 'email' deve ser preenchido.")
            return False
        if self.CB_Cargo.currentIndex() == -1:
            QMessageBox.warning(self, "Erro de Validação", "Um cargo deve ser selecionado.")
            return False
        if self.CB_Setor.currentIndex() == -1:
            QMessageBox.warning(self, "Erro de Validação", "Um setor deve ser selecionado.")
            return False
        if self.LEsenha.text() != self.LEconfirmarSenha.text():
            QMessageBox.warning(self, "Erro de Validação", "As senhas deve ser iguais")
            return False
        return True


    def buscar_cargo(self):
        try:
            cargo = Cargo()
            self.lista_cargo = Cargo.buscar(cargo)
            for item in self.lista_cargo:
                self.cargo_combo.append(item.cargo)
        except Exception as erro:
            print("Erro ao buscar")
            print(erro)

    def buscar_setor(self):
        try:
            setor = Setor()
            self.lista_setor = Setor.buscar(setor)
            for item in self.lista_setor:
                self.setor_combo.append(item.nome_setor)
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