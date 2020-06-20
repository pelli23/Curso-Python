import pandas as pd
import matplotlib.pyplot as plt
import datetime
p_aapl = pd.read_csv('appl.csv')

p_sp500 = pd.read_csv('sp500.csv') 

aapl_dict = p_aapl.to_dict()

sp500_dict = p_sp500.to_dict()


def media(x):
    return sum(x)/len(x)

def varianza(x):
    media_x = media(x)
    return sum([(x_i - media_x)**2 for x_i in x]) / len(x)
        
def covariaza(x,y):
    media_x = media(x)
    media_y = media(y)
    return sum([((x[i]-media_x)*(y[i]-media_y)) for i in range(len(x))]) / len(x)

def beta(accion,mercado):
    return covariaza(accion,mercado) / varianza(mercado)


retornos_aapl = [float(i.replace(",",".").replace("%",""))  for i in aapl_dict["% var."].values()]

retornos_sp500 = [float(i.replace(",",".").replace("%",""))  for i in sp500_dict["% var."].values()]

print(beta(retornos_aapl,retornos_sp500))

import matplotlib.pyplot as plt
import datetime
def str_to_date(str_date):
    return datetime.datetime.strptime(str_date, '%d.%m.%Y')


def media_movil(mm,valores,fechas):
    valores.reverse()
    fechas.reverse()
    media = []
    for i in range(len(valores)):
        if i < mm:
            continue
        m_aux = sum([valores[i-y] for y in range(mm)])/mm
        media.append({"fecha":fechas[i],"valor":m_aux})
    return media

        

cierres = [float(i.replace(",","."))  for i in aapl_dict["Último"].values()]
fechas = [str_to_date(i) for i in aapl_dict["Fecha"].values()]
x = fechas
y = cierres


mm50_appl = media_movil(50,cierres,fechas)

valores_mm = [i["valor"] for i in mm50_appl]
fechas_mm = [i["fecha"] for i in mm50_appl]
plt.plot(x,y)
plt.plot(fechas_mm,valores_mm)
plt.show()


