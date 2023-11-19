import requests

def get_categories():
    #de aqui se va a obtener toda la informacion, la r es ->response
    r = requests.get('https://api.escuelajs.co/api/v1/categories')
    print(r.status_code)
    print(r.text)
    print(type(r.text))
    #metodo para convertir string a json en python
    categories = r.json()
    for category in categories:
        print(category['name'])