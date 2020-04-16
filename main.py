from  PyQt5  import  QtWidgets ,  uic 
import  sys
from CriptNDD import EncryptPW


class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__() 
        uic.loadUi('mainwindow.ui', self) # Carregar UI

        self.result = None 

        #### Encontrando labels ####

        self.GetPrintJobsBtn = self.findChild(QtWidgets.QPushButton, 'GetPrintJobsBtn')
        self.GetPrintJobsBtn.clicked.connect(self.GetPrintJobsUI) 

        self.labelResult = self.findChild(QtWidgets.QLabel, 'labelResult') 

        self.ExportCsvBtn = self.findChild(QtWidgets.QPushButton, 'ExportCsvBtn')

        self.labelDateStartResult = self.findChild(QtWidgets.QLabel, 'labelDateStartResult')
        self.labelWsResult = self.findChild(QtWidgets.QLabel, 'labelWsResult')  
 


        ##### READING INPUTS ##### 

        self.inputEnterprise = self.findChild(QtWidgets.QLineEdit, 'inputEnterprise') 
        self.inputEnterpriseKey = self.findChild(QtWidgets.QLineEdit, 'inputEnterpriseKey') 
        self.inputDate = self.findChild(QtWidgets.QLineEdit, 'inputDate') 
        self.inputDomain = self.findChild(QtWidgets.QLineEdit, 'inputDomain') 
        self.inputLogon = self.findChild(QtWidgets.QLineEdit, 'inputLogon') 
        self.inputPW = self.findChild(QtWidgets.QLineEdit, 'inputPW') 
        self.inputCsvPath = self.findChild(QtWidgets.QLineEdit, 'inputCsvPath') 
        

        self.show() # Mostrar interface

    def printButtonPressed(self):
        print('printButtonPressed')

    def AlterResultText(self):
        self.labelResult.setText("Alterado")

    def PrintInputValue(self):
        print(self.inputEnterprise.text())




app = QtWidgets.QApplication(sys.argv)
window = Ui()
app.exec_()