
from transformers import MarianMTModel, MarianTokenizer

def translate(text, src='en', tgt='fr'):
    model_name = f'Helsinki-NLP/opus-mt-{src}-{tgt}'
    tokenizer = MarianTokenizer.from_pretrained(model_name)
    model = MarianMTModel.from_pretrained(model_name)
    tokens = tokenizer(text, return_tensors='pt')
    translation = model.generate(**tokens)
    return tokenizer.decode(translation[0], skip_special_tokens=True)
