from flask import Flask, render_template


# Create a Flask app
app = Flask(__name__)
                

# Create routes and connect them to relevant HTML files
@app.route('/')
def index():
    return render_template('./index.html')