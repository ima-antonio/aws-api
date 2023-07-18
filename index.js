const express = require('express');
const axios = require('axios');
const { createCanvas, loadImage } = require('canvas');
const tf = require('@tensorflow/tfjs-node');
const mobilenet = require('@tensorflow-models/mobilenet');

const app = express();
const PORT = 5000;

// Rota para receber a URL da imagem e retornar o vetor de características
app.post('/vectorize', async (req, res) => {
  if (!req.body || !req.body.url) {
    return res.status(400).json({ error: 'No image URL provided' });
  }

  const imageUrl = req.body.url;

  try {
    // Obter o vetor de características da imagem
    const vetorCaracteristicas = await obterVetorCaracteristicas(imageUrl);

    res.json({ vector: vetorCaracteristicas });
  } catch (error) {
    console.error(error);
    res.status(500).json({ error: 'Failed to process the image' });
  }
});

// Função para obter o vetor de características de uma imagem a partir da URL
async function obterVetorCaracteristicas(imageUrl) {
  try {
    // Carregar a imagem
    const response = await axios.get(imageUrl, { responseType: 'arraybuffer' });
    const imageBuffer = Buffer.from(response.data, 'binary');
    const image = await loadImage(imageBuffer);
    const canvas = createCanvas(image.width, image.height);
    const ctx = canvas.getContext('2d');
    ctx.drawImage(image, 0, 0);
    const imageData = ctx.getImageData(0, 0, canvas.width, canvas.height).data;

    // Carregar o modelo MobileNet
    const model = await mobilenet.load();

    // Processar a imagem e obter o vetor de características
    const tensor = tf.tensor3d(imageData, [canvas.height, canvas.width, 4], 'int32');
    const processedTensor = tensor.expandDims(0).toFloat().div(255);
    const predictions = await model.predict(processedTensor);
    const vetorCaracteristicas = await predictions.array();

    return vetorCaracteristicas;
  } catch (error) {
    throw error;
  }
}

app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});
