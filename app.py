from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return """
    <h1 style='color:green;text-align:center;'>Bienvenue</h1>
    <p style='text-align:center;'>Application Docker par Lydie</p>
    """

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)