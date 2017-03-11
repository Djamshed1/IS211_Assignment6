#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Week 6 Conversion Refactored.py"""

def conversion(fromUnit, toUnit, value):

#------------------------Temperature-----------------------
    temperature = ["celsius", "fahrenheit", "kelvin"]
    convertSomethingToCelsius = ["value", "(value-32)*5/9", "value-273.15"]
    convertCelsiusToSomething = ["value", "(value*9/5)+32", "value+273.15"]

    if fromUnit.lower() in temperature:
        if not(toUnit.lower() in temperature):
            raise ConversionNotPossible
        else:
            try:
                value = float(value)
            except:
                raise ConversionNotPossible
            else:
                value = eval(convertSomethingToCelsius[temperature.index(fromUnit.lower())])
                value = eval(convertCelsiusToSomething[temperature.index(toUnit.lower())])
                return round(value, 2)
            
#------------------------Distance---------------------------
    distance = ["meters", "miles", "yards"]
    convertSomethingToMeter = ["value", "value/0.00062137", "value/1.0936"]
    convertMeterToSomething = ["value", "value*0.00062137", "value*1.0936"]

    if fromUnit.lower() in distance:
        if not(toUnit.lower() in distance):
            raise ConversionNotPossible
        else:
            try:
                value = float(value)
            except:
                raise ConversionNotPossible
            else:
                value = eval(convertSomethingToMeter[distance.index(fromUnit.lower())])
                value = eval(convertMeterToSomething[distance.index(toUnit.lower())])
                return round(value, 2)
    else:
        raise ConversionNotPossible

class ConversionNotPossible(Exception): pass

