from flask import Flask
from flask import jsonify

# Make project root importable when running this module directly
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[1]))

from generators.api_data_generator import generate_gps_data

app = Flask(__name__)

@app.route("/gps")

def gps():

    return jsonify(

        generate_gps_data()

    )

if __name__ == "__main__":

    app.run(
        port=5001
    )