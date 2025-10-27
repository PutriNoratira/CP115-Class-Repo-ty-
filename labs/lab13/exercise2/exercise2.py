for number in range(100):
    num1 = number % 7
    num2 = number % 13
    if (num1 == 0 and num2 == 0):
        print('Search complete')
        print(found_number)
        print(f'Found first number > 7: {number}')
        break  # Stop searching

