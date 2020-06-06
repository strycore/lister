"""Server for file store API"""
import os
import json
from flask import Flask, request, Response
from flask_cors import CORS

NOTES_DIR = os.environ.get("NOTES_DIR")
app = Flask(__name__)
CORS(app)

@app.route("/<folder>/<filename>", methods=["GET"])
def read_file(folder, filename):
    filepath = os.path.join(NOTES_DIR, folder, filename)
    if os.path.exists(filepath):
        with open(filepath, "r") as infile:
            content = infile.read()
    else:
        content = ""
    return Response(content, mimetype="application/text")


@app.route("/<folder>/<filename>", methods=["POST"])
def write_file(folder, filename):
    with open(os.path.join(NOTES_DIR, folder, filename), "wb") as outfile:
        outfile.write(request.data)
    return Response("", mimetype="application/text")
