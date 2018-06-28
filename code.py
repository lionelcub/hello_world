import random

if __name__ == '__main__':
    print('The dice is {}'.format(random.randint(1,6)))
    print('It plays the dice!')

    print("Let's play a coin toss!")

    for i in range(1,4):
        var = random.randint(0,1)
        if var == 1:
            print("It's head!")
        if var == 0:
            print("It's tail!")
