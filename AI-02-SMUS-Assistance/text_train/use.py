import torch
from time import perf_counter as timer
from sentence_transformers import util, SentenceTransformer

def retrieve_relevant_resources(query: str, embeddings: torch.tensor, model: SentenceTransformer=embedding_model, n_resources_to_return: int = 5, print_time: bool=True):
    query_embedding = model.encode(query, convert_to_tensor=True)
    start_time = timer()
    dot_scores = util.dot_score(query_embedding, embeddings)[0]
    end_time = timer()

    if (print_time):
        print(f"Time taken to compute dot scores: {end_time - start_time} seconds")
    
    scores, indices = torch.topk(input = dot_scores, k=n_resources_to_return)
    return scores, indices
    