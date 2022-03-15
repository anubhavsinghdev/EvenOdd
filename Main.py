
print("This program calculates if a number is even or odd")

def even_or_odd(num):

    #actual calculations
    if (num % 2) == 0:
        print("{0} is Even".format(num))
    else:
        print("{0} is Odd".format(num))

def main():
    #ask for input number
    user_inp = input("Please enter a number or {stop} to stop: ")

    #adapt with ands for stupid users
    if user_inp != "stop" and user_inp != "Stop" and user_inp != "{stop}":

        #cast to int
        input_num = int(user_inp)

        #run actual func
        even_or_odd(input_num)

        #rerun func
        main()

main()
