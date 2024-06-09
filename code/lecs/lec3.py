# while True:
#     try:
#         x = int(input("what is x? "))
#     except ValueError:
#         print("x is not an integer")
#     else:
#         break

# print(f"x is {x}")

# def main():
#     x = get_in()
#     print(f"x is {x}")

# def get_in():
#     while True:
#         try:
#             x = int(input("what is x? "))
#             # break
#         except ValueError:
#             print("x is not an integer")
#         else:
#             break
#     return x

# main()

def main():
    x = get_in()
    print(f"x is {x}")


def get_in():
    while True:
        try:
            x = int(input("what is x? "))
            return x
        except ValueError:
            pass
main()
