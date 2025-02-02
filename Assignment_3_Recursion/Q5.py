# Convert decimal to binary using recursion

def decimal_to_binary(n):
    if n==0:
        return 0
    return n%2 + 10*decimal_to_binary(n//2)

print(decimal_to_binary(2))