import pandas as pd
import xlrd 
 
archivo = r'C:\Users\yandi\OneDrive\Escritorio\terraform\python\report.xls'

def read_cve(archivo):

    wb = xlrd.open_workbook(archivo) 

    hoja = wb.sheet_by_index(0) 
    row=hoja.nrows
    cols=hoja.ncols

    cve_map = {}

    for i in range(row):
        if cve_map.get(hoja.cell_value(i,0)) == None:
            cve_map[hoja.cell_value(i,0)] = []
        cve_map[hoja.cell_value(i,0)].append(hoja.cell_value(i,1))
    
    return cve_map



def read_report_cve(archivo_excel):
    
    # Lee una hoja específica del archivo Excel por su índice (por ejemplo, 0 para la primera hoja)
    #archivo_excel = r'C:\Users\yandi\OneDrive\Escritorio\terraform\python\report.xls'
    indice_hoja = 0  # Reemplaza 0 con el índice de la hoja que deseas leer
    datos = pd.read_excel(archivo_excel, sheet_name=indice_hoja)
    # Muestra los datos
    return datos


if __name__ == "__main__":
    read_cve(archivo)