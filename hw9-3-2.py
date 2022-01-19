#author: DMH 1/18/22

try:
    print('Enter the net sales for')

    previous = float(input('- Prior period:'))
    current = float(input('- Current period:'))

    change = (current - previous) * 100 / previous

    if change > 0:
        result = f'Sales increase {abs(change)}%'
    else:
        result = f'Sales decrease {abs(change)}%'

    print(result)
except ValueError:
    print("Please only input numbers into the console.")
except ZeroDivisionError:
    print("Please do not input a 0 as the first number.")
finally:
    print("Thank you for using the program!")