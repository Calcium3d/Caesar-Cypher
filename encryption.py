import random
import time

choice = input("do you want to encrypt or decrypt?: ")
x = 0
theString = "0"
difference = 0

if choice == "encrypt":
    print("starting encryption")
    time.sleep(5)
    theString = input("Enter the sentence without any spaces: ")
    difference = random.randint(0, 10)

    for i in range(len(theString)):
        i = theString[x]
        if i == 'a':
            alphabet = 1

        if i == 'b':
            alphabet = 2

        if i == 'c':
            alphabet = 3

        if i == 'd':
            alphabet = 4

        if i == 'e':
            alphabet = 5

        if i == 'f':
            alphabet = 6

        if i == 'g':
            alphabet = 7

        if i == 'h':
            alphabet = 8

        if i == 'i':
            alphabet = 9

        if i == 'j':
            alphabet = 10

        if i == 'k':
            alphabet = 11

        if i == 'l':
            alphabet = 12

        if i == 'm':
            alphabet = 13

        if i == 'n':
            alphabet = 14

        if i == 'o':
            alphabet = 15

        if i == 'p':
            alphabet = 16

        if i == 'q':
            alphabet = 17

        if i == 'r':
            alphabet = 18

        if i == 's':
            alphabet = 19

        if i == 't':
            alphabet = 20

        if i == 'u':
            alphabet = 21

        if i == 'v':
            alphabet = 22

        if i == 'w':
            alphabet = 23

        if i == 'x':
            alphabet = 24

        if i == 'y':
            alphabet = 25

        if i == 'z':
            alphabet = 26

        x += 1

        alphabet = int(alphabet) + int(difference)

        if alphabet > 26:
            alphabet = alphabet - 26

        if alphabet == 1:
            result = 'a'

        if alphabet == 2:
            result = 'b'

        if alphabet == 3:
            result = 'c'

        if alphabet == 4:
            result = 'd'

        if alphabet == 5:
            result = 'e'

        if alphabet == 6:
            result = 'f'

        if alphabet == 7:
            result = 'g'

        if alphabet == 8:
            result = 'h'

        if alphabet == 9:
            result = 'i'

        if alphabet == 10:
            result = 'j'

        if alphabet == 11:
            result = 'k'

        if alphabet == 12:
            result = 'l'

        if alphabet == 13:
            result = 'm'

        if alphabet == 14:
            result = 'n'

        if alphabet == 15:
            result = 'o'

        if alphabet == 16:
            result = 'p'

        if alphabet == 17:
            result = 'q'

        if alphabet == 18:
            result = 'r'

        if alphabet == 19:
            result = 's'

        if alphabet == 20:
            result = 't'

        if alphabet == 21:
            result = 'u'

        if alphabet == 22:
            result = 'v'

        if alphabet == 23:
            result = 'w'

        if alphabet == 24:
            result = 'x'

        if alphabet == 25:
            result = 'y'

        if alphabet == 26:
            result = 'z'

        print(result)
    print(difference)

if choice == "decrypt":

    print("Decrypter starting...")
    time.sleep(5)
    theString = input("Enter the sentence without any spaces: ")

    for i in range(len(theString) - 1):
        i = theString[x]
        difference = theString[-1]

        if i == "a":
            alphabet = 1

        if i == "b":
            alphabet = 2

        if i == "c":
            alphabet = 3

        if i == "d":
            alphabet = 4

        if i == "e":
            alphabet = 5

        if i == "f":
            alphabet = 6

        if i == "g":
            alphabet = 7

        if i == "h":
            alphabet = 8

        if i == "i":
            alphabet = 9

        if i == "j":
            alphabet = 10

        if i == "k":
            alphabet = 11

        if i == "l":
            alphabet = 12

        if i == "m":
            alphabet = 13

        if i == "n":
            alphabet = 14

        if i == "o":
            alphabet = 15

        if i == "p":
            alphabet = 16

        if i == "q":
            alphabet = 17

        if i == "r":
            alphabet = 18

        if i == "s":
            alphabet = 19

        if i == "t":
            alphabet = 20

        if i == "u":
            alphabet = 21

        if i == "v":
            alphabet = 22

        if i == "w":
            alphabet = 23

        if i == "x":
            alphabet = 24

        if i == "y":
            alphabet = 25

        if i == "z":
            alphabet = 26

        x += 1

        alphabet = int(alphabet) - int(difference)

        if alphabet < 0:
            alphabet = alphabet + 26

        if alphabet == 1:
            result = "a"

        if alphabet == 2:
            result = "b"

        if alphabet == 3:
            result = "c"

        if alphabet == 4:
            result = "d"

        if alphabet == 5:
            result = "e"

        if alphabet == 6:
            result = "f"

        if alphabet == 7:
            result = "g"

        if alphabet == 8:
            result = "h"

        if alphabet == 9:
            result = "i"

        if alphabet == 10:
            result = "j"

        if alphabet == 11:
            result = "k"

        if alphabet == 12:
            result = "l"

        if alphabet == 13:
            result = "m"

        if alphabet == 14:
            result = "n"

        if alphabet == 15:
            result = "o"

        if alphabet == 16:
            result = "p"

        if alphabet == 17:
            result = "q"

        if alphabet == 18:
            result = "r"

        if alphabet == 19:
            result = "s"

        if alphabet == 20:
            result = "t"

        if alphabet == 21:
            result = "u"

        if alphabet == 22:
            result = "v"

        if alphabet == 23:
            result = "w"

        if alphabet == 24:
            result = "x"

        if alphabet == 25:
            result = "y"

        if alphabet == 26:
            result = "z"

        print(result)
