import os #operating system
#讀取檔案
products = []
if os.path.isfile('products.csv'): #如果這檔案有無在這個絕對路徑 檢查有無這個檔案
	print('yes! file exist')
	with open('product.csv', 'r', encoding = 'utf-8') as f:
		for line in f:
			if 'name,price' in line:
				continue #跳過name price
			name, price = line.strip().split(',')
			producets.append([name, price])
else:
	print('not file exsit')




print(products)

# 讓使用者輸入
while True:
	name = input('Please input name:')
	if name == 'q':
		break
	price = input('Please input price:')
	price = int(price)
	products.append([name, price])
print(products)
