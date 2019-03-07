cas_number = "7732-18-5"

rho = 1000

mu = 1

Tm = 273.15

Tb = 373.13

w = 0.58


def convert_to_kelvin(temperature, units):
    if type(temperature) == int or type(temperature) == float:

        if units == 'C':
            return temperature + 273.15

        if units == 'F':
            return (temperature + 459.67) * (5.0 / 9.0)

        if units == 'K':
            return temperature

    else:

        return None


def is_a_gas(temperature):
    if temperature >= Tb:
        return True

    else:

        return False


def is_a_liquid(temperature):
    if Tm < temperature < Tb:

        return True

    else:

        return False


def is_a_solid(temperature):
    if temperature <= Tm:

        return True

    else:

        return False


def is_a_number(num_str):
    if type(num_str) != str:
        return None

    if '-' in num_str:

        (left, right) = num_str.split("-")
        if left != "":
            return False

        num_str = right

    if '.' in num_str:

        (left, right) = num_str.split('.')

        if left.isdigit() and right.isdigit():

            return True

        else:

            return False

    else:

        return num_str.isdigit()


if __name__ == "__main__":
    user_units = str(raw_input("Desired units?\n")).upper()  # type: str

    if user_units in ('K', 'C', 'F'):

        units = user_units

        temperature_user = str(raw_input("Desired temperature? "))

        if is_a_number(temperature_user):

            temperature2 = float(temperatureuser)

            kelvin_user = convert_to_kelvin(temperature2, units)

            if is_a_gas(kelvin_user):
                print("Gas")

            elif is_a_liquid(kelvin_user):
                print ("Liquid")

            elif is_a_solid(kelvin_user):
                print ("Solid")

        else:
            print ("Invalid Input - not a number")
    else:
        print("Invalid Input - not a unit")
