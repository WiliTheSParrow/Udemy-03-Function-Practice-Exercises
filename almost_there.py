#ALMOST THERE: Given an integer n, return True if n is within 10 of either 100 or 200
#almost_there(90) --> True
#almost_there(104) --> True
#almost_there(150) --> False
#almost_there(209) --> True
#NOTE: abs(num) returns the absolute value of a number

turn True
def almost_there(n):
    if n in range(90,111):
        return True
    elif n in range(190,211):
        return True
    else:
        return False
# Check
almost_there(104)

# Check
almost_there(150)

# Check
almost_there(209)
