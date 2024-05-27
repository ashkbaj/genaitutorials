from typing import Any
import json


json1 = {
	"firstName": "John",
	"lastName": "doe",
	"executiveSummary": "Below, you will find a proposal, etc. etc.",
	"products": [
		{
			"name": "test product",
			"quantity": 5,
			"price": 10,
			"total": 50
		},
		{
			"name": "Creative Name",
			"quantity": 10,
			"price": 20,
			"total": 200
		}
	]
}

class Product:
    name: str
    quantity: int
    price: int
    total: float

    @staticmethod
    def from_dict(obj: Any) -> 'Product':
		#print(str(obj))
        _name = str(obj.get('name'))
        _quantity = int(obj.get('quantity'))
        _price = int(obj.get('price'))
        _total = float(obj.get('total'))
        return Product(_name, _quantity, _price, _total)

dict1 = '''{
			"name": "Creative Name for test - Matar Paneer",
			"quantity": 10,
			"price": 20,
			"total": 200
		}'''

dict2 = {
			"name": "Creative Name for test - Matar Paneer2",
			"quantity": 10,
			"price": 200,
			"total": 2000
		}


#myjson = json.dumps(dict1)
#myjson = json.dumps(dict2)
#myjson = json.loads(dict1) #Product takes no arguments
#myjson = json.dumps(dict2)
jsonstring = json.loads(dict1)
prod1 = Product.from_dict(jsonstring)
print(prod1.name)