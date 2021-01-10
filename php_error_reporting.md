![](images/day6.png)

# PHP error_reporting()
`error_reporting()` ใช้สำหรับแสดงข้อผิดพลาด (Error) ของโปรแกรม PHP โดยแสดงว่ามีข้อผิดพลาดอะไร เพื่อ Dev สามารถแก้ไขได้ถูกจุด ในด้าน Security หากข้อผิดพลาดเกิดไปแสดงต่อผู้ไม่ประสงค์ดี สามารถนำไปสู่การแฮกได้  

### รูปแบบการใช้งาน

```php 
error_reporting ( int $level = ? ) : int
```

### Parameters 

- value - ค่าที่จะกรอง
- filter - 
- options - 

### การคืนค่า

`filter_var()` ส่งคืนข้อมูลที่กรองแล้ว หรือ False หากการกรองไม่สำเร็จ

### ตัวอย่างการใช้ `filter_var()`

### ตัวอย่างแบบที่ 1 ตรวจสอบว่าเป็นที่อยู่อีเมลที่ถูกต้องหรือไม่

```php 
<?php
// Variable to check
$email = "far@maruko.com";

// Validate email
if (filter_var($email, FILTER_VALIDATE_EMAIL)) {
    echo("$email is a valid email address");
} else {
    echo("$email is not a valid email address");
}
?>
```
#### Output: 

```bash
far@maruko.com is a valid email address
```
### ตัวอย่างแบบที่ 1 ตรวจสอบอีเมลว่ารูปแบบถูกต้องหรือไม่

```php 
<?php
// Variable to check
$email = "far@maruko.com";

// Validate email
if (filter_var($email, FILTER_VALIDATE_EMAIL)) {
    echo("$email is a valid email address");
} else {
    echo("$email is not a valid email address");
}
?>
```
#### Output: 

```bash
far@maruko.com is a valid email address
```

#### Reference
- https://www.php.net/manual/en/function.filter-var.php


