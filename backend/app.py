from flask import Flask, render_template, jsonify, request
from userResource import user
from locationResource import location
from flask_cors import CORS
import processor

app = Flask(__name__)
app.config['SECRET_KEY'] = 'enter-a-very-secretive-key-3479373'
app.register_blueprint(user, url_prefix="/user")
app.register_blueprint(location, url_prefix="/location")
CORS(app)


@app.get('/')
def hello_world():  # put application's code here
    return 'Hello World!'


@app.route('/', methods=["GET", "POST"])
def index():
    return render_template('index.html', **locals())



@app.route('/chatbot', methods=["GET", "POST"])
def chatbotResponse():

    if request.method == 'POST':
        the_question = request.form['question']

        response = processor.chatbot_response(the_question)

    return jsonify({"response": response })

if __name__ == '__main__':
    app.run(debug=True, port=5000)
