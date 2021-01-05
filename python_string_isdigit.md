![](images/day-2.png)

# Python String isdigit()

 **str.isdigit()** ใช้ตรวจสอบว่า str เป็นตัวเลขทั้งหมดหรือไม่ ถ้าใช่จะคืนค่าเป็น True หากไม่ใช่จะคืนค่าเป็น False 

### Key Points:

- **Return Type:** จะคืนค่าเป็น True หรือ False
- **Parametric Values:** ไม่จำเป็นต้องแยกพารามิเตอร์ในฟังก์ชัน isdigit ()
- ช่องว่างระหว่างตัวเลข (Blank spces) จะคืนค่าเป็น False
- str ว่างเปล่า จะคืนค่าเป็น False

### รูปแบบการใช้งาน

```python 
str.isdigit()
```

### ตัวอย่างการใช้ isdigit() 

### แบบที่ 1 ตัวเลขทั้งหมด
```python
text = "5555" 

print(text.isdigit())
```
Output: `True`

### แบบที่ 2 ตัวเลข และช่องว่าง (Blank spces)
```python
text = "098 1234567" 

print(text.isdigit())
```
Output: `False`

### แบบที่ 3 ตัวเลขมีจุดทศนิยม
```python
text = "3.14159" 

print(text.isdigit())
```
Output: `False`

### แบบที่ 4 ตัวเลขและตัวอักษร
```python
text = "Far123" 

print(text.isdigit())
```
Output: `False`

### แบบที่ 5 อักขระและตัวเลข
```python
text = "@$123" 

print(text.isdigit())
```
Output: `False`

### แบบที่ 6 str ว่างเปล่า
```python
text = " " 

print(text.isdigit())
```
Output: `False`
![](images/day-2-2.png)

### References:

- https://www.journaldev.com/24049/python-string-isdigit
- https://www.askpython.com/python/string/python-string-isdigit-function

