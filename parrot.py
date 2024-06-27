prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "
#message = ""
#while message != 'выход':
#    message = input(prompt)
#    if message != 'выход':
#        print(message)
active = True
while active:
    message = input(prompt)
    if message == 'выход':
        active = False
    else:
        print(message)