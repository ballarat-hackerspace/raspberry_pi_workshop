from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def main_page():
    # When the main page is accessed, return some text.
    # In your template, include {{ name }}
    return render_template(“template.html”, name=”Robert”)

app.run(host='0.0.0.0')
