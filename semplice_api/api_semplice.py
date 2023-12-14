import requests
# URL dell'API di esempio (JSONPlaceholder)
api_url = 'https://jsonplaceholder.typicode.com/todos/1'

# Effettua una richiesta GET all'API
response = requests.get(api_url)

# Verifica se la richiesta è andata a buon fine (status code 200)
if response.status_code == 200:
    # Stampa la risposta JSON
    print("Risposta JSON:")
    print(response.json())
else:
    print(f"Errore nella richiesta. Status code: {response.status_code}")