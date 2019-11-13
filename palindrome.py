palindrome = input('Input a string:')

if palindrome == palindrome[::-1]:
    print(f'string is a palindrome:{palindrome}')

else:
    print(f'string is a not a palindrome:{palindrome}')

