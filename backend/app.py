from flask import Flask, request, jsonify
from torch import load, device
from transformers import BertTokenizer
app = Flask(__name__)

model = load('Bahamut_NCU.pt', map_location=device('cpu'))
tokenizer = BertTokenizer.from_pretrained('bert-base-chinese')


def getContent(data):
    contents = data['content']
    contents = [i.replace('\n', '') for i in contents]
    return contents


def getPrediction(contents):
    encoding = tokenizer(contents, return_tensors='pt', padding=True, truncation=True)
    input_ids = encoding['input_ids']
    attention_mask = encoding['attention_mask']

    output = model(input_ids, attention_mask)
    prob = output.logits.sigmoid()

    THRESHOLD = 0.3
    prediction = prob.detach().clone()
    prediction[prediction > THRESHOLD] = 1
    prediction[prediction <= THRESHOLD] = 0

    y_hat = []
    label = ['課業', '蓋樓', '生活', '問題', '食物', '其他']
    for idx, i in enumerate(prediction):
        y_hat.append([label[j] for j in range(6) if i[j] == 1])

    return y_hat


@app.route("/")
def hello():
    return "Hello, World!"


@app.route("/test", methods=["POST"])
def test_page():
    data = request.get_json()
    contents = getContent(data)
    y_hats = []
    for i in contents:
        y_hats.append(getPrediction([i]))
    return jsonify({'message': y_hats})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
