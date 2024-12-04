from flask import Flask ,jsonify

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'hello_world'

@app.route('/oddeven/<int:num>')
def oddeven(num):
    if num % 2 ==0:
        result = {"number" : num,
                 "oddeven" : "even" }
        return jsonify(result)
    else:
        result = {"number": num,
                  "oddeven": "odd"}
        return jsonify(result)


if __name__ == "__main__":
    app.run(debug=True)


