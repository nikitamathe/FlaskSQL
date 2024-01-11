from flask import Flask, request, render_template
from markupsafe import escape

app = Flask(__name__)

@app.route('/')
def home():
    name = request.args.get("name", "World")
    return render_template('index.html')

app.run(debug=True)

