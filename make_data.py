# user.json -> friends, elite, 1637138
# checkin.json -> (useless?), 161950
# tip.json -> user, business, 1223094
# review.json -> user, business, (star), 6685900
# business -> attributes, 192609

# userid,
import json
import linecache
import sys
import random

file = sys.argv[1]
data = []
cnt = 0
with open(file, 'r') as f:
    for each_line in f:
        if (random.randint(1,11) == 1):
            data.append(json.loads(each_line))
            cnt = cnt + 1
print(data[0]['name'])
with open('filter.json', 'w') as f:
    for i in data:
        f.write(json.dumps(i) + '\n')







