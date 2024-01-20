import faiss
import pandas as pd
from sentence_transformers import SentenceTransformer

# Create an argument parser
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--filename', help='csv file containing product information.')
parser.add_argument('--query', help='user query')
parser.add_argument('--k', type=int, help='number of similar products returned')
args = parser.parse_args()

class ProductSearcher:
    """
    A collection of product searching methods.
    """
    def __init__(self, filename):
        self.df = pd.read_csv(filename) 
        self.llm =  SentenceTransformer('bert-base-nli-mean-tokens')
    
    def semantics_based_searcher(self, query, k):
        # create embeddings for product descriptions
        product_descriptions = self.df["product_description"].values # assume we have a column in self.df called `product_description`
        embeddings = self.llm.encode(product_descriptions)

        # index embeddings using faiss
        index = faiss.IndexFlatL2(embeddings.shape[1])
        index.add(embeddings)

        print("{} products indexed, each product description is represented by a {}-dimensional vector.".format(embeddings.shape[0], embeddings.shape[1]))

        # implement searching
        D, I = index.search(self.llm.encode([query]), k)  # search

        for i in range(3):
            print("Similarity score: {}".format(D[0][i]))
            print(self.df.loc[I[0][i]]["image_src"])
            print("============================================================")

if __name__ == "__main__":
    ProductSearcher(args.filename).semantics_based_searcher(args.query, args.k)