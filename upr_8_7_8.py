def make_album(name, album, track=''):
    music = {'name':name, 'album':album}
    if track:
        music['track'] = track
    return music

while True:
    print('\nВведите информацию')
    print('Для выхода введите "q"')

    name_musicant = input('Исполнитель: ')
    if name_musicant == 'q':
        break
    name_album = input('Название альбома: ')
    if name_album == 'q':
        break
    tracks = input('количество песен: ')
    if tracks == 'q':
        break
    music_info = make_album (name_musicant, name_album, tracks)
    print(music_info)