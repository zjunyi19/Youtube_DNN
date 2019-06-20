# user.json -> friends, elite, 1637138
# checkin.json -> (useless?), 161950
# tip.json -> user, business, 1223094
# review.json -> user, business, (star), 6685900
# business -> attributes, 192609

import json
import linecache
import sys
import random

file = sys.argv[1]
data = []
final_data = []
cnt = 0
with open(file, 'r', encoding='UTF8') as f:
    for each_line in f:
        if (random.randint(1,11) == 1):
            data.append(json.loads(each_line))
            cnt = cnt + 1

for datum in data:
    # Filter out all the closed restaurants
    if datum["is_open"] == 1:
        # For each restaurant, store info of business_id, latitude/longitude, stars, review_count
        restaurant = dict()
        restaurant['business_id'] = datum['business_id']
        restaurant['latitude'] = datum['latitude']
        restaurant['longitude'] = datum['longitude']
        restaurant['stars'] = datum['stars']
        restaurant['review_count'] = datum['review_count']
        final_data.append(restaurant) # Store each restaurant info into "final_data"

with open('filter.json', 'w') as f: # Store all the restaurants info into 'filter.json' file
    for i in final_data:
        f.write(json.dumps(i) + '\n')
