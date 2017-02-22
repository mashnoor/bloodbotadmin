from flask import Flask
from flask import request
import json
app = Flask(__name__)

@app.route('/', methods=['POST'])
def index():
    req = request.get_json(silent=True, force=True)
    print(json.dumps(req, indent=4))

    return "Hello"

if __name__=="__main__":
    app.run()