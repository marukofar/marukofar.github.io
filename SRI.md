# Subresource Integrity (SRI)

![](images/subresource-integrity-lg@2x.webp)

`Subresource integrity` หรือ `SRI` คือ ฟีเจอร์ความปลอดภัยที่จะเป็นตัวช่วยให้ Browser สามารถตรวจสอบไฟล์ Scripts หรือ Stylesheets นั้นๆ ได้ว่าไม่ถูกแก้ไขไปจากไฟล์ต้นฉบับ ดังนั้น เพื่อเป็นการยืนยันข้อมูลกับ Browser เราจึงต้องมี flag บางอย่างไว้ให้ Browser ไว้คอยตรวจสอบโดย flag ที่ว่านี้ ก็คือ แอตทริบิวต์ที่ชื่อ integrity นั่นเอง เป็นที่ทราบกันดีว่าข้อมูล 1 ชุดเมื่อเข้า hash function แล้วเราจะได้ค่าคงที่เสมอ ดังนั้น เราจึงอาศัยความจริงข้อนี้ในการนำไฟล์ของเราเข้าสู่ hash function แล้วนำค่าที่ได้ไปใส่ใน integrity แต่ก่อนจะนำไปใส่ต้องแปลงค่าเป็นแบบ base64-encoded เสียก่อน ดังตัวอย่างด้านล่าง

```html 
<script
  src="https://cdnjs.cloudflare.com/ajax/libs/redux/4.0.0/redux.js"
  integrity="sha256-KLkq+W1kKUA6iR5s5Xa/tdzU0yAmXNu7qIGKR/PBoUE="
  crossorigin="anonymous"
/>
```
