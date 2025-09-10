import ast
import requests
import json
import pandas as pd

name = dict()
data1 = []
data2 = []
with open("姓名.txt", "r", encoding="utf-8") as f:
    for line in f:
        line = line.strip()
        line = line.split()
        name[line[1]] = line[0]

tar = '牛客周赛 Round 104'

url = "https://ac.nowcoder.com/acm-heavy/acm/contest/profile/contest-joined-history?token=&uid="
url2 = "&page=false&onlyJoinedFilter=true&searchContestName=&onlyRatingFilter=false&contestEndFilter=true&_=1755585467899"
for ids in name:
    resp = requests.get(url + ids + url2)
    text = str(resp.text)
    if tar in text:

        dic = json.loads(text)

        dic = ast.literal_eval(str(dic["data"]))

        dic = ast.literal_eval(str(dic["dataList"]))

        for i in dic:
            cur = ast.literal_eval(str(i))
            if cur['contestName'] == tar:
                rank = cur['rank']
                status = '已参赛'
                ac = cur["acceptedCount"]
                break
    else:
        status = '未参赛'
        ac = ' '
        rank = ' '

    if status == '未参赛':
        data2.append([name[ids], status, rank, ac])
    else:
        data1.append([name[ids], status, int(rank), ac])

data1.sort(key = lambda x: x[2])
data = data1 + data2

df = pd.DataFrame(data, columns=["姓名", "状态", "排名", '过题数'])
df.to_excel(tar + '完成情况.xlsx', index = False)
