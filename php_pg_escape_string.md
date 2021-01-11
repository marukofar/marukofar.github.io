![](images/day7.png)

# pg_escape_string

`pg_escape_string()` ใช้หลีกเลี่ยงสตริง(ทุกตัวแปร) ผ่านการป้อนค่าเข้ามาของผู้ใช้ ฟังก์ชันนี้ใช้สำหรับจัดการฐานข้อมูล PostgreSQL หากใช้ MySQL จะใช้ฟังก์ชัน `mysql_escape_string()` ซึ่งฟังก์ชันเหล่านี้สามารถป้องกัน SQL injection attack ได้

### รูปแบบการใช้งาน

```php 
pg_escape_string ( resource $connection = ? , string $data ) : string
```

### Parameters 

- connection
- data

### การคืนค่า

`pg_escape_string()` 

### ตัวอย่างการใช้ `pg_escape_string()`

### ตัวอย่างแบบที่ 1

```php 

```
#### Output: 

```bash

```

#### Reference
- https://www.php.net/pg_escape_string
