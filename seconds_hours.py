seconds=eval(input("Enter an integer for seconds:"))

hours=seconds//3600

temp=seconds-3600*hours

mins=temp//60

temp=temp-60*mins

print(seconds,"seconds is equal ",hours,"hours",mins,"mins",temp,"seconds")


