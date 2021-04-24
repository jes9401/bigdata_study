import json

cities=[
    {'rank':1,'city':'상하이','population':24150000}
]
with open('top_cities.json','w',encoding='utf-8') as f:
    json.dump(cities,f)