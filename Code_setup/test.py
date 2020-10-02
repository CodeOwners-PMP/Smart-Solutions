from flask import Flask, render_template
from datetime import datetime
import re

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, Flask!"

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