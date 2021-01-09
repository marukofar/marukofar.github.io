![](images/day5.png)

# PHP filter_var()
`filter_var()` ใช้สำหรับตรวจสอบความถูกต้องของข้อมูลที่รับค่าเข้ามา เช่น ข้อมูลอีเมล, เบอร์โทรศัพท์ เป็นต้น ว่ามีรูปแบบถูกต้องหรือไม่ เพื่อป้องกัน  `Cross-site Scripting (XSS)` จึงต้องมีการกรองหรือ Filtering Input โดยการใช้ฟังก์ชัน `filter_var()` สามารถใช้ฟังก์ชันนี้ตรวจสอบข้อความสตริง ว่าเป็น Link หรือไม่ได้ หรือใช้คำสั่ง `filter_var($s, FILTER_SANITIZE_STRING)` เพื่อเอาคำสั่ง HTML ออกก็ได้เหมือนกัน

### รูปแบบการใช้งาน

```php 
filter_var ( mixed $value , int $filter = FILTER_DEFAULT , array|int $options = 0 ) : mixed
```

### Parameters 

- `variable` - จำเป็นต้องใช้ ตัวแปรในการกรอง
- `filter` - ไม่จำเป็น ระบุ ID หรือชื่อของตัวกรองที่จะใช้ ค่าเริ่มต้นคือ FILTER_DEFAULT ซึ่งก็คือไม่มีการกรอง ตัวอย่าง Validate filters เช่น FILTER_VALIDATE_DOMAIN ใช้ตรวจสอบว่าความยาวชื่อโดเมนถูกต้องหรือไม่, FILTER_VALIDATE_EMAIL ตรวจสอบรูปแบบของอีเมล, FILTER_VALIDATE_IP ตรวจสอบรูปแบบ IP, FILTER_VALIDATE_MAC ตรวจสอบรูปแบบ Mac Address เป็นต้น	 		
- `options` - ไม่จำเป็น ระบุหนึ่งหรือมากกว่า flags / ตัวเลือกที่จะใช้ตรวจสอบแต่ละตัวกรองสำหรับตัวเลือกที่เป็นไปได้และ flags

### การคืนค่า

`filter_var()` ส่งคืนข้อมูลที่กรองแล้ว หรือ False หากการกรองไม่สำเร็จ

### ตัวอย่างการใช้ `filter_var()`

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
### ตัวอย่างแบบที่ 2 ตรวจสอบรูปแบบ URL

```php 
<?php
// Variable to check
$url = "https://www.mut.ac.th";

// Validate url
if (filter_var($url, FILTER_VALIDATE_URL)) {
  echo("$url is a valid URL");
} else {
  echo("$url is not a valid URL");
}
?>
```
#### Output: 

```bash
https://www.mut.ac.th is a valid URL
```
### ตัวอย่างแบบที่ 3

```php 
<?php
var_dump(filter_var('far@maruko.com', FILTER_VALIDATE_EMAIL));
var_dump(filter_var('maruko.com', FILTER_VALIDATE_URL, FILTER_FLAG_SCHEME_REQUIRED));
?>
```
#### Output: 

```bash
string(14) "far@maruko.com"
bool(false)
```

#### Reference
- https://www.php.net/manual/en/function.filter-var.php
- https://www.w3schools.com/php/func_filter_var.asp
- https://www.php.net/manual/en/filter.filters.validate.php


