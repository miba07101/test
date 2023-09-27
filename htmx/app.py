from flask import Flask, render_template, jsonify, request
from flask_wtf import FlaskForm
from wtforms import SelectField

app = Flask(__name__)
app.config["SECRET_KEY"] = "your_secret_key"


# Create a simple form with two select fields
class MyForm(FlaskForm):
    fruit = SelectField(
        "Select a fruit", choices=[("apple", "Apple"), ("banana", "Banana")]
    )
    variety = SelectField("Select a variety", choices=[])


# Sample data for the dependent select field
fruit_varieties = {
    "apple": ["Fuji", "Gala", "Granny Smith"],
    "banana": ["Cavendish", "Red Banana", "Plantain"],
}


# Route to render the form
@app.route("/", methods=["GET", "POST"])
def index():
    form = MyForm()

    if form.validate_on_submit():
        selected_fruit = form.fruit.data
        selected_variety = form.variety.data
        return f"Selected Fruit: {selected_fruit}, Selected Variety: {selected_variety}"

    return render_template("index.html", form=form)


# Route to get the dependent options using Flask
@app.route("/get_varieties", methods=["GET"])
def get_varieties():
    selected_fruit = request.args.get("value")
    varieties = fruit_varieties.get(selected_fruit, [])
    options = "".join(
        [f'<option value="{variety}">{variety}</option>' for variety in varieties]
    )
    return jsonify(options=options)


if __name__ == "__main__":
    app.run(debug=True)
