import json
d={"name":"혼자 공부하는 데이터 분석"}
print(d["name"])
d_str = json.dumps(d, ensure_ascii=False)
d3= json.loads('{"name":"혼자 공부하는 데이터 분석","author":"박해선",\
               "year":2022}')
print(d_str)
print(d3["name"])
print(d3["author"][1])
print(d3["year"])

d4_str="""
    [
    {"name":"혼자 공부하는 데이터 분석","author":"박해선","year":2022},
    {"name":"혼자 공부하는 머신러닝+딥러닝","author":"박해선","year":2020},
    ]
"""
# d4 = json.loads(d4_str)
# print(d4[0]["name"])


# import pandas as pd
# pd.read_json(d4_str)

# pd.DataFrame(d4)

x_str ="""
<book>
    <name>혼자 공부하는 데이터 분석</name>
    <author>박해선</author>
    <year>2022</year>
</book>
"""

import xml.etree.ElementTree as et
book =et.fromstring(x_str)

print(type(book))
print(book.tag)
book_childs =list(book)
print(book_childs)
