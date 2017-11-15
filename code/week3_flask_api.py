from flask import Flask, render_template, jsonify
app = Flask(__name__)

@app.route('/json_test')
def json_test():
    data = {“test”: 1, “key”: “value”, “temperature”:23, “units”: “metric”}
    return jsonify(**data)

app.run(host='0.0.0.0')


