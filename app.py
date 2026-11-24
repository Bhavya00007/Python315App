
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <html>
        <head>
            <title>Python 3.15 Web App</title>
        </head>
        <body>
            <h1>Hello Chandigarh University!</h1>
            <h2>My Python Web Application is Running on Azure.</h2>
        </body>
    </html>
    """
