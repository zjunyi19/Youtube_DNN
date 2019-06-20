import json
import linecache
import sys
import random

"""
    Process data:
    1. Join 'user-cleaned.json' and 'review.json', then write them to 'user-review-join.json'.
"""

join = {}

with open('user-cleaned.json', 'r') as f:
    for each_line in f:
        load = json.loads(each_line)
        load['reviews'] = []
        join[load['user_id']] = load

with open('review.json', 'r') as f:
    for each_line in f:
        load = json.loads(each_line)
        if load['user_id'] in join:
            join[load['user_id']]['reviews'].append(load)

with open('user-review-join.json', 'w') as f:
    for i in join.values():
        f.write(json.dumps(i) + '\n')










