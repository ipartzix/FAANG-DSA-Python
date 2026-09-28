s = "azyxyyzaaaa"
q = ["d", "a", "y", "x"]
hash_list = [0] * 26
print(hash_list)

for char in s:
    ascii_val = ord(char)
    index = ascii_val - 97
    hash_list[index] += 1

for char in q:
    ascii_val = ord(char)
    index = ascii_val - 97
    print(hash_list[index])


"""
Sure. Here's the **line-by-line explanation** in simple terms:

```python
s = "azyxyyzaaaa"
```

Stores the input string in `s`.

```python
q = ["d", "a", "y", "x"]
```

Stores the characters whose frequencies we want to find.

```python
hash_list = [0] * 26
```

Creates a list of **26 zeros**, one for each lowercase letter (`a` to `z`).

```python
print(hash_list)
```

Prints the initial list:

```text
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
```

### First loop — counting characters

```python
for char in s:
```

Goes through every character in `s`, one by one.

For example:

```text
a → z → y → x → y → y → z → a → a → a → a
```

```python
ascii_val = ord(char)
```

Converts the character into its ASCII value.

For example:

```text
'a' → 97
'x' → 120
'y' → 121
'z' → 122
```

```python
index = ascii_val - 97
```

Converts the ASCII value into a list index.

For example:

```text
a → 97 - 97  = 0
x → 120 - 97 = 23
y → 121 - 97 = 24
z → 122 - 97 = 25
```

So `a` is stored at index `0`, `x` at `23`, etc.

```python
hash_list[index] += 1
```

Increases the count of that character by `1`.

For example, when `a` appears:

```python
hash_list[0] += 1
```

### Second loop — answering queries

```python
for char in q:
```

Goes through each character in `q`:

```text
d, a, y, x
```

```python
ascii_val = ord(char)
```

Gets the ASCII value of the query character.

```python
index = ascii_val - 97
```

Converts the character into its corresponding index.

```python
print(hash_list[index])
```

Prints how many times that character appeared in `s`.

### Final result

```text
d → 0
a → 5
y → 3
x → 1
```

So the main idea is:

**String → count each character → store counts in `hash_list` → use the index to retrieve the count.**

"""
