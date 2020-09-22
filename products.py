products = []
while True:
    name = input('Please enter the product name: ')
    if name == 'q':
        break
    price = input('Please enter the product price: ')
    products.append([name, price])
print(products)

for p in products:
    print(p[0], 'price is: ', p[1])
    
with open('products.csv', 'w',encoding='utf-8') as f:
#    f.write('Product Name' + ',' + 'Product Price' +'\n')
    f.write('Product Name, Product Price\n')
    for  p in products:
        f.write(p[0] + ',' + p[1] + '\n')
