# Example 3
# def sumNumber ( x , y ):
#     print(x+y)

# sumNumber(1,3)
##__________________________________________________##

#Example 4

# def find_largest_number (num1 , num2):
#     if num1 > num2:
#         print(num1)
#     else:
#         print(num2)

# find_largest_number(75,85)

##__________________________________________________##

#Example 5

# def average (num1 ,num2 ,num3 ):
#     print (int((num1+num2+num3)/3))

# average(1,1,1)

##__________________________________________________##

#Example 6 

# def square ():
#     side = int(input('Enter the side size : '))
#     Environment = side * 4;
#     area = side * side ;
#     print("Environment: ",Environment,'area: ',area)

# square()

##__________________________________________________##

#Example 7

# pi = 3.14
# r = 3
# areaofcircle  = int(pi*(r**2)) 

# areaofsquare = int(((r*2)*(r*2))/2) 

# print(areaofcircle - areaofsquare)

##__________________________________________________##

#Example 8

# def print_digit_count():
#     number = int(input('Enter your namber : '))
#     count = 0
#     while number > 0:
#         number //= 10 
#         count += 1
#     print(count)

# print_digit_count()

##__________________________________________________##

#Example 9

def calculate_final_price(cost_price, profit_percentage):
    if profit_percentage > 1:
        profit_percentage /= 100

    final_price = cost_price * (1 + profit_percentage)
    return int(final_price)

print(calculate_final_price(100,20))
