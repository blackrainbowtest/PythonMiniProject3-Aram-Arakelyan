import time


# CountDown timer
def getCounterTime():
    while True:
        try:
            userTimer = input('Insert time to countdown (h:m:s)\n>>>  ')
            h, m, s = map(int, userTimer.split(':'))
            m, s = divmod(m * 60 + s, 60)
            h, m = divmod(h * 60 + m, 60)
            return h, m, s
        except ValueError:
            print('Incorrect input, please try again.')


# Second converter
def convertSeconds(hour, minute, second):
    return hour * 3600 + minute * 60 + second


def checkChoose():
    while True:
        userAnswer = input('Do you want countdown again? Y/N\n>>>  ')
        if userAnswer.lower() == 'y':
            return False
        elif userAnswer.lower() == 'n':
            return True
        else:
            print('Incorrect input, please try again. Enter Y for Yes or N for No.')


def timerCountDown(seconds):
    while seconds > 0:
        m, s = divmod(seconds, 60)
        h, m = divmod(m, 60)
        print(f"{h:02d}:{m:02d}:{s:02d}")
        seconds -= 1
        time.sleep(1)
    print("\nTime conunter end!\n")


choose = False

while not choose:
    h, m, s = getCounterTime()
    seconds = convertSeconds(h, m, s)
    timerCountDown(seconds)
    choose = checkChoose()
