from flask import Flask, render_template, make_response, session
from flask_weasyprint import HTML, render_pdf
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'

class MyForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    age = IntegerField('Age', validators=[DataRequired()])
    submit = SubmitField("Calculate")

@app.route('/', methods=['GET', 'POST'])
def index():
    form = MyForm()

    if form.validate_on_submit():
        # Set form attributes in session
        session['name'] = form.name.data
        session['age'] = form.age.data

        return 'Form submitted successfully.'

    return render_template('index.html', form=form)

@app.route('/pdf')
def pdf():
    # Get form attributes from session
    name = session.get('name')
    age = session.get('age')

    # Render the sample.html template with the form attributes
    html = render_template('sample.html', name=name, age=age)

    # Create PDF from HTML using Flask-WeasyPrint
    pdf = render_pdf(HTML(string=html))

    # Create a response containing the PDF
    response = make_response(pdf)
    response.headers['Content-Type'] = 'application/pdf'
    response.headers['Content-Disposition'] = 'inline; filename=example.pdf'

    return response

if __name__ == '__main__':
    app.run()
