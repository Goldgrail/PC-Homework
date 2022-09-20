
cook_book = {}
with open('recipies.txt', 'r', encoding='utf8') as recipies:
    for line in recipies:
        dish_name = line.strip()
        cook_b = []
        ingredient_count = recipies.readline()
        for i in range(int(ingredient_count)):
            ingr = (recipies.readline()).strip()
            ingredient, quantity, measure = ingr.split(" | ")
            recip = {'ingredient_name': ingredient,'quantity': quantity, 'measure': measure}
            cook_b.append(recip)
        cook_book[dish_name] = cook_b
        recipies.readline()
print(cook_book)

def get_cook_book(file):
    cook_book = {}
    with open(file, 'r', encoding='utf8') as recipies:
        for line in recipies:
            dish_name = line.strip()
            cook_b = []
            ingredient_count = recipies.readline()
            for i in range(int(ingredient_count)):
                ingr = (recipies.readline()).strip()
                ingredient, quantity, measure = ingr.split(" | ")
                recip = {'ingredient_name': ingredient,'quantity': quantity, 'measure': measure}
                cook_b.append(recip)
            cook_book[dish_name] = cook_b
            recipies.readline()
    return cook_book

def get_shop_list_by_dishes(dishes, person_count):
    cook_book = get_cook_book('recipies.txt')
    shop = {}
    for k, v in cook_book.items():
        for dish in dishes:
            if k == dish:
                for vv in v:
                    if vv['ingredient_name'] in shop:
                        shop[vv['ingredient_name']]["quantity"] += (int(vv['quantity']) * person_count)
                    else:
                        shop[vv['ingredient_name']] = {'measure': vv['measure'],
                                                       'quantity': (int(vv['quantity'])* person_count)}
    print(shop)

get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)

