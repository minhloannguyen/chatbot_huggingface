from transformers import pipeline
import logging

class ChatBot:
    __model_name = "ancs21/xlm-roberta-large-vi-qa"
    __data_path = "dataset/quydinhcapCCCD.txt"

    def __init__(self) -> None:
        self.model = self.load_model()
        self.context = self.load_dataset()

    def load_dataset(self, file_path=__data_path) -> str:
        with open(file_path) as f:
            contents = f.read()

        return contents

    def load_model(self, model=__model_name):
        logging.info(f"Loading model {model}...")
        nlp = pipeline('question-answering', model=model, tokenizer=model)

        return nlp

    def __call__(self, question):
        logging.info(f"question: {question}")
        QA_input = {
            'question': question,
            'context': self.context
        }
        res = self.model(QA_input)
        logging.info('pipeline: {}'.format(res))

        return res

    def run(self, question=""):
        if question:
            return self(question)
        
        return None