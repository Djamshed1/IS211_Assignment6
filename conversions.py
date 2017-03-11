#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Week 6 Conversion.py"""

import decimal

def convertCelsiusToKelvin(celcius):
    """Takes in a float representing a Celsius measurement, and returns that 
        temperature converted into Kelvins.
        
    Args:
        Celcius(float): Converts Celsius to Kelvin
        
    Returns:
        Conversion
        
    Examples:
        >>> convertCelsiusToKelvin('300.00')
        573.15
    """
    conrgn = decimal.Decimal(celcius) + decimal.Decimal('273.15')
    return round(conrgn, 3)

#---------------------------------------------------------------------------------

def convertCelsiusToFahrenheit(celcius):
    """Takes in a float representing a Celsius measurement, and returns 
        that temperature converted into Fahrenheit.
        
    Args:
        Celcius(float): Converts Celsius to Fahrenheit.
        
    Returns:
        Conversion
        
    Examples:
        >>> convertCelsiusToFahrenheit('300.00')
        Decimal('572.00')
    """
    conrgn = (((decimal.Decimal(celcius)* 9) / 5) + 32)
    return conrgn

#---------------------------------------------------------------------------------

def convertFahrenheitToCelsius(fahrenheit):
    """Takes in a float representing a Fahrenheit measurement, and returns 
        that temperature converted into Celsius.
        
    Args:
        Fahrenheit(float): Converts Fahrenheit to Celcius.
        
    Returns:
        Conversion
        
    Examples:
        >>> convertFahrenheitToCelsius('572.00')
        300.0
    """
    conrgn = ((decimal.Decimal(fahrenheit) - 32) * 5) / 9
    return round(conrgn, 3)

#---------------------------------------------------------------------------------

def convertFahrenheitToKelvin(fahrenheit):
    """Takes in a float representing a Fahrenheit measurement, and returns 
        that temperature converted into Kelvin.
        
    Args:
        Fahrenheit(float): Converts Fahrenheit to Kelvin.
        
    Returns:
        Conversion
        
    Examples:
        >>> convertFahrenheitToKelvin('572.00')
        573.15
    """
    conrgn = ((decimal.Decimal(fahrenheit) - 32) * 5) / 9
    conrgn += decimal.Decimal(273.15)
    return round(conrgn, 3)

#---------------------------------------------------------------------------------

def convertKelvinToFahrenheit(kelvin):
    """Takes in a float representing a Kelvin measurement, and returns 
        that temperature converted into Fahrenheit.
        
    Args:
        Kelvin(float): Converts Kelvin to Fahrenheit.
        
    Returns:
        Conversion
        
    Examples:
        >>> convertKelvinToFahrenheit('573.15')
        572.0
    """
    conrgn = (((decimal.Decimal(kelvin) - decimal.Decimal('273.15')) / 5) * 9) + 32
    return round(conrgn, 3)

#---------------------------------------------------------------------------------

def convertKelvinToCelsius(kelvin):
    """Takes in a float representing a Kelvin measurement, and returns 
        that temperature converted into Celsius.
        
    Args:
        Kelvin(float): Converts Kelvin to Celsius.
        
    Returns:
        Conversion
        
    Examples:
        >>> convertKelvinToCelsius('573.15')
        300.0
    """
    conrgn = decimal.Decimal(kelvin) - decimal.Decimal('273.15')
    return round(conrgn, 3)
