import time
import math

def get_digits():
    digits_selection = input("Enter number of digits: ")
    valid = False

    while not valid:
        if digits_selection.isnumeric():
            valid = True
        else:
            digits_selection = input("Enter a valid number of digits: ")

    return digits_selection

def get_algorithm():
    print("1. Taylor Series\n", "2. Taylor Series (Compressed 6x)\n", "3. Binary Splitting", sep = "")
    algorithm_selection = input("Enter selection: ")
    valid = False

    while not valid:
        if algorithm_selection == "1" or algorithm_selection == "2" or algorithm_selection == "3":
            valid = True
        else:
            algorithm_selection = input("Enter a valid selection: ")

    return algorithm_selection

def get_output():
    print("1. Print on screen\n", "2. Output to file", sep = "")
    output_selection = input("Enter selection: ")
    valid = False

    while not valid:
        if output_selection == "1" or output_selection == "2":
            valid = True
        else:
            output_selection = input("Enter a valid selection: ")

    return output_selection

def taylor(digits):
    term = 10 ** (int(digits) + 10)
    k = 2
    e = k * term

    while term:
        term //= k
        e += term
        k += 1

    return e

def taylor_compressed(no_digits):
    digits = 10 ** (int(no_digits) + 35)
    e = 163 * digits // 60
    k = 0
    term = e

    while term:
        a = (1296*k**4+7560*k**3+16524*k**2+16056*k+5861) * (6*k+11) + 1 
        b = 144 * (k+1) * (6*k+7) * (3*k+4) * (2*k+3) * (3*k+5) * (6*k+11) * (3888*k**5+10368*k**4+10800*k**3+5562*k**2+1455*k+163)   
        term = term // b * a
        e += term
        k += 1

    return e

def get_estimate(order):
    L = math.log(order) - math.log(math.sqrt(math.pi * 2))
    x = L / math.e
    L1 = math.log(x)
    L2 = math.log(math.log(x))
    W = L1 - L2 + L2/L1 + L2*(L2-2)/(2*L1**2) + L2*(6-9*L2+2*L2**2)/(6*L1**3) + L2*(36*L2-22*L2**2+3*L2**3-12)/(12*L1**4)
    estimate = math.floor(L / W + 0.5)

    return estimate

def binary_splitting(no_digits):
    order = 10 ** int(no_digits)
    terms = get_estimate(order)
    factorial = math.factorial(terms)
    total = 1

    for i in range(terms - 1, 1, -1):
        total += terms
        terms *= i

    e = total * order * 10 ** 5 // factorial

    return e

def output(e, algorithm, output_method, no_digits):
    e = str(e)

    if algorithm == "1":
        e = e[0] + "." + e[1:-11]
    elif algorithm == "2":
        e = e[0] + "." + e[1:-36]
    else:
        e = "2." + e[:-6]

    if output_method == "1":
        print(e)
    elif output_method == "2":
        filename = no_digits + " digits of e.txt"
        with open(filename, "w") as file:
            file.write(e)

def main():
    no_digits = get_digits()
    algorithm = get_algorithm()
    output_method = get_output()

    start = time.time()

    if algorithm == "1":
        e = taylor(no_digits)
    elif algorithm == "2":
        e = taylor_compressed(no_digits)
    else:
        e = binary_splitting(no_digits)

    finish = time.time()

    output(e, algorithm, output_method, no_digits)

    end = time.time()
    print("Computation time: ", finish - start, "s", sep = "")
    print("Wall to wall time: ", end - start, "s", sep = "")

if __name__ == "__main__":
    main()