# followed:
# https://www.linkedin.com/learning/flask-essential-training/variable-rules-in-urls?u=2012979

from flask import Flask, render_template, request, redirect, url_for, flash, abort, session, jsonify
import json
import os.path
# from werkzeug.exceptions import abort
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.secret_key = "dfsdf7sdf7f8sddfs8sdf8"


@app.route("/")
def home():
    # return 'tell tale please!'
    # return render_template('home.html', var1='Karan') #passing var1 to html template
    return render_template('home.html', codes=session.keys())


@app.route('/your-url', methods=['GET', 'POST'])
def your_url():
    if request.method == 'POST':

        # write data to json file
        urls = dict()

        if os.path.exists('urls.json'):
            with open('urls.json') as urls_file:
                urls = json.load(urls_file)

        # check if code1 already exists in file
        if request.form['code1'] in urls.keys():
            # flash error message
            flash("The short name is already taken. Please give another name.")
            return redirect(url_for('home'))

        if 'url' in request.form.keys():
            # if form contains url:
            urls[request.form['code1']] = {'url': request.form['url']}
        else:
            # if form contains file:
            f = request.files['file']
            full_name = request.form['code1'] + secure_filename(f.filename)
            f.save("D:/kv/ineuron_classes/class work download/session7_Rest aip and sql and "
                   "nosql/21.Flask/LinkedinFlaskEssentialTraining/static/user_files/" + full_name)
            urls[request.form['code1']] = {'file': full_name}

        with open('urls.json', 'w') as url_file:
            session[request.form['code1']] = True
            json.dump(urls, url_file)

        # 'code1' in args is variable used in home tag to be passed to your_url.html
        # in following statement, we will changed request.args to request.form as
        # latter is required for POST request, whereas former for GET request
        # this will throw KeyError otherwise.
        # parameter code1 has to match display value in rendered page i.e. your_url.html in this case
        return render_template("your_url.html", code1=request.form['code1'])
    else:
        # redirects to home.html without your-url in address bar
        # url_for creates sort of a pointer to def home(), as route may change in future
        # return redirect('/') # redirect to route
        return redirect(url_for('home'))


@app.route('/<string:code>')  # code is variable that is to be matched in urls.json
def redirect_to_url(code):
    if os.path.exists("urls.json"):
        with open('urls.json') as urls_file:
            urls = json.load(urls_file)
            if code in urls.keys():
                if 'url' in urls[code].keys():
                    return redirect(urls[code]['url'])
                else:
                    return redirect(url_for('static', filename='user_files/' + urls[code]['file']))
    return abort(404)


@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404


# works with http://127.0.0.1:5000/api
@app.route('/api')
def create_api():
    return jsonify(list(session.keys()))
