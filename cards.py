import requests
import time
from flask import Flask

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    return cards()

@app.route("/cards", methods=["GET"])
def cards():
    response = requests.get("https://www.deckofcardsapi.com/api/deck/new/shuffle/?deck_count=1")
    cartas = response.json()
    deck_id = cartas ["deck_id"]

    image_list = []
    for i in range(0, 14):
        req = requests.get(f"https://www.deckofcardsapi.com/api/deck/{deck_id}/draw/?count=2")
        png = req.json()
        image = png["cards"][0]["image"]
        image_list.append(image)

    html_template = f"""
        <img src="{image_list[0]}">
        <img src="{image_list[1]}">
        <img src="{image_list[2]}">
        <img src="{image_list[3]}">
        <img src="{image_list[4]}">
        <img src="{image_list[5]}">
        <img src="{image_list[6]}">
        <img src="{image_list[7]}">
        <img src="{image_list[8]}">
    """

    return html_template 

@app.route("/latency/<int:ms>", methods=["GET"])
def latency(ms: int):
    print(f"aguardando: {ms}")
    time.sleep(ms)
    return dict(message=f"Essa página est[a aguardando {ms} segundos]")

app.run(host="0.0.0.0", port="8080")


    


    
