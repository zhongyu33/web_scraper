import ast
import requests
import re
import pandas as pd

def find(name):
    id = ''
    for i in name:
        if ord('0') <= ord(i) <= ord('9'):
            id += i
    url = 'https://ac.nowcoder.com/acm/contest/profile/' + id
    res = requests.get(url)
    html = res.text
    match = re.search(r'<title>(.*?)的比赛主页</title>', html)
    return match.group(1)
end_data = []

for i in range(1, 4):
    url = "https://acexam.nowcoder.com/api/competition-platform/contest/v1/rank?contestId=206&matchType=0&trackId=386&roundId=1947&page=" + str(i) + "&pageSize=20&"
    resp = requests.get(url)
    text = resp.text
    data = ast.literal_eval(text)
    data = ast.literal_eval(str(data['data']))
    data = ast.literal_eval(str(data['data']))
    end_data += [i.copy() for i in data]
for i in range(len(end_data)):
    end_data[i][1] = find(end_data[i][1])

df = pd.DataFrame(end_data, columns=["序号", "姓名", "得分", "排名", "奖品"])
df.to_excel("排名.xlsx", index=False)
