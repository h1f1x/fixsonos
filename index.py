import json

import requests
from flask import Flask, render_template, url_for

from soco import SoCo, discover

app = Flask(__name__)

sonos = list(discover())[0]

@app.route("/play")
def play():
    sonos.play()
    return "Ok"


@app.route("/pause")
def pause():
    sonos.pause()
    return "Ok"


@app.route("/next")
def next():
    sonos.next()
    return "Ok"


@app.route("/previous")
def previous():
    sonos.previous()
    return "Ok"

@app.route("/info")
def info():
    track = sonos.get_current_track_info()
    return json.dumps(track)

@app.route("/stop")
def stopall():
    for zone_list in list(discover()):
        if zone_list.is_coordinator:
            # print(f'{zone_list.player_name}*')
            zone_list.stop()
    return "Stopped"

if __name__ == "__main__":
    app.run(debug=True)
