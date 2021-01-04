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

![](images/bwapp7.png)

![](images/bwapp8.png)

![](images/bwapp9.png)

![](images/bwapp10.png)

![](images/bwapp11.png)

![](images/bwapp12.png)



>  -  Fareed Marnleb
>  -  Jaray Paensong