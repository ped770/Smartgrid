# main.py

from mqtt_sender import publish_person_status
import teste
import time

if __name__ == "__main__":
    try:
        last_value = None
        while True:
            current_value = teste.count_person

            if current_value != last_value:
                publish_person_status(current_value)
                last_value = current_value

            time.sleep(1)  # Evita loop muito acelerado
    except KeyboardInterrupt:
        print("Programa finalizado pelo usuário.")
