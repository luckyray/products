products = []
# read from file
with open('products.csv','r', encoding = 'utf-8') as f:
    for line in f:
        if 'Product Name' in line:
            continue # escape this loop, jump to next loop
        name, price = line.strip().split(',')
        products.append([name, price])

print(products)


# ask user to input
while True:
    name = input('Please enter the product name: ')
    if name == 'q':
        break
    price = input('Please enter the product price: ')
    products.append([name, price])
print(products)


# print all purchase record
for p in products:
    print(p[0], 'price is: ', p[1])


# input to file
with open('products.csv', 'w',encoding='utf-8') as f:
#    f.write('Product Name' + ',' + 'Product Price' +'\n')
    f.write('Product Name, Product Price\n')
    for  p in products:
        f.write(p[0] + ',' + p[1] + '\n')
