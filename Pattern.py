def print_hex_pattern(rows, cols):
    for row in range(rows):
        for part in range(3):
            for col in range(cols):
                if part == 0:
                    print("  __ ", end="")
                elif part == 1:
                    print(" /  \\", end="")
                else:
                    print(" \\__/", end="")
            print()
print("inputs :- 4 7")
print_hex_pattern(4,7)

print("\ninputs :- 3 5")
print_hex_pattern(3,5)
