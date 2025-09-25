# 🌡️ Projeto ESP32 + DHT11 + Relé + ThingSpeak

Este projeto foi desenvolvido de forma **individual** como atividade acadêmica.  
O objetivo é integrar **IoT e computação em nuvem** utilizando o microcontrolador **ESP32**, o sensor de temperatura/umidade **DHT11** e um **relé** para acionamento automático.

---

## ⚙️ Funcionalidades
- 📡 Coleta de **temperatura** e **umidade** via sensor **DHT11**.  
- ☁️ Envio dos dados em tempo real para a plataforma **ThingSpeak**.  
- 🔌 Acionamento automático do **relé** caso:
  - Temperatura **> 31°C**  
  - Umidade relativa do ar **> 70%**  
- 🔴 Caso contrário, o relé é desligado.  

---

## 📊 Visualização em Tempo Real
Os dados enviados pelo ESP32 podem ser acompanhados em tempo real no ThingSpeak:  

👉 [Canal ThingSpeak - ESP32 DHT11](https://thingspeak.mathworks.com/channels/3088655)

---

## 📂 Estrutura do Projeto
- `esp32_dht11_rele.py` → Programa principal (coleta dados, envia ao ThingSpeak e controla o relé).  
- `wifi_lib.py` → Biblioteca auxiliar para conexão com o Wi-Fi.  

---

## 🚀 Como Executar
1. Configure as credenciais de **Wi-Fi** dentro do arquivo `wifi_lib.py`.  
2. Substitua a constante `THINGSPEAK_WRITE_API_KEY` pela sua chave de **escrita** do ThingSpeak.  
3. Carregue o código no ESP32 utilizando o **Thonny IDE**.  
4. Abra o canal do ThingSpeak para acompanhar os gráficos atualizados. 
