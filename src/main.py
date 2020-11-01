from modules.lectorExcel import Lector

l = Lector('../testData/datosPrincipales.xlsx', '../testData/datosAdicionales.xlsx')
l.extraerProgramas()
