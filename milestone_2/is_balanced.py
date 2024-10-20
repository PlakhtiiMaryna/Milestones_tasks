def is_balanced (string):
    count = 0
    print(string)
    for i in string:
        if i == ')':
            count -= 1
            if count < 0:
                return False
        elif i == '(':
            count += 1 
    return count == 0