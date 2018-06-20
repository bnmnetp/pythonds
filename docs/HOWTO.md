# Install

```pip install pythonds3```

# Use

```python
import pythonds3
s = pythonds3.basic.Stack()
s.size()  # 0
s.push('Aardvark')
s.push('Beaver')
s.size()  # 2
s.peek()  # 'Beaver'
s.pop()  # 'Beaver'
s.size()  # 1
s.peek()  # 'Aardvark'
```
