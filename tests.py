#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Week 6 Test.py"""

import decimal
import conversions as c

print "Testing of convertCelsiusToKelvin()"
Test = [(300.00, 573.15), (430.00, 703.15), (260.00, 533.15), (320.00, 593.16), (140.00, 413.16)]
for inputt, output in Test:
    conversion = c.convertCelsiusToKelvin(inputt)
    if output==conversion:
        print "Input: %.2f | Expected result: %.2f | Result after conversion: %.2f | Passed"%(inputt, output, conversion)
    else:
        print "Input: %.2f | Expected result: %.2f | Result after conversion: %.2f | Failed"%(inputt, output, conversion)
print ""

#-----------------------------------------------------------------------------------------------------------------------

print "Testing of convertCelsiusToFahrenheit()"
Test = [(0.00, 32.00), (130.00, 266.00), (230.00, 446.00), (350.00, 662.01), (440.00, 824.01)]
for inputt, output in Test:
    conversion = c.convertCelsiusToFahrenheit(inputt)
    if output==conversion:
        print "Input: %.2f | Expected result: %.2f | Result after conversion: %.2f | Passed"%(inputt, output, conversion)
    else:
        print "Input: %.2f | Expected result: %.2f | Result after conversion: %.2f | Failed"%(inputt, output, conversion)
print ""

#-----------------------------------------------------------------------------------------------------------------------

print "Testing of convertFahrenheitToCelsius()"
Test = [(32.00, 0.00), (266.00, 130.00), (446.00, 230.00), (662.00, 350.00), (824.00, 440.00), (932.00, 500.00)]
for inputt, output in Test:
    conversion = c.convertFahrenheitToCelsius(inputt)
    if output==conversion:
        print "Input: %.2f | Expected result: %.2f | Result after conversion: %.2f | Passed"%(inputt, output, conversion)
    else:
        print "Input: %.2f | Expected result: %.2f | Result after conversion: %.2f | Failed"%(inputt, output, conversion)
print ""

#-----------------------------------------------------------------------------------------------------------------------

print "Testing of convertFahrenheitToKelvin()"

Test = [(230.00, 383.15), (248.00, 393.15), (266.00, 403.15), (302.00, 423.15), (320.00, 433.15), (932.00, 773.15)]
for inputt, output in Test:
    conversion = c.convertFahrenheitToKelvin(inputt)
    if output==conversion:
        print "Input: %.2f | Expected result: %.2f | Result after conversion: %.2f | Passed"%(inputt, output, conversion)
    else:
        print "Input: %.2f | Expected result: %.2f | Result after conversion: %.2f | Failed"%(inputt, output, conversion)
print ""

#-----------------------------------------------------------------------------------------------------------------------

print "Testing of convertKelvinToFahrenheit()"

Test = [(383.15, 230.00), (393.15, 248.00), (403.15, 266.00), (423.15, 302.00), (433.15, 320.00), (773.15, 932.00)]
for inputt, output in Test:
    conversion = c.convertKelvinToFahrenheit(inputt)
    if output==conversion:
        print "Input: %.2f | Expected result: %.2f | Result after conversion: %.2f | Passed"%(inputt, output, conversion)
    else:
        print "Input: %.2f | Expected result: %.2f | Result after conversion: %.2f | Failed"%(inputt, output, conversion)

print ""

#-----------------------------------------------------------------------------------------------------------------------

print "Testing of convertKelvinToCelsius()"

Test = [(743.15, 470.00), (713.15, 440.00), (683.15, 410.00), (643.15, 370.00), (593.15, 320.00), (773.15, 500.00)]
for inputt, output in Test:
    conversion = c.convertKelvinToCelsius(inputt)
    if output==conversion:
        print "Input: %.2f | Expected result: %.2f | Result after conversion: %.2f | Passed"%(inputt, output, conversion)
    else:
        print "Input: %.2f | Expected result: %.2f | Result after conversion: %.2f | Failed"%(inputt, output, conversion)
print ""
