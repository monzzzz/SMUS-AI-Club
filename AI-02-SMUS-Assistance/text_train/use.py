import torch
from time import perf_counter as timer
import pandas as pd
import numpy as np
import torch
from sentence_transformers import util, SentenceTransformer


device = "cpu"
embedding_model= SentenceTransformer(model_name_or_path="all-mpnet-base-v2", 
                                      device=device)

def retrieve_relevant_resources(query: str, embeddings: torch.tensor, model: SentenceTransformer=embedding_model, n_resources_to_return: int = 5, print_time: bool=True):
    query_embedding = model.encode(query, convert_to_tensor=True)
    start_time = timer()
    dot_scores = util.dot_score(query_embedding, embeddings)[0]
    end_time = timer()

    if (print_time):
        print(f"Time taken to compute dot scores: {end_time - start_time} seconds")
    
    scores, indices = torch.topk(input = dot_scores, k=n_resources_to_return)
    return scores, indices

def main():
    question = "Who is the head of St.Michael University School?"
    text_chunks_and_embeddings_df_load = pd.read_csv("website_and_handbook_pre_processed.csv")
    text_chunks_and_embeddings_df_load["embedding"] = text_chunks_and_embeddings_df_load["embedding"].apply(lambda x: np.fromstring(x.strip("[]"), sep=" "))
    embeddings = torch.tensor(np.array(text_chunks_and_embeddings_df_load["embedding"].tolist()), dtype=torch.float32).to(device)
    scores, indices = retrieve_relevant_resources(question, embeddings, embedding_model)
    print("Score:", scores)
    print("Indices:", indices)


if __name__ == "__main__":
    main()