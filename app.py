from flask import (render_template, Flask, request)
import os
import numpy
from controllers import modbus_utils as modbus


images_Folder = os.path.join('static', 'images')
app = Flask(__name__)


@app.route('/')
def index():
    return render_template("layout.html")


@app.route("/api")
def posts():
    global values
    modbus.write_register(0, int(request.args.get(
        "roundSliderData")), 1) if request.args.get("roundSliderData") else None
    modbus.write_register(1, int(request.args.get(
        "writeRegister")), 1) if request.args.get("writeRegister") else None
    modbus.write_register(2, int(request.args.get("data").strip(
        '%')), 1) if request.args.get("data") else None
    modbus.write_register(3, int(request.args.get("power")),
                          1) if request.args.get("power") else None

    return '', 204


if __name__ == '__main__':
    app.run(debug=True)
