from flask import Flask, render_template, request, url_for, redirect
from werkzeug.exceptions import BadRequest

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/contribute', methods=['GET', 'POST'])
def contribute():
    if request.method == 'POST':
        try:
            return render_template('thanks.html')
        except BadRequest:
            return redirect(url_for('contribute'))
    return render_template('contribute.html')

@app.route('/SystemAutomation')
def automate():
    return render_template('automate.html')

// Driver Code

if __name__ == "__main__":
    app.run()
