from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/results', methods=['POST'])
def results():
    text = request.form['input_text']
    return render_template('results.html', post=text)
    # return text

if __name__ == '__main__':
    app.run()