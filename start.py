from flask import Flask, jsonify

app = Flask(__name__)

# Consultar(todos)
@app.route('/livros',methods=['GET'])
def obter_livros():
    return jsonify({'status': 'api running'})


app.run(port=5000,host='13.127.185.1',debug=False)
