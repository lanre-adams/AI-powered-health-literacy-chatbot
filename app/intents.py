
from transformers import pipeline

classifier = pipeline("text-classification", model="bert-base-uncased")

def classify_intent(text):
    result = classifier(text)
    return result[0]['label']
