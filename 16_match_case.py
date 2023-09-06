# for edition  > - 3.1.1
# lke switch case in c 
# except python in case break is required 
x= int(input("enter your age\n"))
match x:
    case 1:
        print("you are welcome in kaliyug\n")
    case 11:
        print("you are now a child\n")
    case 111:
        print("OMG ja jake aaram kr\n")
    case _ if x>129:
        print("zoothe haram****")
    case _ :
        print("no criteria for you bro as you are",x )
