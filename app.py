import flask
from flask import Flask

app= Flask('app')
@app.route('/command', methods= ['POST'])
def command():
    return "TESTE"

if __name__== '__main__':
    app.run(host='0.0.0.0', port=13000)
 
