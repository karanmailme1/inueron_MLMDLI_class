from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/karan1', methods=['POST'])
def test():
    return "test_this1"
    #return jsonify(1+2)
    #return 4 #error

@app.route('/karan2') #default is GET method
def test2():
    return "test_this2"
    #return jsonify(1+2)
    #return 4 #error

if __name__ == '__main__':
    app.run(debug=True)
