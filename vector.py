import torch
import torchvision.models as models
import torchvision.transforms as transforms
from PIL import Image
from io import BytesIO
import requests
from flask import Flask, request, jsonify

app = Flask(__name__)

# Carregar o modelo ResNet pré-treinado
modelo_resnet = models.resnet50(pretrained=True)
modelo_resnet.eval()

# Definir transformações de pré-processamento
transform = transforms.Compose([
    transforms.Resize(256),
    transforms.CenterCrop(224),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
])

# Rota para receber a URL da imagem e retornar o vetor
@app.route('/vectorize', methods=['POST'])
def vectorize_image():
    # Verificar se foi enviada uma URL na requisição
    if 'url' not in request.json:
        return jsonify({'error': 'No image URL found'})

    image_url = request.json['url']

    # Carregar e pré-processar a imagem
    response = requests.get(image_url)
    image = Image.open(BytesIO(response.content))
    image = transform(image)
    image = image.unsqueeze(0)

    # Obter o vetor de características da imagem
    vetor_caracteristicas = modelo_resnet(image)
    vetor_caracteristicas = torch.flatten(vetor_caracteristicas).detach().numpy()

    return jsonify({'vector': vetor_caracteristicas.tolist()})

if __name__ == '__main__':
    app.run()
    app.run(port=5000,host='13.127.185.1',debug=False)
