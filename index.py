from flask import Flask, request
app = Flask(__name__)
@app.route("/")
def hello():
    return "Hello World!"

@app.route("/what")
def what():
    msg = request.args.get("message")
    if msg:
        return f"{msg} right back to ya."
    else:
        return "There was no message."
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int("5000"), debug=True)
