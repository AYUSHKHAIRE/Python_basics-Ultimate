def func1():
  try:
    l = [1, 5, 6, 7]
    i = int(input("Enter the index: "))
    print(l[i])
    return 1
  except:
    print("error occurred")
    return 0

  finally: # hona hai to hona hai
    print("I am always executed")
  # print("I am always executed")


x = func1()
print(x)
