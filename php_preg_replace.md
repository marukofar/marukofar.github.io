![](images/day4.png)

# PHP preg_replace

`preg_replace ()` ใช้ในการตรวจสอบข้อความตาม pattern ที่กำหนดหรือไม่ (คำนึงถึงตัวอักษรพิมพ์เล็กและพิมพ์ใหญ่) แล้วแทนที่ข้อความด้วยฟังก์ชัน `preg_replace ()`  ฟังก์ชันนี้เสริม security อย่างไร? `preg_replace ()` สามารถใช้ดักจับข้อความที่ไม่ตรงตาม pattern ที่กำหนดไว้ เช่น ดักจับอักขระพิเศษแล้วแทนที่ด้วยค่าอื่นหรือค่าว่างก็ยังได้  ฟังก์ชันนี้เหมาะสำหรับกันผู้ไม่ประสงค์ดีสั่งรันคริปต์เข้ามา หรือผู้ใช้กรอกข้อความหรืออักขระไม่ตรงตาม pattern ที่เราคาดหวัง หรือจะใช้กรองคำด่า คำเสียดสีแล้วแทนที่ด้วยคำอื่นก็ได้ 
`preg_replace ()` ประมวลผลเร็วกว่าฟังก์ชัน `ereg_replace()` 

### รูปแบบการใช้งาน

```php 
preg_replace ( string|array $pattern , string|array $replacement , string|array $subject , int $limit = -1 , int &$count = null ) : string|array|null
```

### Parameters 

- pattern
- replacement
- subject
- limit
- count

### การคืนค่า

`preg_replace ()` คืนค่าอาร์เรย์หาก subject parameter เป็นอาร์เรย์หรือสตริงเป็นอย่างอื่น 

### ตัวอย่างการใช้ `preg_replace ()`

### ตัวอย่างที่ 1 แทนที่อักขระพิเศษให้เป็นค่าว่าง

```php 
<?php
$data = "Maruko'$%#&far-1-2-3"; 
$data = preg_replace("/[^a-z\d]/i", '', $data);
echo $data;
?>
```
#### Output:

```bash
Marukofar123
```
### ตัวอย่างที่ 2 

```php 
<?php
$string = 'The quick brown fox jumps over the lazy dog.';
$patterns = array();
$patterns[0] = '/quick/';
$patterns[1] = '/brown/';
$patterns[2] = '/fox/';
$replacements = array();
$replacements[2] = 'bear';
$replacements[1] = 'black';
$replacements[0] = 'slow';
echo preg_replace($patterns, $replacements, $string);
?>
```
#### Output:

```bash
The bear black slow jumps over the lazy dog.
```
แล้วนำมาเรียงให้ตรงตาม pattern ที่ต้องการ

```php 
<?php
ksort($patterns);
ksort($replacements);
echo preg_replace($patterns, $replacements, $string);
?>
```
#### Output:

```bash
The slow black bear jumps over the lazy dog.
```
### ตัวอย่างที่ 3 แทนที่ด้วยค่าต่าง ๆ 

```php 
<?php
$patterns = array ('/(19|20)(\d{2})-(\d{1,2})-(\d{1,2})/',
                   '/^\s*{(\w+)}\s*=/');
$replace = array ('\3/\4/\1\2', '$\1 =');
echo preg_replace($patterns, $replace, '{startDate} = 1999-5-27');
?>
```
#### Output:

```bash
$startDate = 5/27/1999
```
### ตัวอย่างที่ 4 ตัดช่องว่าง (Blank spaces) ส่วนเกินออกจากสตริง 

```php 
<?php
$str = 'fa   r';
$str = preg_replace('/\s\s+/', ' ', $str);

echo $str;
?>
```
#### Output: 
```bash
fa r
```
### ตัวอย่างที่ 5 ใช้ `count` parameter

```php 
<?php
$count = 0;

echo preg_replace(array('/\d/', '/\s/'), '*', 'xp 4 to', -1 , $count);
echo $count; //3
?>
```
#### Output: 

```bash
xp***to
3
```

#### Reference
- https://www.php.net/manual/en/function.preg-replace.php
