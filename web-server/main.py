import store
from fastapi import FastAPI
from fastapi.response import HTMLResponse

app = FastAPI()

@app.route('/')
def get_list():
    return [1, 2, 3]

@app.route('/contact', response_class=HTMLResponse)
def get_list():
    return """
        <h1>Hola mundoooo</h1>
        <p>soy Daniel</p>
    """



def run():
    store.get_categories()

if __name__ == '__main__':
    run()