"""This script includes functions fahr_to_celsius(temp_fahrenheit) and temp_classifier(temp_celsius).

"""

"""Converts fahrenheit values to celsius.
Parameters:
    temp_fahrenheit, fahrenheit value to convert it to celsius

Returns:
    converted_temp = (temp_fahrenheit - 32) / 1.8, temp_fahrenheit converted to celsius float value

Author:
    Henna Ylimaa - 11.2.2022
"""
# function that converts fahrenheits to celsius
# one value in fahrenheit is given to the funtion
def fahr_to_celsius(temp_fahrenheit):
    
    # converts temp_fahrenheit to celsius with math
    converted_temp = (temp_fahrenheit - 32) / 1.8
    
    # converted_temp that have the celsius value is returned
    return converted_temp

"""Classifies given celsius value to one of 4 group

Parameter:
    temp_celsius, celsius value to classify to one of 4 groups introduced below
    
Returns:
    0 = if temp_celsius below -2 degrees Celsius
    1 = if temp_celsius equal or warmer than -2, but less than +2 degrees Celsius
    2 = if temp_celsius equal or warmer than +2, but less than +15 degrees Celsius
    3 = if temp_celsius equal or warmer than +15 degrees Celsius

Author:
    Henna Ylimaa - 11.2.2022
"""
# this function classifies given celsius value to one of 4 group (0, 1, 2, 3)
def temp_classifier(temp_celsius):
    # if value in temp_celsius is less than -2, 0 is returned
    if temp_celsius < -2:
        return 0
    
    #  if upper condition isn't true, code continues to this and if value in temp_celsius is -2 or more but less than 2, 1 is returned
    elif temp_celsius >= -2 and temp_celsius < 2:
        return 1
    
    # if upper condition isn't true, code continues to this and if value in temp_celsius is 2 or more but less than 15, 2 is returned
    elif temp_celsius >=2 and temp_celsius < 15:
        return 2
    # if upper condition isn't true, code continues to this and returns 3 as temp_condition have to be 15 or greater
    else:
        return 3