age = 13
if age < 2:
    messege = "младенец"
elif age >=2 and age <4:
    messege = "малыш"
elif age >=4 and age <13:
    messege = "ребенок"
elif age >=13 and age <20:
    messege = "подросток"
elif age >=20 and age <65:
    messege = "взрослый"    
elif age >=65:
    messege = "пожилой человек"  
print(messege)