import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt

class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Product Manager")
        self.setWindowIcon(QIcon('icons/icon.ico'))
        self.setGeometry(450, 150, 1350, 750)
        self.setFixedSize(self.size())

        self.UI()
        self.show()

    def UI(self):
        self.toolBar()
        self.tabWidget()
        self.widgets()
        self.layouts()

    def toolBar(self):
        self.tb = self.addToolBar("Tool Bar")
        self.tb.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        ############Toolbar Buttons##########
        ############Add Product##############
        self.addProduct = QAction(QIcon('icons/add.png'), "Add Product", self)
        self.tb.addAction(self.addProduct)
        self.tb.addSeparator()
        ############Add Member##############
        self.addMember = QAction(QIcon('icons/users.png'), "Add Memeber", self)
        self.tb.addAction(self.addMember)
        self.tb.addSeparator()
        ############Selling##############
        self.sellProduct = QAction(QIcon('icons/sell.png'), "Sell Product", self)
        self.tb.addAction(self.sellProduct)
        self.tb.addSeparator()

    def tabWidget(self):
        self.tabs = QTabWidget()
        self.setCentralWidget(self.tabs)
        self.tab1 = QWidget()
        self.tab2 = QWidget()
        self.tab3 = QWidget()
        self.tabs.addTab(self.tab1, "Products")
        self.tabs.addTab(self.tab2, "Members")
        self.tabs.addTab(self.tab3, "Statistics")


    def widgets(self):
        ############Tab 1 Widgets##############
        ############Main Left Layout Widget##############
        self.prodcutTable = QTableWidget()
        self.prodcutTable.setColumnCount(6)
        # Hide the column product id
        self.prodcutTable.setColumnHidden(0, True)
        self.prodcutTable.setHorizontalHeaderItem(0, QTableWidgetItem("Product ID"))
        self.prodcutTable.setHorizontalHeaderItem(1, QTableWidgetItem("Product Name"))
        self.prodcutTable.setHorizontalHeaderItem(2, QTableWidgetItem("Manufacture"))
        self.prodcutTable.setHorizontalHeaderItem(3, QTableWidgetItem("Price"))
        self.prodcutTable.setHorizontalHeaderItem(4, QTableWidgetItem("Quota"))
        self.prodcutTable.setHorizontalHeaderItem(5, QTableWidgetItem("Availability"))
        ############Right Top Layout Widget##############
        self.searchText = QLabel("Search")
        self.searchEntry = QLineEdit()
        self.searchEntry.setPlaceholderText("Search for products")
        self.searchButton = QPushButton("Search")
        ############Right Middle Layout Widget##############
        self.allProduct = QRadioButton("All Products")
        self.availableProduct = QRadioButton("Available")
        self.notAvailableProduct = QRadioButton("Not Available")
        self.listButton = QPushButton("List")





    def layouts(self):
        ############Tab1 Layout##############
        self.mainLayout = QHBoxLayout()
        self.mainLeftLayout = QVBoxLayout()
        self.mainRightLayout = QVBoxLayout()
        self.rightTopLayout = QHBoxLayout()
        self.rightMiddleLayout = QHBoxLayout()
        #self.rightBottomLayout = QVBoxLayout()
        self.topGroupBox = QGroupBox("Search Box")
        self.middleGroupBox = QGroupBox("List Box")
        #self.bottomGroupBox = QGroupBox("Product Image")

        ############Add Widgets##############
        ############Left Main Layout Widgets##############
        self.mainLeftLayout.addWidget(self.prodcutTable)

        ############Right Top Layout Widgets##############
        self.rightTopLayout.addWidget(self.searchText)
        self.rightTopLayout.addWidget(self.searchEntry)
        self.rightTopLayout.addWidget(self.searchButton)
        self.topGroupBox.setLayout(self.rightTopLayout)

        ############Right Middle Layout Widget##############
        self.rightMiddleLayout.addWidget(self.allProduct)
        self.rightMiddleLayout.addWidget(self.availableProduct)
        self.rightMiddleLayout.addWidget(self.notAvailableProduct)
        self.rightMiddleLayout.addWidget(self.listButton)
        self.middleGroupBox.setLayout(self.rightMiddleLayout)


        self.mainRightLayout.addWidget(self.topGroupBox)
        self.mainRightLayout.addWidget(self.middleGroupBox)
        self.mainLayout.addLayout(self.mainLeftLayout, 70)
        self.mainLayout.addLayout(self.mainRightLayout, 30)
        self.tab1.setLayout(self.mainLayout)






def main():
    App = QApplication(sys.argv)
    window = Main()
    sys.exit(App.exec_())

if __name__ == '__main__':
    main()

