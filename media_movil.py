import matplotlib.pyplot as plt
import pandas as pd
import datetime

p_aapl = pd.read_csv('appl.csv')


aapl_dict = p_aapl.to_dict()

def str_to_date(str_date):
   return datetime.datetime.strptime(str_date,"%d.%m.%Y")


def media_movil(mm,valores,fechas2):
    valores.reverse()
    fechas2.reverse()
    medias = []
    for i in range(len(valores)):
        if i < mm:
            continue
        m_i = sum([valores[i-y] for y in range(mm)])/mm
        dict_media_fecha = {"fecha":fechas[i],"valor":m_i}
        medias.append(dict_media_fecha)
    return medias



cierres = [float(i.replace(",",".")) for i in  aapl_dict["Último"].values()]
fechas = [str_to_date(i) for i in  aapl_dict["Fecha"].values()]

mm50_appl = media_movil(50,cierres,fechas)

mm200_appl = media_movil(200,cierres,fechas)
valores_mm = [i["valor"] for i in mm50_appl]
fechas_mm = [i["fecha"] for i in mm50_appl]

plt.plot(fechas,cierres)

plt.plot(fechas_mm,valores_mm)
plt.plot([i["fecha"] for i in mm200_appl],[i["valor"] for i in mm200_appl])
plt.show()