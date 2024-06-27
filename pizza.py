pizzas = ['пипперони', 'мясная', 'маргарита', 'цезарь']
#for pizza in pizzas:
#    print ("Я люблю " + pizza + " пиццу")
#print("\nЯ очень люблю пиццу")

friend_pizzas = pizzas[:]

pizzas.append("123")
friend_pizzas.append("333")

print("Моя")
for pizza in pizzas:
    print(pizza)
print("Не моя")
for pizza in friend_pizzas:
    print(pizza)