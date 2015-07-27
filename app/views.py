from app import app
from app import ptshownotes
from .forms import chatImport
from flask import render_template
from flask import Markup
from flask import request

def allowed_file(filename):
    return '.' in filename and \
        filename.rsplit('.', 1)[1] in app.config.ALLOWED_EXTENSIONS

@app.route('/', methods = ['GET', 'POST'])
@app.route('/index', methods = ['GET', 'POST'])
def index():
    form = chatImport()
    input_text = str()
    if request.method == 'POST': 
        if form.input_file:
            import os
            from werkzeug import secure_filename
            file = request.files['input_file']
            file = file.read()
            links = ptshownotes.Shownotes(file.decode('utf-8'))

        elif input_text:
            links = ptshownotes.Shownotes(form.input_text)
        md_text = links.md_text.split('\n')
        bad_links = links.bad_links
        er_cnt = len(bad_links)
        return render_template('index.html', form = form, md_text = md_text, bad_links = bad_links, er_cnt = er_cnt) 

    return render_template('index.html', form = form, er_cnt = 0)



