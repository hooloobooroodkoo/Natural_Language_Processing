from flask import Flask, request, render_template
from analyze import analyze

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/results', methods=['POST'])
def results():
    text = request.form['input_text']
    with open('text.txt', 'w') as file:
        file.write(text)
    print(analyze('text.txt'))
    return render_template('results.html', post=text)

if __name__ == '__main__':
    app.run()