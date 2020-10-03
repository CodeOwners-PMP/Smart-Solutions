import time, os, requests, cv2, argparse, re
import numpy as np
import tensorflow as tf
from datetime import datetime

# Import utilites
from flask import Flask, flash, render_template, Response, request, redirect, url_for, abort, send_from_directory, send_file
from werkzeug.utils import secure_filename

app = Flask(__name__)

UPLOAD_DIRECTORY = "/project/api_uploaded_files"

def create_directory():
    if not os.path.exists(UPLOAD_DIRECTORY):
        os.makedirs(UPLOAD_DIRECTORY)

@app.route("/")
def home():
    # print("Hello, Flask!")
    return render_template('person.html')

@app.route("/upload/<file_name>")
def hello_there(file_name):
    now = datetime.now()
    formatted_now = now.strftime("%A, %d %B, %Y at %X")

    # Filter the name argument to letters only using regular expressions. URL arguments
    # can contain arbitrary text, so we restrict to safe characters only.
    match_object = re.match("[a-zA-Z.]+", file_name)

    if match_object:
        clean_name = match_object.group(0)
    else:
        clean_name = "Your Image file"

    content = "Hello there, {} is properly saved at {}".format(clean_name, formatted_now)
    return content

@app.route("/hello/")
@app.route("/hello/<name>")
def run_html_file(name = None):
    return render_template("hello_there.html", name=name, date=datetime.now())

@app.route("/downloadfile/<filename>", methods = ['GET'])
def download_file(filename):
    return render_template('person.html',value=filename)

@app.route("/files/<path:path>")
def get_file(path):
    """Download a file."""
    return send_from_directory(UPLOAD_DIRECTORY, path, as_attachment=True)

if __name__ == '__main__':
    app.run(host='172.26.101.101', port=8834,debug=True)
    app.run( port=8834,debug=True)