from flask import Flask, jsonify, request
from flask import render_template
from flask_cors import CORS


import processor
from userService import UserService

userService = UserService()
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


        arg = request.get_json()
        the_question = arg.get("question")
        q = userService.Decode(the_question)
        print(q)
        q.get("question")
        response = processor.chatbot_response(q.get("question"))

        return jsonify({"response": response })


if __name__ == '__main__':
    app.run(debug=True, port=5000)
