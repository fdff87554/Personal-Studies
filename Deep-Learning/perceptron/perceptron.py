def perceptron(x1, x2, w1, w2, b, theta):
    
    return 1 if x1*w1 + x2*w2 + b > theta else 0


def AND(x1, x2):
    w1, w2, b, theta = 0.5, 0.5, -0.7, 0.0
    
    return perceptron(x1, x2, w1, w2, theta)

def NAND(x1, x2):
    w1, w2, b, theta = -0.5, -0.5, 0.7, 0.0
    
    return perceptron(x1, x2, w1, w2, theta)

def OR(x1, x2):
    w1, w2, b, theta = 0.5, 0.5, -0.3, 0.0
    
    return perceptron(x1, x2, w1, w2, theta)

def main():
    print("AND")
    print(f"0 and 0: {AND(0, 0)}")
    print(f"0 and 1: {AND(0, 1)}")
    print(f"1 and 0: {AND(1, 0)}")
    print(f"1 and 1: {AND(1, 1)}")

    print("OR")
    print(f"0 or 0: {OR(0, 0)}")
    print(f"0 or 1: {OR(0, 1)}")
    print(f"1 or 0: {OR(1, 0)}")
    print(f"1 or 1: {OR(1, 1)}")

    print("NAND")
    print(f"0 nand 0: {NAND(0, 0)}")
    print(f"0 nand 1: {NAND(0, 1)}")
    print(f"1 nand 0: {NAND(1, 0)}")
    print(f"1 nand 1: {NAND(1, 1)}")


if __name__ == "__main__":
    main()
