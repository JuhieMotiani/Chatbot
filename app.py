from flask import Flask, render_template, request
import generateOutput

app = Flask("__main__")

@app.route("/", methods=['GET'])
def my_index():
    return render_template("index.html")

@app.route("/output", methods=['GET'])
def output():
    if request.method == 'GET':
        user_input = request.args.get('message')
        output = generateOutput.response(user_input)
        return output
        
            
app.run(debug=True, port=8000)