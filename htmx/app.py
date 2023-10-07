from flask import Flask, render_template

app = Flask(__name__)


@app.route("/load-content")
def load_content():
    # This is the content that will replace the "outside-container" div
    new_content = "<p>New content loaded via htmx!</p>"
    return new_content


@app.route("/")
def index():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
