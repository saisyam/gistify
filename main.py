from flask import Flask
from flask import render_template
from flask import Markup
from flask_cors import CORS
from gitparse import *

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return "<h1>Landing page coming soon...</h1>"

@app.route('/<path:url>')
def gistify(url):
    filename = url.split("/")[-1]
    rawurl = url.replace("blob", "raw")
    document = parsegit(url)
    return render_template('gistify.html', document=Markup(document), filename=filename, rawurl=rawurl, url=url)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)