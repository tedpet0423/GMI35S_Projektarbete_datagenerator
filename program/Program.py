import random
import csv

with open('product_data.csv', 'w', encoding='utf-8-sig') as csvfile:
    csvfile.write('id,color,category,price,rating')
with open('sales_data.csv', 'w', encoding='utf-8-sig') as csvfile2:
    csvfile2.write('id,rating,return_rate,location,sales')
rating = 0
returnrate = 0
price = 0
color = 0
category = 0
location = 0
sales = 0
counter = 0
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

def write_to_sales_data(ID, rating, returnrate, location, sales,):
    with open('sales_data.csv', 'a', encoding='utf-8-sig') as file:
        file.write(f'\n{ID},{rating},{returnrate},{location},{sales}')



def write_to_product_data(ID, color, category, price, rating):
    with open('product_data.csv', 'a', encoding='utf-8-sig') as file:
        file.write(f'\n{ID},{color},{category},{price},{rating}')

for counter in range(10000):
    counter += 1
    id = str(counter).zfill(4)
    rating = ((random.randint(0,10)+(random.randint(0,10)*0.1)))
    returnrate = ((random.randint(0,10000))*0.00001)
    color = random.randint(1,5)
    price =((random.randint(0,29)*100+99))
    location = random.randint(1,7)
    category = random.randint(2,12)
    sales = int(((((rating*location)+(price/category))*(returnrate/0.01)+random.randint(0,10))*100)+random.randint(0,100))
    write_to_sales_data(id, rating, returnrate,location, sales)
    write_to_product_data(id,color,category,price,rating)
    print(f'ID: {id}'
          f'\nRating: {rating}'
          f'\nReturnrate: {returnrate}'
          f'\nColor: {color}'
          f'\nPrice: {price}'
          f'\nLocation: {location}'
          f'\nCategory: {category}'
          f'\nSales: {sales}')
