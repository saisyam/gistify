from flask import Flask
from flask import render_template
from flask import Markup
from gitparse import *

app = Flask(__name__)

@app.route('/<path:url>')
def index(url):
    filename = url.split("/")[-1]
    rawurl = url.replace("blob", "raw")
    document = parsegit(url)
    return render_template('gistify.html', document=Markup(document), filename=filename, rawurl=rawurl, url=url)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
