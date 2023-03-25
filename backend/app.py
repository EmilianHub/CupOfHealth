from flask import Flask, jsonify, request
from flask import render_template
from flask_cors import CORS
from flask_login import LoginManager

import processor
from locationResource import location
from userResource import user
import rsaEncryption

app = Flask(__name__)
rsaEncryption.saveToFile()
app.config['SECRET_KEY'] = 'enter-a-very-secretive-key-3479373'
app.register_blueprint(user, url_prefix="/user")
app.register_blueprint(location, url_prefix="/location")
CORS(app)


@app.route('/', methods=["GET", "POST"])
def index():
    return render_template('index.html', **locals())


@app.post('/chatbot')
def chatbotResponse():

    #if request.method == 'POST':
        arg = request.get_json()
        the_question = arg.get("question")
        #the_question = request.form['question']
        #
        response = processor.chatbot_response(the_question)

        return jsonify({"response": response })


if __name__ == '__main__':
    app.run(debug=True, port=5000)
