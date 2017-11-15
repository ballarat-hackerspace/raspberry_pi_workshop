from flask import Flask
app = Flask(__name__)

@app.route('/')
def main_page():
    # When the main page is accessed, return some text.
    return 'Hack me!'

app.run(host='0.0.0.0', debug=True)
