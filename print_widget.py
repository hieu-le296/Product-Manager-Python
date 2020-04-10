from PyQt5.QtCore import Qt
from PyQt5.QtPrintSupport import QPrinter, QPrintPreviewDialog
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import sqlite3

sqlConnect = sqlite3.connect("products.db")
cur = sqlConnect.cursor()

class Print(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Print Preview")
        self.setWindowIcon(QIcon('icons/printer.svg'))
        self.setGeometry(850, 450, 250, 180)
        self.setFixedSize(self.size())
        self.widgets()
        self.layouts()
        self.setWindowIcon(QIcon('icons/printer.svg'))
        self.show()

    def widgets(self):
        self.text = QLabel("Select one option", self)
        self.product = QRadioButton("Products", self)
        self.product.setChecked(True)
        self.member = QRadioButton("Membership", self)
        self.selling = QRadioButton('Selling History', self)
        self.printBtn = QPushButton("Open Print Dialog", self)
        self.printBtn.clicked.connect(self.printPreviewDialog)
        self.setStyleSheet("QLabel {font-size: 15px} QRadioButton {font-size: 12px}")

    def layouts(self):
        self.mainLayout = QVBoxLayout()
        self.topLayout = QVBoxLayout()
        self.bottomLayout = QFormLayout()
        self.topFrame = QFrame()

        self.topLayout.addWidget(self.text)
        self.topLayout.addWidget(self.product)
        self.topLayout.addWidget(self.member)
        self.topLayout.addWidget(self.selling)
        self.topLayout.addWidget(self.printBtn)
        self.topLayout.setAlignment(Qt.AlignCenter)
        self.topFrame.setLayout(self.topLayout)


        self.mainLayout.addWidget(self.topFrame)
        self.setLayout(self.mainLayout)



    def printPreviewDialog(self):
        printer = QPrinter(QPrinter.HighResolution)
        previewDialog = QPrintPreviewDialog(printer, self)
        previewDialog.paintRequested.connect(self.printPreview)
        previewDialog.exec_()

    def printPreview(self, printer):
        self.textEdit = QTextEdit(self)
        if self.product.isChecked():
            products = cur.execute(
                "SELECT product_id, product_name, product_manufacturer, product_price, product_quota, product_date, product_availability FROM products")
            self.textEdit.append(
                "                                                                              Product List        ")
            for product in products:
                product_id = product[0]
                product_name = product[1]
                product_manu = product[2]
                product_price = product[3]
                product_quota = product[4]
                product_date = product[5]
                product_status = product[6]
                self.textEdit.append("Product ID: " + str(product_id))
                self.textEdit.append("Product Name: " + product_name)
                self.textEdit.append("Manufacturer: " + product_manu)
                self.textEdit.append("Price: $" + str(product_price))
                self.textEdit.append("Quantity: " + str(product_quota))
                self.textEdit.append("Date Added: " + str(product_date))
                self.textEdit.append("Status: " + product_status)
                self.textEdit.append("-----------------------------------------------------")
        elif self.member.isChecked():
            members = cur.execute("SELECT * FROM members")
            self.textEdit.append(
                "                                                                                  Membership List        ")
            for member in members:
                member_id = member[0]
                member_fname = member[1]
                member_lname = member[2]
                member_phone = member[3]
                member_addr = member[4]
                self.textEdit.append("Member ID: " + str(member_id))
                self.textEdit.append("First name: " + member_fname)
                self.textEdit.append("Last name: " + str(member_lname))
                self.textEdit.append("Phone number: " + str(member_phone))
                self.textEdit.append("Address: " + str(member_addr))
                self.textEdit.append("-----------------------------------------------------")

        elif self.selling.isChecked():
            query ="SELECT products.product_name, products.product_manufacturer, products.product_price, members.member_fname, sellings.selling_quantity, sellings.selling_amount, sellings.selling_date FROM products, members, sellings WHERE products.product_id = sellings.selling_product_id AND members.member_id = sellings.selling_member_id"
            history = cur.execute(query).fetchall()
            self.textEdit.append("                                                                               Selling History        ")
            for record in history:
                product_name = record[0]
                product_manu = record[1]
                product_price = record[2]
                member_name = record[3]
                selling_quantity = record[4]
                selling_amount = record[5]
                selling_date = record[6]
                self.textEdit.append("Product Name: " + product_name)
                self.textEdit.append("Manufacturer: " + product_manu)
                self.textEdit.append("Product Price: $" + str(product_price))
                self.textEdit.append("Selling to: " + member_name)
                self.textEdit.append("Quantity: " + str(selling_quantity))
                self.textEdit.append("Amount: $" + str(selling_amount))
                self.textEdit.append("Date Sold: " + str(selling_date))
                self.textEdit.append("-----------------------------------------------------")

        self.textEdit.document().print_(printer)

