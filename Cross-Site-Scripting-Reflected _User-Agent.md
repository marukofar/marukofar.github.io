# Cross-Site Scripting - Reflected (User-Agent)

**Step 1:** เปิด browser เข้า URL [bWAPP](#). **Log in** เข้าสู่ระบบ

![](images/bwapp1-1.png)


**Step 2:** เลือกช่องโหว่ที่ต้องการทดสอบ ในที่นี้คือ **XSS - Reflected (User-Agent)** คลิกเลือก **Cross-Site Scripting - Reflected (User-Agent)** และคลิก **Hack**

![](images/bwapp2.png)

![](images/bwapp3.png)


**Step 3:** Scan ช่องโหว่ด้วย **RIPS** จะแสดงช่องโหว่ **''Cross-Site Scripting"** ที่ตรวจเจอ

![](images/bwapp4-1.png)


**Step 4:** ทดสอบใช้ประโยชน์จากช่องโหว่ที่ตรวจเจอด้วยโปรแกรม **Burp Suite** ซึ่งสามารถ Download ได้จากเว็บไซต์ [portswigger](https://portswigger.net/).
เมื่อเข้าหน้าโปรแกรมให้กด **Proxy** > **Intercept** > **Intercept is on** (เลือกเป็น On)

![](images/bwapp5.png)


**Step 5.** คลิกเลือกช่องโหว่ **Cross-Site Scripting - Stored (User-Agent)** > **Hack**

![](images/bwapp6-1.png)


**Step 6.** แก้ไขข้อความในส่วนของ User-Agent ด้วยคำสั่ง **<script>alert('xxx')</script>** เพื่อสั่งให้ Popup เด้งขึ้นมาด้วยข้อความที่ตั้งไว้ (Hacked by Marukofar) แล้วคลิก **Forward**

![](images/bwapp7.png)


**Step 7.** หน้าเว็บไซต์ URL ที่มีช่องโหว่ข้างต้นจะเด้ง Popup ขึ้นมาด้วยข้อความที่ถูกตั้งไว้

![](images/bwapp8.png)


## วิธีแก้ไข

**Step 1.** ใช้ฟังก์ชัน **htmlentities()** เพื่อป้องกันการโจมตีจาก Script ใน PHP เพิ่มเข้าไปในส่วนของตัวแปร **$user_agent**

![](images/bwapp9.png)

![](images/bwapp10.png)


**Step 2.** ทดสอบ Scan ช่องโหว่อีกครั้งด้วย **RIPS** จะเห็นว่าช่องโหว่ได้รับการแก้ไขแล้ว

![](images/bwapp11.png)


**Step 3.** ทดสอบใช้โปรแกรม **Burp Suite** สั่งรันด้วยคำสั่งเดิมจะพบว่าไม่สามารถสั่งให้ Popup เด้งได้

![](images/bwapp12.png)



>  -  Fareed Marnleb
>  -  Jaray Paensong