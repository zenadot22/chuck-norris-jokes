import requests
from flask import Flask,url_for,render_template

app = Flask(__name__)
@app.route('/')
def get_chuck_norris_jokes():

    api_url = "https://api.chucknorris.io/jokes/random"
    response = requests.get(api_url).json()
    image_tag = "<img src=" + response['icon_url']+" alt='Flowers in Chania'>"
    return "<strong>Random joke from chuck norris: </strong>" + response['value'] + image_tag


if __name__=='__main__':
    app.run(debug=True)


