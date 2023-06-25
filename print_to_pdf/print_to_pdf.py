from flask import Flask, render_template, make_response, render_template_string
from flask_weasyprint import HTML, CSS

# app = Flask(__name__)
# app.config['WEASYPRINT_FONT_CONFIG'] = '/usr/share/fonts/truetype/msttcorefonts/Arial.ttf'
#
# @app.route('/')
# def index():
#     return render_template('index.html')
#
# @app.route('/pdf')
# def generate_pdf():
#     css = CSS(string='@page { size: letter; margin: 1in; }')
#     response = make_response(HTML(string=render_template_string('{% extends "index.html" %}{% block content %}'
#                                                                 '{% filter replace(" \\n", "") %}'
#                                                                 '.col-md-6:not(:nth-child(2)) { display: none; }'
#                                                                 '.col-md-6:nth-child(2) { width: 100%; }'
#                                                                 '{% endfilter %}{% endblock %}')).write_pdf(stylesheets=[css]))
#     response.headers['Content-Type'] = 'application/pdf'
#     response.headers['Content-Disposition'] = 'attachment; filename=column2.pdf'
#     return response
#
# if __name__ == '__main__':
#     app.run(debug=True)

from weasyprint import default_url_fetcher


app = Flask(__name__)
# app.config['WEASYPRINT_FONT_CONFIG'] = '/usr/share/fonts/truetype/msttcorefonts/Arial.ttf'
# app.config['WEASYPRINT_URL_FETCHER'] = default_url_fetcher


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/pdf')
def generate_pdf():
    # css = CSS(string='.col-md-6:not(:nth-child(2)) { display: none; } .col-md-6:nth-child(2) { width: 100%; }')
    css = CSS(string='.do-not-print { display: none; } .print-this-pdf { width: 100%; }')
    response = make_response(HTML(string=render_template('index.html')).write_pdf(stylesheets=[css], presentational_hints=True, attachments=None, styles=None, font_config=None))
    response.headers['Content-Type'] = 'application/pdf'
    # response.headers['Content-Disposition'] = 'attachment; filename=column2.pdf'
    response.headers['Content-Disposition'] = 'inline; filename=column2.pdf'
    return response


if __name__ == '__main__':
    app.run(debug=True)

