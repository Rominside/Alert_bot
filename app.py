import re
import json
from main import main
from flask import Flask, request

host_name = "0.0.0.0"
port = 5002

app = Flask(__name__)  # create an app instance

APP_VERSION = "1.0.2"


@app.route("/topic/alerts", methods=['POST'])
async def update():
    with open('config.json') as file:
        templates = json.loads(file.read())
    content = request.json
    print(content)
    title = "General"
    try:
        title = str(re.search("🔥.*🔥", content["message"]).group(0))
    except TypeError:
        print(TypeError)

    if title == "General":
        title = str(re.search("✅.*✅", content["message"]).group(0))
    title = title.replace("🔥", "").replace("✅", "").replace(" ", "")

    await main(title, content["message"])
    return "200"


def start_rest():
    app.run(host=host_name, port=port, debug=True, use_reloader=False)


if __name__ == "__main__":  # on running python app.py
    start_rest()
