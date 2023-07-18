import numpy as np
import requests
from skimage import io
from skimage.transform import resize
from sklearn.preprocessing import normalize
from flask import Flask, request, jsonify

app = Flask(__name__)

# Carregar o modelo pré-treinado (opcional)
# model = ...

# Rota para receber a URL da imagem e retornar o vetor
@app.route('/vectorize', methods=['POST'])
def vectorize_image():
    # Verificar se foi enviada uma URL na requisição
    if 'url' not in request.json:
        return jsonify({'error': 'No image URL found'})

    image_url = request.json['url']

    # Obter a imagem da URL
    img = io.imread(image_url)
    img = resize(img, (224, 224), anti_aliasing=True)  # Redimensionar a imagem para o tamanho esperado

    # Converter a imagem para vetor e normalizar
    vector = img.flatten()
    vector = normalize(vector.reshape(1, -1))

    # Obter o vetor de características da imagem usando o modelo pré-treinado (opcional)
    # features = model.predict(vector)

    return jsonify({'vector': vector.tolist()})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
