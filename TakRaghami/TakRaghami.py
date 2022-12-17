num = int(input())
modulus = 0
while num//10 != 0:
    modulus = (num % 10) + modulus
    num = num//10
    if num < 10:
        modulus=modulus + num
        num = modulus
        modulus = 0
print(num)