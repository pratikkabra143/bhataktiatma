'''# app.py
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
        return 'Grim Reaper 💀'
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
'''
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Define the home route
@app.route('/')
def index():
    return render_template('index.html')

# Define the greeting page route
@app.route('/greet', methods=['POST', 'GET'])
def greet():
    if request.method == 'POST':
        user = request.form['name']
        return render_template('greet.html', name=user)
    else:
        return redirect(url_for('index'))

if __name__ == '__main__':
    app.run()