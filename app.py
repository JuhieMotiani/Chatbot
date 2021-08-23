from flask import Flask, render_template, request
from flask_sslify import SSLify
import generateOutput

app = Flask(__name__)
sslify = SSLify(app)

@app.route("/", methods=['GET'])
def my_index():
    return render_template("index.html")

@app.route("/output", methods=['GET'])
def output():
    if request.method == 'GET':
        user_input = request.args.get('message')
        output = generateOutput.response(user_input)
        return output
        

if __name__ == "__main__":
    app.run(debug=True)