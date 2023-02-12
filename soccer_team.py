d = {}
for i in range(5):
    print("Enter player %s's jersey number:" %str(i+1))
    jn = int(input())
    print("Enter player %s's rating:\n" %str(i+1))
    pr = int(input())
    if jn not in d:
        d[jn] = pr
print('ROSTER')
for x,y in sorted(d.items()):
    print("Jersey number: ", x, ", Rating: ", y, sep='')
print()

while True:
    print('MENU')
    print('a - Add player')
    print('d - Remove player')
    print('u - Update player rating')
    print('r - Output players above a rating')
    print('o - Output roster')
    print('q - Quit\n')
    print('Choose an option:')
    usropt = input()

    if usropt == 'o':
        print('ROSTER')
        for x,y in sorted(d.items()):
            print("Jersey number: ", x, ", Rating: ", y, sep='')
        print()
    elif usropt == 'a':
        print("Enter a new player's jersey number:")
        jn = int(input())
        print("Enter the player's rating:")
        pr = int(input())
        if jn not in d:
            d[jn] = pr
        else:
            print("This player's name is already in the roster.")
    elif usropt == 'd':
        print("Enter a jersey number:")
        jn = int(input())
        if jn in d:
            del d[jn]
        else:
            print("This player's name is not in the roster.")
    elif usropt == 'u':
        print("Enter a jersey number:")
        jn = int(input())
        print("Enter a new rating for player:")
        pr = int(input())
        if jn in d:
            d[jn] = pr
        else:
            print("This player's name is not in the roster.")
    elif usropt == 'r':
        print("Enter a rating:\n")
        pr = int(input())
        print("ABOVE", pr)
        for x,y in sorted(d.items()):
            if y>pr:
                print("Jersey number: ", x, ", Rating: ", y, sep='')
        print()
    elif usropt == 'q':
        break
