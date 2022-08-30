import json
from pathlib import Path

# cars=[{'make': 'seat','color':'black', 'max_speed':200 , 'price':[120000,5500,3000]},
#       {'make': 'mazda','color':'red', 'max_speed':220,'price':[180000,5500,3000]},
#       {'make': 'volvo','color':'blue', 'max_speed':300,'price':[18880,5500,3000]},
#       {'make': 'audi','color':'black', 'max_speed':120,'price':[34435,5500,3000]}
#       ]
# print(cars)
#
# data = json.dumps(cars)
# print(data)
#
# Path('Cars.json').write_text(data)

data = Path('Cars.json').read_text()
Cars = json.loads(data)
print(type(Cars))
print(type(data))
print(data[0])
print(Cars[0])