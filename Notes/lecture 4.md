## libraries：
- 别人写的代码在自己的库中使用
- modulus  模块

### `import`
- sequence 序列
```cpp
import random
from random import choice  //选择确定的modulus 
```
- `random`
- `shuffle`

### `sys`

```python
import sys
print("hello,my name is",sys.argv[1])
```
- `argv[0]`是啥   是filename

### `packages`
- PyPI
- pypi.org
#### cowsay

### `API`
- Application program interface  应用程序编程接口
- `reuqests`
- JSON
`dumps` 转存储字符串，返回`JSON`值


### `if __name__ = "__main__"`
- 将文件作为`import`导入时，最好写一个
- `main`不会被调用，从上到下，输出所有；而是调用**特定**的名称函数，在新的工程中使用了的