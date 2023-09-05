import re
from bot import start_bot
from flask import Flask, request

host_name = "0.0.0.0"
port = 5002

app = Flask(__name__)  # create an app instance

APP_VERSION = "1.0.2"


@app.route("/topic/alerts", methods=['POST'])
async def update():
    content = request.json
    title = "General"
    try:
        title = str(re.search("🔥.*🔥", content["message"]).group(0))
    except Exception:
        try:
            title = str(re.search("✅.*✅", content["message"]).group(0))
        except Exception:
            print(Exception)

    title = title.replace("🔥", "").replace(" ", "").replace("✅", "")
    await start_bot(title, content["message"])


def start_rest():
    app.run(host=host_name, port=port, debug=True, use_reloader=False)


if __name__ == "__main__":  # on running python app.py
    start_rest()
