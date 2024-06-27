def get_city_name(city, country, population=''):
    """Строит отформатированное полное имя."""
    if population:
        msg = city + ', ' + country + ' population= ' + population
    else:
        msg = city + ', ' + country
    return msg.title()