command=""
start=False
while True:
    command=input("> ").lower()
    if command=='start':
        if start:
            print('already started')
        else:
            start=True
            print('car start..')
    elif command=='quit':
        break
    elif command=='help':
        print('''
> start ---- to start the game
> quit  ---- to quit the game
> help  ---- to help    
    ''')
    elif command=='stop':
        if not start:
            print('already stopped!!')
        else:
            start=False
            print('car stopped..')