a = input("enter an integer between 5 to 9 or 'quit': ")
if a == "quit":
    print("exit")
else:
    try:
        a = int(a)  # Convert the input to an integer
        if 5 <= a <= 9:
            print('good boy/girl/men/women/uncle/aunty')
        else:
            raise ValueError("Input should be an integer between 5 and 9")
    except ValueError:
        print('bhai ne bola karne ka TO KARNE KA')
        raise ValueError("Input should be an integer or 'quit'")
