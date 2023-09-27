from flask import Flask, request

app = Flask(__name__)
app.secret_key = "your_secret_key"  # Change this to a secure secret key
app.config["SESSION_TYPE"] = "filesystem"


@app.route("/")
def home():
    user_agent = request.user_agent.string
    return f"Welcome to the homepage, user info: {user_agent}"


if __name__ == "__main__":
    app.run()
