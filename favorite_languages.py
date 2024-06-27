#favorite_languages = {
#'jen': 'python',
#'sarah': 'c',
#'edward': 'ruby',
#'phil': 'python',
#}

#new_users = ['ed', 'john', 'jen']
#for user in new_users:
#    if user not in favorite_languages.keys():
#        print (user.title() + " не прошли опрос ")
#    else:
#        for name, language in favorite_languages.items():
#            print(name.title() + " прошли опрос ")

favorite_languages = {
    'jen': ['python', 'ruby'],
    'sarah': ['c'],
    'edward': ['ruby', 'go'],
    'phil': ['python', 'haskell'],
    }
for name, languages in favorite_languages.items():
    if len(languages) > 1:
        print("\n" + name.title() + "'s favorite languages are:")
    else:
        print("\n" + name.title() + "'s favorite language are:") 
    for language in languages:
        print("\t" + language.title())