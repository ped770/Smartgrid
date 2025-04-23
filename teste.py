from inference_sdk import InferenceHTTPClient
import json

client = InferenceHTTPClient(
    api_url="https://detect.roboflow.com",
    api_key="15xYryWoHYdkSwZVMr50"
)

result = client.run_workflow(
    workspace_name="teste-da-smartgrid",
    workflow_id="teste-api",
    images={
        "image": "imagem_teste.jpg"
    },
    use_cache=True # cache workflow definition for 15 minutes
)

# Verificando se o resultado é uma lista
if isinstance(result, list):
    dados = result
else:
    dados = json.loads(result)

# Contando objetos com "class": "person"
count_person = 0
for item in dados:  # Iterando sobre a lista principal
    if isinstance(item, dict) and "predictions" in item:  # Verificando se há a chave "predictions"
        predictions = item["predictions"].get("predictions", [])  # Acessando a lista de "predictions"
        for prediction in predictions:  # Iterando sobre as previsões
            if prediction.get("class") == "person":  # Verificando se a "class" é "person"
                count_person += 1

if count_person == 0:
    print("Não há pessoas nesse frame")
else:
    print(f"Há {count_person} pessoas nesse frame")