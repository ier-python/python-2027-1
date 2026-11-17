import pandas as pd 
import glob as glob      

def import_esolmet(mes="01",cadena="../data/001_raw/ejercicio_02_fechas/ClimaLab_",anio="2026"):
    f = cadena + anio + "-"  + mes + "*"
    # print(f)
    archivos = glob.glob(f)
    # archivos
    try:
        esolmet = pd.concat([pd.read_csv(archivo,index_col=0,parse_dates=True) for archivo in archivos ],axis=0,sort=True)
        esolmet = esolmet.sort_index()
        # esolmet.info()
        return esolmet
    except:
        print(f"archivos es {archivos}")



def saluda():
    print("HOLA MUNDO")
