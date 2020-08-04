# manipulando dados da web JASON - 04/08/2020 - jonatan paschoal
import urllib.request
import json

def ManipulaJSON():
    endereco = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/2.5_day.geojson"
    webURL = urllib.request.urlopen(endereco)
    if(webURL.getcode() == 200):
        dados = webURL.read()
        oJSON = json.loads(dados)

        contagem = oJSON["metadata"]["count"]
        print("Contage: " + str(contagem))

        for local in oJSON["features"]:
            if local["properties"]["place"] == "268 km NE of Saipan, Northern Mariana Islands":
                print('***Encontrado registro especial***')
            else:
                print(local["properties"]["place"])

ManipulaJSON() 