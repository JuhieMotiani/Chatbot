# from flask import Flask

# app = Flask(__name__)

# @app.route('/')
# def hello():
#     return "Hello World"

# if __name__ == '__main__':
#     app.run(port=3000)

from flask import Flask, render_template, request
import pandas as pd
import cosine_similarity

app = Flask("__main__")

@app.route("/", methods=['GET'])
def my_index():
    return render_template("index.html")

@app.route("/output", methods=['GET'])
def output():
    if request.method == 'GET':
        user_input = request.args.get('message')
        output = cosine_similarity.response(user_input)
        return output
        
            
            
            

app.run(debug=True, port=3000)