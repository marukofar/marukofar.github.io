![](images/day-2.png)

# Python String isdigit()

`str.isdigit()` ใช้ตรวจสอบว่า str เป็นตัวเลขทั้งหมดหรือไม่ ถ้าใช่จะคืนค่าเป็น True หากไม่ใช่จะคืนค่าเป็น False ฟังก์ชัน isdigit() จะเสริม Security ในการป้อนข้อมูลของผู้ใช้ (Input Validation) เพื่อตรวจสอบค่าที่รับมาตรงตามที่ต้องการและถูกต้องหรือไม่ เช่น เราต้องการรับค่าเลขบัตรเครดิตเฉพาะตัวเลขเท่านั้น หากผู้ใช้หรือผู้ไม่ประสงค์ดีกรอกอักขระแปลกปลอมเข้ามา ฟังก์ชันนี้สามารถเช็คกรองความถูกต้องให้ได้ 

### Key Points:

- **Return Type:** จะคืนค่าเป็น True หรือ False
- **Parametric Values:** ไม่จำเป็นต้องแยกพารามิเตอร์ในฟังก์ชัน isdigit()
- ช่องว่างระหว่างตัวเลข (Blank spaces) จะคืนค่าเป็น False
- str ว่างเปล่า จะคืนค่าเป็น False
- เลขยกกำลังถือว่าเป็นตัวเลข

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

### แบบที่ 2 ตัวเลข และช่องว่าง (Blank spaces)
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
text = "123Far" 

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

#### References:

- https://www.journaldev.com/24049/python-string-isdigit
- https://www.askpython.com/python/string/python-string-isdigit-function

