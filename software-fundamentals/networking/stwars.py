import requests

def get_stwars(resource: str):
    url = "https://swapi.dev/api/" + resource

    response = requests.get(url)

    if response.status_code == 200:
        return response.json()

if __name__ == "__main__":
    print(get_stwars("planets"))