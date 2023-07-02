from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    color = 'white'
    if request.method == 'POST':
        color = request.form['color']
    return render_template('background.html', color=color)

if __name__ == '__main__':
    app.run(debug=True)

