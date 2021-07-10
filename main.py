from flask import Flask, jsonify
import pandas as pd

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello I like to make AI Apps'

@app.route('/html')
def html():
    return """
    <title>This is a Hello World Page</title>
    <p>Hello</p>
    <p><b>World</b></p>
    """

@app.route('/pandas')
def pandas():
    df = pd.read_csv("https://raw.githubusercontent.com/noahgift/sugar/master/data/education_sugar_cdc_2003.csv")
    return jsonify(df.to_dict())

@app.route('/name/<value>')
def name(value):
    val = {"value": value}
    return jsonify(val)



if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
