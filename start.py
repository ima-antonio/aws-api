from flask import Flask, jsonify

app = Flask(__name__)

# Consultar(todos)
@app.route('/test',methods=['GET'])
def obter_livros():
    return jsonify({'status': 'api running'})

if __name__ == '__main__':
    app.run(host='13.127.185.1', port=5000)
