import random
import csv

with open('product_data3.csv', 'w', encoding='utf-8-sig') as csvfile:
    csvfile.write('id,color,category,price,rating,base_discount,net_price')
with open('sales_data3.csv', 'w', encoding='utf-8-sig') as csvfile2:
    csvfile2.write('id,rating,return_rate,location,sales,revenue,margin')
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

def write_to_sales_data(ID, rating, returnrate, location, sales, revenue, margin):
    with open('sales_data3.csv', 'a', encoding='utf-8-sig') as file:
        file.write(f'\n{ID},{rating},{returnrate},{location},{sales},{revenue},{margin}')



def write_to_product_data(ID, color, category, price, rating, base_discount, net_price):
    with open('product_data3.csv', 'a', encoding='utf-8-sig') as file:
        file.write(f'\n{ID},{color},{category},{price},{rating},{base_discount},{net_price}')

for counter in range(3000):
    counter += 1
    id = str(counter).zfill(4)
    id2 = f'P{id}'
    color = random.randint(1,5)
    price =((random.randint(0,19)*100+99))
    location = random.randint(1,7)
    category = random.randint(1,5)
    sales_multiplier = 10
    if category == 1:
        base_discount = 0.8
        rating = ((random.randint(1, 9) + (random.randint(5, 10) * 0.1)))
        price = ((random.randint(12, 19) * 100 + 99))
    if category == 2:
        base_discount = 0.75
        rating = ((random.randint(1, 9) + (random.randint(4, 10) * 0.1)))
        price = ((random.randint(8, 15) * 100 + 99))
    if category == 3:
        base_discount = 0.7
        rating = ((random.randint(1, 9) + (random.randint(3, 10) * 0.1)))
        price = ((random.randint(5, 12) * 100 + 99))
    if category == 4:
        base_discount = 0.6
        rating = ((random.randint(1, 9) + (random.randint(2, 10) * 0.1)))
        price = ((random.randint(3, 10) * 100 + 99))
    if category == 5:
        base_discount = 0.5
        rating = ((random.randint(1, 9) + (random.randint(1, 10) * 0.1)))
        price = ((random.randint(0, 7) * 100 + 99))
    #sales = int(((((rating*location)+(price/category))*(returnrate/0.01)+random.randint(0,10))*100)+random.randint(0,100))
    #sales = int((sales_multiplier+price+color+returnrate+(rating*3)+location+base_discount)*10+(random.randint(0,10)))
    
    returnrate = ((10 - rating) + (random.randint(0, 10) * 0.1) * 0.01) / 100
   
    sales = int((((2000-price)+((10-rating))-(returnrate*10)*200)*(100+(random.randint(0,10))-60))+8500)
    print(f'{price},{sales}, {rating}')

    net_price = price * base_discount
    revenue = net_price * sales
    margin = sales * (price-net_price)
    write_to_sales_data(id2, rating, returnrate,location, sales, revenue, margin)
    write_to_product_data(id2,color,category,price,rating, base_discount, net_price)

