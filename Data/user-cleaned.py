import json
import linecache
import sys
import random

"""
    Process data:
    1. Randomly pick 1% user, and write them to 'user-cleaned.json'.
"""

data = []
cnt = 0
with open('user.json', 'r') as f:
    for each_line in f:
        if random.randint(1, 101) == 11:
            data.append(json.loads(each_line))
            cnt = cnt + 1

with open('user_random_001.json', 'w') as f:
    for i in data:
        f.write(json.dumps(i) + '\n')

print(cnt)







