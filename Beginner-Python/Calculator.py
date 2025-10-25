print('\n\t\t\t\tTHIS IS A CALCULATOR')
print('This calculator accepts two values from you the user and any operation you want to perform\n\n')

# This is to initialize a counter variable for the user allow
# the user perform a calculation multiple times.
query = str(input('Do want to perform a calculation? Y/N: ')).lower()

if query == 'y':
    # I initialized a variable for counting the various operations 
    # performed and 4 others for counting the number of specific 
    # operations carried out
    n_add = -1
    n_diff = -1
    n_product = -1
    n_div = -1
    ops = -1
    
    # The list my results and operations will be stored in
    add_list = []
    diff_list = []
    product_list = []
    div_list = []
    operations = []
        
    while query == 'y':
        num1 = float(input('\nEnter a number: ')) 
        # the newline is to make this line of code begin 2 lines after the 'continue' question
        num2 = float(input('Enter a second number: '))
        op = input('''Which Operation would you like to perform on the two numbers, i.e., +, -, /, *: ''')
        
        # Four conditional statements for performing various operation
        if op == '+':
            ops += 1
            operations.insert(ops, op)
            n_add += 1
            add = num1 + num2
            add_list.insert(n_add, add)
            print(f'Sum of the two numbers, {num1} and {num2}, is = {add}')
            

        elif op == '-':
            ops += 1
            operations.insert(ops, op)
            n_diff +=1
            diff = num1 - num2
            diff_list.insert(n_diff, diff)
            print(f'Difference of the two numbers, {num1} and {num2}, is = {diff}')
            

        elif op == '*':
            ops += 1
            operations.insert(ops, op)
            n_product += 1
            product = num1 * num2
            product_list.insert(n_product, product)
            print(f'Product of the two numbers, {num1} and {num2}, is = {product}')
            

        elif op == '/':
            ops += 1
            operations.insert(ops, op)
            n_div += 1
            div = num1 / num2
            div_list.insert(n_div, div)
            print(f'Divion of the two numbers, {num1} and {num2}, is = {div}')
            

        query = str(input('\n\nDo want to perform another calculation? Y/N: ')).lower()

    # If query eventually becomes 'n', this section of the code 
    # checks if any of the operations were performed and prints the calculations performed
    if ('+' in operations) and (query == 'n'):
        print('\nThe results of the additions you performed are :')
        # A for loop to print the results of all addition operations performed, if any
        for Sum in add_list:
            print(add_list.index(Sum), ".\t",Sum)

    if ('-' in operations) and (query == 'N' or query == 'n'):
        print('\nThe results of the subtractions you performed are :')
        # A for loop to print the results of all subtraction operations performed, if any
        for diff in diff_list:
            print(diff_list.index(diff), ".\t", diff)

    if ('*' in operations) and (query == 'N' or query == 'n'):
        print('\nThe results of the multiplications you performed are :')
        # A for loop to print the results of all subtraction operations performed, if any
        for mul in product_list:
            print(product_list.index(mul), ".\t",  mul)

    if ('/' in operations) and (query == 'N' or query == 'n'):
        print('\nThe results of the divisions you performed are :')
        # A for loop to print the results of all subtraction operations performed, if any
        for div in div_list:
            print(div_list.index(div), ".\t", div)

    print('Thank you for using my calculator.')    

else:
    print('\nOkay, carry on boss, calculator has been terminated')
