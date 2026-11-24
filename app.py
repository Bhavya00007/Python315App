
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <html>
        <head>
            <title>Python 3.15 Web App</title>
            <meta name="google-site-verification" content="dOvbjDkm9c_-E8A8kzLw1Oe_jZz-1o9gnOIHSk_4clM" />
        </head>
        <body>
            <h1>Hello Chandigarh University!</h1>
            <h2>My Python Web Application is Running on Azure.</h2>
        </body>
    </html>
    """

if __name__ == "__main__":
    app.run()
