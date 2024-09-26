from transformers import AutoTokenizer, AutoModel
import torch

def get_embedding(text, model = "text-embedding-3-small"):
    # Load the tokenizer and model from Hugging Face
    tokenizer = AutoTokenizer.from_pretrained('bert-base-uncased')
    model = AutoModel.from_pretrained('bert-base-uncased')
    # Tokenize input and generate embeddings
    inputs = tokenizer(text, max_length=512, truncation=True, return_tensors='pt')
    with torch.no_grad():
        outputs = model(**inputs)
    embeddings = outputs.last_hidden_state
    return embeddings