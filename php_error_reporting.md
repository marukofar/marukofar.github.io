![](images/day6.png)

# PHP error_reporting()
`error_reporting()` ใช้สำหรับแสดงข้อผิดพลาด (Error) ของโปรแกรม PHP โดยแสดงว่ามีข้อผิดพลาดอะไร เพื่อ Dev สามารถแก้ไขได้ง่ายและถูกจุด สะดวกต่อการทำ Debug ในด้าน Security หากข้อผิดพลาดเกิดไปแสดงต่อผู้ไม่ประสงค์ดี สามารถนำไปสู่การแฮกได้  

### รูปแบบการใช้งาน

```php 
error_reporting ( int $level = ? ) : int
```

### Parameters 

- `level` - 

### การคืนค่า

จะคืนค่า level ของ`error_reporting` ก่อนหน้า หรือ level ปัจจุบันหากไม่มีการกำหนด level parameter

### ตัวอย่างการใช้ `error_reporting()`

### ตัวอย่างแบบที่ 1 

```php 
<?php

// Turn off all error reporting
error_reporting(0);

// Report simple running errors
error_reporting(E_ERROR | E_WARNING | E_PARSE);

// Reporting E_NOTICE can be good too (to report uninitialized
// variables or catch variable name misspellings ...)
error_reporting(E_ERROR | E_WARNING | E_PARSE | E_NOTICE);

// Report all errors except E_NOTICE
error_reporting(E_ALL & ~E_NOTICE);

// Report all PHP errors (see changelog)
error_reporting(E_ALL);

// Report all PHP errors
error_reporting(-1);

// Same as error_reporting(E_ALL);
ini_set('error_reporting', E_ALL);

?>
```
#### Output: 



#### Reference
- https://www.php.net/manual/en/function.error-reporting.php


