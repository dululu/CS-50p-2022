def main():
    print_size(2)

def print_size(size):
    for i in range(size):
        for j in range(size):
            print("#",end="")
        print()

main()