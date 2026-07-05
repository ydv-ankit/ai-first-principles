def or_gate(x1, x2):
    return x1 | x2

def and_gate(x1, x2):
    return x1 & x2

def nand_gate(x1, x2):
    a = and_gate(x1, x2)
    if a == 0:
        return 1
    else:
        return 0

def xor(x1, x2):
    a = or_gate(x1, x2)
    b = nand_gate(x1, x2)
    return and_gate(a, b)

if __name__ == "__main__":
    print(xor(0,0))
    print(xor(1,0))
    print(xor(0,1))
    print(xor(1,1))