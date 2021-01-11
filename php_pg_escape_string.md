![](images/day7.png)

# pg_escape_string
`pg_escape_string()` ใช้หลีกเลี่ยงสตริง(ทุกตัวแปร) ผ่านการป้อนค่าเข้ามาของผู้ใช้ ฟังก์ชันนี้ใช้สำหรับจัดการฐานข้อมูล PostgreSQL หากใช้ MySQL จะใช้ฟังก์ชัน `mysql_escape_string()` แทน ซึ่งฟังก์ชันเหล่านี้สามารถป้องกัน SQL injection attack ได้

## SQL injection คืออะไร?
การ..
จากข้อมูลของ [OWASP](https://owasp.org/www-project-top-ten/2017/) OWASP Top 10 Application Security Risks - 2017 จะเห็นได้ว่า SQL injection attacks เป็นช่องโหว่หรือภัยคุกคามต่อความปลอดภัยของเว็บไซต์ที่เหล่าผู้ไม่ประสงค์(Hacker) ใช้งานมากเป็นอันดับ 1



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
