from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return " i am so into you into youuuuu intoo youuuu!!!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
