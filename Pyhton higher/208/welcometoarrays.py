names = ["", "", "", "", ""]
testscores = ["", "", "", "", ""]

for i in range(5):
    names[i] = input("What is your name?: ")
    while True:
        testscores[i] = int(input("What is your result?: "))
        if testscores[i] < 0 or testscores[i] > 100:
            print("that is not a score you cheaty trickster")
            continue
        else:
            break

print(names, testscores)