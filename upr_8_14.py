def make_car(brend,model,**car_info):
    profile = {}
    profile['brend'] = brend
    profile['model'] = model
    for key, value in car_info.items():
        profile[key] = value
    return profile

car = make_car('subaru', 'outback', color='blue', tow_package=True)
print(car)