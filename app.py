from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/quote')
def quote():
    return render_template('quote.html')

if __name__ == "__main__":
    app.run(debug=True)