import json
import linecache

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
