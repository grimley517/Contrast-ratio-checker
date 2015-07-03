#! /usr/bin/env python3.4

import math

def componentise(hexValue):
    '''Take an input hex string represtentation of a colour and splits it into 
    its component hex values.  Returning a list of strings.'''
    hexValue = str(hexValue)
    if hexValue[0]=="#":
        hexValue = hexValue[1:]
    size = len(hexValue)
    if size%3 !=0:
        raise ValueError('hex value length should be divisible by 3')
    size = int(size / 3)
    if size > 2:
        raise ValueError('hex value should be 6 or 3 characters long {0} is invalid'.format(hexValue))
    if size <1:
        raise ValueError('hex value cannot be empty')
    if size == 2:
        answer = [hexValue[0:2], hexValue[2: 4], hexValue[4:6]]
    if size == 1:
        answer = [hexValue[0]*2, hexValue[1]*2, hexValue[2]*2]
    return (answer)

def hexVal(component):
    value = int(component, 16)
    return (value)
    
def unitise(component):
    '''Converts the component value to a float represtening the colours relative luninance
    unitise(255) == 1
    unitise(0) == 0
    '''
    component = float(component)
    return (component / 255)

def weight(component):
    '''Weights each Component and returns their lumanence value as a float
    Literal vlues in this Fucntion from WCAG 2.0 specification'''
    if component <= 0.03928:
        answer = component / 12.92
    else:
        answer = component + 0.055
        answer = answer / 1.055
        answer = answer ** 2.4
    return (answer)
        
    
    
def luminanceComponent(component):
    '''from an entered string representing a hex colour compont 
    the return value is a float 
    '''
    component = hexVal(component)
    component = unitise(component)
    component = weight(component) 
    return (component)
    

def relLuminance(hexValue):
    hexValue = str(hexValue)
    colour = componentise(hexValue)
    for i in range(len(colour)):
        colour[i] = luminanceComponent(colour[i])
    luminance = 0.2126 * colour[0] 
    luminance += 0.7152 * colour[1]
    luminance += 0.0722 *colour[2]
    return (luminance)
    
def ratio(colour1, colour2):
    '''from two colours entered as their hex value string representations, 
    calculates the contrast ratio'''
    c1 = relLuminance(colour1) + 0.05
    c2 = relLuminance(colour2) + 0.05
    answer = float(c1) / float(c2)
    if answer <1:
        answer = 1.0 / float(answer)
    return (answer)
    
    
if __name__ == "__main__":
    print ('''Contrast ratio calculator, \nWritten By B Jones''')
    colourText = input("Please enter the Hexadecimal code for the text colour you are intending to use. ")
    colourBG = input("And please enter the Code for the fine colour that you wish for your background? ")
    result = ratio(colourText, colourBG)
    print ("That combination has a colour ratio of {0:.3f}.\n".format(result))
    if result >= 7:
        print ("According to the Rules, Thats an accessible contrast")
    elif result >= 4.5:
        print ("thats an OK Contrast Ratio for levvel AA compliance, but not for AAA Compliance")
    elif result >= 3:
        print ("thats an OK Contrast Ratio for large text (over 18 pt, or 14 pt Bold)")
    else:
        print ("You need more contrast my friend!")
