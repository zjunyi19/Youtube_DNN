"""
*************************************************************
*                                                           *
*    Deep Neural Network Recommendation System for Yelp     *
*                                                           *
*************************************************************

Main function that combine different section.

"""

from Data.data import *
from Model.embedding import *


class config():
    # batch_size = 128
    embedding_size = 256
    skip_window = 1  # How many words to consider left and right.
    num_skips = 2  # How many times to reuse an input to generate a context.
    num_sampled = 64
    num_steps = 100001


def main():
    # Load data
    print("Start loading data...")
    user, business = load_grouped_data()
    print("Data loading finished...")

    # Extract Embedding Data
    print("Start Extracting for embedding...")
    user_bus_data, user_bus_dict, reverse_user_bus_dict, user_bus_count = extract_embedding_user_business(user)
    business_cat_data, business_cat_count = extract_embedding_catagory(business)
    print("Extracting finished...")

    print("Start Embedding...")
    user_bus_embed = Embedding(user_bus_data, user_bus_count)

    bus_cat_embed = Embedding(business_cat_data, business_cat_count)






if __name__ == '__main__':
    main()
