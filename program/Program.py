import random
import csv

with open('product_data3.csv', 'w', encoding='utf-8-sig') as csvfile:
    csvfile.write('id,color,category,price,rating,base_discount,net_price')
with open('sales_data3.csv', 'w', encoding='utf-8-sig') as csvfile2:
    csvfile2.write('id,rating,return_rate,location,sales,revenue')
rating = 0
returnrate = 0
price = 0
color = 0
category = 0
location = 0
sales = 0
sales_multiplier = 0
counter = 0
base_discount = 0
#rating = random.randint(0,10)
#returnrate = ((random.randint(0,10))*0.01)
#color = random.randint(0,5)
#price =((random.randint(0,29)*100+99))
#location = random.randint(1,7)
#category = random.randint(2,12)
#sales = (int((rating*location)+(price/category))*(returnrate/0.002)+random.randint(0,10))
#print(f'Rating: {rating}'
#      f'\nReturnrate: {returnrate}'
#      f'\nColor: {color}'
#      f'\nPrice: {price}'
#      f'\nLocation: {location}'
#      f'\nCategory: {category}'
#      f'\nSales: {sales}')

def write_to_sales_data(ID, rating, returnrate, location, sales, revenue):
    with open('sales_data3.csv', 'a', encoding='utf-8-sig') as file:
        file.write(f'\n{ID},{rating},{returnrate},{location},{sales},{revenue}')



def write_to_product_data(ID, color, category, price, rating, base_discount, net_price):
    with open('product_data3.csv', 'a', encoding='utf-8-sig') as file:
        file.write(f'\n{ID},{color},{category},{price},{rating},{base_discount},{net_price}')

for counter in range(10000):
    counter += 1
    id = str(counter).zfill(4)
    id2 = f'P{id}'
    rating = ((random.randint(1,9)+(random.randint(0,10)*0.1)))
    returnrate = ((10-rating)+(random.randint(0,10)*0.1)*0.01)/100
    color = random.randint(1,5)
    price =((random.randint(0,19)*100+99))
    location = random.randint(1,7)
    category = random.randint(1,5)
    sales_multiplier = 10
    if category == 1:
        base_discount = 0.8
    if category == 2:
        base_discount = 0.75
    if category == 3:
        base_discount = 0.7
    if category == 4:
        base_discount = 0.6
    if category == 5:
        base_discount = 0.5
    #sales = int(((((rating*location)+(price/category))*(returnrate/0.01)+random.randint(0,10))*100)+random.randint(0,100))
    #sales = int((sales_multiplier+price+color+returnrate+(rating*3)+location+base_discount)*10+(random.randint(0,10)))

    sales = int(((price*0.0001)+(rating)-base_discount-returnrate)*1000)
    net_price = price * base_discount
    revenue = net_price * sales
    write_to_sales_data(id2, rating, returnrate,location, sales, revenue)
    write_to_product_data(id2,color,category,price,rating, base_discount, net_price)

