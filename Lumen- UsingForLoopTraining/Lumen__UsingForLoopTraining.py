# The For Loop

print("Choose an option")
print("1 Numbers 1 to 10, 2- Numbers 1 to 50, 3- Numbers 1 to 100")
choose = int(input())

match choose:
    case 1:
        for i in range(1,10):
            print(i)
    case 2:
        for i in range(1,50):
            print(i)
    case 3:
        for i in range(1,100):
            print(i)

    case _:
        print("invalid option")