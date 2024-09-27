import pandas as pd
import pandas as pd
import numpy as np
import re
from spacy.lang.en import English
from tqdm.auto import tqdm
from sentence_transformers import SentenceTransformer

device = "cpu"

embedding_model = SentenceTransformer(model_name_or_path= "all-mpnet-base-v2",
                                      device=device)
nlp = English()

nlp.add_pipe("sentencizer")

doc = nlp("This is a sentence. This another sentence. I like Elephants")

def assign_properties(pages_and_text, column = "Page Content"):
    result = []
    print(len(pages_and_text[column].tolist()))
    for index, page in enumerate(pages_and_text[column].tolist()):
        result.append({"page_number": index,
                               "page_char_count": len(page),
                               "page_word_count": len(page.split(" ")),
                               "page_sentences": len(page.split(".")),
                               "page_token_count": len(page)/4, # 1 token ~ 4 characters
                                "text": page
                               })
    return result
def splitting_into_sentences(pages_and_texts):
    for item in tqdm(pages_and_texts):
        item["sentences"] = list(nlp(item["text"]).sents)
        item["sentences"] = [str(sentence) for sentence in item["sentences"]]
        item["page_space_count_spacy"] = len(item["sentences"])
    return pages_and_texts


def split_list(input_list: list, slice_size: int) -> list[list[str]]:
    return [input_list[i : i + slice_size] for i in range(0, len(input_list), slice_size)]


def chunk(pages_and_texts, num_sentence_chuck_size = 10):
    for item in tqdm(pages_and_texts):
        item["sentence_chunks"] = split_list(input_list=item["sentences"],
                                         slice_size=num_sentence_chuck_size)
        item["num_chunk"] = len(item["sentence_chunks"])
    return pages_and_texts


def join_sentences(pages_and_texts):
    pages_and_chunks = []
    for item in tqdm(pages_and_texts):
        for sentence_chunk in item["sentence_chunks"]:
            chunk_dict = {}
            chunk_dict["page_number"] = item["page_number"]

            # Join the sentences, so that the sentence start with capital letter after period
            joined_sentence_chunk = "".join(sentence_chunk).replace(" ", " ").strip()
            joined_sentence_chunk = re.sub(r'\.([A-Z])', r'. \1', joined_sentence_chunk)

            chunk_dict["sentence_chunk"] = joined_sentence_chunk

            chunk_dict["chunk_char_count"] = len(joined_sentence_chunk)
            chunk_dict["chunk_word_count"] = len([word for word in joined_sentence_chunk.split(" ")])
            chunk_dict["chunk_token_count"] = len(joined_sentence_chunk)/4

            pages_and_chunks.append(chunk_dict)
    return pages_and_chunks

def get_embeddings(text):
    embeddings = embedding_model.encode(text)
    return embeddings

def main():
    pages_and_text = []
    # Load data
    df_smus_website = pd.read_csv("smus_page.csv") 
    df_smus_handbook = pd.read_csv("smus_handbook.csv")
    for page in df_smus_website["Page Content"]:
        pages_and_text.append(page.replace("\n", " "))
    for page in df_smus_handbook["Page Content"]:
        pages_and_text.append(page)

    # Convert to dataframe
    df = pd.DataFrame(pages_and_text, columns = ["Page Content"])

    # Assign Properties
    pages_and_text = assign_properties(df)

    # Splitting the sentences
    pages_and_text = splitting_into_sentences(pages_and_text)

    # Chunk Sentences
    pages_and_chunks = chunk(pages_and_text)

    # Join Sentences
    pages_and_chunks = join_sentences(pages_and_chunks)

    # Get Embeddings
    for item in tqdm(pages_and_chunks):
        item["embedding"] = get_embeddings([item["sentence_chunk"]])

    # Convert to DataFrame
    text_chunks_and_embeddings_df = pd.DataFrame(pages_and_chunks)

    # Save Embeddings
    text_chunks_and_embeddings_df.to_csv("website_and_handbook_pre_processed.csv", index = False)


if __name__ == '__main__':
    main()