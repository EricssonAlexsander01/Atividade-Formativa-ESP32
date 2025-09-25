from wifi_lib import conecta
import urequests
import dht
from machine import Pin
import time

# Inicialização do sensor DHT11 e do relé
dht_sensor = dht.DHT11(Pin(4))
rele = Pin(2, Pin.OUT)

# Configuração do ThingSpeak
THINGSPEAK_WRITE_API_KEY = "4W61U618R8SVEMZL"
THINGSPEAK_URL = "https://api.thingspeak.com/update"

print("Conectando ao Wifi...")
station = conecta("Cabral", "Cabral1502onre") 

if not station.isconnected():
    print("Erro: não conectou ao WIFI.")
else:
    print("WIFI conectado!")

while True:
    try:
        # Medição de temperatura e umidade
        dht_sensor.measure()
        temp = dht_sensor.temperature()
        hum = dht_sensor.humidity()

        print("Temperatura: {}°C".format(temp))
        print("Umidade: {}%".format(hum))

        # Lógica do relé
        if temp > 31 or hum > 70:
            rele.value(1)
            estado_rele = 1
            print("Relé LIGADO")
        else:
            rele.value(0)
            estado_rele = 0
            print("Relé DESLIGADO")

        # Envio dos dados ao ThingSpeak
        url = (
            THINGSPEAK_URL +
            "?api_key=" + THINGSPEAK_WRITE_API_KEY +
            "&field1=" + str(temp) +
            "&field2=" + str(hum) +
            "&field3=" + str(estado_rele)
        )

        response = urequests.get(url)
        response.close()
        print("Dados enviados ao ThingSpeak!")

    except OSError as e:
        print("Erro na leitura do sensor:", e)

    time.sleep(15)


        