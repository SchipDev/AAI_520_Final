from flask import Flask, request, jsonify, render_template
import torch
from transformers import BertForQuestionAnswering, AutoTokenizer
app = Flask(__name__)
directory_path = "trained_model_bert"
model = torch.load(directory_path, map_location=torch.device('cpu'))  # Ensure model is loaded to CPU
tokenizer = AutoTokenizer.from_pretrained('bert-large-uncased-whole-word-masking-finetuned-squad')
@app.route('/')
def index():
    return render_template('index.html')
@app.route('/get_bot_response', methods=['POST'])
def get_bot_response():
    question = request.form['user_question']
    inputs = tokenizer(
        question,
        return_tensors='pt',
        max_length=1024,
        truncation=True
    )
    inputs = {key: val.to('cpu') for key, val in inputs.items()}  # Ensure tensors are on CPU
    outputs = model(**inputs)
    answer_start_scores = outputs.start_logits
    answer_end_scores = outputs.end_logits
    answer_start = torch.argmax(answer_start_scores)
    answer_end = torch.argmax(answer_end_scores) + 1
    answer = tokenizer.convert_tokens_to_string(
        tokenizer.convert_ids_to_tokens(inputs['input_ids'][0][answer_start:answer_end])
    )
    return jsonify({'bot_response': answer})
if __name__ == '__main__':
    app.run()


