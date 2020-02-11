def myFunction(num): #definition. num is a formal parameter.
# ''' Do some operations to demo docstring
# myFunction returns (num * 3)^(num/2)'''
    tripled = num * 3 #12
    halved = num/2  #2
    answer = tripled ** halved #12**2 = 144
    return answer

def main():
    result_1 = myFuction(4) #calling. sending an argument (actual parameter)
    print("4 becomes" + str(result_2) )

    some_value = 5.3
    result_2 = myFunction(some_value)
    print("some_value becomes" + str(result_2))

main()

 