from flask import Flask, request, jsonify, render_template
import bert

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    inp_string = [x for x in request.form.values()]
    sent = inp_string[0]
    index = bert.bert_checker(sent)
    print("here1")
    output = "correct" if index == 1 else "in-correct"
    return render_template('index.html', 
                           prediction_bert='"{}" is grammatically {}'.format(sent, output))


if __name__ == "__main__":
    app.run(debug=True)
