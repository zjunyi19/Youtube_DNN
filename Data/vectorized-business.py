import json
import linecache

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


