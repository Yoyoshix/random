def is_prime(number):
    if number == 1 or number%2 == 0:
        return 0
    for i in range(3, int(number**0.5)+1, 2):
        if number%i == 0:
            return 0
    return 1

def prime_factor(number):
    prime_list = []
    while number % 2 == 0:
        prime_list.append(2)
        number = number // 2
    div = 3
    while div <= number:
        while number % div == 0:
            prime_list.append(div)
            number = number // div
        div += 2
    return prime_list

def generate(number):
    if abs(number) == 2:
        return "*~1"
    res = ""
    yes = is_prime(abs(number))
    prime_list = prime_factor(abs(number) + yes)
    for prime in prime_list:
        res += generate(prime)
    return "*" + "~("*yes + res[1:] + "*~0"*((prime_list.count(2)+yes)%2) + ")"*yes
    
def make_tilde_expression(number):
    if number == -1:
        return "~0"
    if number in [0,1]:
        return str(number)
    if number == 2:
        return "~1*~0"
    
    res = generate(number)[1:] + "*~0"*(number < 0)
    res = res.replace("*~0*~0", "")
    print(number)
    print(eval(res))
    print(res)
