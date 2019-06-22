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

PATH = "/Users/syiming/Project_Large/Youtube_DNN/Data/"

def load_grouped_data():
    """
    Load 1% data from original dataset
    :return: user and business dictionary
    """
    dl = DataLoader()
    dl.load_user()
    dl.load_business()
    print(" # ", dl.user_count, " user data loaded.")
    print(" # ", dl.business_count, " business data loaded.")

    return dl.user_data, dl.business_data


class DataLoader:
    def __init__(self):
        self.user_count = 0
        self.user_data = {}

        self.business_count = 0
        self.business_data = {}

    def __user_random__(self):
        data = []

        with open(PATH + 'user.json', 'r') as rf:
            print("\tRandom select user")
            for each_line in rf:
                if random.randint(1, 101) == 11:
                    data.append(json.loads(each_line))

        print("\tWrite random file")
        with open(PATH + 'user-random.json', 'w') as wf:
            for i in data:
                wf.write(json.dumps(i) + '\n')

    def __user_review_join__(self):

        print("\tEnter join")

        join = {}

        with open(PATH + 'user-random.json', 'r') as rf:
            for each_line in rf:
                data = json.loads(each_line)
                data['reviews'] = []
                join[data['user_id']] = data

        with open(PATH + 'review.json', 'r') as rf:
            for each_line in rf:
                data = json.loads(each_line)
                if data['user_id'] in join:
                    join[data['user_id']]['reviews'].append(data)

        print("\tWrite join file")
        with open(PATH + 'user-review-join.json', 'w') as wf:
            for i in join.values():
                wf.write(json.dumps(i) + '\n')

    def __vectorized_user__(self):
        wf = open(PATH + "load-user.json", "w+")
        with open(PATH + "user-review-join.json") as rf:
            for each_line in rf:
                data = json.loads(each_line)
                del data['name']
                del data['yelping_since']
                del data['elite']
                del data['compliment_hot']
                del data['compliment_more']
                del data['compliment_profile']
                del data['compliment_cute']
                del data['compliment_list']
                del data['compliment_note']
                del data['compliment_plain']
                del data['compliment_cool']
                del data['compliment_funny']
                del data['compliment_writer']
                del data['compliment_photos']
                for review in data['reviews']:
                    del review['text']

                d = dict()
                d[data['user_id']] = data
                del d[data['user_id']]['user_id']

                wf.write(json.dumps(d) + '\n')

        # print(list(json.loads(linecache.getline("load-user.json", 1)).values())[0].keys())
        # (['review_count', 'useful', 'funny', 'cool', 'friends', 'fans', 'average_stars', 'reviews'])

    def __vectorized_business__(self):
        s = {}
        cnt = 0
        wf = open(PATH + "_.json", "w+")
        with open(PATH + "business.json") as rf:
            for each_line in rf:
                data = json.loads(each_line)
                del data['name']
                del data['address']
                del data['city']
                del data['state']
                del data['postal_code']
                del data['is_open']
                del data['attributes']
                del data['hours']
                categories = data['categories']
                if categories:
                    for i in categories.split(","):
                        if (i[1:] if i[0] == " " else i) in s:
                            continue
                        s[(i[1:] if i[0] == " " else i)] = cnt;
                        cnt = cnt + 1
                wf.write(json.dumps(data) + '\n')
            rf.close()
        wf.close()

        wf = open(PATH + "load-business.json", "w+")
        # print(json.loads(linecache.getline("vectorized-business.json", 500))['categories'])
        with open(PATH + "_.json") as rf:
            for each_line in rf:
                data = json.loads(each_line)
                categories = data['categories']
                data['vector'] = {}
                if categories:
                    for i in categories.split(","):
                        data['vector'][(i[1:] if i[0] == " " else i)] = s[(i[1:] if i[0] == " " else i)]
                del data['categories']

                d = dict()
                d[data['business_id']] = data
                del d[data['business_id']]['business_id']

                wf.write(json.dumps(d) + '\n')
            rf.close()
        wf.close()

    def load_user(self):
        if not os.path.exists(PATH + 'user-random.json'):
            self.__user_random__()

        if not os.path.exists(PATH + 'user-review-join.json'):
            self.__user_review_join__()

        if not os.path.exists(PATH + 'load-user.json'):
            self.__vectorized_user__()

        with open(PATH + "load-user.json") as rf:
            for each_line in rf:
                data = json.loads(each_line)
                self.user_data.update(data)

        self.user_count = len(self.user_data)

    def load_business(self):
        if not os.path.exists(PATH + 'load-business.json'):
            self.__vectorized_business__()

        with open(PATH + "load-business.json") as rf:
            for each_line in rf:
                data = json.loads(each_line)
                self.business_data.update(data)

        self.business_count = len(self.business_data)
