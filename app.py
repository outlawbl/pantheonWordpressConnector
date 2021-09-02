from flask import Flask, render_template, request, flash, redirect, url_for
from flask_bootstrap import Bootstrap
from werkzeug.utils import redirect
from main import main
app = Flask(__name__)
Bootstrap(app)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/sync')
def sinhronizacija():
    main()
    return render_template('home.html')


if __name__ == '__main__':
    app.run(port=8000, debug=True)