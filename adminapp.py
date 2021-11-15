from PyQt5 import QtWidgets
import sys
from interfaces import interface, create, delete, del_char, del_prod, del_type, new_char, new_prod, new_type
from database import db, query, create_db

create_db()


class AdminApp(QtWidgets.QMainWindow):
    def __init__(self):
        super(AdminApp, self).__init__()
        self.ui = interface.Ui_MainWindow()
        self.ui.setupUi(self)
        self.init_UI()

    def init_UI(self):
        self.setWindowTitle('Admin.app')
        self.ui.pushButton.clicked.connect(self.create)
        self.ui.pushButton_2.clicked.connect(self.delete)
        self.ui.pushButton_4.clicked.connect(sys.exit)

    def back_menu(self):
        self.ui = interface.Ui_MainWindow()
        self.ui.setupUi(self)
        self.init_UI()

# Create------------------------------------------------

    def create(self):
        self.ui = create.Create()
        self.ui.setupUi(self)
        self.setWindowTitle('Admin.app')
        self.ui.pushButton.clicked.connect(self.show_nc)
        self.ui.pushButton_2.clicked.connect(self.show_pr)
        self.ui.pushButton_3.clicked.connect(self.show_tp)
        self.ui.pushButton_4.clicked.connect(self.back_menu)

    def show_nc(self):
        self.ui = new_char.New_char()
        self.ui.setupUi(self)
        self.setWindowTitle('Admin.app')
        self.ui.pushButton_4.clicked.connect(self.create)
        self.ui.pushButton.clicked.connect(self.get_lineEdit)

    def show_tp(self):
        self.ui = new_type.New_type()
        self.ui.setupUi(self)
        self.setWindowTitle('Admin.app')
        self.ui.pushButton_4.clicked.connect(self.create)
        self.ui.pushButton.clicked.connect(self.get_lineEdit)

    def show_pr(self):
        self.ui = new_prod.New_prod()
        self.ui.setupUi(self)
        self.setWindowTitle('Admin.app')
        self.ui.pushButton_4.clicked.connect(self.create)
        self.ui.pushButton.clicked.connect(self.get_lineEdit_prod)

    def get_lineEdit(self):
        name = [self.ui.lineEdit.text()]
        if self.ui.label_3.text() == 'Имя персонажа':
            query.execute(""" INSERT INTO character(name) VALUES(?) """, name)
            db.commit()
        elif self.ui.label_3.text() == 'Название':
            query.execute(""" INSERT INTO product_type(name) VALUES(?) """, name)
            db.commit()
        print(name)
        self.ui.lineEdit.clear()

    def get_lineEdit_prod(self):
        values = [self.ui.lineEdit.text(), self.ui.lineEdit_2.text(),
                  self.ui.lineEdit_3.text(), self.ui.lineEdit_4.text()]
        query.execute(""" INSERT INTO product(name, link, char, type) VALUES(?, ?, ?, ?) """, values)
        db.commit()
        print(values)

# Delete---------------------------------------------------------

    def delete(self):
        self.ui = delete.Delete()
        self.ui.setupUi(self)
        self.setWindowTitle('Admin.app')
        self.ui.pushButton.clicked.connect(self.show_dc)
        self.ui.pushButton_2.clicked.connect(self.show_dpr)
        self.ui.pushButton_3.clicked.connect(self.show_dtp)
        self.ui.pushButton_4.clicked.connect(self.back_menu)

    def show_dc(self):
        self.ui = del_char.Del_char()
        self.ui.setupUi(self)
        self.setWindowTitle('Admin.app')
        self.ui.pushButton_4.clicked.connect(self.delete)
        self.ui.pushButton.clicked.connect(self.get_combox)
        self.forcomb = query.execute(""" SELECT name FROM character """).fetchall()
        combolist = []
        for i in self.forcomb:
            combolist.append(str(i[0]))
        self.ui.comboBox.addItems(combolist)

    def show_dpr(self):
        self.ui = del_prod.Del_prod()
        self.ui.setupUi(self)
        self.setWindowTitle('Admin.app')
        self.ui.pushButton_4.clicked.connect(self.delete)
        self.ui.pushButton.clicked.connect(self.get_combox)
        self.forcomb = query.execute(""" SELECT name FROM product """).fetchall()
        combolist = []
        for i in self.forcomb:
            combolist.append(str(i[0]))
        self.ui.comboBox.addItems(combolist)

    def show_dtp(self):
        self.ui = del_type.Del_type()
        self.ui.setupUi(self)
        self.setWindowTitle('Admin.app')
        self.ui.pushButton_4.clicked.connect(self.delete)
        self.ui.pushButton.clicked.connect(self.get_combox)
        self.forcomb = query.execute(""" SELECT name FROM product_type """).fetchall()
        combolist = []
        for i in self.forcomb:
            combolist.append(str(i[0]))
        self.ui.comboBox.addItems(combolist)

    def get_combox(self):
        if self.ui.label_3.text() == 'Имя персонажа':
            name = [self.ui.comboBox.currentText()]
            query.execute(""" DELETE from character WHERE name = ?""", name)
            db.commit()
            query.execute(""" DELETE from product  WHERE char = ?""", name)
            db.commit()

        elif self.ui.label_3.text() == 'Название товара':
            name = [self.ui.comboBox.currentText()]
            query.execute(""" DELETE from product WHERE name = ?""", name)
            db.commit()

        elif self.ui.label_3.text() == 'Название':
            name = [self.ui.comboBox.currentText()]
            query.execute(""" DELETE from product_type WHERE name = ?""", name)
            db.commit()
            query.execute(""" DELETE from product  WHERE type = ?""", name)
            db.commit()


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    interf = AdminApp()
    interf.show()

    sys.exit(app.exec())
