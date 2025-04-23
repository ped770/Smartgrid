import paho.mqtt.client as mqtt

# Configurações do broker
BROKER = "test.mosquitto.org"
PORT = 1883
TOPIC = "sala/ocupacao"

def get_person_status(count_person):
    """
    Retorna 'y' se count_person > 0, senão 'n'.
    """
    return 'y' if count_person > 0 else 'n'

def publish_person_status(count_person):
    """
    Conecta ao broker MQTT e envia uma única mensagem com base em count_person.
    """
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Conectado ao broker MQTT com sucesso!")
        else:
            print(f"Falha na conexão. Código de retorno: {rc}")

    client = mqtt.Client()
    client.on_connect = on_connect
    client.connect(BROKER, PORT, 60)
    client.loop_start()

    person = get_person_status(count_person)
    message = f"person = {person}"
    client.publish(TOPIC, message)
    print(f"Mensagem enviada: {message}")

    client.loop_stop()
    client.disconnect()
