import json
import linecache

"""
    Process data:
    1. Delete some of the columns.
    
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
"""

wf = open("data.json", "w+")
with open("user-review-join.json") as rf:
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
        wf.write(json.dumps(data) + '\n')

print(json.loads(linecache.getline("data.json", 1)).keys())
