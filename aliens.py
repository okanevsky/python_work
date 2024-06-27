aliens = []


for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)

for alian in aliens[0:3]:
    if alian['color'] == 'green':
        alian['color'] = 'yellow'
        alian['points'] = 10
        alian['speed'] = 'medium'

for alian in aliens[:5]:
    print(alian)
print ("......")
print("Общее количество - " + str(len(aliens)))