def fizzBuzz(n):
    for i in range(1, n+1):
        if i%3==0 and i%5==0:
            print("Fizzbuzz")
        elif i%3==0:
            print("Fizz")
        elif i%5==0:
            print("Buzz")
        else:
            print(i)

fizzBuzz(15)


def Reverse(lst):
    new_lst = lst[::-1]
    return new_lst
      
print(Reverse([10, 11, 12, 13, 14, 15]))
