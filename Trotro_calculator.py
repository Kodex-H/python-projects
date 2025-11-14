# Trotro fare calculator

boarders = {}
totalF = 0
print("========Fares======= \n Accra ------> Madina = GHS 5\nAccra ------> Kasoa = GHS 10 \n Accra ------> Tema 8GHS")
number_of_boarders = int(input("How many people are boarding the car? "))
for no in range(number_of_boarders):
    drop_off = input("Where would you like to drop off?").lower()
    if drop_off == "madina":
        print("pay the mate GHS 5.00")
        fare = 5
    elif drop_off == "kasoa":
        print("pay the mate GHS 10 ")
        fare = 10
    elif drop_off == "tema":
        print("pay the mate GHS 8")
        fare = 8
    else:
        print("We will not be going there. Sorry ")
        continue
    boarders[f'passenger{no}'] = fare
    totalF += fare

    print("\n===== Summary =====")
    for passenger, fare in boarders.items():
        print(f"{passenger}: GHS {fare}")

    print(f"\nTotal fare collected: GHS {totalF}")
