import requests

def get_city_info():
    try:
        # Utilizza ipinfo.io per ottenere informazioni sulla posizione basate sull'IP
        response = requests.get('https://ipinfo.io/json')
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Errore nella richiesta. Status code: {response.status_code}")
            return None
    except Exception as e:
        print(f"Errore durante la richiesta: {e}")
        return None

def display_city_info(city_info):
    if city_info:
        print(f"Informazioni sulla città:")
        print(f"IP: {city_info['ip']}")
        print(f"Città: {city_info['city']}")
        print(f"Regione: {city_info['region']}")
        print(f"Paese: {city_info['country']}")
        print(f"Coordinate: {city_info['loc']}")
    else:
        print("Nessuna informazione sulla città disponibile.")

if __name__ == "__main__":
    city_info = get_city_info()
    display_city_info(city_info)