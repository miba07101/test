# please write me a flask app for printing to pdf using flask-weasyprint. Make simple page with 3 columns. column 1 is sidebar. column 2 is content. column 3 is also content with loremipsum text. In navbar make button for "print to pdf". But i want only print to pdf third column!

# The `index()` function renders the `index.html` template which contains the three columns. The `print_pdf()` function generates a PDF of the third column by first rendering the entire page with `print_pdf=True` and then using Flask-WeasyPrint's `render_pdf()` function to generate the PDF.
from flask import Flask, render_template, Response
from flask_weasyprint import HTML, render_pdf

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/print')
def print_pdf():
    html_string = render_template('print_version.html')
    return Response(render_pdf(HTML(string=html_string, base_url=request.host_url)),
                    mimetype='application/pdf')

if __name__ == '__main__':
    app.run(debug=True)
