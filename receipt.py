import csv

PRODUCT_NUMBER = 0
ITEM_NAME = 1
RETAIL_PRICE = 2

def main():
    products = read_products('products.csv')
    print('Products')
    print(products)
    print('')
    print('Requested Items')
    request('request.csv', products)


def read_products(file_name):
    products_dict = {}
    with open(file_name, 'rt') as products:
        csv_products = csv.reader(products)
        next(csv_products)
        for row in csv_products:
            key = row[PRODUCT_NUMBER]
            name = row[ITEM_NAME]
            retail_price = float(row[RETAIL_PRICE])
            products_dict[key] = name, retail_price
    return products_dict

def request(shopping_list_file, products_dict):
    with open(shopping_list_file, 'rt') as shopping_list:
        csv_shopping_list = csv.reader(shopping_list)
        #print(csv_shopping_list)
        next(csv_shopping_list)
        for row in csv_shopping_list:
            item_key = row[0]
            item = products_dict[item_key]
            # separated_item_and_price = item[]
            item_name = item[0]
            item_price = item[1]
            requested_item_quantity = row[1]
            print(f'{item_name}: {requested_item_quantity} @ {item_price}')

if __name__ == main():
    main()