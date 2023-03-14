import main
from flask import Flask, request, render_template


app = Flask(__name__)
inp = 0


@app.route('/')
def man():
    return render_template('index1.html')


@app.route('/', methods=['POST', 'GET'])
def home():
    if request.method == "POST":
        inp = request.form['size1']
        x = main.get_movie(str(inp))
    return render_template('index1.html', recommendation=x,movie_input=inp)


if __name__ == '__main__':
    app.run(debug=True)
