"""
*************************************************************
*                                                           *
*    Deep Neural Network Recommendation System for Yelp     *
*                                                           *
*************************************************************

Process data:
    1. Load data and write data into .json.
    2. Group data by userID, businessID

Data format:
    User dictionary:
        Relative data grouped by UserID
        Attributes:
            1. user_id, string, 22 character unique user id, maps to the user in 'user.json'.
            2. review_count, integer, the number of reviews they've written.
            3. userful, integer, number of useful votes sent by the user.
            4. funny, integer, number of funny votes sent by the user.
            5. cool, integer, number of cool votes sent by the user.
            6. friends, array of strings, an array of the user's friend as user_ids.
            7. fans, integer, number of fans the user has.
            8. average_stars, float, average rating of all reviews.
            9. reviews, a JSON array, all reviews a user sent.

    Business dictionary:
        Relative data grouped by BusinessID
        Attributes:
            1. business_id, string, 22 character unique string business id.
            2. latitude, float, latitude.
            3. longitude, float, latitude.
            4. stars, float, star rating, rounded to half-stars.
            5. review_count, integer, number of reviews.
            6. categories, a dictionary maps category to specific number.
"""

import json
import linecache
import random
import sys
import os


def load_grouped_data():
    dl = DataLoader

    return

class DataLoader():
    def __init__(self):
        self.user_count = 0
        self.user_data = {}

        self.business_count = 0

    def __load_user(self):
        cnt = 0
        with open('user.json', 'r') as f:
            for each_line in f:
                if random.randint(1, 101) == 11:
                    self.user_data.append(json.loads(each_line))
                    cnt = cnt + 1

        with open('user_random.json', 'w') as f:
            for i in data:
                f.write(json.dumps(i) + '\n')

        self.user_count = cnt

    def __load_business(self):


    def data_count(self):
        return


