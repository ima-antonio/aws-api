from flask import Flask, request, jsonify
import urllib.request
from PIL import Image
import imagehash

app = Flask(__name__)

@app.route('/calcular_hash', methods=['POST'])
def calcular_hash():
    try:
        # Obter a URL da imagem enviada na requisição
        data = request.get_json()
        url_imagem = data.get('imagem')

        # Baixar a imagem da URL
        response = urllib.request.urlopen(url_imagem)
        img = Image.open(response)

        # Calcular o hash perceptual da imagem
        hash_img = imagehash.average_hash(img)

        # Transformar o hash em uma string hexadecimal
        identificador = str(hash_img)

        return jsonify({"identificador": identificador})
    except Exception as e:
        return jsonify({"error": f"Erro ao calcular o identificador: {e}"}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)