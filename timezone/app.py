from flask import Flask, request

app = Flask(__name__)


@app.route("/")
def index():
    return app.send_static_file("index.html")


@app.route("/set_timezone", methods=["POST"])
def set_timezone():
    data = request.get_json()
    user_timezone = data.get("timezone")

    # You can store the user's timezone in a session or database
    # For demonstration purposes, we'll just print it here
    print("User timezone:", user_timezone)

    return "Timezone set successfully"


if __name__ == "__main__":
    app.run()
