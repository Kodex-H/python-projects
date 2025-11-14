while True:
    print('==========Welcome to Nelly Cocoa Farms==========')
    start = input('would you like to continue (y/n): ')
    if start == 'n':
        print('thank you for your time ')
        break
    elif start != 'y' and start != 'n':
        print('Invalid input')
        continue
    bags = int(input("how many bags did you get this time: "))
    total = bags * 850
    print(f'\nthe income from {bags} bags is {total}.00GHS')
    if bags >= 100:
        total += 2000
        print(f'the total income  with your bonus is {total}.')
    else:
        print(f'the total income with your bonus is {total}.\n\n')