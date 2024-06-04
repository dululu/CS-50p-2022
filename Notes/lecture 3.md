Exceptions

## syntaxError
	语法错误
- handle syntaxError
- catch error
### NameError: name 'x' is not defined
```python
try:

    x = int(input("what is x? "))

except ValueError:

    print("x is not an integer")

print(f"x is {x}")
```
原因：如果输入的是字符串`cat`,首先`int`无法转换，其次输出`x is not an integer`,
但是`printf`输出不了`x`

### break
```python
def main():
    x = get_in()
    print(f"x is {x}")
  
def get_in():
    while True:
        try:
            x = int(input("what is x? "))
            # break
        except ValueError:
            print("x is not an integer")
        else:
            break   # return x
    return x

main() 
```
`break`跳出循环
`return`不仅会跳出循环，还会返回一个值。两件事
#### 还可以更简化
```python
def main():
    x = get_in()
    print(f"x is {x}")
  
def get_in():
    while True:
        try:
            x = int(input("what is x? "))
			return x
        except ValueError:
            print("x is not an integer")
main() 
```

### pass
忽略,处理错误的机制
```python
def main():
    x = get_in()
    print(f"x is {x}")
  
def get_in(promt):
    while True:
        try:
	            x = int(input(promtive))
		        return x  
        except ValueError:
			 pass
main() 
```

使用`promotive`