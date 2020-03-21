from flask import Flask
from flask import render_template
from flask import Markup
from flask_cors import CORS
from gitparse import *

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return render_template('index.html')

# provide github URL to get complete code
# to give linenumbers add /l/<lineno> - 1,2 or 1,3-5,8 etc
@app.route('/<path:url>')
def gistify(url):
    try:
        urlitems = url.split("/")
        filename = None
        lineno = None
        giturl = None
        
        if urlitems[-2] == "l":
            lineno = urlitems[-1]
            filename = urlitems[-3]
            giturl = url[:url.index("/l/")]
        else:
            filename = urlitems[-1]
            lineno = None
            giturl = url
        rawurl = giturl.replace("blob", "raw")
        document = parsegit(giturl, lineno)
        return render_template('gistify.html', document=Markup(document), filename=filename, rawurl=rawurl, url=giturl)
    except:
        return render_template('error.html', url=url)

@app.route('/contribution/<username>')
def contribution(username):
    url = "https://github.com/"+username
    document = github_contribution(url)
    return render_template('contribution.html', document=Markup(document))

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)