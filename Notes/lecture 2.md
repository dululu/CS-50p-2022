# loops
### `while`
循环
### `for`
迭代
#### `range(100)`
将单个变量命名为下划线`_`  #Pythonic
```python
for _ in range(20):

    print("meow")
```

### 调用函数
```python
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
```

## `List
### `len`
length
```python
range(len(students))
for _ in [0,3,4]
```

### `dict`
key:value
#### 2D
![2D|300](Pasted%20image%2020240601024756.png)
```python
students = {"Hermione":"a","Harry":"b","Ron":"c"}

for s in students:

    print(s,students[s],sep=", ")
```
#### 3D
![|300](Pasted%20image%2020240601025027.png)
```python
students = [

    {"name":"Hermione","house":"Gryffindor","pat":"Otter"},

    {"name":"Harry","house":"Gryffindor","pat":None},

]
for student in students:

    print(student["name"],student["house"],student["pat"],sep=", ")
```
#### `None`
