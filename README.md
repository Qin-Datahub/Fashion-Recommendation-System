# **AI/ML-driven Fashion Recommendation System**

## **Objective**

The goal of this project is to develop an AI/ML-driven Fashion Recommendation System that revolutionizes the online shopping experiences by providing personalized styling guidance and improving the accuracy of product search systems used by major e-commerce stores like Macy's or Nordstorm. The project aims to accomplish the following objectives:

* **Personalized Styling Guidance**
    * Build an intelligent system that acts as a virtual fashion stylist, offering personalized outfit recommendations to users based on their individual preferences, style, body type, and occasion.
    * Utilize advanced ML algorithms to analyze user data, including clothing items, accessories, style profiles, fashion trends, and user feedback, to generate tailored styling suggestions.
    * Incorporate image recognition, color analysis, style compatibility, and fashion trend forecasting to ensure visually appealing and fashionable outfit recommendations that align with the users' unique style preferences.

* **Enhanced Product Search Accuracy**
    * Develop AI/ML models that enhance search algorithms, ensuring more precise and relevant search results for users, even when dealing with complex queries or ambiguous search terms.
    * Explore advanced techniques such as image recognition and semantic search to improve search relevance, product categorization, and attribute extraction.
    * Continuously refine and optimize the search algorithms using user feedback, behavior analysis, purchase history, and real-time fashion trends to provide an increasingly tailored and accurate shopping experience.

## **Methodologies**

### **Semantics-based Product Search**

The first methodology applied for this project focuses on implementing a semantics-based product search system to improve the accuracy and relevance of search results. Through data preprocessing, semantic embeddings for each product stored in the DB and the embeddings for user queries are generated using advanced NLP techniques. These embeddings capture the meaning and context of user queries and product descriptions. By applying semantic matching algorithms and developing a relevance ranking mechanism, the search results are refined based on the similarity scores and other relevant factors (e.g., color and price).

For example:

```
from product_search import ProductSearcher

searcher = ProductSearcher("jeans.csv")
searcher.semantics_based_searcher(query="high-rise straight jeans", k=3)

# k stands for the number of similar products you want to pull out from the product store.
=========================================================================
# Example output:
1619 products indexed, each product description is represented by a 768-dimensional vector.
Similarity score: 26.24447250366211
brand                                                 Calvin Klein Jeans
product_description                         High-Rise Straight-Leg Jeans
original_price                                                    $79.50
image_src              https://slimages.macysassets.com/is/image/MCY/...
Name: 10, dtype: object
=========================================================================

Similarity score: 26.24447250366211
brand                                                       And Now This
product_description                         High-Rise Straight-Leg Jeans
original_price                                                    $49.00
image_src              https://slimages.macysassets.com/is/image/MCY/...
Name: 81, dtype: object
=========================================================================

Similarity score: 31.84622573852539
brand                                                Lauren Ralph Lauren
product_description                       High-Rise Straight Ankle Jeans
original_price                                                   $115.00
image_src              https://slimages.macysassets.com/is/image/MCY/...
Name: 886, dtype: object
=========================================================================
```

<img src="https://slimages.macysassets.com/is/image/MCY/products/3/optimized/25527343_fpx.tif?$browse$&wid=1200&fmt=jpeg" alt="Image 1" width="32%"/> <img src="https://slimages.macysassets.com/is/image/MCY/products/4/optimized/24882424_fpx.tif?$browse$&wid=1200&fmt=jpeg" alt="Image 2" width="32%"/> <img src="https://slimages.macysassets.com/is/image/MCY/products/4/optimized/23388484_fpx.tif?$browse$&wid=1200&fmt=jpeg" alt="Image 3" width="32%"/>

