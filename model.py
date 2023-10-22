import torch
import os
from transformers import BertForQuestionAnswering, AutoTokenizer

class ChatBot():
    
    def __init__(self):
        checkpoint_dir = "checkpoint-21500"

        self.tokenizer =  AutoTokenizer.from_pretrained('bert-large-uncased-whole-word-masking-finetuned-squad')
        self.model = BertForQuestionAnswering.from_pretrained('bert-large-uncased-whole-word-masking-finetuned-squad')

        self.context = []

    def generate_response(self, user_message):
        self.context.append(user_message)
        input_ids = self.tokenizer.encode(' '.join(self.context), return_tensors='pt', max_length=1024, truncation=True)
        output_ids = self.model.generate(input_ids)
        output_text = self.tokenizer.decode(output_ids[0], skip_special_tokens=True)
        bot_response = output_text.split('.')[-1]
        self.context.append(bot_response)
        return bot_response
    

