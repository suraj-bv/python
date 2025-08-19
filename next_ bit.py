bits = input("Enter bits (e.g. 1011): ")
num = int(bits, 2)        # convert to integer
next_num = num + 1
next_bits = bin(next_num)[2:]  # convert back to binary string
print("Next bit code:", next_bits)