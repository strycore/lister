"""Server for file store API"""
import os
import json
from flask import Flask, request, Response
from flask_cors import CORS

NOTES_DIR = os.environ.get("NOTES_DIR")
app = Flask(__name__)
CORS(app)


@app.route("/<folder>", methods=["GET"])
def list_folder(folder):
    """Lists the contents of a folder as return it as plain text"""
    folderpath = os.path.join(NOTES_DIR, folder)
    if os.path.exists(folderpath):
        content = "\n".join(os.listdir(folderpath))
    else:
        content = ""
    return Response(content, mimetype="application/text")


@app.route("/<folder>/<filename>", methods=["GET"])
def read_file(folder, filename):
    """Read the contents of a file and return it as plain text"""
    filepath = os.path.join(NOTES_DIR, folder, filename)
    if os.path.exists(filepath):
        with open(filepath, "r") as infile:
            content = infile.read()
    else:
        content = ""
    return Response(content, mimetype="application/text")


@app.route("/<folder>/<filename>", methods=["POST"])
def write_file(folder, filename):
    """Write raw POST data to a text file"""
    with open(os.path.join(NOTES_DIR, folder, filename), "wb") as outfile:
        outfile.write(request.data)
    return Response("", mimetype="application/text")
