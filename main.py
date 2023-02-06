from api import API

app = API()

@app.route(path="/home")
def home(request, response):
    response.text = "Page home"

@app.route(path="/about")
def about(request, response):
    response.text = "Page about"

@app.route(path="/hello/{name}")
def greeting(request, response, name: str):
    response.text = f"Hello, {name}"



