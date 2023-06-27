from flask import Flask, render_template

site = Flask(__name__)

@site.route('/')
def index():
    return render_template('index.html')

site.run(debug=False)