from PyQt5 import QtCore, QtGui,QtWidgets, uic
import matplotlib
import matplotlib.pyplot as plt
matplotlib.use('Qt5Agg')
from PyQt5.QtWidgets import QFileDialog
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg, NavigationToolbar2QT as Navi
from matplotlib.figure import Figure
import seaborn as sns
import pandas as pd
import sip
import io
import os
import csv
import sys
from Crud.CrudUsers import CrudUser
from PyQt5.QtWidgets import QMessageBox
from PyQt5 import QtWidgets, uic
from PyQt5.QtCore import Qt
from messagebox import msg_about, msg_error
import sqlite3 as sql
import logo_sipromind_rc
import mina_oxid_rc



# iniciar app
app = QtWidgets.QApplication([])

#base de datos usada
base_datos = "base de datos sipropanel.db"

# cargar archivos .ui
login = uic.loadUi("Ui/n00_login_principal.ui")
error = uic.loadUi("Ui/n00_login_error.ui")
procesos = uic.loadUi("Ui/n00_login_procesos.ui")
register = uic.loadUi("Ui/n00_login_register.ui")

EDA_oxid = uic.loadUi("Ui/EDA_oxid.ui")
EDA_base_oxid = uic.loadUi("Ui/EDA_base_oxid.ui")
EDA_scatter_oxid = uic.loadUi("Ui/EDA_scatter_oxid.ui")

##NUEVO
EDA_kernel_oxid = uic.loadUi("Ui/EDA_kernel_oxid.ui")
EDA_plotcorr_oxid = uic.loadUi("Ui/EDA_plotcorr_oxid.ui")

sulf=uic.loadUi("Ui/n01_principal_sulfurados.ui")
sulf_perfo = uic.loadUi("Ui/n02_procesos_sulf_01perforacion2.ui")
sulf_carguio = uic.loadUi("Ui/n02_procesos_sulf_02carguio2.ui")
sulf_chancado = uic.loadUi("Ui/n02_procesos_sulf_03chancado2.ui")
sulf_flotacion = uic.loadUi("Ui/n02_procesos_sulf_04flotacion2.ui")
sulf_espconc = uic.loadUi("Ui/n02_procesos_sulf_05espconcentrado2.ui")
sulf_esprelave = uic.loadUi("Ui/n02_procesos_sulf_06esprelave2.ui")

oxid=uic.loadUi("Ui/n01_principal_oxidados.ui")
oxid_perfo = uic.loadUi("Ui/n02_procesos_oxid_01perforacion2.ui")
oxid_carguio = uic.loadUi("Ui/n02_procesos_oxid_02carguio2.ui")
oxid_chancado = uic.loadUi("Ui/n02_procesos_oxid_03chancado2.ui")
oxid_lixiviacion = uic.loadUi("Ui/n02_procesos_oxid_04lixiviacion2.ui")
oxid_SX = uic.loadUi("Ui/n02_procesos_oxid_05SX2.ui")
oxid_EW = uic.loadUi("Ui/n02_procesos_oxid_06EW2.ui")


sulf_perfo.spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
sulf_perfo.verticalLayout.addItem(sulf_perfo.spacerItem1)
sulf_carguio.spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
sulf_carguio.verticalLayout.addItem(sulf_carguio.spacerItem1)
sulf_chancado.spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
sulf_chancado.verticalLayout.addItem(sulf_chancado.spacerItem1)
sulf_flotacion.spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
sulf_flotacion.verticalLayout.addItem(sulf_flotacion.spacerItem1)
sulf_espconc.spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
sulf_espconc.verticalLayout.addItem(sulf_espconc.spacerItem1)
sulf_esprelave.spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
sulf_esprelave.verticalLayout.addItem(sulf_esprelave.spacerItem1)

oxid_perfo.spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
oxid_perfo.verticalLayout.addItem(oxid_perfo.spacerItem1)
oxid_carguio.spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
oxid_carguio.verticalLayout.addItem(oxid_carguio.spacerItem1)
oxid_chancado.spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
oxid_chancado.verticalLayout.addItem(oxid_chancado.spacerItem1)
oxid_lixiviacion.spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
oxid_lixiviacion.verticalLayout.addItem(oxid_lixiviacion.spacerItem1)
oxid_SX.spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
oxid_SX.verticalLayout.addItem(oxid_SX.spacerItem1)
oxid_EW.spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
oxid_EW.verticalLayout.addItem(oxid_EW.spacerItem1)

# funciones de navegacion
def msg_about(title, message):
    msgBox = QMessageBox()
    msgBox.setIcon(QMessageBox.Information)
    msgBox.setWindowTitle(title)
    msgBox.setText(message)
    msgBox.setStandardButtons(QMessageBox.Ok)
    returnValue = msgBox.exec()
    if returnValue == QMessageBox.Ok:
        pass

def msg_error(title, message):
    msgBox = QMessageBox()
    msgBox.setIcon(QMessageBox.Critical)
    msgBox.setWindowTitle(title)
    msgBox.setText(message)
    msgBox.setStandardButtons(QMessageBox.Ok)
    returnValue = msgBox.exec()
    if returnValue == QMessageBox.Ok:
        pass

class MatplotlibCanvas(FigureCanvasQTAgg):
    def __init__(self,parent=None, width=5,height=4, dpi=120):
        fig = Figure(figsize = (width,height), dpi=dpi)
        self.axes=fig.add_subplot(111)
        super(MatplotlibCanvas,self).__init__(fig)
        #fig.tight_layout()
        fig.subplots_adjust(left=0.2,right=0.9,
                            bottom=0.2,top=0.9,
                            hspace=0.2,wspace=0.2)

try:
    con = sql.connect(base_datos)
    con.commit()
    con.close()
except:
    print("Error en la base de datos...")

def gui_login():
    name = login.usuarioText.text()
    password = login.passwordText.text()

    if len(name)==0 or len(password)==0:
        login.hidelabel.setText("Ingrese todos los datos")
    else:
        con = sql.connect(base_datos)
        cursor = con.cursor()
        cursor.execute('SELECT nombre, contraseña FROM usuarios WHERE nombre = ? AND contraseña = ?',(name, password))
        if cursor.fetchall():
            gui_entrar()
        else:
            gui_error()

def crear_tabla():
    con = sql.connect(base_datos)
    cursor = con.cursor()
    cursor.execute(
        """ CREATE TABLE IF NOT EXISTS usuarios (
            nombre text,
            apellido_paterno text,
            apellido_materno text, 
            contraseña text
            )"""
    )
    con.commit()
    con.close()

def registrar(nombre, ap, am, contraseña):
    con = sql.connect(base_datos)
    cursor = con.cursor()
    instruccion = f"INSERT INTO usuarios VALUES ('{nombre}', '{ap}', '{am}'," \
                  f"'{contraseña}')"
    cursor.execute(instruccion)
    con.commit()
    con.close()

def datos():
    nombre = register.nombreText.text()
    apellido_p = register.apellido1Text.text()
    apellido_m = register.apellido2Text.text()
    contraseña = register.passwordText.text()
    contraseña_2 = register.ConpasswordText.text()
    if contraseña != contraseña_2:
        msg_error("Error", "Las contraseñas no son iguales...")
    elif contraseña == contraseña_2:
        registrar(nombre, apellido_p, apellido_m, contraseña)
        msg_about("Éxito!", "Se ha registrado exitosamente! \n Tu nombre es tu usuario")
        register.nombreText.setText("")
        register.apellido1Text.setText("")
        register.apellido2Text.setText("")
        register.passwordText.setText("")
        register.ConpasswordText.setText("")

def gui_entrar():
    login.hide()
    procesos.show()

def gui_registrar():
    login.hide()
    register.show()
    crear_tabla()

def regresar_forma():
    register.hide()
    login.show()

def regresar_entrar():
    procesos.hide()
    login.label_5.setText("")
    login.show()

def salir():
    app.exit()
        
def gui_register():
    from PyQt5 import QtWidgets, uic
    from PyQt5 import QtCore, QtGui, QtWidgets
    login.hide()
    register.show()

def registrar_usuario():
    user = register.usuarioText.text()
    password = register.passwordText.text()
    confirmpasswod = register.ConpasswordText.text()
    
    if len(user) == 0 or len(password) == 0 or len(confirmpasswod) == 0:
      register.hidelabel.setText("Por favor ingrese todos los campos.")
    elif password != confirmpasswod:
      register.hidelabel.setText("Passwords no son iguales.")
    else:
      crudusers = CrudUser(nombre=user, password=password)
      crudusers.insert_user()
      register.hidelabel.setText("Usuario creado.")
    
def gui_register2login():
    from PyQt5 import QtWidgets, uic
    from PyQt5 import QtCore, QtGui, QtWidgets
    register.hide()
    login.show()

def gui_procesos():
    from PyQt5 import QtWidgets, uic
    from PyQt5 import QtCore, QtGui, QtWidgets
    login.hide()
    procesos.show()

def gui_oxid():
    from PyQt5 import QtWidgets, uic
    from PyQt5 import QtCore, QtGui, QtWidgets
    procesos.hide()
    oxid.show()
    
def gui_sulf():
    from PyQt5 import QtWidgets, uic
    from PyQt5 import QtCore, QtGui, QtWidgets
    procesos.hide()
    sulf.show()
    
def gui_sulf2oxid():
    from PyQt5 import QtWidgets, uic
    from PyQt5 import QtCore, QtGui, QtWidgets
    sulf.hide()
    oxid.show()
    
def gui_oxid2sulf():
    from PyQt5 import QtWidgets, uic
    from PyQt5 import QtCore, QtGui, QtWidgets
    oxid.hide()
    sulf.show()
 
def gui_error():
    from PyQt5 import QtWidgets, uic
    from PyQt5 import QtCore, QtGui, QtWidgets
    login.hide()
    error.show()  
    
def gui_volver_error():
    from PyQt5 import QtWidgets, uic
    from PyQt5 import QtCore, QtGui, QtWidgets
    error.hide()
    login.show()

def gui_sulf2perfo():    
    from PyQt5 import QtWidgets, uic
    from PyQt5 import QtCore, QtGui, QtWidgets
    sulf.hide()
    sulf_perfo.show()
    
def gui_oxid2perfo():    
    from PyQt5 import QtWidgets, uic
    from PyQt5 import QtCore, QtGui, QtWidgets
    oxid.hide()
    oxid_perfo.show()
    
def gui_sulf2carguio():    
    from PyQt5 import QtWidgets, uic
    from PyQt5 import QtCore, QtGui, QtWidgets
    sulf.hide()
    sulf_carguio.show()
    
def gui_oxid2carguio():    
    from PyQt5 import QtWidgets, uic
    from PyQt5 import QtCore, QtGui, QtWidgets
    oxid.hide()
    oxid_carguio.show()
    
def gui_sulf2chancado():
    from PyQt5 import QtWidgets, uic
    from PyQt5 import QtCore, QtGui, QtWidgets
    sulf.hide()
    sulf_chancado.show()

def gui_oxid2chancado():
    from PyQt5 import QtWidgets, uic
    from PyQt5 import QtCore, QtGui, QtWidgets
    oxid.hide()
    oxid_chancado.show()
    
def gui_sulf2flotacion():
    from PyQt5 import QtWidgets, uic
    from PyQt5 import QtCore, QtGui, QtWidgets
    sulf.hide()
    sulf_flotacion.show()
    
def gui_oxid2lixiviacion():
    from PyQt5 import QtWidgets, uic
    from PyQt5 import QtCore, QtGui, QtWidgets
    oxid.hide()
    oxid_lixiviacion.show()
    
def gui_sulf2espconc():
    from PyQt5 import QtWidgets, uic
    from PyQt5 import QtCore, QtGui, QtWidgets
    sulf.hide()
    sulf_espconc.show()
    
def gui_oxid2SX():
    from PyQt5 import QtWidgets, uic
    from PyQt5 import QtCore, QtGui, QtWidgets
    oxid.hide()
    oxid_SX.show()
    
def gui_sulf2esprelave():
    from PyQt5 import QtWidgets, uic
    from PyQt5 import QtCore, QtGui, QtWidgets
    sulf.hide()
    sulf_esprelave.show()
    
def gui_oxid2EW():
    from PyQt5 import QtWidgets, uic
    from PyQt5 import QtCore, QtGui, QtWidgets
    oxid.hide()
    oxid_EW.show()

def gui_perfo2sulf():
    from PyQt5 import QtWidgets, uic
    from PyQt5 import QtCore, QtGui, QtWidgets
    sulf_perfo.hide()
    sulf.show()    
    
def gui_carguio2sulf():
    from PyQt5 import QtWidgets, uic
    from PyQt5 import QtCore, QtGui, QtWidgets
    sulf_carguio.hide()
    sulf.show()  

def gui_chancado2sulf():
    from PyQt5 import QtWidgets, uic
    from PyQt5 import QtCore, QtGui, QtWidgets
    sulf_chancado.hide()
    sulf.show()
    
def gui_flotacion2sulf():
    from PyQt5 import QtWidgets, uic
    from PyQt5 import QtCore, QtGui, QtWidgets
    sulf_flotacion.hide()
    sulf.show()  

def gui_espconc2sulf():
    from PyQt5 import QtWidgets, uic
    from PyQt5 import QtCore, QtGui, QtWidgets
    sulf_espconc.hide()
    sulf.show()      

def gui_esprelave2sulf():
    from PyQt5 import QtWidgets, uic
    from PyQt5 import QtCore, QtGui, QtWidgets
    sulf_esprelave.hide()
    sulf.show()
    
def gui_perfo2oxid():
    from PyQt5 import QtWidgets, uic
    from PyQt5 import QtCore, QtGui, QtWidgets
    oxid_perfo.hide()
    oxid.show()    
    
def gui_carguio2oxid():
    from PyQt5 import QtWidgets, uic
    from PyQt5 import QtCore, QtGui, QtWidgets
    oxid_carguio.hide()
    oxid.show()  

def gui_chancado2oxid():
    from PyQt5 import QtWidgets, uic
    from PyQt5 import QtCore, QtGui, QtWidgets
    oxid_chancado.hide()
    oxid.show()
    
def gui_lixiviacion2oxid():
    from PyQt5 import QtWidgets, uic
    from PyQt5 import QtCore, QtGui, QtWidgets
    oxid_lixiviacion.hide()
    oxid.show()  

def gui_SX2oxid():
    from PyQt5 import QtWidgets, uic
    from PyQt5 import QtCore, QtGui, QtWidgets
    oxid_SX.hide()
    oxid.show()      

def gui_EW2oxid():
    from PyQt5 import QtWidgets, uic
    from PyQt5 import QtCore, QtGui, QtWidgets
    oxid_EW.hide()
    oxid.show()
    
def gui_sulf_perfo2carguio():
    from PyQt5 import QtWidgets, uic
    from PyQt5 import QtCore, QtGui, QtWidgets
    sulf_perfo.hide()
    sulf_carguio.show()
    
def gui_sulf_carguio2perfo():
    from PyQt5 import QtWidgets, uic
    from PyQt5 import QtCore, QtGui, QtWidgets
    sulf_carguio.hide()
    sulf_perfo.show()
    
def gui_sulf_carguio2chancado():
    from PyQt5 import QtWidgets, uic
    from PyQt5 import QtCore, QtGui, QtWidgets
    sulf_carguio.hide()
    sulf_chancado.show()
    
def gui_sulf_chancado2carguio():
    from PyQt5 import QtWidgets, uic
    from PyQt5 import QtCore, QtGui, QtWidgets
    sulf_chancado.hide()
    sulf_carguio.show()
    
def gui_sulf_chancado2flotacion():
    from PyQt5 import QtWidgets, uic
    from PyQt5 import QtCore, QtGui, QtWidgets
    sulf_chancado.hide()
    sulf_flotacion.show()
    
def gui_sulf_flotacion2chancado():
    from PyQt5 import QtWidgets, uic
    from PyQt5 import QtCore, QtGui, QtWidgets
    sulf_flotacion.hide()
    sulf_chancado.show()
    
def gui_sulf_flotacion2espconc():
    from PyQt5 import QtWidgets, uic
    from PyQt5 import QtCore, QtGui, QtWidgets
    sulf_flotacion.hide()
    sulf_espconc.show()
    
def gui_sulf_flotacion2esprelave():
    from PyQt5 import QtWidgets, uic
    from PyQt5 import QtCore, QtGui, QtWidgets
    sulf_flotacion.hide()
    sulf_esprelave.show()
    
def gui_sulf_espconc2flotacion():
    from PyQt5 import QtWidgets, uic
    from PyQt5 import QtCore, QtGui, QtWidgets
    sulf_espconc.hide()
    sulf_flotacion.show()
    
def gui_sulf_esprelave2flotacion():
    from PyQt5 import QtWidgets, uic
    from PyQt5 import QtCore, QtGui, QtWidgets
    sulf_esprelave.hide()
    sulf_flotacion.show()

def gui_oxid_perfo2carguio():
    from PyQt5 import QtWidgets, uic
    from PyQt5 import QtCore, QtGui, QtWidgets
    oxid_perfo.hide()
    oxid_carguio.show()
    
def gui_oxid_carguio2perfo():
    from PyQt5 import QtWidgets, uic
    from PyQt5 import QtCore, QtGui, QtWidgets
    oxid_carguio.hide()
    oxid_perfo.show()
    
def gui_oxid_carguio2chancado():
    from PyQt5 import QtWidgets, uic
    from PyQt5 import QtCore, QtGui, QtWidgets
    oxid_carguio.hide()
    oxid_chancado.show()
    
def gui_oxid_chancado2carguio():
    from PyQt5 import QtWidgets, uic
    from PyQt5 import QtCore, QtGui, QtWidgets
    oxid_chancado.hide()
    oxid_carguio.show() 
    
def gui_oxid_chancado2lixiviacion():
    from PyQt5 import QtWidgets, uic
    from PyQt5 import QtCore, QtGui, QtWidgets
    oxid_chancado.hide()
    oxid_lixiviacion.show() 
    
def gui_oxid_lixiviacion2chancado():
    from PyQt5 import QtWidgets, uic
    from PyQt5 import QtCore, QtGui, QtWidgets
    oxid_lixiviacion.hide()
    oxid_chancado.show()
    
def gui_oxid_lixiviacion2SX():
    from PyQt5 import QtWidgets, uic
    from PyQt5 import QtCore, QtGui, QtWidgets
    oxid_lixiviacion.hide()
    oxid_SX.show() 
    
def gui_oxid_SX2lixiviacion():
    from PyQt5 import QtWidgets, uic
    from PyQt5 import QtCore, QtGui, QtWidgets
    oxid_SX.hide()
    oxid_lixiviacion.show() 
    
def gui_oxid_SX2EW():
    from PyQt5 import QtWidgets, uic
    from PyQt5 import QtCore, QtGui, QtWidgets
    oxid_SX.hide()
    oxid_EW.show() 

def gui_oxid_EW2SX():
    from PyQt5 import QtWidgets, uic
    from PyQt5 import QtCore, QtGui, QtWidgets
    oxid_EW.hide()
    oxid_SX.show() 

def oxid_EDA_oxid():
    from PyQt5 import QtWidgets, uic
    from PyQt5 import QtCore, QtGui, QtWidgets
    oxid.hide()
    EDA_oxid.show()
    
def EDA_oxid_oxid():
    from PyQt5 import QtWidgets, uic
    from PyQt5 import QtCore, QtGui, QtWidgets
    EDA_oxid.hide()
    oxid.show()
    
def EDA_oxid_base():
    from PyQt5 import QtWidgets, uic
    from PyQt5 import QtCore, QtGui, QtWidgets
    EDA_oxid.hide()
    EDA_base_oxid.show()
    EDA_verbase_oxid()
    
def base_EDA_oxid():
    from PyQt5 import QtWidgets, uic
    from PyQt5 import QtCore, QtGui, QtWidgets
    EDA_base_oxid.hide()
    EDA_oxid.show()
    
def EDA_oxid_scatter():
    from PyQt5 import QtWidgets, uic
    from PyQt5 import QtCore, QtGui, QtWidgets
    #EDA_oxid.hide()
    #EDA_scatter_oxid.show()
    EDA_verscatter_oxid()

def scatter_EDA_oxid():
    from PyQt5 import QtWidgets, uic
    from PyQt5 import QtCore, QtGui, QtWidgets
    EDA_scatter_oxid.hide()
    EDA_oxid.show()  
    
def EDA_oxid_kernel():
    from PyQt5 import QtWidgets, uic
    from PyQt5 import QtCore, QtGui, QtWidgets
    EDA_verkernel_oxid()

    
def kernel_EDA_oxid():
    from PyQt5 import QtWidgets, uic
    from PyQt5 import QtCore, QtGui, QtWidgets
    EDA_kernel_oxid.hide()
    EDA_oxid.show()    
    
def EDA_oxid_plotcorr():
    from PyQt5 import QtWidgets, uic
    from PyQt5 import QtCore, QtGui, QtWidgets
    #EDA_oxid.hide()
    #EDA_kernel_oxid.show()
    EDA_verplotcorr_oxid()
    
def plotcorr_EDA_oxid():
    from PyQt5 import QtWidgets, uic
    from PyQt5 import QtCore, QtGui, QtWidgets
    EDA_plotcorr_oxid.hide()
    EDA_oxid.show()  
    
#funciones EDA_oxid
import sqlite3
import pandas as pd
import sqlalchemy 
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm
from PyQt5.QtWidgets import QApplication, QTableView
from PyQt5.QtCore import QAbstractTableModel, Qt

class PandasModel(QAbstractTableModel):

    def __init__(self, data):
        super().__init__()
        self._data = data

    def rowCount(self, index):
        # The length of the outer list.
        return self._data.shape[0]
    
    def columnCount(self, index):
        # The following takes the first sub-list, and returns
        # the length (only works if all rows are an equal length)
        return self._data.shape[1]

    def data(self, index, role=Qt.DisplayRole):
        if index.isValid():
            if role == Qt.DisplayRole:
                return str(self._data.iloc[index.row(), index.column()])
            return None
    
    def headerData(self, col, orientation, role):
        if orientation == Qt.Horizontal and role == Qt.DisplayRole:
            return self._data.columns[col]
        return None
    
    
def getFile_EDA_oxid():
    """this function will get the address of the csv file location also calls a readData function"""
    EDA_oxid.filename=QFileDialog.getOpenFileName(filter="db(*.db)")[0]
    EDA_oxid.archivo=EDA_oxid.filename.split('/')
    #print("File:",self.archivo[-1])
    EDA_oxid.browser_datos.append(EDA_oxid.archivo[-1])
    readData_EDA_oxid()
    
def readData_EDA_oxid():
    """ This function will the data using pandas and call the update function to plot"""
    #EDA_oxid.df=pd.read_csv(EDA_oxid.filename,encoding='utf-8').fillna(1)      #csv
    # creating file path
    import sqlite3
    import pandas as pd
    import sqlalchemy 
    import numpy as np
    import matplotlib.pyplot as plt
    import statsmodels.api as sm
    from PyQt5.QtWidgets import QApplication, QTableView
    from PyQt5.QtCore import QAbstractTableModel, Qt

    EDA_oxid.dbfile = EDA_oxid.filename
    try:
        EDA_oxid.conn = sqlite3.connect(EDA_oxid.dbfile)    
    except Exception as e:
        print(e)

    EDA_oxid.cursor = EDA_oxid.conn.cursor()
    EDA_oxid.cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    EDA_oxid.data = pd.read_sql_query('SELECT * FROM FLOTACION', EDA_oxid.conn)
    EDA_oxid.stri=f"{EDA_oxid.cursor.fetchall()}"
    EDA_oxid.nombre = EDA_oxid.stri[25:34]
    EDA_oxid.nfilas = EDA_oxid.data.shape[0]
    EDA_oxid.ncolumnas = EDA_oxid.data.shape[1]
    EDA_oxid.info_nombre.setText(EDA_oxid.nombre)
    EDA_oxid.info_nfilas.setText(str(EDA_oxid.nfilas))
    EDA_oxid.info_ncolumnas.setText(str(EDA_oxid.ncolumnas))
    EDA_oxid.table_typedata = QtWidgets.QTableView()
    buffer = io.StringIO()
    EDA_oxid.data.info(buf=buffer)
    EDA_oxid.lines = buffer.getvalue().splitlines()
    EDA_oxid.infoestad = EDA_oxid.data.describe()
    #{"A":1, "B":2, "C":3, "D":4}
    EDA_oxid.infoestad.round(4)
    EDA_oxid.infoestad.insert(0, "PS",['count','mean','std','min','25%','50%','75%','max'])
    EDA_oxid.database1 = (pd.DataFrame([x.split() for x in EDA_oxid.lines[5:-2]], columns=EDA_oxid.lines[3].split())
           .drop('Count',axis=1)
           .rename(columns={'Non-Null':'Non-Null Count'}))    
    EDA_oxid.model_typedata = PandasModel(EDA_oxid.database1)
    EDA_oxid.model_infoestad = PandasModel(EDA_oxid.infoestad)
    
    EDA_oxid.tableView_typedata.setModel(EDA_oxid.model_typedata)
    EDA_oxid.tableView_infoestad.setModel(EDA_oxid.model_infoestad)
    
    EDA_oxid.conn.close()
    
def EDA_verbase_oxid():
    
    EDA_base_oxid.dbfile = EDA_oxid.filename
    try:
        EDA_base_oxid.conn = sqlite3.connect(EDA_oxid.dbfile)    
    except Exception as e:
        print(e)

    EDA_base_oxid.cursor = EDA_base_oxid.conn.cursor()
    EDA_base_oxid.cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    EDA_base_oxid.data = pd.read_sql_query('SELECT * FROM FLOTACION', EDA_base_oxid.conn)
    buffer = io.StringIO()
    EDA_base_oxid.data.info(buf=buffer)
    EDA_base_oxid.lines = buffer.getvalue().splitlines()
    
    
    EDA_base_oxid.model_data = PandasModel(EDA_base_oxid.data)
    
    
    EDA_base_oxid.tableView_base.setModel(EDA_base_oxid.model_data)
    
    EDA_base_oxid.conn.close()

def EDA_verscatter_oxid():
    #print(value1)
    EDA_base_oxid.dbfile = EDA_oxid.filename
    try:
        EDA_scatter_oxid.conn = sqlite3.connect(EDA_oxid.dbfile)    #CARGA EL DOCUMENTO
    except Exception as e:
        print(e)

    EDA_scatter_oxid.cursor = EDA_scatter_oxid.conn.cursor()
    EDA_scatter_oxid.cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    EDA_scatter_oxid.data = pd.read_sql_query('SELECT * FROM FLOTACION', EDA_scatter_oxid.conn)
    plt.style.use('classic')  
    
    try:
        EDA_scatter_oxid.horizontalLayout.removeWidget(EDA_scatter_oxid.toolbar)
        EDA_scatter_oxid.verticalLayout.removeWidget(EDA_scatter_oxid.canv)
        sip.delete(EDA_scatter_oxid.toolbar)
        sip.delete(EDA_scatter_oxid.canv)
        EDA_scatter_oxid.toolbar=None
        EDA_scatter_oxid.canv=None
        EDA_scatter_oxid.verticalLayout.removeItem(EDA_scatter_oxid.spacerItem1)
    except Exception as e:
        print(e)
        pass
    
    EDA_scatter_oxid.canv=MatplotlibCanvas(EDA_scatter_oxid)
    EDA_scatter_oxid.toolbar=Navi(EDA_scatter_oxid.canv,EDA_scatter_oxid.centralwidget)
    EDA_scatter_oxid.horizontalLayout.addWidget(EDA_scatter_oxid.toolbar)
    EDA_scatter_oxid.verticalLayout.addWidget(EDA_scatter_oxid.canv)
    EDA_scatter_oxid.canv.axes.cla()
    ax=EDA_scatter_oxid.canv.axes
    #print(EDA_scatter_oxid.data)
    #EDA_scatter_oxid.data12 = EDA_scatter_oxid.data.iloc[:, 0:2]
    #print(EDA_scatter_oxid.data12)
    #EDA_scatter_oxid.data.plot.scatter(x='DIA_TURNO', y='TPD', s=15, ax=EDA_scatter_oxid.canv.axes)
    
    x_vars=list(EDA_scatter_oxid.data.columns)
    print(x_vars)
    i=0

    
    while i < (len(list(EDA_scatter_oxid.data.columns))):
        y_vars = x_vars[i]
        g = sns.PairGrid(EDA_scatter_oxid.data, x_vars= x_vars,y_vars=y_vars)
        g.map(sns.scatterplot, s=15)
        legend=ax.legend()
        legend.set_draggable(True)
        i=i+1

# FUNCION PARA KERNEL
def EDA_verkernel_oxid():
    #print(value1)
    EDA_base_oxid.dbfile = EDA_oxid.filename
    
    try:
        EDA_kernel_oxid.conn = sqlite3.connect(EDA_oxid.dbfile)    #CARGA EL DOCUMENTO
    except Exception as e:
        print(e)

    EDA_kernel_oxid.cursor = EDA_kernel_oxid.conn.cursor()
    EDA_kernel_oxid.cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    EDA_kernel_oxid.data = pd.read_sql_query('SELECT * FROM FLOTACION', EDA_kernel_oxid.conn)
    plt.style.use('classic')  
     
    try:
         EDA_kernel_oxid.horizontalLayout.removeWidget(EDA_kernel_oxid.toolbar)
         EDA_kernel_oxid.verticalLayout.removeWidget(EDA_kernel_oxid.canv)
         sip.delete(EDA_kernel_oxid.toolbar)
         sip.delete(EDA_kernel_oxid.canv)
         EDA_kernel_oxid.toolbar=None
         EDA_kernel_oxid.canv=None
         EDA_kernel_oxid.verticalLayout.removeItem(EDA_kernel_oxid.spacerItem1)
    except Exception as e:
         print(e)
         pass
     
    EDA_kernel_oxid.canv=MatplotlibCanvas(EDA_kernel_oxid)
    EDA_kernel_oxid.toolbar=Navi(EDA_kernel_oxid.canv,EDA_kernel_oxid.centralwidget)
    EDA_kernel_oxid.horizontalLayout.addWidget(EDA_kernel_oxid.toolbar)
    EDA_kernel_oxid.verticalLayout.addWidget(EDA_kernel_oxid.canv)
    EDA_kernel_oxid.canv.axes.cla()
    ax=EDA_kernel_oxid.canv.axes

    x_vars=list(EDA_kernel_oxid.data.columns)
    j=0
    print(len(list(EDA_kernel_oxid.data.columns)))
     
    while j < (len(list(EDA_kernel_oxid.data.columns))):
          y_vars = x_vars[j]
          g = sns.PairGrid(EDA_kernel_oxid.data, x_vars= x_vars,y_vars=y_vars)
          g.map(sns.kdeplot, s=15)
          legend=ax.legend()
          legend.set_draggable(True)
          j=j+1   

def EDA_verplotcorr_oxid():
     EDA_base_oxid.dbfile = EDA_oxid.filename
     try:
         EDA_plotcorr_oxid.conn = sqlite3.connect(EDA_oxid.dbfile) 
     except Exception as e:
         print(e)
         
     EDA_plotcorr_oxid.cursor = EDA_plotcorr_oxid.conn.cursor()
     EDA_plotcorr_oxid.cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
     EDA_plotcorr_oxid.data = pd.read_sql_query('SELECT * FROM FLOTACION', EDA_plotcorr_oxid.conn)
     plt.style.use('classic')  
        
     try:
         EDA_plotcorr_oxid.horizontalLayout.removeWidget(EDA_plotcorr_oxid.toolbar)
         EDA_plotcorr_oxid.verticalLayout.removeWidget(EDA_plotcorr_oxid.canv)
         sip.delete(EDA_plotcorr_oxid.toolbar)
         sip.delete(EDA_plotcorr_oxid.canv)
         EDA_plotcorr_oxid.toolbar=None
         EDA_plotcorr_oxid.canv=None
         EDA_plotcorr_oxid.verticalLayout.removeItem(EDA_plotcorr_oxid.spacerItem1)
     except Exception as e:
         print(e)
         pass
     
     EDA_plotcorr_oxid.canv=MatplotlibCanvas(EDA_plotcorr_oxid)
     EDA_plotcorr_oxid.toolbar=Navi(EDA_plotcorr_oxid.canv,EDA_plotcorr_oxid.centralwidget)
     EDA_plotcorr_oxid.horizontalLayout.addWidget(EDA_plotcorr_oxid.toolbar)
     EDA_plotcorr_oxid.verticalLayout.addWidget(EDA_plotcorr_oxid.canv)
     EDA_plotcorr_oxid.canv.axes.cla()
     ax=EDA_plotcorr_oxid.canv.axes
     
 ##CODIGO QUE FUNCIONA
     x_vars=list(EDA_plotcorr_oxid.data.columns)
     print(x_vars)
     i=0
     
     while i < (len(x_vars)):
          y_vars = x_vars[i]
          print(y_vars)
          corr = EDA_plotcorr_oxid.data.set_index(y_vars).corr()
          sm.graphics.plot_corr(corr, xnames=list(corr.columns))
          legend=ax.legend()
          legend.set_draggable(True)
          i=i+1

    
#funciones perforacion (sulfurados)  
def selectmodelo_sulf_perfo(value2):
    sulf_perfo.text_objetivo=['',
                        'Función Batch de Kynch, para la muestra de relave requerida',
                        'Función de estrés efectivo de sólido, para la muestra de relave requerida',
                        'Función de Dosificación, para la muestra de relave requerida',
                        'Función batch de Kynch, estrés efectivo de sólido y dosificación, para la muestra de relave requerida']
    sulf_perfo.text_requerimientos=['',
                              '1. Mineralogía de la muestra \n2. GravEDA_oxid_oxidd específica',
                              '1. Mineralogía de la muestra \n2. GravEDA_oxidd específica',
                              '1. Mineralogía de la muestra \n2. GravEDA_oxidd específica',
                              '1. Mineralogía de la muestra \n2. GravEDA_oxidd específica']
    sulf_perfo.text_resultados=['',
                          '1. Gráfico de Función batch de Kynch vs concentración de relave',
                          '1. Gráfico de Función de estrés efectivo de sólido vs concentración de relave',
                          '1. Gráfico de Dosificación vs concentración de relave',
                          '1. Gráfico de función batch de Kynch vs concentración de relave \n2. Gráfico de función de estrés efectivo de sólido \n3. Gráfico de función de dosificación']
    sulf_perfo.text_title=['',
                     'Función batch de Kynch',
                     'Función de estrés efectivo de sólido',
                     'Función de dosificación',
                     'Funciones constitutivas']
    for i in range(len(sulf_perfo.modelos)):
        if value2 == sulf_perfo.modelos[i]:
            sulf_perfo.info_title.setText(sulf_perfo.text_title[i])
            sulf_perfo.info_objetivo.setText(sulf_perfo.text_objetivo[i])
            sulf_perfo.info_requerimientos.setText(sulf_perfo.text_requerimientos[i])
            sulf_perfo.info_resultados.setText(sulf_perfo.text_resultados[i])

def resetear_sulf_perfo():
    sulf_perfo.browser_datos.clear() 
    sulf_perfo.comboBox_listagraficos.clear()
    sulf_perfo.comboBox_listamodelos.clear()
    sulf_perfo.comboBox_listamodelos.addItems(sulf_perfo.modelos)
    sulf_perfo.info_objetivo.clear()
    sulf_perfo.info_requerimientos.clear()
    sulf_perfo.info_resultados.clear()
    try:
        sulf_perfo.verticalLayout.removeWidget(sulf_perfo.canv)
        sip.delete(sulf_perfo.canv)
        sulf_perfo.canv=None
        sulf_perfo.verticalLayout.removeItem(sulf_perfo.spacerItem1)
    except Exception as e:
        print(e)
        pass     

def graficos_sulf_perfo(value1):  
    #print(value1)
    plt.style.use('classic')          
    if value1 == "Función batch de Kynch":
        try:
            sulf_perfo.horizontalLayout.removeWidget(sulf_perfo.toolbar)
            sulf_perfo.verticalLayout.removeWidget(sulf_perfo.canv)
            sip.delete(sulf_perfo.toolbar)
            sip.delete(sulf_perfo.canv)
            sulf_perfo.toolbar=None
            sulf_perfo.canv=None
            sulf_perfo.verticalLayout.removeItem(sulf_perfo.spacerItem1)
        except Exception as e:
            print(e)
            pass
        sulf_perfo.canv=MatplotlibCanvas(sulf_perfo)
        sulf_perfo.toolbar=Navi(sulf_perfo.canv,sulf_perfo.centralwidget)
        sulf_perfo.horizontalLayout.addWidget(sulf_perfo.toolbar)
        sulf_perfo.verticalLayout.addWidget(sulf_perfo.canv)
        sulf_perfo.canv.axes.cla()
        ax=sulf_perfo.canv.axes
        sulf_perfo.df.plot(x=0,y=1,ax=sulf_perfo.canv.axes)
        legend=ax.legend()
        legend.set_draggable(True)
        ax.set_xlabel('Concentración [-]')
        ax.set_ylabel('Función batch de Kynch')
        ax.set_title('Función batch de Kynch (f_bk) vs Concentración')
        ax.set_xlim(0, 1)
        ax.grid(color='grey', linestyle='--', linewidth=.5)
        ax.set_adjustable("box") 
        sulf_perfo.canv.draw()
    if value1 == "Función estrés efectivo de sólido":
        try:
            sulf_perfo.horizontalLayout.removeWidget(sulf_perfo.toolbar)
            sulf_perfo.verticalLayout.removeWidget(sulf_perfo.canv)
            sip.delete(sulf_perfo.toolbar)
            sip.delete(sulf_perfo.canv)
            sulf_perfo.toolbar=None
            sulf_perfo.canv=None
            sulf_perfo.verticalLayout.removeItem(sulf_perfo.spacerItem1)
        except Exception as e:
            print(e)
            pass
        sulf_perfo.canv=MatplotlibCanvas(sulf_perfo)
        sulf_perfo.toolbar=Navi(sulf_perfo.canv,sulf_perfo.centralwidget)
        sulf_perfo.horizontalLayout.addWidget(sulf_perfo.toolbar)
        sulf_perfo.verticalLayout.addWidget(sulf_perfo.canv)
        sulf_perfo.canv.axes.cla()
        ax=sulf_perfo.canv.axes
        sulf_perfo.df.plot(x=0,y=2,ax=sulf_perfo.canv.axes)
        legend=ax.legend()
        legend.set_draggable(True)
        ax.set_xlabel('Concentración [-]')
        ax.set_ylabel('Función estrés efectivo de sólido')
        ax.set_title('Función estrés efectivo de sólido vs Concentración')
        ax.set_xlim(0, 1)
        ax.grid(color='grey', linestyle='--', linewidth=.5)
        ax.set_adjustable("box") 
        sulf_perfo.canv.draw()
    if value1 == "Función de dosificación":
        try:
            sulf_perfo.horizontalLayout.removeWidget(sulf_perfo.toolbar)
            sulf_perfo.verticalLayout.removeWidget(sulf_perfo.canv)
            
            sip.delete(sulf_perfo.toolbar)
            sip.delete(sulf_perfo.canv)
            sulf_perfo.toolbar=None
            sulf_perfo.canv=None
            sulf_perfo.verticalLayout.removeItem(sulf_perfo.spacerItem1)
        except Exception as e:
            print(e)
            pass
        sulf_perfo.canv=MatplotlibCanvas(sulf_perfo)
        sulf_perfo.toolbar=Navi(sulf_perfo.canv,sulf_perfo.centralwidget)
        sulf_perfo.horizontalLayout.addWidget(sulf_perfo.toolbar)
        sulf_perfo.verticalLayout.addWidget(sulf_perfo.canv)
        sulf_perfo.canv.axes.cla()
        ax=sulf_perfo.canv.axes
        sulf_perfo.df.plot(x=0,y=3,ax=sulf_perfo.canv.axes)
        legend=ax.legend()
        legend.set_draggable(True)
        ax.set_xlabel('Concentración [-]')
        ax.set_ylabel('Función de dosificación')
        ax.set_title('Función de dosificación vs Concentración')
        ax.set_xlim(0, 1)
        ax.grid(color='grey', linestyle='--', linewidth=.5)
        ax.set_adjustable("box") 
        sulf_perfo.canv.draw()
        
def simular_sulf_perfo():
    graficos=['Función batch de Kynch','Función estrés efectivo de sólido','Función de dosificación']
    sulf_perfo.comboBox_listagraficos.addItems(graficos) 

def getFile_sulf_perfo():
    """this function will get the address of the csv file location also calls a readData function"""
    sulf_perfo.filename=QFileDialog.getOpenFileName(filter="csv(*.csv)")[0]
    sulf_perfo.archivo=sulf_perfo.filename.split('/')
    #print("File:",self.archivo[-1])
    sulf_perfo.browser_datos.append(sulf_perfo.archivo[-1])
    readData_sulf_perfo()
    
def readData_sulf_perfo():
    """ This function will the data using pandas and call the update function to plot"""
    sulf_perfo.df=pd.read_csv(sulf_perfo.filename,encoding='utf-8').fillna(1)

def guardar_csv_sulf_perfo():
    sulf_perfo.to_filename=QFileDialog.getSaveFileName(filter="csv(*.csv)")[0]
    
    if sulf_perfo.to_filename:
        sulf_perfo.df.to_csv(sulf_perfo.to_filename)

#Funciones carguio (sulfurados)
def selectmodelo_sulf_carguio(value2):
    sulf_carguio.text_objetivo=['',
                        'Función Batch de Kynch, para la muestra de relave requerida',
                        'Función de estrés efectivo de sólido, para la muestra de relave requerida',
                        'Función de Dosificación, para la muestra de relave requerida',
                        'Función batch de Kynch, estrés efectivo de sólido y dosificación, para la muestra de relave requerida']
    sulf_carguio.text_requerimientos=['',
                              '1. Mineralogía de la muestra \n2. Gravedad específica',
                              '1. Mineralogía de la muestra \n2. Gravedad específica',
                              '1. Mineralogía de la muestra \n2. Gravedad específica',
                              '1. Mineralogía de la muestra \n2. Gravedad específica']
    sulf_carguio.text_resultados=['',
                          '1. Gráfico de Función batch de Kynch vs concentración de relave',
                          '1. Gráfico de Función de estrés efectivo de sólido vs concentración de relave',
                          '1. Gráfico de Dosificación vs concentración de relave',
                          '1. Gráfico de función batch de Kynch vs concentración de relave \n2. Gráfico de función de estrés efectivo de sólido \n3. Gráfico de función de dosificación']
    sulf_carguio.text_title=['',
                     'Función batch de Kynch',
                     'Función de estrés efectivo de sólido',
                     'Función de dosificación',
                     'Funciones constitutivas']
    for i in range(len(sulf_carguio.modelos)):
        if value2 == sulf_carguio.modelos[i]:
            sulf_carguio.info_title.setText(sulf_carguio.text_title[i])
            sulf_carguio.info_objetivo.setText(sulf_carguio.text_objetivo[i])
            sulf_carguio.info_requerimientos.setText(sulf_carguio.text_requerimientos[i])
            sulf_carguio.info_resultados.setText(sulf_carguio.text_resultados[i])

def resetear_sulf_carguio():
    sulf_carguio.browser_datos.clear() 
    sulf_carguio.comboBox_listagraficos.clear()
    sulf_carguio.comboBox_listamodelos.clear()
    sulf_carguio.comboBox_listamodelos.addItems(sulf_carguio.modelos)
    sulf_carguio.info_objetivo.clear()
    sulf_carguio.info_requerimientos.clear()
    sulf_carguio.info_resultados.clear()
    try:
        sulf_carguio.verticalLayout.removeWidget(sulf_carguio.canv)
        sip.delete(sulf_carguio.canv)
        sulf_carguio.canv=None
        sulf_carguio.verticalLayout.removeItem(sulf_carguio.spacerItem1)
    except Exception as e:
        print(e)
        pass     

def graficos_sulf_carguio(value1):  
    #print(value1)
    plt.style.use('classic')          
    if value1 == "Función batch de Kynch":
        try:
            sulf_carguio.horizontalLayout.removeWidget(sulf_carguio.toolbar)
            sulf_carguio.verticalLayout.removeWidget(sulf_carguio.canv)
            sip.delete(sulf_carguio.toolbar)
            sip.delete(sulf_carguio.canv)
            sulf_carguio.toolbar=None
            sulf_carguio.canv=None
            sulf_carguio.verticalLayout.removeItem(sulf_carguio.spacerItem1)
        except Exception as e:
            print(e)
            pass
        sulf_carguio.canv=MatplotlibCanvas(sulf_carguio)
        sulf_carguio.toolbar=Navi(sulf_carguio.canv,sulf_carguio.centralwidget)
        sulf_carguio.horizontalLayout.addWidget(sulf_carguio.toolbar)
        sulf_carguio.verticalLayout.addWidget(sulf_carguio.canv)
        sulf_carguio.canv.axes.cla()
        ax=sulf_carguio.canv.axes
        sulf_carguio.df.plot(x=0,y=1,ax=sulf_carguio.canv.axes)
        legend=ax.legend()
        legend.set_draggable(True)
        ax.set_xlabel('Concentración [-]')
        ax.set_ylabel('Función batch de Kynch')
        ax.set_title('Función batch de Kynch (f_bk) vs Concentración')
        ax.set_xlim(0, 1)
        ax.grid(color='grey', linestyle='--', linewidth=.5)
        ax.set_adjustable("box") 
        sulf_carguio.canv.draw()
    if value1 == "Función estrés efectivo de sólido":
        try:
            sulf_carguio.horizontalLayout.removeWidget(sulf_carguio.toolbar)
            sulf_carguio.verticalLayout.removeWidget(sulf_carguio.canv)
            sip.delete(sulf_carguio.toolbar)
            sip.delete(sulf_carguio.canv)
            sulf_carguio.toolbar=None
            sulf_carguio.canv=None
            sulf_carguio.verticalLayout.removeItem(sulf_carguio.spacerItem1)
        except Exception as e:
            print(e)
            pass
        sulf_carguio.canv=MatplotlibCanvas(sulf_carguio)
        sulf_carguio.toolbar=Navi(sulf_carguio.canv,sulf_carguio.centralwidget)
        sulf_carguio.horizontalLayout.addWidget(sulf_carguio.toolbar)
        sulf_carguio.verticalLayout.addWidget(sulf_carguio.canv)
        sulf_carguio.canv.axes.cla()
        ax=sulf_carguio.canv.axes
        sulf_carguio.df.plot(x=0,y=2,ax=sulf_carguio.canv.axes)
        legend=ax.legend()
        legend.set_draggable(True)
        ax.set_xlabel('Concentración [-]')
        ax.set_ylabel('Función estrés efectivo de sólido')
        ax.set_title('Función estrés efectivo de sólido vs Concentración')
        ax.set_xlim(0, 1)
        ax.grid(color='grey', linestyle='--', linewidth=.5)
        ax.set_adjustable("box") 
        sulf_carguio.canv.draw()
    if value1 == "Función de dosificación":
        try:
            sulf_carguio.horizontalLayout.removeWidget(sulf_carguio.toolbar)
            sulf_carguio.verticalLayout.removeWidget(sulf_carguio.canv)
            
            sip.delete(sulf_carguio.toolbar)
            sip.delete(sulf_carguio.canv)
            sulf_carguio.toolbar=None
            sulf_carguio.canv=None
            sulf_carguio.verticalLayout.removeItem(sulf_carguio.spacerItem1)
        except Exception as e:
            print(e)
            pass
        sulf_carguio.canv=MatplotlibCanvas(sulf_carguio)
        sulf_carguio.toolbar=Navi(sulf_carguio.canv,sulf_carguio.centralwidget)
        sulf_carguio.horizontalLayout.addWidget(sulf_carguio.toolbar)
        sulf_carguio.verticalLayout.addWidget(sulf_carguio.canv)
        sulf_carguio.canv.axes.cla()
        ax=sulf_carguio.canv.axes
        sulf_carguio.df.plot(x=0,y=3,ax=sulf_carguio.canv.axes)
        legend=ax.legend()
        legend.set_draggable(True)
        ax.set_xlabel('Concentración [-]')
        ax.set_ylabel('Función de dosificación')
        ax.set_title('Función de dosificación vs Concentración')
        ax.set_xlim(0, 1)
        ax.grid(color='grey', linestyle='--', linewidth=.5)
        ax.set_adjustable("box") 
        sulf_carguio.canv.draw()
        
def simular_sulf_carguio():
    graficos=['Función batch de Kynch','Función estrés efectivo de sólido','Función de dosificación']
    sulf_carguio.comboBox_listagraficos.addItems(graficos) 

def getFile_sulf_carguio():
    """this function will get the address of the csv file location also calls a readData function"""
    sulf_carguio.filename=QFileDialog.getOpenFileName(filter="csv(*.csv)")[0]
    sulf_carguio.archivo=sulf_carguio.filename.split('/')
    sulf_carguio.browser_datos.append(sulf_carguio.archivo[-1])
    readData_sulf_carguio()
    
def readData_sulf_carguio():
    """ This function will the data using pandas and call the update function to plot"""
    sulf_carguio.df=pd.read_csv(sulf_carguio.filename,encoding='utf-8').fillna(1)

def guardar_csv_sulf_carguio():
    sulf_carguio.to_filename=QFileDialog.getSaveFileName(filter="csv(*.csv)")[0]
    
    if sulf_carguio.to_filename:
        sulf_carguio.df.to_csv(sulf_carguio.to_filename)
        
#funciones chancado  (sulfurados)  
def selectmodelo_sulf_chancado(value2):
    sulf_chancado.text_objetivo=['',
                        'Función Batch de Kynch, para la muestra de relave requerida',
                        'Función de estrés efectivo de sólido, para la muestra de relave requerida',
                        'Función de Dosificación, para la muestra de relave requerida',
                        'Función batch de Kynch, estrés efectivo de sólido y dosificación, para la muestra de relave requerida']
    sulf_chancado.text_requerimientos=['',
                              '1. Mineralogía de la muestra \n2. Gravedad específica',
                              '1. Mineralogía de la muestra \n2. Gravedad específica',
                              '1. Mineralogía de la muestra \n2. Gravedad específica',
                              '1. Mineralogía de la muestra \n2. Gravedad específica']
    sulf_chancado.text_resultados=['',
                          '1. Gráfico de Función batch de Kynch vs concentración de relave',
                          '1. Gráfico de Función de estrés efectivo de sólido vs concentración de relave',
                          '1. Gráfico de Dosificación vs concentración de relave',
                          '1. Gráfico de función batch de Kynch vs concentración de relave \n2. Gráfico de función de estrés efectivo de sólido \n3. Gráfico de función de dosificación']
    sulf_chancado.text_title=['',
                     'Función batch de Kynch',
                     'Función de estrés efectivo de sólido',
                     'Función de dosificación',
                     'Funciones constitutivas']
    for i in range(len(sulf_chancado.modelos)):
        if value2 == sulf_chancado.modelos[i]:
            sulf_chancado.info_title.setText(sulf_chancado.text_title[i])
            sulf_chancado.info_objetivo.setText(sulf_chancado.text_objetivo[i])
            sulf_chancado.info_requerimientos.setText(sulf_chancado.text_requerimientos[i])
            sulf_chancado.info_resultados.setText(sulf_chancado.text_resultados[i])

def resetear_sulf_chancado():
    sulf_chancado.browser_datos.clear() 
    sulf_chancado.comboBox_listagraficos.clear()
    sulf_chancado.comboBox_listamodelos.clear()
    sulf_chancado.comboBox_listamodelos.addItems(sulf_chancado.modelos)
    sulf_chancado.info_objetivo.clear()
    sulf_chancado.info_requerimientos.clear()
    sulf_chancado.info_resultados.clear()
    try:
        sulf_chancado.verticalLayout.removeWidget(sulf_chancado.canv)
        sip.delete(sulf_chancado.canv)
        sulf_chancado.canv=None
        sulf_chancado.verticalLayout.removeItem(sulf_chancado.spacerItem1)
    except Exception as e:
        print(e)
        pass     

def graficos_sulf_chancado(value1):  
    #print(value1)
    plt.style.use('classic')          
    if value1 == "Función batch de Kynch":
        try:
            sulf_chancado.horizontalLayout.removeWidget(sulf_chancado.toolbar)
            sulf_chancado.verticalLayout.removeWidget(sulf_chancado.canv)
            sip.delete(sulf_chancado.toolbar)
            sip.delete(sulf_chancado.canv)
            sulf_chancado.toolbar=None
            sulf_chancado.canv=None
            sulf_chancado.verticalLayout.removeItem(sulf_chancado.spacerItem1)
        except Exception as e:
            print(e)
            pass
        sulf_chancado.canv=MatplotlibCanvas(sulf_chancado)
        sulf_chancado.toolbar=Navi(sulf_chancado.canv,sulf_chancado.centralwidget)
        sulf_chancado.horizontalLayout.addWidget(sulf_chancado.toolbar)
        sulf_chancado.verticalLayout.addWidget(sulf_chancado.canv)
        sulf_chancado.canv.axes.cla()
        ax=sulf_chancado.canv.axes
        sulf_chancado.df.plot(x=0,y=1,ax=sulf_chancado.canv.axes)
        legend=ax.legend()
        legend.set_draggable(True)
        ax.set_xlabel('Concentración [-]')
        ax.set_ylabel('Función batch de Kynch')
        ax.set_title('Función batch de Kynch (f_bk) vs Concentración')
        ax.set_xlim(0, 1)
        ax.grid(color='grey', linestyle='--', linewidth=.5)
        ax.set_adjustable("box") 
        sulf_chancado.canv.draw()
    if value1 == "Función estrés efectivo de sólido":
        try:
            sulf_chancado.horizontalLayout.removeWidget(sulf_chancado.toolbar)
            sulf_chancado.verticalLayout.removeWidget(sulf_chancado.canv)
            sip.delete(sulf_chancado.toolbar)
            sip.delete(sulf_chancado.canv)
            sulf_chancado.toolbar=None
            sulf_chancado.canv=None
            sulf_chancado.verticalLayout.removeItem(sulf_chancado.spacerItem1)
        except Exception as e:
            print(e)
            pass
        sulf_chancado.canv=MatplotlibCanvas(sulf_chancado)
        sulf_chancado.toolbar=Navi(sulf_chancado.canv,sulf_chancado.centralwidget)
        sulf_chancado.horizontalLayout.addWidget(sulf_chancado.toolbar)
        sulf_chancado.verticalLayout.addWidget(sulf_chancado.canv)
        sulf_chancado.canv.axes.cla()
        ax=sulf_chancado.canv.axes
        sulf_chancado.df.plot(x=0,y=2,ax=sulf_chancado.canv.axes)
        legend=ax.legend()
        legend.set_draggable(True)
        ax.set_xlabel('Concentración [-]')
        ax.set_ylabel('Función estrés efectivo de sólido')
        ax.set_title('Función estrés efectivo de sólido vs Concentración')
        ax.set_xlim(0, 1)
        ax.grid(color='grey', linestyle='--', linewidth=.5)
        ax.set_adjustable("box") 
        sulf_chancado.canv.draw()
    if value1 == "Función de dosificación":
        try:
            sulf_chancado.horizontalLayout.removeWidget(sulf_chancado.toolbar)
            sulf_chancado.verticalLayout.removeWidget(sulf_chancado.canv)
            
            sip.delete(sulf_chancado.toolbar)
            sip.delete(sulf_chancado.canv)
            sulf_chancado.toolbar=None
            sulf_chancado.canv=None
            sulf_chancado.verticalLayout.removeItem(sulf_chancado.spacerItem1)
        except Exception as e:
            print(e)
            pass
        sulf_chancado.canv=MatplotlibCanvas(sulf_chancado)
        sulf_chancado.toolbar=Navi(sulf_chancado.canv,sulf_chancado.centralwidget)
        sulf_chancado.horizontalLayout.addWidget(sulf_chancado.toolbar)
        sulf_chancado.verticalLayout.addWidget(sulf_chancado.canv)
        sulf_chancado.canv.axes.cla()
        ax=sulf_chancado.canv.axes
        sulf_chancado.df.plot(x=0,y=3,ax=sulf_chancado.canv.axes)
        legend=ax.legend()
        legend.set_draggable(True)
        ax.set_xlabel('Concentración [-]')
        ax.set_ylabel('Función de dosificación')
        ax.set_title('Función de dosificación vs Concentración')
        ax.set_xlim(0, 1)
        ax.grid(color='grey', linestyle='--', linewidth=.5)
        ax.set_adjustable("box") 
        sulf_chancado.canv.draw()
        
def simular_sulf_chancado():
    graficos=['Función batch de Kynch','Función estrés efectivo de sólido','Función de dosificación']
    sulf_chancado.comboBox_listagraficos.addItems(graficos) 

def getFile_sulf_chancado():
    """this function will get the address of the csv file location also calls a readData function"""
    sulf_chancado.filename=QFileDialog.getOpenFileName(filter="csv(*.csv)")[0]
    sulf_chancado.archivo=sulf_chancado.filename.split('/')
    #print("File:",self.archivo[-1])
    sulf_chancado.browser_datos.append(sulf_chancado.archivo[-1])
    readData_sulf_chancado()
    
def readData_sulf_chancado():
    """ This function will the data using pandas and call the update function to plot"""
    sulf_chancado.df=pd.read_csv(sulf_chancado.filename,encoding='utf-8').fillna(1)

def guardar_csv_sulf_chancado():
    sulf_chancado.to_filename=QFileDialog.getSaveFileName(filter="csv(*.csv)")[0]
    
    if sulf_chancado.to_filename:
        sulf_chancado.df.to_csv(sulf_chancado.to_filename)        

#funciones flotacion   (sulfurados)
def selectmodelo_sulf_flotacion(value2):
    sulf_flotacion.text_objetivo=['',
                        'Función Batch de Kynch, para la muestra de relave requerida',
                        'Función de estrés efectivo de sólido, para la muestra de relave requerida',
                        'Función de Dosificación, para la muestra de relave requerida',
                        'Función batch de Kynch, estrés efectivo de sólido y dosificación, \npara la muestra de relave requerida']
    sulf_flotacion.text_requerimientos=['',
                              '1. Mineralogía de la muestra \n2. Gravedad específica',
                              '1. Mineralogía de la muestra \n2. Gravedad específica',
                              '1. Mineralogía de la muestra \n2. Gravedad específica',
                              '1. Mineralogía de la muestra \n2. Gravedad específica']
    sulf_flotacion.text_resultados=['',
                          '1. Gráfico de Función batch de Kynch vs concentración de relave',
                          '1. Gráfico de Función de estrés efectivo de sólido vs concentración de relave',
                          '1. Gráfico de Dosificación vs concentración de relave',
                          '1. Gráfico de función batch de Kynch vs concentración de relave \n2. Gráfico de función de estrés efectivo de sólido \n3. Gráfico de función de dosificación']
    sulf_flotacion.text_title=['',
                     'Función batch de Kynch',
                     'Función de estrés efectivo de sólido',
                     'Función de dosificación',
                     'Funciones constitutivas']
    for i in range(len(sulf_flotacion.modelos)):
        if value2 == sulf_flotacion.modelos[i]:
            sulf_flotacion.info_title.setText(sulf_flotacion.text_title[i])
            sulf_flotacion.info_objetivo.setText(sulf_flotacion.text_objetivo[i])
            sulf_flotacion.info_requerimientos.setText(sulf_flotacion.text_requerimientos[i])
            sulf_flotacion.info_resultados.setText(sulf_flotacion.text_resultados[i])

def resetear_sulf_flotacion():
    sulf_flotacion.browser_datos.clear() 
    sulf_flotacion.comboBox_listagraficos.clear()
    sulf_flotacion.comboBox_listamodelos.clear()
    sulf_flotacion.comboBox_listamodelos.addItems(sulf_flotacion.modelos)
    sulf_flotacion.info_objetivo.clear()
    sulf_flotacion.info_requerimientos.clear()
    sulf_flotacion.info_resultados.clear()
    try:
        sulf_flotacion.verticalLayout.removeWidget(sulf_flotacion.canv)
        sip.delete(sulf_flotacion.canv)
        sulf_flotacion.canv=None
        sulf_flotacion.verticalLayout.removeItem(sulf_flotacion.spacerItem1)
    except Exception as e:
        print(e)
        pass     

def graficos_sulf_flotacion(value1):  
    #print(value1)
    plt.style.use('classic')          
    if value1 == "Función batch de Kynch":
        try:
            sulf_flotacion.horizontalLayout.removeWidget(sulf_flotacion.toolbar)
            sulf_flotacion.verticalLayout.removeWidget(sulf_flotacion.canv)
            sip.delete(sulf_flotacion.toolbar)
            sip.delete(sulf_flotacion.canv)
            sulf_flotacion.toolbar=None
            sulf_flotacion.canv=None
            sulf_flotacion.verticalLayout.removeItem(sulf_flotacion.spacerItem1)
        except Exception as e:
            print(e)
            pass
        sulf_flotacion.canv=MatplotlibCanvas(sulf_flotacion)
        sulf_flotacion.toolbar=Navi(sulf_flotacion.canv,sulf_flotacion.centralwidget)
        sulf_flotacion.horizontalLayout.addWidget(sulf_flotacion.toolbar)
        sulf_flotacion.verticalLayout.addWidget(sulf_flotacion.canv)
        sulf_flotacion.canv.axes.cla()
        ax=sulf_flotacion.canv.axes
        sulf_flotacion.df.plot(x=0,y=1,ax=sulf_flotacion.canv.axes)
        legend=ax.legend()
        legend.set_draggable(True)
        ax.set_xlabel('Concentración [-]')
        ax.set_ylabel('Función batch de Kynch')
        ax.set_title('Función batch de Kynch (f_bk) vs Concentración')
        ax.set_xlim(0, 1)
        ax.grid(color='grey', linestyle='--', linewidth=.5)
        ax.set_adjustable("box") 
        sulf_flotacion.canv.draw()
    if value1 == "Función estrés efectivo de sólido":
        try:
            sulf_flotacion.horizontalLayout.removeWidget(sulf_flotacion.toolbar)
            sulf_flotacion.verticalLayout.removeWidget(sulf_flotacion.canv)
            sip.delete(sulf_flotacion.toolbar)
            sip.delete(sulf_flotacion.canv)
            sulf_flotacion.toolbar=None
            sulf_flotacion.canv=None
            sulf_flotacion.verticalLayout.removeItem(sulf_flotacion.spacerItem1)
        except Exception as e:
            print(e)
            pass
        sulf_flotacion.canv=MatplotlibCanvas(sulf_flotacion)
        sulf_flotacion.toolbar=Navi(sulf_flotacion.canv,sulf_flotacion.centralwidget)
        sulf_flotacion.horizontalLayout.addWidget(sulf_flotacion.toolbar)
        sulf_flotacion.verticalLayout.addWidget(sulf_flotacion.canv)
        sulf_flotacion.canv.axes.cla()
        ax=sulf_flotacion.canv.axes
        sulf_flotacion.df.plot(x=0,y=2,ax=sulf_flotacion.canv.axes)
        legend=ax.legend()
        legend.set_draggable(True)
        ax.set_xlabel('Concentración [-]')
        ax.set_ylabel('Función estrés efectivo de sólido')
        ax.set_title('Función estrés efectivo de sólido vs Concentración')
        ax.set_xlim(0, 1)
        ax.grid(color='grey', linestyle='--', linewidth=.5)
        ax.set_adjustable("box") 
        sulf_flotacion.canv.draw()
    if value1 == "Función de dosificación":
        try:
            sulf_flotacion.horizontalLayout.removeWidget(sulf_flotacion.toolbar)
            sulf_flotacion.verticalLayout.removeWidget(sulf_flotacion.canv)
            
            sip.delete(sulf_flotacion.toolbar)
            sip.delete(sulf_flotacion.canv)
            sulf_flotacion.toolbar=None
            sulf_flotacion.canv=None
            sulf_flotacion.verticalLayout.removeItem(sulf_flotacion.spacerItem1)
        except Exception as e:
            print(e)
            pass
        sulf_flotacion.canv=MatplotlibCanvas(sulf_flotacion)
        sulf_flotacion.toolbar=Navi(sulf_flotacion.canv,sulf_flotacion.centralwidget)
        sulf_flotacion.horizontalLayout.addWidget(sulf_flotacion.toolbar)
        sulf_flotacion.verticalLayout.addWidget(sulf_flotacion.canv)
        sulf_flotacion.canv.axes.cla()
        ax=sulf_flotacion.canv.axes
        sulf_flotacion.df.plot(x=0,y=3,ax=sulf_flotacion.canv.axes)
        legend=ax.legend()
        legend.set_draggable(True)
        ax.set_xlabel('Concentración [-]')
        ax.set_ylabel('Función de dosificación')
        ax.set_title('Función de dosificación vs Concentración')
        ax.set_xlim(0, 1)
        ax.grid(color='grey', linestyle='--', linewidth=.5)
        ax.set_adjustable("box") 
        sulf_flotacion.canv.draw()
        
def simular_sulf_flotacion():
    graficos=['Función batch de Kynch','Función estrés efectivo de sólido','Función de dosificación']
    sulf_flotacion.comboBox_listagraficos.addItems(graficos) 

def getFile_sulf_flotacion():
    """this function will get the address of the csv file location also calls a readData function"""
    sulf_flotacion.filename=QFileDialog.getOpenFileName(filter="csv(*.csv)")[0]
    sulf_flotacion.archivo=sulf_flotacion.filename.split('/')
    #print("File:",self.archivo[-1])
    sulf_flotacion.browser_datos.append(sulf_flotacion.archivo[-1])
    readData_sulf_flotacion()
    
def readData_sulf_flotacion():
    """ This function will the data using pandas and call the update function to plot"""
    sulf_flotacion.df=pd.read_csv(sulf_flotacion.filename,encoding='utf-8').fillna(1)

def guardar_csv_sulf_flotacion():
    sulf_flotacion.to_filename=QFileDialog.getSaveFileName(filter="csv(*.csv)")[0]
    
    if sulf_flotacion.to_filename:
        sulf_flotacion.df.to_csv(sulf_flotacion.to_filename) 
        
#funciones espesamiento concentrado  (sulfurados) 
def selectmodelo_sulf_espconc(value2):
    sulf_espconc.text_objetivo=['',
                        'Función Batch de Kynch, para la muestra de relave requerida',
                        'Función de estrés efectivo de sólido, para la muestra de relave requerida',
                        'Función de Dosificación, para la muestra de relave requerida',
                        'Función batch de Kynch, estrés efectivo de sólido y dosificación, \npara la muestra de relave requerida']
    sulf_espconc.text_requerimientos=['',
                              '1. Mineralogía de la muestra \n2. Gravedad específica',
                              '1. Mineralogía de la muestra \n2. Gravedad específica',
                              '1. Mineralogía de la muestra \n2. Gravedad específica',
                              '1. Mineralogía de la muestra \n2. Gravedad específica']
    sulf_espconc.text_resultados=['',
                          '1. Gráfico de Función batch de Kynch vs concentración de relave',
                          '1. Gráfico de Función de estrés efectivo de sólido vs concentración de relave',
                          '1. Gráfico de Dosificación vs concentración de relave',
                          '1. Gráfico de función batch de Kynch vs concentración de relave \n2. Gráfico de función de estrés efectivo de sólido \n3. Gráfico de función de dosificación']
    sulf_espconc.text_title=['',
                     'Función batch de Kynch',
                     'Función de estrés efectivo de sólido',
                     'Función de dosificación',
                     'Funciones constitutivas']
    for i in range(len(sulf_espconc.modelos)):
        if value2 == sulf_espconc.modelos[i]:
            sulf_espconc.info_title.setText(sulf_espconc.text_title[i])
            sulf_espconc.info_objetivo.setText(sulf_espconc.text_objetivo[i])
            sulf_espconc.info_requerimientos.setText(sulf_espconc.text_requerimientos[i])
            sulf_espconc.info_resultados.setText(sulf_espconc.text_resultados[i])

def resetear_sulf_espconc():
    sulf_espconc.browser_datos.clear() 
    sulf_espconc.comboBox_listagraficos.clear()
    sulf_espconc.comboBox_listamodelos.clear()
    sulf_espconc.comboBox_listamodelos.addItems(sulf_espconc.modelos)
    sulf_espconc.info_objetivo.clear()
    sulf_espconc.info_requerimientos.clear()
    sulf_espconc.info_resultados.clear()
    try:
        sulf_espconc.verticalLayout.removeWidget(sulf_espconc.canv)
        sip.delete(sulf_espconc.canv)
        sulf_espconc.canv=None
        sulf_espconc.verticalLayout.removeItem(sulf_espconc.spacerItem1)
    except Exception as e:
        print(e)
        pass     

def graficos_sulf_espconc(value1):  
    #print(value1)
    plt.style.use('classic')          
    if value1 == "Función batch de Kynch":
        try:
            sulf_espconc.horizontalLayout.removeWidget(sulf_espconc.toolbar)
            sulf_espconc.verticalLayout.removeWidget(sulf_espconc.canv)
            sip.delete(sulf_espconc.toolbar)
            sip.delete(sulf_espconc.canv)
            sulf_espconc.toolbar=None
            sulf_espconc.canv=None
            sulf_espconc.verticalLayout.removeItem(sulf_espconc.spacerItem1)
        except Exception as e:
            print(e)
            pass
        sulf_espconc.canv=MatplotlibCanvas(sulf_espconc)
        sulf_espconc.toolbar=Navi(sulf_espconc.canv,sulf_espconc.centralwidget)
        sulf_espconc.horizontalLayout.addWidget(sulf_espconc.toolbar)
        sulf_espconc.verticalLayout.addWidget(sulf_espconc.canv)
        sulf_espconc.canv.axes.cla()
        ax=sulf_espconc.canv.axes
        sulf_espconc.df.plot(x=0,y=1,ax=sulf_espconc.canv.axes)
        legend=ax.legend()
        legend.set_draggable(True)
        ax.set_xlabel('Concentración [-]')
        ax.set_ylabel('Función batch de Kynch')
        ax.set_title('Función batch de Kynch (f_bk) vs Concentración')
        ax.set_xlim(0, 1)
        ax.grid(color='grey', linestyle='--', linewidth=.5)
        ax.set_adjustable("box") 
        sulf_espconc.canv.draw()
    if value1 == "Función estrés efectivo de sólido":
        try:
            sulf_espconc.horizontalLayout.removeWidget(sulf_espconc.toolbar)
            sulf_espconc.verticalLayout.removeWidget(sulf_espconc.canv)
            sip.delete(sulf_espconc.toolbar)
            sip.delete(sulf_espconc.canv)
            sulf_espconc.toolbar=None
            sulf_espconc.canv=None
            sulf_espconc.verticalLayout.removeItem(sulf_espconc.spacerItem1)
        except Exception as e:
            print(e)
            pass
        sulf_espconc.canv=MatplotlibCanvas(sulf_espconc)
        sulf_espconc.toolbar=Navi(sulf_espconc.canv,sulf_espconc.centralwidget)
        sulf_espconc.horizontalLayout.addWidget(sulf_espconc.toolbar)
        sulf_espconc.verticalLayout.addWidget(sulf_espconc.canv)
        sulf_espconc.canv.axes.cla()
        ax=sulf_espconc.canv.axes
        sulf_espconc.df.plot(x=0,y=2,ax=sulf_espconc.canv.axes)
        legend=ax.legend()
        legend.set_draggable(True)
        ax.set_xlabel('Concentración [-]')
        ax.set_ylabel('Función estrés efectivo de sólido')
        ax.set_title('Función estrés efectivo de sólido vs Concentración')
        ax.set_xlim(0, 1)
        ax.grid(color='grey', linestyle='--', linewidth=.5)
        ax.set_adjustable("box") 
        sulf_espconc.canv.draw()
    if value1 == "Función de dosificación":
        try:
            sulf_espconc.horizontalLayout.removeWidget(sulf_espconc.toolbar)
            sulf_espconc.verticalLayout.removeWidget(sulf_espconc.canv)
            
            sip.delete(sulf_espconc.toolbar)
            sip.delete(sulf_espconc.canv)
            sulf_espconc.toolbar=None
            sulf_espconc.canv=None
            sulf_espconc.verticalLayout.removeItem(sulf_espconc.spacerItem1)
        except Exception as e:
            print(e)
            pass
        sulf_espconc.canv=MatplotlibCanvas(sulf_espconc)
        sulf_espconc.toolbar=Navi(sulf_espconc.canv,sulf_espconc.centralwidget)
        sulf_espconc.horizontalLayout.addWidget(sulf_espconc.toolbar)
        sulf_espconc.verticalLayout.addWidget(sulf_espconc.canv)
        sulf_espconc.canv.axes.cla()
        ax=sulf_espconc.canv.axes
        sulf_espconc.df.plot(x=0,y=3,ax=sulf_espconc.canv.axes)
        legend=ax.legend()
        legend.set_draggable(True)
        ax.set_xlabel('Concentración [-]')
        ax.set_ylabel('Función de dosificación')
        ax.set_title('Función de dosificación vs Concentración')
        ax.set_xlim(0, 1)
        ax.grid(color='grey', linestyle='--', linewidth=.5)
        ax.set_adjustable("box") 
        sulf_espconc.canv.draw()
        
def simular_sulf_espconc():
    graficos=['Función batch de Kynch','Función estrés efectivo de sólido','Función de dosificación']
    sulf_espconc.comboBox_listagraficos.addItems(graficos) 

def getFile_sulf_espconc():
    """this function will get the address of the csv file location also calls a readData function"""
    sulf_espconc.filename=QFileDialog.getOpenFileName(filter="csv(*.csv)")[0]
    sulf_espconc.archivo=sulf_espconc.filename.split('/')
    #print("File:",self.archivo[-1])
    sulf_espconc.browser_datos.append(sulf_espconc.archivo[-1])
    readData_sulf_espconc()
    
def readData_sulf_espconc():
    """ This function will the data using pandas and call the update function to plot"""
    sulf_espconc.df=pd.read_csv(sulf_espconc.filename,encoding='utf-8').fillna(1)

def guardar_csv_sulf_espconc():
    sulf_espconc.to_filename=QFileDialog.getSaveFileName(filter="csv(*.csv)")[0]
    
    if sulf_espconc.to_filename:
        sulf_espconc.df.to_csv(sulf_espconc.to_filename)   

#funciones espesamiento relave (sulfurados)
def selectmodelo_sulf_esprelave(value2):
    sulf_esprelave.text_objetivo=['',
                        'Función Batch de Kynch, para la muestra de relave requerida',
                        'Función de estrés efectivo de sólido, para la muestra de relave requerida',
                        'Función de Dosificación, para la muestra de relave requerida',
                        'Función batch de Kynch, estrés efectivo de sólido y dosificación, \npara la muestra de relave requerida']
    sulf_esprelave.text_requerimientos=['',
                              '1. Mineralogía de la muestra \n2. Gravedad específica',
                              '1. Mineralogía de la muestra \n2. Gravedad específica',
                              '1. Mineralogía de la muestra \n2. Gravedad específica',
                              '1. Mineralogía de la muestra \n2. Gravedad específica']
    sulf_esprelave.text_resultados=['',
                          '1. Gráfico de Función batch de Kynch vs concentración de relave',
                          '1. Gráfico de Función de estrés efectivo de sólido vs concentración de relave',
                          '1. Gráfico de Dosificación vs concentración de relave',
                          '1. Gráfico de función batch de Kynch vs concentración de relave \n2. Gráfico de función de estrés efectivo de sólido \n3. Gráfico de función de dosificación']
    sulf_esprelave.text_title=['',
                     'Función batch de Kynch',
                     'Función de estrés efectivo de sólido',
                     'Función de dosificación',
                     'Funciones constitutivas']
    for i in range(len(sulf_esprelave.modelos)):
        if value2 == sulf_esprelave.modelos[i]:
            sulf_esprelave.info_title.setText(sulf_esprelave.text_title[i])
            sulf_esprelave.info_objetivo.setText(sulf_esprelave.text_objetivo[i])
            sulf_esprelave.info_requerimientos.setText(sulf_esprelave.text_requerimientos[i])
            sulf_esprelave.info_resultados.setText(sulf_esprelave.text_resultados[i])

def resetear_sulf_esprelave():
    sulf_esprelave.browser_datos.clear() 
    sulf_esprelave.comboBox_listagraficos.clear()
    sulf_esprelave.comboBox_listamodelos.clear()
    sulf_esprelave.comboBox_listamodelos.addItems(sulf_esprelave.modelos)
    sulf_esprelave.info_objetivo.clear()
    sulf_esprelave.info_requerimientos.clear()
    sulf_esprelave.info_resultados.clear()
    try:
        sulf_esprelave.verticalLayout.removeWidget(sulf_esprelave.canv)
        sip.delete(sulf_esprelave.canv)
        sulf_esprelave.canv=None
        sulf_esprelave.verticalLayout.removeItem(sulf_esprelave.spacerItem1)
    except Exception as e:
        print(e)
        pass     

def graficos_sulf_esprelave(value1):  
    #print(value1)
    plt.style.use('classic')          
    if value1 == "Función batch de Kynch":
        try:
            sulf_esprelave.horizontalLayout.removeWidget(sulf_esprelave.toolbar)
            sulf_esprelave.verticalLayout.removeWidget(sulf_esprelave.canv)
            sip.delete(sulf_esprelave.toolbar)
            sip.delete(sulf_esprelave.canv)
            sulf_esprelave.toolbar=None
            sulf_esprelave.canv=None
            sulf_esprelave.verticalLayout.removeItem(sulf_esprelave.spacerItem1)
        except Exception as e:
            print(e)
            pass
        sulf_esprelave.canv=MatplotlibCanvas(sulf_esprelave)
        sulf_esprelave.toolbar=Navi(sulf_esprelave.canv,sulf_esprelave.centralwidget)
        sulf_esprelave.horizontalLayout.addWidget(sulf_esprelave.toolbar)
        sulf_esprelave.verticalLayout.addWidget(sulf_esprelave.canv)
        sulf_esprelave.canv.axes.cla()
        ax=sulf_esprelave.canv.axes
        sulf_esprelave.df.plot(x=0,y=1,ax=sulf_esprelave.canv.axes)
        legend=ax.legend()
        legend.set_draggable(True)
        ax.set_xlabel('Concentración [-]')
        ax.set_ylabel('Función batch de Kynch')
        ax.set_title('Función batch de Kynch (f_bk) vs Concentración')
        ax.set_xlim(0, 1)
        ax.grid(color='grey', linestyle='--', linewidth=.5)
        ax.set_adjustable("box") 
        sulf_esprelave.canv.draw()
    if value1 == "Función estrés efectivo de sólido":
        try:
            sulf_esprelave.horizontalLayout.removeWidget(sulf_esprelave.toolbar)
            sulf_esprelave.verticalLayout.removeWidget(sulf_esprelave.canv)
            sip.delete(sulf_esprelave.toolbar)
            sip.delete(sulf_esprelave.canv)
            sulf_esprelave.toolbar=None
            sulf_esprelave.canv=None
            sulf_esprelave.verticalLayout.removeItem(sulf_esprelave.spacerItem1)
        except Exception as e:
            print(e)
            pass
        sulf_esprelave.canv=MatplotlibCanvas(sulf_esprelave)
        sulf_esprelave.toolbar=Navi(sulf_esprelave.canv,sulf_esprelave.centralwidget)
        sulf_esprelave.horizontalLayout.addWidget(sulf_esprelave.toolbar)
        sulf_esprelave.verticalLayout.addWidget(sulf_esprelave.canv)
        sulf_esprelave.canv.axes.cla()
        ax=sulf_esprelave.canv.axes
        sulf_esprelave.df.plot(x=0,y=2,ax=sulf_esprelave.canv.axes)
        legend=ax.legend()
        legend.set_draggable(True)
        ax.set_xlabel('Concentración [-]')
        ax.set_ylabel('Función estrés efectivo de sólido')
        ax.set_title('Función estrés efectivo de sólido vs Concentración')
        ax.set_xlim(0, 1)
        ax.grid(color='grey', linestyle='--', linewidth=.5)
        ax.set_adjustable("box") 
        sulf_esprelave.canv.draw()
    if value1 == "Función de dosificación":
        try:
            sulf_esprelave.horizontalLayout.removeWidget(sulf_esprelave.toolbar)
            sulf_esprelave.verticalLayout.removeWidget(sulf_esprelave.canv)
            
            sip.delete(sulf_esprelave.toolbar)
            sip.delete(sulf_esprelave.canv)
            sulf_esprelave.toolbar=None
            sulf_esprelave.canv=None
            sulf_esprelave.verticalLayout.removeItem(sulf_esprelave.spacerItem1)
        except Exception as e:
            print(e)
            pass
        sulf_esprelave.canv=MatplotlibCanvas(sulf_esprelave)
        sulf_esprelave.toolbar=Navi(sulf_esprelave.canv,sulf_esprelave.centralwidget)
        sulf_esprelave.horizontalLayout.addWidget(sulf_esprelave.toolbar)
        sulf_esprelave.verticalLayout.addWidget(sulf_esprelave.canv)
        sulf_esprelave.canv.axes.cla()
        ax=sulf_esprelave.canv.axes
        sulf_esprelave.df.plot(x=0,y=3,ax=sulf_esprelave.canv.axes)
        legend=ax.legend()
        legend.set_draggable(True)
        ax.set_xlabel('Concentración [-]')
        ax.set_ylabel('Función de dosificación')
        ax.set_title('Función de dosificación vs Concentración')
        ax.set_xlim(0, 1)
        ax.grid(color='grey', linestyle='--', linewidth=.5)
        ax.set_adjustable("box") 
        sulf_esprelave.canv.draw()
        
def simular_sulf_esprelave():
    graficos=['Función batch de Kynch','Función estrés efectivo de sólido','Función de dosificación']
    sulf_esprelave.comboBox_listagraficos.addItems(graficos) 

def getFile_sulf_esprelave():
    """this function will get the address of the csv file location also calls a readData function"""
    sulf_esprelave.filename=QFileDialog.getOpenFileName(filter="csv(*.csv)")[0]
    sulf_esprelave.archivo=sulf_esprelave.filename.split('/')
    #print("File:",self.archivo[-1])
    sulf_esprelave.browser_datos.append(sulf_esprelave.archivo[-1])
    readData_sulf_esprelave()
    
def readData_sulf_esprelave():
    """ This function will the data using pandas and call the update function to plot"""
    sulf_esprelave.df=pd.read_csv(sulf_esprelave.filename,encoding='utf-8').fillna(1)

def guardar_csv_sulf_esprelave():
    sulf_esprelave.to_filename=QFileDialog.getSaveFileName(filter="csv(*.csv)")[0]
    
    if sulf_esprelave.to_filename:
        sulf_esprelave.df.to_csv(sulf_esprelave.to_filename)   

#funciones perforacion (oxidados)  
def selectmodelo_oxid_perfo(value2):
    oxid_perfo.text_objetivo=['',
                        'Función Batch de Kynch, para la muestra de relave requerida',
                        'Función de estrés efectivo de sólido, para la muestra de relave requerida',
                        'Función de Dosificación, para la muestra de relave requerida',
                        'Función batch de Kynch, estrés efectivo de sólido y dosificación, \npara la muestra de relave requerida']
    oxid_perfo.text_requerimientos=['',
                              '1. Mineralogía de la muestra \n2. Gravedad específica',
                              '1. Mineralogía de la muestra \n2. Gravedad específica',
                              '1. Mineralogía de la muestra \n2. Gravedad específica',
                              '1. Mineralogía de la muestra \n2. Gravedad específica']
    oxid_perfo.text_resultados=['',
                          '1. Gráfico de Función batch de Kynch vs concentración de relave',
                          '1. Gráfico de Función de estrés efectivo de sólido vs concentración de relave',
                          '1. Gráfico de Dosificación vs concentración de relave',
                          '1. Gráfico de función batch de Kynch vs concentración de relave \n2. Gráfico de función de estrés efectivo de sólido \n3. Gráfico de función de dosificación']
    oxid_perfo.text_title=['',
                     'Función batch de Kynch',
                     'Función de estrés efectivo de sólido',
                     'Función de dosificación',
                     'Funciones constitutivas']
    for i in range(len(oxid_perfo.modelos)):
        if value2 == oxid_perfo.modelos[i]:
            oxid_perfo.info_title.setText(oxid_perfo.text_title[i])
            oxid_perfo.info_objetivo.setText(oxid_perfo.text_objetivo[i])
            oxid_perfo.info_requerimientos.setText(oxid_perfo.text_requerimientos[i])
            oxid_perfo.info_resultados.setText(oxid_perfo.text_resultados[i])

def resetear_oxid_perfo():
    oxid_perfo.browser_datos.clear() 
    oxid_perfo.comboBox_listagraficos.clear()
    oxid_perfo.comboBox_listamodelos.clear()
    oxid_perfo.comboBox_listamodelos.addItems(oxid_perfo.modelos)
    oxid_perfo.info_objetivo.clear()
    oxid_perfo.info_requerimientos.clear()
    oxid_perfo.info_resultados.clear()
    try:
        oxid_perfo.verticalLayout.removeWidget(oxid_perfo.canv)
        sip.delete(oxid_perfo.canv)
        oxid_perfo.canv=None
        oxid_perfo.verticalLayout.removeItem(oxid_perfo.spacerItem1)
    except Exception as e:
        print(e)
        pass     

def graficos_oxid_perfo(value1):  
    #print(value1)
    plt.style.use('classic')          
    if value1 == "Función batch de Kynch":
        try:
            oxid_perfo.horizontalLayout.removeWidget(oxid_perfo.toolbar)
            oxid_perfo.verticalLayout.removeWidget(oxid_perfo.canv)
            sip.delete(oxid_perfo.toolbar)
            sip.delete(oxid_perfo.canv)
            oxid_perfo.toolbar=None
            oxid_perfo.canv=None
            oxid_perfo.verticalLayout.removeItem(oxid_perfo.spacerItem1)
        except Exception as e:
            print(e)
            pass
        oxid_perfo.canv=MatplotlibCanvas(oxid_perfo)
        oxid_perfo.toolbar=Navi(oxid_perfo.canv,oxid_perfo.centralwidget)
        oxid_perfo.horizontalLayout.addWidget(oxid_perfo.toolbar)
        oxid_perfo.verticalLayout.addWidget(oxid_perfo.canv)
        oxid_perfo.canv.axes.cla()
        ax=oxid_perfo.canv.axes
        oxid_perfo.df.plot(x=0,y=1,ax=oxid_perfo.canv.axes)
        legend=ax.legend()
        legend.set_draggable(True)
        ax.set_xlabel('Concentración [-]')
        ax.set_ylabel('Función batch de Kynch')
        ax.set_title('Función batch de Kynch (f_bk) vs Concentración')
        ax.set_xlim(0, 1)
        ax.grid(color='grey', linestyle='--', linewidth=.5)
        ax.set_adjustable("box") 
        oxid_perfo.canv.draw()
    if value1 == "Función estrés efectivo de sólido":
        try:
            oxid_perfo.horizontalLayout.removeWidget(oxid_perfo.toolbar)
            oxid_perfo.verticalLayout.removeWidget(oxid_perfo.canv)
            sip.delete(oxid_perfo.toolbar)
            sip.delete(oxid_perfo.canv)
            oxid_perfo.toolbar=None
            oxid_perfo.canv=None
            oxid_perfo.verticalLayout.removeItem(oxid_perfo.spacerItem1)
        except Exception as e:
            print(e)
            pass
        oxid_perfo.canv=MatplotlibCanvas(oxid_perfo)
        oxid_perfo.toolbar=Navi(oxid_perfo.canv,oxid_perfo.centralwidget)
        oxid_perfo.horizontalLayout.addWidget(oxid_perfo.toolbar)
        oxid_perfo.verticalLayout.addWidget(oxid_perfo.canv)
        oxid_perfo.canv.axes.cla()
        ax=oxid_perfo.canv.axes
        oxid_perfo.df.plot(x=0,y=2,ax=oxid_perfo.canv.axes)
        legend=ax.legend()
        legend.set_draggable(True)
        ax.set_xlabel('Concentración [-]')
        ax.set_ylabel('Función estrés efectivo de sólido')
        ax.set_title('Función estrés efectivo de sólido vs Concentración')
        ax.set_xlim(0, 1)
        ax.grid(color='grey', linestyle='--', linewidth=.5)
        ax.set_adjustable("box") 
        oxid_perfo.canv.draw()
    if value1 == "Función de dosificación":
        try:
            oxid_perfo.horizontalLayout.removeWidget(oxid_perfo.toolbar)
            oxid_perfo.verticalLayout.removeWidget(oxid_perfo.canv)
            
            sip.delete(oxid_perfo.toolbar)
            sip.delete(oxid_perfo.canv)
            oxid_perfo.toolbar=None
            oxid_perfo.canv=None
            oxid_perfo.verticalLayout.removeItem(oxid_perfo.spacerItem1)
        except Exception as e:
            print(e)
            pass
        oxid_perfo.canv=MatplotlibCanvas(oxid_perfo)
        oxid_perfo.toolbar=Navi(oxid_perfo.canv,oxid_perfo.centralwidget)
        oxid_perfo.horizontalLayout.addWidget(oxid_perfo.toolbar)
        oxid_perfo.verticalLayout.addWidget(oxid_perfo.canv)
        oxid_perfo.canv.axes.cla()
        ax=oxid_perfo.canv.axes
        oxid_perfo.df.plot(x=0,y=3,ax=oxid_perfo.canv.axes)
        legend=ax.legend()
        legend.set_draggable(True)
        ax.set_xlabel('Concentración [-]')
        ax.set_ylabel('Función de dosificación')
        ax.set_title('Función de dosificación vs Concentración')
        ax.set_xlim(0, 1)
        ax.grid(color='grey', linestyle='--', linewidth=.5)
        ax.set_adjustable("box") 
        oxid_perfo.canv.draw()
        
def simular_oxid_perfo():
    graficos=['Función batch de Kynch','Función estrés efectivo de sólido','Función de dosificación']
    oxid_perfo.comboBox_listagraficos.addItems(graficos) 

def getFile_oxid_perfo():
    """this function will get the address of the csv file location also calls a readData function"""
    oxid_perfo.filename=QFileDialog.getOpenFileName(filter="csv(*.csv)")[0]
    oxid_perfo.archivo=oxid_perfo.filename.split('/')
    #print("File:",self.archivo[-1])
    oxid_perfo.browser_datos.append(oxid_perfo.archivo[-1])
    readData_oxid_perfo()
    
def readData_oxid_perfo():
    """ This function will the data using pandas and call the update function to plot"""
    oxid_perfo.df=pd.read_csv(oxid_perfo.filename,encoding='utf-8').fillna(1)

def guardar_csv_oxid_perfo():
    oxid_perfo.to_filename=QFileDialog.getSaveFileName(filter="csv(*.csv)")[0]
    
    if oxid_perfo.to_filename:
        oxid_perfo.df.to_csv(oxid_perfo.to_filename)

#Funciones carguio (oxidados)
def selectmodelo_oxid_carguio(value2):
    oxid_carguio.text_objetivo=['',
                        'Función Batch de Kynch, para la muestra de relave requerida',
                        'Función de estrés efectivo de sólido, para la muestra de relave requerida',
                        'Función de Dosificación, para la muestra de relave requerida',
                        'Función batch de Kynch, estrés efectivo de sólido y dosificación, \npara la muestra de relave requerida']
    oxid_carguio.text_requerimientos=['',
                              '1. Mineralogía de la muestra \n2. Gravedad específica',
                              '1. Mineralogía de la muestra \n2. Gravedad específica',
                              '1. Mineralogía de la muestra \n2. Gravedad específica',
                              '1. Mineralogía de la muestra \n2. Gravedad específica']
    oxid_carguio.text_resultados=['',
                          '1. Gráfico de Función batch de Kynch vs concentración de relave',
                          '1. Gráfico de Función de estrés efectivo de sólido vs concentración de relave',
                          '1. Gráfico de Dosificación vs concentración de relave',
                          '1. Gráfico de función batch de Kynch vs concentración de relave \n2. Gráfico de función de estrés efectivo de sólido \n3. Gráfico de función de dosificación']
    oxid_carguio.text_title=['',
                     'Función batch de Kynch',
                     'Función de estrés efectivo de sólido',
                     'Función de dosificación',
                     'Funciones constitutivas']
    for i in range(len(oxid_carguio.modelos)):
        if value2 == oxid_carguio.modelos[i]:
            oxid_carguio.info_title.setText(oxid_carguio.text_title[i])
            oxid_carguio.info_objetivo.setText(oxid_carguio.text_objetivo[i])
            oxid_carguio.info_requerimientos.setText(oxid_carguio.text_requerimientos[i])
            oxid_carguio.info_resultados.setText(oxid_carguio.text_resultados[i])

def resetear_oxid_carguio():
    oxid_carguio.browser_datos.clear() 
    oxid_carguio.comboBox_listagraficos.clear()
    oxid_carguio.comboBox_listamodelos.clear()
    oxid_carguio.comboBox_listamodelos.addItems(oxid_carguio.modelos)
    oxid_carguio.info_objetivo.clear()
    oxid_carguio.info_requerimientos.clear()
    oxid_carguio.info_resultados.clear()
    try:
        oxid_carguio.verticalLayout.removeWidget(oxid_carguio.canv)
        sip.delete(oxid_carguio.canv)
        oxid_carguio.canv=None
        oxid_carguio.verticalLayout.removeItem(oxid_carguio.spacerItem1)
    except Exception as e:
        print(e)
        pass     

def graficos_oxid_carguio(value1):  
    #print(value1)
    plt.style.use('classic')          
    if value1 == "Función batch de Kynch":
        try:
            oxid_carguio.horizontalLayout.removeWidget(oxid_carguio.toolbar)
            oxid_carguio.verticalLayout.removeWidget(oxid_carguio.canv)
            sip.delete(oxid_carguio.toolbar)
            sip.delete(oxid_carguio.canv)
            oxid_carguio.toolbar=None
            oxid_carguio.canv=None
            oxid_carguio.verticalLayout.removeItem(oxid_carguio.spacerItem1)
        except Exception as e:
            print(e)
            pass
        oxid_carguio.canv=MatplotlibCanvas(oxid_carguio)
        oxid_carguio.toolbar=Navi(oxid_carguio.canv,oxid_carguio.centralwidget)
        oxid_carguio.horizontalLayout.addWidget(oxid_carguio.toolbar)
        oxid_carguio.verticalLayout.addWidget(oxid_carguio.canv)
        oxid_carguio.canv.axes.cla()
        ax=oxid_carguio.canv.axes
        oxid_carguio.df.plot(x=0,y=1,ax=oxid_carguio.canv.axes)
        legend=ax.legend()
        legend.set_draggable(True)
        ax.set_xlabel('Concentración [-]')
        ax.set_ylabel('Función batch de Kynch')
        ax.set_title('Función batch de Kynch (f_bk) vs Concentración')
        ax.set_xlim(0, 1)
        ax.grid(color='grey', linestyle='--', linewidth=.5)
        ax.set_adjustable("box") 
        oxid_carguio.canv.draw()
    if value1 == "Función estrés efectivo de sólido":
        try:
            oxid_carguio.horizontalLayout.removeWidget(oxid_carguio.toolbar)
            oxid_carguio.verticalLayout.removeWidget(oxid_carguio.canv)
            sip.delete(oxid_carguio.toolbar)
            sip.delete(oxid_carguio.canv)
            oxid_carguio.toolbar=None
            oxid_carguio.canv=None
            oxid_carguio.verticalLayout.removeItem(oxid_carguio.spacerItem1)
        except Exception as e:
            print(e)
            pass
        oxid_carguio.canv=MatplotlibCanvas(oxid_carguio)
        oxid_carguio.toolbar=Navi(oxid_carguio.canv,oxid_carguio.centralwidget)
        oxid_carguio.horizontalLayout.addWidget(oxid_carguio.toolbar)
        oxid_carguio.verticalLayout.addWidget(oxid_carguio.canv)
        oxid_carguio.canv.axes.cla()
        ax=oxid_carguio.canv.axes
        oxid_carguio.df.plot(x=0,y=2,ax=oxid_carguio.canv.axes)
        legend=ax.legend()
        legend.set_draggable(True)
        ax.set_xlabel('Concentración [-]')
        ax.set_ylabel('Función estrés efectivo de sólido')
        ax.set_title('Función estrés efectivo de sólido vs Concentración')
        ax.set_xlim(0, 1)
        ax.grid(color='grey', linestyle='--', linewidth=.5)
        ax.set_adjustable("box") 
        oxid_carguio.canv.draw()
    if value1 == "Función de dosificación":
        try:
            oxid_carguio.horizontalLayout.removeWidget(oxid_carguio.toolbar)
            oxid_carguio.verticalLayout.removeWidget(oxid_carguio.canv)
            
            sip.delete(oxid_carguio.toolbar)
            sip.delete(oxid_carguio.canv)
            oxid_carguio.toolbar=None
            oxid_carguio.canv=None
            oxid_carguio.verticalLayout.removeItem(oxid_carguio.spacerItem1)
        except Exception as e:
            print(e)
            pass
        oxid_carguio.canv=MatplotlibCanvas(oxid_carguio)
        oxid_carguio.toolbar=Navi(oxid_carguio.canv,oxid_carguio.centralwidget)
        oxid_carguio.horizontalLayout.addWidget(oxid_carguio.toolbar)
        oxid_carguio.verticalLayout.addWidget(oxid_carguio.canv)
        oxid_carguio.canv.axes.cla()
        ax=oxid_carguio.canv.axes
        oxid_carguio.df.plot(x=0,y=3,ax=oxid_carguio.canv.axes)
        legend=ax.legend()
        legend.set_draggable(True)
        ax.set_xlabel('Concentración [-]')
        ax.set_ylabel('Función de dosificación')
        ax.set_title('Función de dosificación vs Concentración')
        ax.set_xlim(0, 1)
        ax.grid(color='grey', linestyle='--', linewidth=.5)
        ax.set_adjustable("box") 
        oxid_carguio.canv.draw()
        
def simular_oxid_carguio():
    graficos=['Función batch de Kynch','Función estrés efectivo de sólido','Función de dosificación']
    oxid_carguio.comboBox_listagraficos.addItems(graficos) 

def getFile_oxid_carguio():
    """this function will get the address of the csv file location also calls a readData function"""
    oxid_carguio.filename=QFileDialog.getOpenFileName(filter="csv(*.csv)")[0]
    oxid_carguio.archivo=oxid_carguio.filename.split('/')
    oxid_carguio.browser_datos.append(oxid_carguio.archivo[-1])
    readData_oxid_carguio()
    
def readData_oxid_carguio():
    """ This function will the data using pandas and call the update function to plot"""
    oxid_carguio.df=pd.read_csv(oxid_carguio.filename,encoding='utf-8').fillna(1)

def guardar_csv_oxid_carguio():
    oxid_carguio.to_filename=QFileDialog.getSaveFileName(filter="csv(*.csv)")[0]
    
    if oxid_carguio.to_filename:
        oxid_carguio.df.to_csv(oxid_carguio.to_filename)
        
#funciones chancado  (oxidados)  
def selectmodelo_oxid_chancado(value2):
    oxid_chancado.text_objetivo=['',
                        'Función Batch de Kynch, para la muestra de relave requerida',
                        'Función de estrés efectivo de sólido, para la muestra de relave requerida',
                        'Función de Dosificación, para la muestra de relave requerida',
                        'Función batch de Kynch, estrés efectivo de sólido y dosificación, \npara la muestra de relave requerida']
    oxid_chancado.text_requerimientos=['',
                              '1. Mineralogía de la muestra \n2. Gravedad específica',
                              '1. Mineralogía de la muestra \n2. Gravedad específica',
                              '1. Mineralogía de la muestra \n2. Gravedad específica',
                              '1. Mineralogía de la muestra \n2. Gravedad específica']
    oxid_chancado.text_resultados=['',
                          '1. Gráfico de Función batch de Kynch vs concentración de relave',
                          '1. Gráfico de Función de estrés efectivo de sólido vs concentración de relave',
                          '1. Gráfico de Dosificación vs concentración de relave',
                          '1. Gráfico de función batch de Kynch vs concentración de relave \n2. Gráfico de función de estrés efectivo de sólido \n3. Gráfico de función de dosificación']
    oxid_chancado.text_title=['',
                     'Función batch de Kynch',
                     'Función de estrés efectivo de sólido',
                     'Función de dosificación',
                     'Funciones constitutivas']
    for i in range(len(oxid_chancado.modelos)):
        if value2 == oxid_chancado.modelos[i]:
            oxid_chancado.info_title.setText(oxid_chancado.text_title[i])
            oxid_chancado.info_objetivo.setText(oxid_chancado.text_objetivo[i])
            oxid_chancado.info_requerimientos.setText(oxid_chancado.text_requerimientos[i])
            oxid_chancado.info_resultados.setText(oxid_chancado.text_resultados[i])

def resetear_oxid_chancado():
    oxid_chancado.browser_datos.clear() 
    oxid_chancado.comboBox_listagraficos.clear()
    oxid_chancado.comboBox_listamodelos.clear()
    oxid_chancado.comboBox_listamodelos.addItems(oxid_chancado.modelos)
    oxid_chancado.info_objetivo.clear()
    oxid_chancado.info_requerimientos.clear()
    oxid_chancado.info_resultados.clear()
    try:
        oxid_chancado.verticalLayout.removeWidget(oxid_chancado.canv)
        sip.delete(oxid_chancado.canv)
        oxid_chancado.canv=None
        oxid_chancado.verticalLayout.removeItem(oxid_chancado.spacerItem1)
    except Exception as e:
        print(e)
        pass     

def graficos_oxid_chancado(value1):  
    #print(value1)
    plt.style.use('classic')          
    if value1 == "Función batch de Kynch":
        try:
            oxid_chancado.horizontalLayout.removeWidget(oxid_chancado.toolbar)
            oxid_chancado.verticalLayout.removeWidget(oxid_chancado.canv)
            sip.delete(oxid_chancado.toolbar)
            sip.delete(oxid_chancado.canv)
            oxid_chancado.toolbar=None
            oxid_chancado.canv=None
            oxid_chancado.verticalLayout.removeItem(oxid_chancado.spacerItem1)
        except Exception as e:
            print(e)
            pass
        oxid_chancado.canv=MatplotlibCanvas(oxid_chancado)
        oxid_chancado.toolbar=Navi(oxid_chancado.canv,oxid_chancado.centralwidget)
        oxid_chancado.horizontalLayout.addWidget(oxid_chancado.toolbar)
        oxid_chancado.verticalLayout.addWidget(oxid_chancado.canv)
        oxid_chancado.canv.axes.cla()
        ax=oxid_chancado.canv.axes
        oxid_chancado.df.plot(x=0,y=1,ax=oxid_chancado.canv.axes)
        legend=ax.legend()
        legend.set_draggable(True)
        ax.set_xlabel('Concentración [-]')
        ax.set_ylabel('Función batch de Kynch')
        ax.set_title('Función batch de Kynch (f_bk) vs Concentración')
        ax.set_xlim(0, 1)
        ax.grid(color='grey', linestyle='--', linewidth=.5)
        ax.set_adjustable("box") 
        oxid_chancado.canv.draw()
    if value1 == "Función estrés efectivo de sólido":
        try:
            oxid_chancado.horizontalLayout.removeWidget(oxid_chancado.toolbar)
            oxid_chancado.verticalLayout.removeWidget(oxid_chancado.canv)
            sip.delete(oxid_chancado.toolbar)
            sip.delete(oxid_chancado.canv)
            oxid_chancado.toolbar=None
            oxid_chancado.canv=None
            oxid_chancado.verticalLayout.removeItem(oxid_chancado.spacerItem1)
        except Exception as e:
            print(e)
            pass
        oxid_chancado.canv=MatplotlibCanvas(oxid_chancado)
        oxid_chancado.toolbar=Navi(oxid_chancado.canv,oxid_chancado.centralwidget)
        oxid_chancado.horizontalLayout.addWidget(oxid_chancado.toolbar)
        oxid_chancado.verticalLayout.addWidget(oxid_chancado.canv)
        oxid_chancado.canv.axes.cla()
        ax=oxid_chancado.canv.axes
        oxid_chancado.df.plot(x=0,y=2,ax=oxid_chancado.canv.axes)
        legend=ax.legend()
        legend.set_draggable(True)
        ax.set_xlabel('Concentración [-]')
        ax.set_ylabel('Función estrés efectivo de sólido')
        ax.set_title('Función estrés efectivo de sólido vs Concentración')
        ax.set_xlim(0, 1)
        ax.grid(color='grey', linestyle='--', linewidth=.5)
        ax.set_adjustable("box") 
        oxid_chancado.canv.draw()
    if value1 == "Función de dosificación":
        try:
            oxid_chancado.horizontalLayout.removeWidget(oxid_chancado.toolbar)
            oxid_chancado.verticalLayout.removeWidget(oxid_chancado.canv)
            
            sip.delete(oxid_chancado.toolbar)
            sip.delete(oxid_chancado.canv)
            oxid_chancado.toolbar=None
            oxid_chancado.canv=None
            oxid_chancado.verticalLayout.removeItem(oxid_chancado.spacerItem1)
        except Exception as e:
            print(e)
            pass
        oxid_chancado.canv=MatplotlibCanvas(oxid_chancado)
        oxid_chancado.toolbar=Navi(oxid_chancado.canv,oxid_chancado.centralwidget)
        oxid_chancado.horizontalLayout.addWidget(oxid_chancado.toolbar)
        oxid_chancado.verticalLayout.addWidget(oxid_chancado.canv)
        oxid_chancado.canv.axes.cla()
        ax=oxid_chancado.canv.axes
        oxid_chancado.df.plot(x=0,y=3,ax=oxid_chancado.canv.axes)
        legend=ax.legend()
        legend.set_draggable(True)
        ax.set_xlabel('Concentración [-]')
        ax.set_ylabel('Función de dosificación')
        ax.set_title('Función de dosificación vs Concentración')
        ax.set_xlim(0, 1)
        ax.grid(color='grey', linestyle='--', linewidth=.5)
        ax.set_adjustable("box") 
        oxid_chancado.canv.draw()
        
def simular_oxid_chancado():
    graficos=['Función batch de Kynch','Función estrés efectivo de sólido','Función de dosificación']
    oxid_chancado.comboBox_listagraficos.addItems(graficos) 

def getFile_oxid_chancado():
    """this function will get the address of the csv file location also calls a readData function"""
    oxid_chancado.filename=QFileDialog.getOpenFileName(filter="csv(*.csv)")[0]
    oxid_chancado.archivo=oxid_chancado.filename.split('/')
    #print("File:",self.archivo[-1])
    oxid_chancado.browser_datos.append(oxid_chancado.archivo[-1])
    readData_oxid_chancado()
    
def readData_oxid_chancado():
    """ This function will the data using pandas and call the update function to plot"""
    oxid_chancado.df=pd.read_csv(oxid_chancado.filename,encoding='utf-8').fillna(1)

def guardar_csv_oxid_chancado():
    oxid_chancado.to_filename=QFileDialog.getSaveFileName(filter="csv(*.csv)")[0]
    
    if oxid_chancado.to_filename:
        oxid_chancado.df.to_csv(oxid_chancado.to_filename)

#funciones lixiviacion (oxidados)  
def selectmodelo_oxid_lixiviacion(value2):
    oxid_lixiviacion.text_objetivo=['',
                        'Función Batch de Kynch, para la muestra de relave requerida',
                        'Función de estrés efectivo de sólido, para la muestra de relave requerida',
                        'Función de Dosificación, para la muestra de relave requerida',
                        'Función batch de Kynch, estrés efectivo de sólido y dosificación, \npara la muestra de relave requerida']
    oxid_lixiviacion.text_requerimientos=['',
                              '1. Mineralogía de la muestra \n2. Gravedad específica',
                              '1. Mineralogía de la muestra \n2. Gravedad específica',
                              '1. Mineralogía de la muestra \n2. Gravedad específica',
                              '1. Mineralogía de la muestra \n2. Gravedad específica']
    oxid_lixiviacion.text_resultados=['',
                          '1. Gráfico de Función batch de Kynch vs concentración de relave',
                          '1. Gráfico de Función de estrés efectivo de sólido vs concentración de relave',
                          '1. Gráfico de Dosificación vs concentración de relave',
                          '1. Gráfico de función batch de Kynch vs concentración de relave \n2. Gráfico de función de estrés efectivo de sólido \n3. Gráfico de función de dosificación']
    oxid_lixiviacion.text_title=['',
                     'Función batch de Kynch',
                     'Función de estrés efectivo de sólido',
                     'Función de dosificación',
                     'Funciones constitutivas']
    for i in range(len(oxid_lixiviacion.modelos)):
        if value2 == oxid_lixiviacion.modelos[i]:
            oxid_lixiviacion.info_title.setText(oxid_lixiviacion.text_title[i])
            oxid_lixiviacion.info_objetivo.setText(oxid_lixiviacion.text_objetivo[i])
            oxid_lixiviacion.info_requerimientos.setText(oxid_lixiviacion.text_requerimientos[i])
            oxid_lixiviacion.info_resultados.setText(oxid_lixiviacion.text_resultados[i])

def resetear_oxid_lixiviacion():
    oxid_lixiviacion.browser_datos.clear() 
    oxid_lixiviacion.comboBox_listagraficos.clear()
    oxid_lixiviacion.comboBox_listamodelos.clear()
    oxid_lixiviacion.comboBox_listamodelos.addItems(oxid_lixiviacion.modelos)
    oxid_lixiviacion.info_objetivo.clear()
    oxid_lixiviacion.info_requerimientos.clear()
    oxid_lixiviacion.info_resultados.clear()
    try:
        oxid_lixiviacion.verticalLayout.removeWidget(oxid_lixiviacion.canv)
        sip.delete(oxid_lixiviacion.canv)
        oxid_lixiviacion.canv=None
        oxid_lixiviacion.verticalLayout.removeItem(oxid_lixiviacion.spacerItem1)
    except Exception as e:
        print(e)
        pass     

def graficos_oxid_lixiviacion(value1):  
    #print(value1)
    plt.style.use('classic')          
    if value1 == "Función batch de Kynch":
        try:
            oxid_lixiviacion.horizontalLayout.removeWidget(oxid_lixiviacion.toolbar)
            oxid_lixiviacion.verticalLayout.removeWidget(oxid_lixiviacion.canv)
            sip.delete(oxid_lixiviacion.toolbar)
            sip.delete(oxid_lixiviacion.canv)
            oxid_lixiviacion.toolbar=None
            oxid_lixiviacion.canv=None
            oxid_lixiviacion.verticalLayout.removeItem(oxid_lixiviacion.spacerItem1)
        except Exception as e:
            print(e)
            pass
        oxid_lixiviacion.canv=MatplotlibCanvas(oxid_lixiviacion)
        oxid_lixiviacion.toolbar=Navi(oxid_lixiviacion.canv,oxid_lixiviacion.centralwidget)
        oxid_lixiviacion.horizontalLayout.addWidget(oxid_lixiviacion.toolbar)
        oxid_lixiviacion.verticalLayout.addWidget(oxid_lixiviacion.canv)
        oxid_lixiviacion.canv.axes.cla()
        ax=oxid_lixiviacion.canv.axes
        oxid_lixiviacion.df.plot(x=0,y=1,ax=oxid_lixiviacion.canv.axes)
        legend=ax.legend()
        legend.set_draggable(True)
        ax.set_xlabel('Concentración [-]')
        ax.set_ylabel('Función batch de Kynch')
        ax.set_title('Función batch de Kynch (f_bk) vs Concentración')
        ax.set_xlim(0, 1)
        ax.grid(color='grey', linestyle='--', linewidth=.5)
        ax.set_adjustable("box") 
        oxid_lixiviacion.canv.draw()
    if value1 == "Función estrés efectivo de sólido":
        try:
            oxid_lixiviacion.horizontalLayout.removeWidget(oxid_lixiviacion.toolbar)
            oxid_lixiviacion.verticalLayout.removeWidget(oxid_lixiviacion.canv)
            sip.delete(oxid_lixiviacion.toolbar)
            sip.delete(oxid_lixiviacion.canv)
            oxid_lixiviacion.toolbar=None
            oxid_lixiviacion.canv=None
            oxid_lixiviacion.verticalLayout.removeItem(oxid_lixiviacion.spacerItem1)
        except Exception as e:
            print(e)
            pass
        oxid_lixiviacion.canv=MatplotlibCanvas(oxid_lixiviacion)
        oxid_lixiviacion.toolbar=Navi(oxid_lixiviacion.canv,oxid_lixiviacion.centralwidget)
        oxid_lixiviacion.horizontalLayout.addWidget(oxid_lixiviacion.toolbar)
        oxid_lixiviacion.verticalLayout.addWidget(oxid_lixiviacion.canv)
        oxid_lixiviacion.canv.axes.cla()
        ax=oxid_lixiviacion.canv.axes
        oxid_lixiviacion.df.plot(x=0,y=2,ax=oxid_lixiviacion.canv.axes)
        legend=ax.legend()
        legend.set_draggable(True)
        ax.set_xlabel('Concentración [-]')
        ax.set_ylabel('Función estrés efectivo de sólido')
        ax.set_title('Función estrés efectivo de sólido vs Concentración')
        ax.set_xlim(0, 1)
        ax.grid(color='grey', linestyle='--', linewidth=.5)
        ax.set_adjustable("box") 
        oxid_lixiviacion.canv.draw()
    if value1 == "Función de dosificación":
        try:
            oxid_lixiviacion.horizontalLayout.removeWidget(oxid_lixiviacion.toolbar)
            oxid_lixiviacion.verticalLayout.removeWidget(oxid_lixiviacion.canv)
            
            sip.delete(oxid_lixiviacion.toolbar)
            sip.delete(oxid_lixiviacion.canv)
            oxid_lixiviacion.toolbar=None
            oxid_lixiviacion.canv=None
            oxid_lixiviacion.verticalLayout.removeItem(oxid_lixiviacion.spacerItem1)
        except Exception as e:
            print(e)
            pass
        oxid_lixiviacion.canv=MatplotlibCanvas(oxid_lixiviacion)
        oxid_lixiviacion.toolbar=Navi(oxid_lixiviacion.canv,oxid_lixiviacion.centralwidget)
        oxid_lixiviacion.horizontalLayout.addWidget(oxid_lixiviacion.toolbar)
        oxid_lixiviacion.verticalLayout.addWidget(oxid_lixiviacion.canv)
        oxid_lixiviacion.canv.axes.cla()
        ax=oxid_lixiviacion.canv.axes
        oxid_lixiviacion.df.plot(x=0,y=3,ax=oxid_lixiviacion.canv.axes)
        legend=ax.legend()
        legend.set_draggable(True)
        ax.set_xlabel('Concentración [-]')
        ax.set_ylabel('Función de dosificación')
        ax.set_title('Función de dosificación vs Concentración')
        ax.set_xlim(0, 1)
        ax.grid(color='grey', linestyle='--', linewidth=.5)
        ax.set_adjustable("box") 
        oxid_lixiviacion.canv.draw()
        
def simular_oxid_lixiviacion():
    graficos=['Función batch de Kynch','Función estrés efectivo de sólido','Función de dosificación']
    oxid_lixiviacion.comboBox_listagraficos.addItems(graficos) 

def getFile_oxid_lixiviacion():
    """this function will get the address of the csv file location also calls a readData function"""
    oxid_lixiviacion.filename=QFileDialog.getOpenFileName(filter="csv(*.csv)")[0]
    oxid_lixiviacion.archivo=oxid_lixiviacion.filename.split('/')
    #print("File:",self.archivo[-1])
    oxid_lixiviacion.browser_datos.append(oxid_lixiviacion.archivo[-1])
    readData_oxid_lixiviacion()
    
def readData_oxid_lixiviacion():
    """ This function will the data using pandas and call the update function to plot"""
    oxid_lixiviacion.df=pd.read_csv(oxid_lixiviacion.filename,encoding='utf-8').fillna(1)

def guardar_csv_oxid_lixiviacion():
    oxid_lixiviacion.to_filename=QFileDialog.getSaveFileName(filter="csv(*.csv)")[0]
    
    if oxid_lixiviacion.to_filename:
        oxid_lixiviacion.df.to_csv(oxid_lixiviacion.to_filename) 

#funciones SX (oxidados)  
def selectmodelo_oxid_SX(value2):
    oxid_SX.text_objetivo=['',
                        'Función Batch de Kynch, para la muestra de relave requerida',
                        'Función de estrés efectivo de sólido, para la muestra de relave requerida',
                        'Función de Dosificación, para la muestra de relave requerida',
                        'Función batch de Kynch, estrés efectivo de sólido y dosificación, \npara la muestra de relave requerida']
    oxid_SX.text_requerimientos=['',
                              '1. Mineralogía de la muestra \n2. Gravedad específica',
                              '1. Mineralogía de la muestra \n2. Gravedad específica',
                              '1. Mineralogía de la muestra \n2. Gravedad específica',
                              '1. Mineralogía de la muestra \n2. Gravedad específica']
    oxid_SX.text_resultados=['',
                          '1. Gráfico de Función batch de Kynch vs concentración de relave',
                          '1. Gráfico de Función de estrés efectivo de sólido vs concentración de relave',
                          '1. Gráfico de Dosificación vs concentración de relave',
                          '1. Gráfico de función batch de Kynch vs concentración de relave \n2. Gráfico de función de estrés efectivo de sólido \n3. Gráfico de función de dosificación']
    oxid_SX.text_title=['',
                     'Función batch de Kynch',
                     'Función de estrés efectivo de sólido',
                     'Función de dosificación',
                     'Funciones constitutivas']
    for i in range(len(oxid_SX.modelos)):
        if value2 == oxid_SX.modelos[i]:
            oxid_SX.info_title.setText(oxid_SX.text_title[i])
            oxid_SX.info_objetivo.setText(oxid_SX.text_objetivo[i])
            oxid_SX.info_requerimientos.setText(oxid_SX.text_requerimientos[i])
            oxid_SX.info_resultados.setText(oxid_SX.text_resultados[i])

def resetear_oxid_SX():
    oxid_SX.browser_datos.clear() 
    oxid_SX.comboBox_listagraficos.clear()
    oxid_SX.comboBox_listamodelos.clear()
    oxid_SX.comboBox_listamodelos.addItems(oxid_SX.modelos)
    oxid_SX.info_objetivo.clear()
    oxid_SX.info_requerimientos.clear()
    oxid_SX.info_resultados.clear()
    try:
        oxid_SX.verticalLayout.removeWidget(oxid_SX.canv)
        sip.delete(oxid_SX.canv)
        oxid_SX.canv=None
        oxid_SX.verticalLayout.removeItem(oxid_SX.spacerItem1)
    except Exception as e:
        print(e)
        pass     

def graficos_oxid_SX(value1):  
    #print(value1)
    plt.style.use('classic')          
    if value1 == "Función batch de Kynch":
        try:
            oxid_SX.horizontalLayout.removeWidget(oxid_SX.toolbar)
            oxid_SX.verticalLayout.removeWidget(oxid_SX.canv)
            sip.delete(oxid_SX.toolbar)
            sip.delete(oxid_SX.canv)
            oxid_SX.toolbar=None
            oxid_SX.canv=None
            oxid_SX.verticalLayout.removeItem(oxid_SX.spacerItem1)
        except Exception as e:
            print(e)
            pass
        oxid_SX.canv=MatplotlibCanvas(oxid_SX)
        oxid_SX.toolbar=Navi(oxid_SX.canv,oxid_SX.centralwidget)
        oxid_SX.horizontalLayout.addWidget(oxid_SX.toolbar)
        oxid_SX.verticalLayout.addWidget(oxid_SX.canv)
        oxid_SX.canv.axes.cla()
        ax=oxid_SX.canv.axes
        oxid_SX.df.plot(x=0,y=1,ax=oxid_SX.canv.axes)
        legend=ax.legend()
        legend.set_draggable(True)
        ax.set_xlabel('Concentración [-]')
        ax.set_ylabel('Función batch de Kynch')
        ax.set_title('Función batch de Kynch (f_bk) vs Concentración')
        ax.set_xlim(0, 1)
        ax.grid(color='grey', linestyle='--', linewidth=.5)
        ax.set_adjustable("box") 
        oxid_SX.canv.draw()
    if value1 == "Función estrés efectivo de sólido":
        try:
            oxid_SX.horizontalLayout.removeWidget(oxid_SX.toolbar)
            oxid_SX.verticalLayout.removeWidget(oxid_SX.canv)
            sip.delete(oxid_SX.toolbar)
            sip.delete(oxid_SX.canv)
            oxid_SX.toolbar=None
            oxid_SX.canv=None
            oxid_SX.verticalLayout.removeItem(oxid_SX.spacerItem1)
        except Exception as e:
            print(e)
            pass
        oxid_SX.canv=MatplotlibCanvas(oxid_SX)
        oxid_SX.toolbar=Navi(oxid_SX.canv,oxid_SX.centralwidget)
        oxid_SX.horizontalLayout.addWidget(oxid_SX.toolbar)
        oxid_SX.verticalLayout.addWidget(oxid_SX.canv)
        oxid_SX.canv.axes.cla()
        ax=oxid_SX.canv.axes
        oxid_SX.df.plot(x=0,y=2,ax=oxid_SX.canv.axes)
        legend=ax.legend()
        legend.set_draggable(True)
        ax.set_xlabel('Concentración [-]')
        ax.set_ylabel('Función estrés efectivo de sólido')
        ax.set_title('Función estrés efectivo de sólido vs Concentración')
        ax.set_xlim(0, 1)
        ax.grid(color='grey', linestyle='--', linewidth=.5)
        ax.set_adjustable("box") 
        oxid_SX.canv.draw()
    if value1 == "Función de dosificación":
        try:
            oxid_SX.horizontalLayout.removeWidget(oxid_SX.toolbar)
            oxid_SX.verticalLayout.removeWidget(oxid_SX.canv)
            
            sip.delete(oxid_SX.toolbar)
            sip.delete(oxid_SX.canv)
            oxid_SX.toolbar=None
            oxid_SX.canv=None
            oxid_SX.verticalLayout.removeItem(oxid_SX.spacerItem1)
        except Exception as e:
            print(e)
            pass
        oxid_SX.canv=MatplotlibCanvas(oxid_SX)
        oxid_SX.toolbar=Navi(oxid_SX.canv,oxid_SX.centralwidget)
        oxid_SX.horizontalLayout.addWidget(oxid_SX.toolbar)
        oxid_SX.verticalLayout.addWidget(oxid_SX.canv)
        oxid_SX.canv.axes.cla()
        ax=oxid_SX.canv.axes
        oxid_SX.df.plot(x=0,y=3,ax=oxid_SX.canv.axes)
        legend=ax.legend()
        legend.set_draggable(True)
        ax.set_xlabel('Concentración [-]')
        ax.set_ylabel('Función de dosificación')
        ax.set_title('Función de dosificación vs Concentración')
        ax.set_xlim(0, 1)
        ax.grid(color='grey', linestyle='--', linewidth=.5)
        ax.set_adjustable("box") 
        oxid_SX.canv.draw()
        
def simular_oxid_SX():
    graficos=['Función batch de Kynch','Función estrés efectivo de sólido','Función de dosificación']
    oxid_SX.comboBox_listagraficos.addItems(graficos) 

def getFile_oxid_SX():
    """this function will get the address of the csv file location also calls a readData function"""
    oxid_SX.filename=QFileDialog.getOpenFileName(filter="csv(*.csv)")[0]
    oxid_SX.archivo=oxid_SX.filename.split('/')
    #print("File:",self.archivo[-1])
    oxid_SX.browser_datos.append(oxid_SX.archivo[-1])
    readData_oxid_SX()
    
def readData_oxid_SX():
    """ This function will the data using pandas and call the update function to plot"""
    oxid_SX.df=pd.read_csv(oxid_SX.filename,encoding='utf-8').fillna(1)

def guardar_csv_oxid_SX():
    oxid_SX.to_filename=QFileDialog.getSaveFileName(filter="csv(*.csv)")[0]
    
    if oxid_SX.to_filename:
        oxid_SX.df.to_csv(oxid_SX.to_filename) 
        
#funciones EW (oxidados)  
def selectmodelo_oxid_EW(value2):
    oxid_EW.text_objetivo=['',
                        'Función Batch de Kynch, para la muestra de relave requerida',
                        'Función de estrés efectivo de sólido, para la muestra de relave requerida',
                        'Función de Dosificación, para la muestra de relave requerida',
                        'Función batch de Kynch, estrés efectivo de sólido y dosificación, \npara la muestra de relave requerida']
    oxid_EW.text_requerimientos=['',
                              '1. Mineralogía de la muestra \n2. Gravedad específica',
                              '1. Mineralogía de la muestra \n2. Gravedad específica',
                              '1. Mineralogía de la muestra \n2. Gravedad específica',
                              '1. Mineralogía de la muestra \n2. Gravedad específica']
    oxid_EW.text_resultados=['',
                          '1. Gráfico de Función batch de Kynch vs concentración de relave',
                          '1. Gráfico de Función de estrés efectivo de sólido vs concentración de relave',
                          '1. Gráfico de Dosificación vs concentración de relave',
                          '1. Gráfico de función batch de Kynch vs concentración de relave \n2. Gráfico de función de estrés efectivo de sólido \n3. Gráfico de función de dosificación']
    oxid_EW.text_title=['',
                     'Función batch de Kynch',
                     'Función de estrés efectivo de sólido',
                     'Función de dosificación',
                     'Funciones constitutivas']
    for i in range(len(oxid_EW.modelos)):
        if value2 == oxid_EW.modelos[i]:
            oxid_EW.info_title.setText(oxid_EW.text_title[i])
            oxid_EW.info_objetivo.setText(oxid_EW.text_objetivo[i])
            oxid_EW.info_requerimientos.setText(oxid_EW.text_requerimientos[i])
            oxid_EW.info_resultados.setText(oxid_EW.text_resultados[i])

def resetear_oxid_EW():
    oxid_EW.browser_datos.clear() 
    oxid_EW.comboBox_listagraficos.clear()
    oxid_EW.comboBox_listamodelos.clear()
    oxid_EW.comboBox_listamodelos.addItems(oxid_EW.modelos)
    oxid_EW.info_objetivo.clear()
    oxid_EW.info_requerimientos.clear()
    oxid_EW.info_resultados.clear()
    try:
        oxid_EW.verticalLayout.removeWidget(oxid_EW.canv)
        sip.delete(oxid_EW.canv)
        oxid_EW.canv=None
        oxid_EW.verticalLayout.removeItem(oxid_EW.spacerItem1)
    except Exception as e:
        print(e)
        pass     

def graficos_oxid_EW(value1):  
    #print(value1)
    plt.style.use('classic')          
    if value1 == "Función batch de Kynch":
        try:
            oxid_EW.horizontalLayout.removeWidget(oxid_EW.toolbar)
            oxid_EW.verticalLayout.removeWidget(oxid_EW.canv)
            sip.delete(oxid_EW.toolbar)
            sip.delete(oxid_EW.canv)
            oxid_EW.toolbar=None
            oxid_EW.canv=None
            oxid_EW.verticalLayout.removeItem(oxid_EW.spacerItem1)
        except Exception as e:
            print(e)
            pass
        oxid_EW.canv=MatplotlibCanvas(oxid_EW)
        oxid_EW.toolbar=Navi(oxid_EW.canv,oxid_EW.centralwidget)
        oxid_EW.horizontalLayout.addWidget(oxid_EW.toolbar)
        oxid_EW.verticalLayout.addWidget(oxid_EW.canv)
        oxid_EW.canv.axes.cla()
        ax=oxid_EW.canv.axes
        oxid_EW.df.plot(x=0,y=1,ax=oxid_EW.canv.axes)
        legend=ax.legend()
        legend.set_draggable(True)
        ax.set_xlabel('Concentración [-]')
        ax.set_ylabel('Función batch de Kynch')
        ax.set_title('Función batch de Kynch (f_bk) vs Concentración')
        ax.set_xlim(0, 1)
        ax.grid(color='grey', linestyle='--', linewidth=.5)
        ax.set_adjustable("box") 
        oxid_EW.canv.draw()
    if value1 == "Función estrés efectivo de sólido":
        try:
            oxid_EW.horizontalLayout.removeWidget(oxid_EW.toolbar)
            oxid_EW.verticalLayout.removeWidget(oxid_EW.canv)
            sip.delete(oxid_EW.toolbar)
            sip.delete(oxid_EW.canv)
            oxid_EW.toolbar=None
            oxid_EW.canv=None
            oxid_EW.verticalLayout.removeItem(oxid_EW.spacerItem1)
        except Exception as e:
            print(e)
            pass
        oxid_EW.canv=MatplotlibCanvas(oxid_EW)
        oxid_EW.toolbar=Navi(oxid_EW.canv,oxid_EW.centralwidget)
        oxid_EW.horizontalLayout.addWidget(oxid_EW.toolbar)
        oxid_EW.verticalLayout.addWidget(oxid_EW.canv)
        oxid_EW.canv.axes.cla()
        ax=oxid_EW.canv.axes
        oxid_EW.df.plot(x=0,y=2,ax=oxid_EW.canv.axes)
        legend=ax.legend()
        legend.set_draggable(True)
        ax.set_xlabel('Concentración [-]')
        ax.set_ylabel('Función estrés efectivo de sólido')
        ax.set_title('Función estrés efectivo de sólido vs Concentración')
        ax.set_xlim(0, 1)
        ax.grid(color='grey', linestyle='--', linewidth=.5)
        ax.set_adjustable("box") 
        oxid_EW.canv.draw()
    if value1 == "Función de dosificación":
        try:
            oxid_EW.horizontalLayout.removeWidget(oxid_EW.toolbar)
            oxid_EW.verticalLayout.removeWidget(oxid_EW.canv)
            
            sip.delete(oxid_EW.toolbar)
            sip.delete(oxid_EW.canv)
            oxid_EW.toolbar=None
            oxid_EW.canv=None
            oxid_EW.verticalLayout.removeItem(oxid_EW.spacerItem1)
        except Exception as e:
            print(e)
            pass
        oxid_EW.canv=MatplotlibCanvas(oxid_EW)
        oxid_EW.toolbar=Navi(oxid_EW.canv,oxid_EW.centralwidget)
        oxid_EW.horizontalLayout.addWidget(oxid_EW.toolbar)
        oxid_EW.verticalLayout.addWidget(oxid_EW.canv)
        oxid_EW.canv.axes.cla()
        ax=oxid_EW.canv.axes
        oxid_EW.df.plot(x=0,y=3,ax=oxid_EW.canv.axes)
        legend=ax.legend()
        legend.set_draggable(True)
        ax.set_xlabel('Concentración [-]')
        ax.set_ylabel('Función de dosificación')
        ax.set_title('Función de dosificación vs Concentración')
        ax.set_xlim(0, 1)
        ax.grid(color='grey', linestyle='--', linewidth=.5)
        ax.set_adjustable("box") 
        oxid_EW.canv.draw()
        
def simular_oxid_EW():
    graficos=['Función batch de Kynch','Función estrés efectivo de sólido','Función de dosificación']
    oxid_EW.comboBox_listagraficos.addItems(graficos) 

def getFile_oxid_EW():
    """this function will get the address of the csv file location also calls a readData function"""
    oxid_EW.filename=QFileDialog.getOpenFileName(filter="csv(*.csv)")[0]
    oxid_EW.archivo=oxid_EW.filename.split('/')
    #print("File:",self.archivo[-1])
    oxid_EW.browser_datos.append(oxid_EW.archivo[-1])
    readData_oxid_EW()
    
def readData_oxid_EW():
    """ This function will the data using pandas and call the update function to plot"""
    oxid_EW.df=pd.read_csv(oxid_EW.filename,encoding='utf-8').fillna(1)

def guardar_csv_oxid_EW():
    oxid_EW.to_filename=QFileDialog.getSaveFileName(filter="csv(*.csv)")[0]
    
    if oxid_EW.to_filename:
        oxid_EW.df.to_csv(oxid_EW.to_filename) 

# botones de navegacion login

login.registrarseButton.clicked.connect(gui_registrar)
login.salirButton.clicked.connect(salir)
login.ingresarButton.clicked.connect(gui_login)

register.button_volver.clicked.connect(regresar_forma)
register.button_OK.clicked.connect(datos)

error.volverButton.clicked.connect(gui_volver_error) 

procesos.OxidButton.clicked.connect(gui_oxid)
procesos.SulfButton.clicked.connect(gui_sulf)

sulf.button_perfo.clicked.connect(gui_sulf2perfo)
sulf.button_carguio.clicked.connect(gui_sulf2carguio)
sulf.button_chancado.clicked.connect(gui_sulf2chancado)
sulf.button_flotacion.clicked.connect(gui_sulf2flotacion)
sulf.button_espconc.clicked.connect(gui_sulf2espconc)
sulf.button_esprelave.clicked.connect(gui_sulf2esprelave)
sulf.Button_other.clicked.connect(gui_sulf2oxid)

oxid.button_perfo.clicked.connect(gui_oxid2perfo)
oxid.button_carguio.clicked.connect(gui_oxid2carguio)
oxid.button_chancado.clicked.connect(gui_oxid2chancado)
oxid.button_lixiviacion.clicked.connect(gui_oxid2lixiviacion)
oxid.button_SX.clicked.connect(gui_oxid2SX)
oxid.button_EW.clicked.connect(gui_oxid2EW)
oxid.Button_other.clicked.connect(gui_oxid2sulf)
oxid.button_eda_oxid.clicked.connect(oxid_EDA_oxid)

#botones EDA_oxid
EDA_oxid.button_cargar.clicked.connect(getFile_EDA_oxid)
EDA_oxid.button_principal.clicked.connect(EDA_oxid_oxid)
EDA_oxid.button_base.clicked.connect(EDA_oxid_base)
EDA_oxid.button_scatter.clicked.connect(EDA_oxid_scatter)

#MODIFICADO
EDA_oxid.button_kde.clicked.connect(EDA_oxid_kernel)
EDA_oxid.button_plotcorr.clicked.connect(EDA_oxid_plotcorr)

#botones EDA_oxid_base
EDA_base_oxid.button_main.clicked.connect(base_EDA_oxid)

#botones EDA_oxid_scatter
EDA_scatter_oxid.button_main.clicked.connect(scatter_EDA_oxid)

#botones EDA_oxid_kernel(NUEVO)
EDA_kernel_oxid.button_main.clicked.connect(kernel_EDA_oxid)

#botones EDA_oxid_plotcorr
EDA_plotcorr_oxid.button_main.clicked.connect(plotcorr_EDA_oxid)

#botones perforacion (sulf)
sulf_perfo.button_volver.clicked.connect(gui_perfo2sulf)
sulf_perfo.button_next.clicked.connect(gui_sulf_perfo2carguio)
sulf_perfo.modelos=['Ingrese Modelo',
                  'Predicción Función Batch de Kynch',
                  'Predicción Función de estrés efectivo de sólido',
                  'Predicción Función de Dosificación',
                  'Predicción de Funciones Constitutivas de Sedimentación']
sulf_perfo.comboBox_listamodelos.addItems(sulf_perfo.modelos)
sulf_perfo.filename=''
sulf_perfo.canv=MatplotlibCanvas(sulf_perfo)
sulf_perfo.df=[]
sulf_perfo.toolbar=Navi(sulf_perfo.canv,sulf_perfo.centralwidget)
sulf_perfo.horizontalLayout.addWidget(sulf_perfo.toolbar)
sulf_perfo.button_simular.clicked.connect(simular_sulf_perfo)
sulf_perfo.comboBox_listamodelos.currentIndexChanged['QString'].connect(selectmodelo_sulf_perfo)
sulf_perfo.comboBox_listagraficos.currentIndexChanged['QString'].connect(graficos_sulf_perfo)
sulf_perfo.button_datos_new_2.clicked.connect(getFile_sulf_perfo)
sulf_perfo.button_reset.clicked.connect(resetear_sulf_perfo)
sulf_perfo.button_guardar.clicked.connect(guardar_csv_sulf_perfo)

#botones carguio (sulf)
sulf_carguio.button_volver.clicked.connect(gui_carguio2sulf)
sulf_carguio.button_previous.clicked.connect(gui_sulf_carguio2perfo)
sulf_carguio.button_next.clicked.connect(gui_sulf_carguio2chancado)
sulf_carguio.modelos=['Ingrese Modelo',
                  'Predicción Función Batch de Kynch',
                  'Predicción Función de estrés efectivo de sólido',
                  'Predicción Función de Dosificación',
                  'Predicción de Funciones Constitutivas de Sedimentación']
sulf_carguio.comboBox_listamodelos.addItems(sulf_carguio.modelos)
sulf_carguio.filename=''
sulf_carguio.canv=MatplotlibCanvas(sulf_carguio)
sulf_carguio.df=[]
sulf_carguio.toolbar=Navi(sulf_carguio.canv,sulf_carguio.centralwidget)
sulf_carguio.horizontalLayout.addWidget(sulf_carguio.toolbar)
sulf_carguio.button_simular.clicked.connect(simular_sulf_carguio)
sulf_carguio.comboBox_listamodelos.currentIndexChanged['QString'].connect(selectmodelo_sulf_carguio)
sulf_carguio.comboBox_listagraficos.currentIndexChanged['QString'].connect(graficos_sulf_carguio)
sulf_carguio.button_datos_new_2.clicked.connect(getFile_sulf_carguio)
sulf_carguio.button_reset.clicked.connect(resetear_sulf_carguio)
sulf_carguio.button_guardar.clicked.connect(guardar_csv_sulf_carguio)

#botones chancado (sulf)
sulf_chancado.button_volver.clicked.connect(gui_chancado2sulf)
sulf_chancado.button_previous.clicked.connect(gui_sulf_chancado2carguio)
sulf_chancado.button_next.clicked.connect(gui_sulf_chancado2flotacion)
sulf_chancado.modelos=['Ingrese Modelo',
                  'Predicción Función Batch de Kynch',
                  'Predicción Función de estrés efectivo de sólido',
                  'Predicción Función de Dosificación',
                  'Predicción de Funciones Constitutivas de Sedimentación']
sulf_chancado.comboBox_listamodelos.addItems(sulf_chancado.modelos)
sulf_chancado.filename=''
sulf_chancado.canv=MatplotlibCanvas(sulf_chancado)
sulf_chancado.df=[]
sulf_chancado.toolbar=Navi(sulf_chancado.canv,sulf_chancado.centralwidget)
sulf_chancado.horizontalLayout.addWidget(sulf_chancado.toolbar)
sulf_chancado.button_simular.clicked.connect(simular_sulf_chancado)
sulf_chancado.comboBox_listamodelos.currentIndexChanged['QString'].connect(selectmodelo_sulf_chancado)
sulf_chancado.comboBox_listagraficos.currentIndexChanged['QString'].connect(graficos_sulf_chancado)
sulf_chancado.button_datos_new_2.clicked.connect(getFile_sulf_chancado)
sulf_chancado.button_reset.clicked.connect(resetear_sulf_chancado)
sulf_chancado.button_guardar.clicked.connect(guardar_csv_sulf_chancado)

#botones flotacion (sulf)
sulf_flotacion.button_volver.clicked.connect(gui_flotacion2sulf)
sulf_flotacion.button_previous.clicked.connect(gui_sulf_flotacion2chancado)
sulf_flotacion.button_next1.clicked.connect(gui_sulf_flotacion2espconc)
sulf_flotacion.button_next2.clicked.connect(gui_sulf_flotacion2esprelave)
sulf_flotacion.modelos=['Ingrese Modelo',
                  'Predicción Función Batch de Kynch',
                  'Predicción Función de estrés efectivo de sólido',
                  'Predicción Función de Dosificación',
                  'Predicción de Funciones Constitutivas de Sedimentación']
sulf_flotacion.comboBox_listamodelos.addItems(sulf_flotacion.modelos)
sulf_flotacion.filename=''
sulf_flotacion.canv=MatplotlibCanvas(sulf_flotacion)
sulf_flotacion.df=[]
sulf_flotacion.toolbar=Navi(sulf_flotacion.canv,sulf_flotacion.centralwidget)
sulf_flotacion.horizontalLayout.addWidget(sulf_flotacion.toolbar)
sulf_flotacion.button_simular.clicked.connect(simular_sulf_flotacion)
sulf_flotacion.comboBox_listamodelos.currentIndexChanged['QString'].connect(selectmodelo_sulf_flotacion)
sulf_flotacion.comboBox_listagraficos.currentIndexChanged['QString'].connect(graficos_sulf_flotacion)
sulf_flotacion.button_datos_new_2.clicked.connect(getFile_sulf_flotacion)
sulf_flotacion.button_reset.clicked.connect(resetear_sulf_flotacion)
sulf_flotacion.button_guardar.clicked.connect(guardar_csv_sulf_flotacion)

#botones espconc (sulf)
sulf_espconc.button_volver.clicked.connect(gui_espconc2sulf)
sulf_espconc.button_previous.clicked.connect(gui_sulf_espconc2flotacion)
sulf_espconc.modelos=['Ingrese Modelo',
                  'Predicción Función Batch de Kynch',
                  'Predicción Función de estrés efectivo de sólido',
                  'Predicción Función de Dosificación',
                  'Predicción de Funciones Constitutivas de Sedimentación']
sulf_espconc.comboBox_listamodelos.addItems(sulf_espconc.modelos)
sulf_espconc.filename=''
sulf_espconc.canv=MatplotlibCanvas(sulf_espconc)
sulf_espconc.df=[]
sulf_espconc.toolbar=Navi(sulf_espconc.canv,sulf_espconc.centralwidget)
sulf_espconc.horizontalLayout.addWidget(sulf_espconc.toolbar)
sulf_espconc.button_simular.clicked.connect(simular_sulf_espconc)
sulf_espconc.comboBox_listamodelos.currentIndexChanged['QString'].connect(selectmodelo_sulf_espconc)
sulf_espconc.comboBox_listagraficos.currentIndexChanged['QString'].connect(graficos_sulf_espconc)
sulf_espconc.button_datos_new_2.clicked.connect(getFile_sulf_espconc)
sulf_espconc.button_reset.clicked.connect(resetear_sulf_espconc)
sulf_espconc.button_guardar.clicked.connect(guardar_csv_sulf_espconc)

#botones esprelave (sulf)
sulf_esprelave.button_volver.clicked.connect(gui_esprelave2sulf)
sulf_esprelave.button_previous.clicked.connect(gui_sulf_esprelave2flotacion)
sulf_esprelave.modelos=['Ingrese Modelo',
                  'Predicción Función Batch de Kynch',
                  'Predicción Función de estrés efectivo de sólido',
                  'Predicción Función de Dosificación',
                  'Predicción de Funciones Constitutivas de Sedimentación']
sulf_esprelave.comboBox_listamodelos.addItems(sulf_esprelave.modelos)
sulf_esprelave.filename=''
sulf_esprelave.canv=MatplotlibCanvas(sulf_esprelave)
sulf_esprelave.df=[]
sulf_esprelave.toolbar=Navi(sulf_esprelave.canv,sulf_esprelave.centralwidget)
sulf_esprelave.horizontalLayout.addWidget(sulf_esprelave.toolbar)
sulf_esprelave.button_simular.clicked.connect(simular_sulf_esprelave)
sulf_esprelave.comboBox_listamodelos.currentIndexChanged['QString'].connect(selectmodelo_sulf_esprelave)
sulf_esprelave.comboBox_listagraficos.currentIndexChanged['QString'].connect(graficos_sulf_esprelave)
sulf_esprelave.button_datos_new_2.clicked.connect(getFile_sulf_esprelave)
sulf_esprelave.button_reset.clicked.connect(resetear_sulf_esprelave)
sulf_esprelave.button_guardar.clicked.connect(guardar_csv_sulf_esprelave)

#botones perforacion (oxid)
oxid_perfo.button_volver.clicked.connect(gui_perfo2oxid)
oxid_perfo.button_next.clicked.connect(gui_oxid_perfo2carguio)
oxid_perfo.modelos=['Ingrese Modelo',
                  'Predicción Función Batch de Kynch',
                  'Predicción Función de estrés efectivo de sólido',
                  'Predicción Función de Dosificación',
                  'Predicción de Funciones Constitutivas de Sedimentación']
oxid_perfo.comboBox_listamodelos.addItems(oxid_perfo.modelos)
oxid_perfo.filename=''
oxid_perfo.canv=MatplotlibCanvas(oxid_perfo)
oxid_perfo.df=[]
oxid_perfo.toolbar=Navi(oxid_perfo.canv,oxid_perfo.centralwidget)
oxid_perfo.horizontalLayout.addWidget(oxid_perfo.toolbar)
oxid_perfo.button_simular.clicked.connect(simular_oxid_perfo)
oxid_perfo.comboBox_listamodelos.currentIndexChanged['QString'].connect(selectmodelo_oxid_perfo)
oxid_perfo.comboBox_listagraficos.currentIndexChanged['QString'].connect(graficos_oxid_perfo)
oxid_perfo.button_datos_new_2.clicked.connect(getFile_oxid_perfo)
oxid_perfo.button_reset.clicked.connect(resetear_oxid_perfo)
oxid_perfo.button_guardar.clicked.connect(guardar_csv_oxid_perfo)

#botones carguio (oxidados)
oxid_carguio.button_volver.clicked.connect(gui_carguio2oxid)
oxid_carguio.button_previous.clicked.connect(gui_oxid_carguio2perfo)
oxid_carguio.button_next.clicked.connect(gui_oxid_carguio2chancado)
oxid_carguio.modelos=['Ingrese Modelo',
                  'Predicción Función Batch de Kynch',
                  'Predicción Función de estrés efectivo de sólido',
                  'Predicción Función de Dosificación',
                  'Predicción de Funciones Constitutivas de Sedimentación']
oxid_carguio.comboBox_listamodelos.addItems(oxid_carguio.modelos)
oxid_carguio.filename=''
oxid_carguio.canv=MatplotlibCanvas(oxid_carguio)
oxid_carguio.df=[]
oxid_carguio.toolbar=Navi(oxid_carguio.canv,oxid_carguio.centralwidget)
oxid_carguio.horizontalLayout.addWidget(oxid_carguio.toolbar)
oxid_carguio.button_simular.clicked.connect(simular_oxid_carguio)
oxid_carguio.comboBox_listamodelos.currentIndexChanged['QString'].connect(selectmodelo_oxid_carguio)
oxid_carguio.comboBox_listagraficos.currentIndexChanged['QString'].connect(graficos_oxid_carguio)
oxid_carguio.button_datos_new_2.clicked.connect(getFile_oxid_carguio)
oxid_carguio.button_reset.clicked.connect(resetear_oxid_carguio)
oxid_carguio.button_guardar.clicked.connect(guardar_csv_oxid_carguio)

#botones chancado (oxidados)
oxid_chancado.button_volver.clicked.connect(gui_chancado2oxid)
oxid_chancado.button_previous.clicked.connect(gui_oxid_chancado2carguio)
oxid_chancado.button_next.clicked.connect(gui_oxid_chancado2lixiviacion)
oxid_chancado.modelos=['Ingrese Modelo',
                  'Predicción Función Batch de Kynch',
                  'Predicción Función de estrés efectivo de sólido',
                  'Predicción Función de Dosificación',
                  'Predicción de Funciones Constitutivas de Sedimentación']
oxid_chancado.comboBox_listamodelos.addItems(oxid_chancado.modelos)
oxid_chancado.filename=''
oxid_chancado.canv=MatplotlibCanvas(oxid_chancado)
oxid_chancado.df=[]
oxid_chancado.toolbar=Navi(oxid_chancado.canv,oxid_chancado.centralwidget)
oxid_chancado.horizontalLayout.addWidget(oxid_chancado.toolbar)
oxid_chancado.button_simular.clicked.connect(simular_oxid_chancado)
oxid_chancado.comboBox_listamodelos.currentIndexChanged['QString'].connect(selectmodelo_oxid_chancado)
oxid_chancado.comboBox_listagraficos.currentIndexChanged['QString'].connect(graficos_oxid_chancado)
oxid_chancado.button_datos_new_2.clicked.connect(getFile_oxid_chancado)
oxid_chancado.button_reset.clicked.connect(resetear_oxid_chancado)
oxid_chancado.button_guardar.clicked.connect(guardar_csv_oxid_chancado)

#botones lixiviacion (oxid)
oxid_lixiviacion.button_volver.clicked.connect(gui_lixiviacion2oxid)
oxid_lixiviacion.button_previous.clicked.connect(gui_oxid_lixiviacion2chancado)
oxid_lixiviacion.button_next.clicked.connect(gui_oxid_lixiviacion2SX)
oxid_lixiviacion.modelos=['Ingrese Modelo',
                  'Predicción Función Batch de Kynch',
                  'Predicción Función de estrés efectivo de sólido',
                  'Predicción Función de Dosificación',
                  'Predicción de Funciones Constitutivas de Sedimentación']
oxid_lixiviacion.comboBox_listamodelos.addItems(oxid_lixiviacion.modelos)
oxid_lixiviacion.filename=''
oxid_lixiviacion.canv=MatplotlibCanvas(oxid_lixiviacion)
oxid_lixiviacion.df=[]
oxid_lixiviacion.toolbar=Navi(oxid_lixiviacion.canv,oxid_lixiviacion.centralwidget)
oxid_lixiviacion.horizontalLayout.addWidget(oxid_lixiviacion.toolbar)
oxid_lixiviacion.button_simular.clicked.connect(simular_oxid_lixiviacion)
oxid_lixiviacion.comboBox_listamodelos.currentIndexChanged['QString'].connect(selectmodelo_oxid_lixiviacion)
oxid_lixiviacion.comboBox_listagraficos.currentIndexChanged['QString'].connect(graficos_oxid_lixiviacion)
oxid_lixiviacion.button_datos_new_2.clicked.connect(getFile_oxid_lixiviacion)
oxid_lixiviacion.button_reset.clicked.connect(resetear_oxid_lixiviacion)
oxid_lixiviacion.button_guardar.clicked.connect(guardar_csv_oxid_lixiviacion)

#botones SX (oxidados)
oxid_SX.button_volver.clicked.connect(gui_SX2oxid)
oxid_SX.button_previous.clicked.connect(gui_oxid_SX2lixiviacion)
oxid_SX.button_next.clicked.connect(gui_oxid_SX2EW)
oxid_SX.modelos=['Ingrese Modelo',
                  'Predicción Función Batch de Kynch',
                  'Predicción Función de estrés efectivo de sólido',
                  'Predicción Función de Dosificación',
                  'Predicción de Funciones Constitutivas de Sedimentación']
oxid_SX.comboBox_listamodelos.addItems(oxid_SX.modelos)
oxid_SX.filename=''
oxid_SX.canv=MatplotlibCanvas(oxid_SX)
oxid_SX.df=[]
oxid_SX.toolbar=Navi(oxid_SX.canv,oxid_SX.centralwidget)
oxid_SX.horizontalLayout.addWidget(oxid_SX.toolbar)
oxid_SX.button_simular.clicked.connect(simular_oxid_SX)
oxid_SX.comboBox_listamodelos.currentIndexChanged['QString'].connect(selectmodelo_oxid_SX)
oxid_SX.comboBox_listagraficos.currentIndexChanged['QString'].connect(graficos_oxid_SX)
oxid_SX.button_datos_new_2.clicked.connect(getFile_oxid_SX)
oxid_SX.button_reset.clicked.connect(resetear_oxid_SX)
oxid_SX.button_guardar.clicked.connect(guardar_csv_oxid_SX)

#botones EW (oxidados)
oxid_EW.button_volver.clicked.connect(gui_EW2oxid)
oxid_EW.button_previous.clicked.connect(gui_oxid_EW2SX)
oxid_EW.modelos=['Ingrese Modelo',
                  'Predicción Función Batch de Kynch',
                  'Predicción Función de estrés efectivo de sólido',
                  'Predicción Función de Dosificación',
                  'Predicción de Funciones Constitutivas de Sedimentación']
oxid_EW.comboBox_listamodelos.addItems(oxid_EW.modelos)
oxid_EW.filename=''
oxid_EW.canv=MatplotlibCanvas(oxid_EW)
oxid_EW.df=[]
oxid_EW.toolbar=Navi(oxid_EW.canv,oxid_EW.centralwidget)
oxid_EW.horizontalLayout.addWidget(oxid_EW.toolbar)
oxid_EW.button_simular.clicked.connect(simular_oxid_EW)
oxid_EW.comboBox_listamodelos.currentIndexChanged['QString'].connect(selectmodelo_oxid_EW)
oxid_EW.comboBox_listagraficos.currentIndexChanged['QString'].connect(graficos_oxid_EW)
oxid_EW.button_datos_new_2.clicked.connect(getFile_oxid_EW)
oxid_EW.button_reset.clicked.connect(resetear_oxid_EW)
oxid_EW.button_guardar.clicked.connect(guardar_csv_oxid_EW)

# ejecutable
login.show()
app.exec()