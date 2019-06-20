import json
import linecache

"""
    Process data:
    1. Delete some of the columns, map every category to a number (can be further used to construct category vector)
    
    Attributes:
    1. business_id, string, 22 character unique string business id.
    2. latitude, float, latitude.
    3. longitude, float, latitude.
    4. stars, float, star rating, rounded to half-stars.
    5. review_count, integer, number of reviews.
    6. categories, a dictionary maps category to specific number. 
"""

s = {}
cnt = 0
wf = open("vectorized-business.json", "w+")
with open("business.json") as rf:
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

wf = open("vector.json", "w+")
#print(json.loads(linecache.getline("vectorized-business.json", 500))['categories'])
with open("vectorized-business.json") as rf:
    for each_line in rf:
        data = json.loads(each_line)
        categories = data['categories']
        data['vector'] = {}
        if categories:
            for i in categories.split(","):
                data['vector'][(i[1:] if i[0] == " " else i)] = s[(i[1:] if i[0] == " " else i)]
        del data['categories']
        wf.write(json.dumps(data) + '\n')
    rf.close()
wf.close()


