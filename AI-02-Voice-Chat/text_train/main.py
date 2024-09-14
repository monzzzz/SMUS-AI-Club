import pandas as pd
from rag import get_embedding
import load_dotenv
load_dotenv.load_dotenv()

def main():
    df = pd.read_csv('smus_page.csv')
    df.head()
    # get the embedding of the first row
    get_embedding(df['Page Content'].iloc[0])
    print(df['Page Content'].head(5).apply(get_embedding))
    

if __name__ == "__main__":
    main()