from flask import Flask, request
from flask_cors import CORS

import processor
import rsaEncryption
import diseaseCache
from jwtService import decodeRequest, encodeResponse
from locationResource import location
from userResource import user

app = Flask(__name__)
rsaEncryption.saveToFile()
app.config['SECRET_KEY'] = 'enter-a-very-secretive-key-3479373'
app.register_blueprint(user, url_prefix="/user")
app.register_blueprint(location, url_prefix="/location")
CORS(app)


@app.post('/chatbot')
def chatbotResponse():
    arg = request.get_data()
    the_question = decodeRequest(arg).get("question")
    response = processor.chatbot_response(the_question)
    json = {"response": response,
            "suggestCure": diseaseCache.suggestCure
            }

    return encodeResponse(json)


if __name__ == '__main__':
    app.run(debug=True, port=5000, host="0.0.0.0")
