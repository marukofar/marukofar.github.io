![](images/day3.png)

# PHP password_hash()

`password_hash()` ใช้สำหรับเข้ารหัส Password ซึ่งโดยปกติการจัดเก็บ Password ให้ปลอดภัยนั้นจะไม่มีการเก็บเป็น Plain text ตรง ๆ เพื่อป้องกันผู้ไม่ประสงค์ดีขโมยข้อมูล Password แล้วนำไปใช้ได้ จึงจำเป็นจะต้องมีการแฮช เช่น md5, sha1, sha256  และอีกมากมายซึ่งทั้งหมดทั้งมวลเข้ารหัสไว้แบบทางเดียว (hashing) ทำให้สามารถ Crack password ได้ด้วย Rainbow Table เมื่อโดน Crack ได้จึงเป็นที่มาของฟังก์ชัน `password_hash()` ฟังก์ชันนี้เข้ามาอุดช่องโหว่นี้เอาไว้ ต่างจากแฮชจำพวกอื่นอย่างไร? ต่างกันที่ `password_hash()` มีการเติม Salt เข้าไปเป็นค่าเริ่มต้น 

### Salt เกลือ?

อธิบายให้เข้าใจง่าย ๆ เราปรุงอาหารมาหม้อหนึ่งให้ทุกคนทาน ทุกคนจะได้รสชาติที่เหมือนกัน หากแต่ละคนเติมเกลือลงไปย่อมทำให้เกิดรสชาติต่างกัน การเติม salt ในด้าน security ก็เช่นเดียวกัน ทำให้ Rainbow Table ไม่สามารถ Crack password ได้หรือ Crack password ได้ยากขึ้นนั่นเอง

`password_hash()` Support ตั้งแต่ PHP 5.5 เป็นต้นไป

### Key Points:

- อัลกอริทึมที่ใช้ : `PASSWORD_DEFAULT`, `PASSWORD_BCRYPT` และ `PASSWORD_ARGON2I` (PHP 7.2 ขึ้นไป)
- `password_hash()` ค่าเริ่มต้นจะเติม Salt ให้โดยอัตโนมัติ

### รูปแบบการใช้งาน

```php 
password_hash ( string $password , mixed $algo , array $options = ? ) : string|false
```

### การคืนค่า

จะคืนค่าเป็นค่าแฮช หรือ False เมื่อแฮชไม่สำเร็จ

### ตัวอย่างการใช้ `password_hash()` 

### แบบที่ 1
```php
<?php

echo password_hash("Marukofar", PASSWORD_DEFAULT);
?>
```
#### Output:

```bash
$2y$10$WmkE7k9DoZNR42Pp/TPl6uO9Yc0NRhy56NWv2qcehvyRiwZYtQecy
```
### แบบที่ 2 กำหนด cost เอง 
(PASSWORD_BCRYPT - ใช้อัลกอริทึม CRYPT_BLOWFISH เพื่อสร้างแฮช ซึ่งจะสร้างแฮชที่เข้ากันได้กับ crypt () มาตรฐาน โดยใช้ตัวระบุ "$2y$" ผลลัพธ์จะเป็น str 60 ตัวเสมอหรือเป็น False เมื่อแฮชไม่สำเร็จ)
```php
<?php

$options = [
    'cost' => 12,
];
echo password_hash("Marukofar", PASSWORD_BCRYPT, $options);
?> 
```
#### Output:

```bash
$2y$12$Kdmrke76bnkGb4KmwPAAxub77n5a3SECuSfOjMRgrh5ySvOr31Zjm
```

### แบบที่ 3 หาค่า Cost ที่ดีที่สุด
```php
<?php

$timeTarget = 0.05; // 50 มิลลิวินาที 

$cost = 8;
do {
    $cost++;
    $start = microtime(true);
    password_hash("test", PASSWORD_BCRYPT, ["cost" => $cost]);
    $end = microtime(true);
} while (($end - $start) < $timeTarget);

echo "Appropriate Cost Found: " . $cost;
?>
```
#### Output:

```bash
Appropriate Cost Found: 10
```

### แบบที่ 4 ใช้ Argon2i hash
```php
<?php

echo 'Argon2i hash: ' . password_hash('Marukofar', PASSWORD_ARGON2I);
?>
```
#### Output:

```bash
Argon2i hash: $argon2i$v=19$m=65536,t=4,p=1$WTZldDY4MGx0eTNMaWdBbg$tjNNHbFUk1SsXaU8XC52+asIOblsFTp7uv7vRA0uRJA
```

### Note

> **คำเตือน!!!**
> สำหรับฟังก์ชัน password_hash() ไม่แนะนำให้เติม salt ด้วยตัวเอง โดยค่าเริ่มต้นฟังก์ชั่นนี้ จะเติม Salt ให้อัตโนมัติซึ่งมีความปลอดภัยอยู่แล้ว
> 
> ตั้งแต่ PHP 7.0 เป็นต้นไปจะขึ้นคำเตือนห้ามเติม Salt ด้วยตัวเอง และในอนาคต PHP เวอร์ชั่นใหม่ก็จะยกเลิกการเติม Salt ด้วยตัวเองไปโดยปริยาย 


#### References:

- https://www.php.net/manual/en/function.password-hash.php
- https://medium.com/@jamesirichai/%E0%B9%80%E0%B8%81%E0%B9%87%E0%B8%9A%E0%B8%A3%E0%B8%AB%E0%B8%B1%E0%B8%AA%E0%B8%9C%E0%B9%88%E0%B8%B2%E0%B8%99%E0%B8%94%E0%B9%89%E0%B8%A7%E0%B8%A2%E0%B8%A0%E0%B8%B2%E0%B8%A9%E0%B8%B2-php-%E0%B8%A2%E0%B8%B1%E0%B8%87%E0%B9%84%E0%B8%87%E0%B8%94%E0%B8%B5%E0%B8%99%E0%B8%B0-9f47b4157174


