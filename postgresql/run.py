from flask import Flask, request, render_template, url_for, jsonify, redirect, flash
from flask_sqlalchemy import SQLAlchemy

# Init App
app = Flask(__name__)
app.config["SECRET_KEY"] = "thisissecret"
# our database uri
username = "vimisql"
password = "8992"
dbname = "vimidb"
app.config[
    "SQLALCHEMY_DATABASE_URI"
] = f"postgresql://{username}:{password}@localhost:5432/{dbname}"

db = SQLAlchemy(app)


# Create A Model For Table
class BlogPosts(db.Model):
    __tablename__ = "blogposts"
    id = db.Column(db.Integer, primary_key=True)
    blog_title = db.Column(db.String(1000))
    blog_description = db.Column(db.String(6000))


@app.route("/", methods=["GET"])
def index():
    posts = BlogPosts.query.all()
    return render_template("index.html", posts=posts)


@app.route("/posts", methods=["GET", "POST"])
def add_posts():
    if request.method == "POST":
        blog_title = request.form["blog_title"]
        blog_description = request.form["blog_description"]
        blog_post = BlogPosts(blog_title=blog_title, blog_description=blog_description)
        db.session.add(blog_post)
        db.session.commit()
        flash("Post Added")
    return redirect(url_for("index"))


if __name__ == "__main__":
    with app.app_context():
        db.create_all()  # <--- create db object.
    app.run(debug=True)
