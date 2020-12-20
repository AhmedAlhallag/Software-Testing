def fizz_buzz(param):
    if isMultiple(param, 3):
        if isMultiple(param, 5):
            return "FizzBuzz"
        return "Fizz"
    elif isMultiple(param, 5):
        return "Buzz"

    return str(param)


def isMultiple(param, mod):
    return (param % mod) == 0
