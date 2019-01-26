#讀取檔案
products = []
with open('product.csv', 'r', encoding = 'utf-8') as f:
	for line in f:
		if 'name,price' in line:
			continue #跳過name price
		name, price = line.strip().split(',')
		producets.append([name, price])

print(products)

# 讓使用者輸入
while True:
	name = input('Please input name:')
	if name == 'q':
		break
	price = input('Please input price:')
	price = int(price)
	producets.append([name, price])
print(products)
