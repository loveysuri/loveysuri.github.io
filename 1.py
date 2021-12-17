import json
import tabulate
f=open('assignment.json')
file=json.load(f)
products=file['products']
list=[]
for k in products:
    list.append(products[k])
list.sort(key=lambda i:int(i['price']),reverse=True)
header = list[0].keys()
rows =  [x.values() for x in list]
print(tabulate.tabulate(rows,header))


