# i = 3
# while i != 0:
#     print("meow")
#     i = i-1

# for i in [1,4,5,"ty"]:
#     print("meow")

def main():
    number = get_number()
    meow(number)

def get_number():
    while True:
        n = int(input("What's n?"))
        if n > 0:
            break
    return n

def meow(n):
    for _ in range(n):
        print("meow")

main()