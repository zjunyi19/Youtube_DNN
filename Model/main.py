"""
*************************************************************
*                                                           *
*    Deep Neural Network Recommendation System for Yelp     *
*                                                           *
*************************************************************

Main function that combine different section.

"""

from Data.data import *

class config():
    batch_size = 128
    embedding_size = 256
    skip_window = 1  # How many words to consider left and right.
    num_skips = 2  # How many times to reuse an input to generate a context.


def main():
    # Load data
    print("Start loading data...")
    user, business = load_grouped_data()
    print("Data loading finished...")

    # Embedding Data






if __name__ == '__main__':
    main()
