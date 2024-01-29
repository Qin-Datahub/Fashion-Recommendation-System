import faiss
import ast
import pandas as pd
from sentence_transformers import SentenceTransformer
from colormath.color_diff import delta_e_cie1994
from colormath.color_objects import LabColor, sRGBColor
from colormath.color_conversions import convert_color

# Create an argument parser
# import argparse

# def tuple_type(arg):
#     try:
#         # Split the argument string into individual values
#         values = arg.split(',')
#         # Convert the values to integers
#         values = tuple(map(int, values))
#         return values
#     except ValueError:
#         raise argparse.ArgumentTypeError('Tuple must contain comma-separated integers')

# parser = argparse.ArgumentParser()
# parser.add_argument('--filename', help='csv file containing product information.')
# parser.add_argument('--query', help='user query')
# parser.add_argument('--reference_color', type=tuple_type, help='reference color.')
# parser.add_argument('--k', type=int, help='number of similar products returned')
# args = parser.parse_args()

class ProductSearcher:
    """
    A collection of product searching methods.
    """
    def __init__(self, filename):
        self.df = pd.read_csv(filename) # pandas dataframe contains the product information
        self.llm =  SentenceTransformer('bert-base-nli-mean-tokens')
    
    def semantics_based_searcher(self, query_description, k):
        """
        Search for products with similar descriptions.
        """
        # create embeddings for product descriptions
        product_descriptions = self.df["product_description"].values # assume we have a column in self.df called `product_description`
        embeddings = self.llm.encode(product_descriptions)

        # index embeddings using faiss
        index = faiss.IndexFlatL2(embeddings.shape[1])
        index.add(embeddings)

        print("{} products indexed, each product description is represented by a {}-dimensional vector.".format(embeddings.shape[0], embeddings.shape[1]))

        # implement searching
        D, I = index.search(self.llm.encode([query_description]), k)  # search

        for i in range(k):
            print("Similarity score: {}".format(D[0][i]))
            print(self.df.loc[I[0][i]]["image_src"])
            print("============================================================")
    
    def color_based_searcher(self, query_color, k):
        """
        Search for products with similar colors.
        Input:
            - query_color: query color
            - k: number of similar products returned
        """
        # Calculate color diffs
        color_similarity_scores = []
        for _, row in self.df.iterrows():
            sample_color = ast.literal_eval(row["dominant_color"])

            color1_lab = convert_color(sRGBColor(*query_color), LabColor)
            color2_lab = convert_color(sRGBColor(*sample_color), LabColor)

            color_similarity_scores.append(delta_e_cie1994(color1_lab, color2_lab))

        # Sort color diffs
        self.df["color_similarity_score"] = color_similarity_scores
        self.df = self.df.sort_values('color_similarity_score').reset_index()

        # Return the top k products
        for i in range(k):
            print("Similarity score: {}".format(self.df.loc[i]["color_similarity_score"]))
            print(self.df.loc[i]["image_src"])
            print("============================================================")

 