import requests as r
import matplotlib.pyplot as plt


def peticion_depth():
    maximo = []
    minimo = []
    close  = []
    trades = []
    open    = []

    ventana_9 = []
    ventana_25 = []
    ventana_55 = []


    x = []
    contador = 0

    a = r.get('https://api.binance.com/api/v3/klines?symbol=SOLUSDT&interval=12h&limit=1000')

    diccionario = a.json()
    print(diccionario)

    # data = diccionario['bids']

    # print(data)
    for i in diccionario:

        # lista_0.append(float(i[4]))
        minimo.append(float(i[3]))
        maximo.append(float(i[2]))
        close.append(float(i[4]))
        trades.append(float(i[9]))



    ###########################################################################################

    indicador_1 =[]
    for i in range(len(minimo)):

        var_min_10 = min(minimo[i:i+59])
        var_max_10 = max(maximo[i:i+59])
        indicador_1.append((var_max_10+var_min_10)/2)
        var_min_25 = min(minimo[i:i + 25])
        var_max_25 = max(maximo[i:i + 25])










    # plt.plot(lista_0)

    plt.plot(close)
    plt.plot(indicador_1)
    # plt.plot(minimo)
    # plt.plot(trades)
    plt.show()




# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    peticion_depth()
