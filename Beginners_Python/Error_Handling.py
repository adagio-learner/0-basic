#Error handling

while True:
    try:
        age = int(input("what is your age?"))
        10/age
        print(age)
        raise ValueError("hey cut it out")
    # except ValueError:                         comment out
    #     print("please enter a number")         for raise
    #     continue                               function.
    except ZeroDivisionError as err:
        print("exception type : ",type(err).__name__)
        print(err)
        print("please enter age higher than 00")
    else:
        print("thank you")
        break
    finally:
        print("ok, i am finally done") #finally: runs regardless of anything.
        # use to have a record that someone try to break the program.
        # or user try to login 10 times.
    print("can you hear me?")