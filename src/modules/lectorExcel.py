class Lector:
    def __init__(self, archivoPrincipal, archivoAdicionales):
        self._wbPrincipal = load_workbook(filename=archivoPrincipal)
        self._wbAdicional = load_workbook(filename=archivoAdicionales)

    def __del__(self):
        self._wbPrincipal.close()
        self._wbAdicional.close()
