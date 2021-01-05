# Python String encode()
# การเข้ารหัสข้อความใน Python ด้วย encode() 

ตั้งแต่ Python 3.0 สตริง (str) จะถูกจัดเก็บเป็น Unicode ค่าเริ่มต้นเป็น UTF-8 
โดยฟังก์ชัน encode จะเปลี่ยน str ให้เป็น bytes 

#### รูปแบบการใช้งาน

```bash 
str.encode(encoding='UTF-8',errors='strict') 
```

#### Parameters

- **encoding** - str สำหรับระบุรูปแบบที่ใช้เข้ารหัส เช่น UTF-8, base64 เป็นต้น หากไม่ระบุค่าเริ่มต้นจะเป็น UTF-8
- **errors** - str สำหรับระบุ Error (จะระบุหรือไม่ระบุก็ได้) ค่าเริ่มต้นสำหรับข้อผิดพลาดคือ "strict" ก็คือ ข้อผิดพลาดในการเข้ารหัสทำให้เกิด UnicodeError นั่นเอง โดยค่าที่ใช้ได้มีดังนี้
    - **strict** - (ค่าเริ่มต้น) แจ้งว่าเกิดข้อผิดพลาด UnicodeError
    - **backslashreplace** - ใช้เครื่องหมาย \ แทนตัวอักษรที่ไม่สามารถเข้ารหัสได้
    - **ignore** - ไม่สนใจตัวอักษรที่ไม่สามารถเข้ารหัสได้
    - **namereplace** - แทนที่ตัวอักษรด้วยข้อความสำหรับอธิบายตัวอักษรนั้น
    - **replace** - แทนที่ตัวอักษรด้วยเครื่องหมายคำถาม ?
    - **xmlcharrefreplace** - แทนที่ตัวอักษรด้วย xml character

#### ตัวอย่างการใช้ encode() ไม่ระบุรูปแบบการเข้ารหัส

```bash
text = "ภาษา pythön" 

x = text.encode()

print("Encoded String: " + str(x))
```

#### Output:

```bash
Encoded String: b'\xe0\xb8\xa0\xe0\xb8\xb2\xe0\xb8\xa9\xe0\xb8\xb2 pyth\xc3\xb6n' 
```

## ตัวอย่างการใช้ encode() ระบุรูปแบบการเข้ารหัสเป็น UTF16

```bash
text = "Today is Wendy"

x = text.encode(UTF-16)
 
print("Encoded String: " + str(x))
```

## Output:


```bash
Encoded String:  
```
