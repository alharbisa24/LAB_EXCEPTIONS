

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9


message = 'Enter a temperature and its unit (e.g., "25 C" or "77 F"):'

msg = input(message)
while msg != 'exit':
    try:
        msg = msg.split()
        temperature = float(msg[0])
        unit = msg[1].upper()
        if unit == 'C':
            converted = celsius_to_fahrenheit(temperature)
            print(f"Temperature in Fahrenheit: {converted:.2f} F")
        elif unit == 'F':
            converted = fahrenheit_to_celsius(temperature)
            print(f"Temperature in Celsius: {converted:.2f} C")
        else:
            raise TypeError("Invalid unit. Please use 'C' for Celsius or 'F' for Fahrenheit.")
        
    except ValueError as e:
        print(f"Invalid temprature. Please enter valid temprature. {e}")
    except TypeError as e:
        print(e)

    msg = input(message)


