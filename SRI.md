# Subresource Integrity (SRI)

![](images/subresource-integrity-lg@2x.webp)

`Subresource integrity` หรือ `SRI` คือ ฟีเจอร์ความปลอดภัยที่จะเป็นตัวช่วยให้เบราว์เซอร์ สามารถตรวจสอบไฟล์ Scripts หรือ Stylesheets นั้นๆ ได้ว่าไม่ถูกแก้ไขไปจากไฟล์ต้นฉบับ ดังนั้น เพื่อเป็นการยืนยันข้อมูลกับเบราว์เซอร์ เราจึงต้องมี flag บางอย่างไว้ให้เบราว์เซอร์ไว้คอยตรวจสอบโดย flag ที่ว่านี้ ก็คือ แอตทริบิวต์ที่ชื่อ integrity นั่นเอง เป็นที่ทราบกันดีว่าข้อมูล 1 ชุดเมื่อเข้า hash function แล้วเราจะได้ค่าคงที่เสมอ ดังนั้น เราจึงอาศัยความจริงข้อนี้ในการนำไฟล์ของเราเข้าสู่ hash function แล้วนำค่าที่ได้ไปใส่ใน integrity แต่ก่อนจะนำไปใส่ต้องแปลงค่าเป็นแบบ base64-encoded เสียก่อน ดังตัวอย่างด้านล่าง

```html 
<script
  src="https://cdnjs.cloudflare.com/ajax/libs/redux/4.0.0/redux.js"
  integrity="sha256-KLkq+W1kKUA6iR5s5Xa/tdzU0yAmXNu7qIGKR/PBoUE="
  crossorigin="anonymous"
/>
```

อย่างไรก็ตาม SRI แตกต่างจาก CSP ตรงที่มี hash function ที่ต้องใช้ไฟล์ที่ดึงมาเพื่อจับคู่ สิ่งนี้มีประโยชน์ในกรณีที่ผู้โจมตีสามารถเข้าถึงไฟล์เว็บของคุณที่ส่งผ่านบริการของบุคคลที่สาม (เช่น CDN) และแทรกเนื้อหาตามอำเภอใจ ปัจจุบันความสามารถในการใช้งานร่วมกันได้ของ Subresource กับเบราว์เซอร์อยู่ที่ประมาณ 75% เมื่อพิจารณาจากเบราว์เซอร์หลักทั้งหมด 

![](images/subresource-integrity-support-2018-1-lg@2x.webp)

## Subresource Integrity (SRI) ทำงานอย่างไร?

หลังจากที่เข้าเว็บไซต์ เบราว์เซอร์จะเริ่มทำการอ่านไฟล์ที่อยู่ในแท็ก `<script>` หรือ `<link>` ซึ่งถ้าหากแท็กดังกล่าวมีการะบุแอตทริบิวต์ integrity เอาไว้ มันจะทำการตรวจสอบไฟล์ดังกล่าวโดยการดูรหัส hash หากพบว่ามีข้อมูลไม่ตรงกัน Browser จะปฎิเสธการโหลดไฟล์นั้นทันที 

## การสร้าง Subresource Integrity Hash

```bash
openssl dgst -sha384 -binary FILENAME.js | openssl base64 -A
```
หรือสามารถใช้ tool ที่เรียกว่า [srihash.org](https://www.srihash.org/).

![](images/sri-hash-generator-lg@2x.webp)

tool นี้เพียงแค่เราคัดลอก URL ของ resource ที่เราต้องการสร้างแฮชและจะส่งคืนองค์ประกอบ `<link>` หรือ `<script>` ที่จัดฟอร์แมตอย่างถูกต้องสำหรับ resource นั้น ตัวอย่างเช่น สมมติว่าเราต้องการสร้างแฮชสำหรับไฟล์ Font Awesome ซึ่งโฮสต์บนเซิร์ฟเวอร์ของเรา: 

```bash
https://cdn.keycdn.com/css/font-awesome-4.4.0.min.css
```

เราสามารถป้อนเนื้อหานี้ลงใน tool `srihash` และจะสร้างผลลัพธ์ต่อไปนี้: 

```bash
<link rel="stylesheet" href="https://cdn.keycdn.com/css/font-awesome-4.4.0.min.css" integrity="sha384-MI32KR77SgI9QAPUs+6R7leEOwtop70UsjEtFEezfKnMjXWx15NENsZpfDgq8m8S" crossorigin="anonymous">
```
## ใช้ SRI กับ CSP

จากนโยบายความปลอดภัยของเนื้อหาหรือ CSP เราสามารถกำหนดประเภทของไฟล์ที่เราต้องการใช้ได้ โดยใช้ `Subresource integrity` เช่น หากเราต้องการตรวจสอบ Stylesheets ทั้งหมดโดยใช้ SRI เราสามารถเพิ่มกฎต่อไปนี้ในไฟล์ CSP: 

```bash
Content-Security-Policy: require-sri-for style;
```
นอกจากนี้หากต้องการให้ไฟล์ JavaScript ทั้งหมดใช้ Integrity ของ SRI เราสามารถใช้สิ่งต่อไปนี้:

```bash
Content-Security-Policy: require-sri-for script;
```

เรายังสามารถรวมทั้ง Scripts และ Stylesheets ไว้ในกฎข้อเดียวเช่น:

```bash
Content-Security-Policy: require-sri-for script style;
```
**การกำหนดสิ่งนี้ทำให้ Stylesheets หรือเนื้อหา Scripts ใด ๆ ที่ไม่มีความสมบูรณ์จะไม่ถูกโหลด**

## Subresource integrity tool

นอกจาก tool srihash ที่กล่าวถึงข้างต้นแล้วยังมี tool อื่น ๆ ที่สามารถช่วยให้นำ Subresource integrity ไปใช้ได้อย่างมีประสิทธิภาพ สิ่งที่จะพูดถึงในบทความนี้เรียกว่า [webpack-subresource-integrity](https://www.npmjs.com/package/webpack-subresource-integrity). 

![](images/webpack.png)

`webpack` คือ เครื่องมือที่ใช้ในการรวม module ที่เราเขียน ให้เป็นไฟล์ที่เราจะนำไปใช้งานจริงๆ ความสามารถหลักๆของมันมีดังนี้ครับ รวม module หลายๆ module ให้กลายเป็นไฟล์ๆเดียว (หรือมากกว่าก็ได้) แปลง ES6, JSX, CSS เป็นต้น ให้สามารถใช้งานบน browser ทั่วไปได้ ปลั๊กอินนี้มีขั้นตอนการติดตั้งที่ค่อนข้างง่าย: 

```bash
npm install webpack-subresource-integrity --save-dev
```

เมื่อติดตั้งแล้วให้ใช้ตัวอย่างการกำหนดค่า webpack ต่อไปนี้ตามที่กำหนดไว้ในหน้าปลั๊กอิน: 

```javascript
import SriPlugin from 'webpack-subresource-integrity';

const compiler = webpack({
    output: {
        crossOriginLoading: 'anonymous',
    },
    plugins: [
        new SriPlugin({
            hashFuncNames: ['sha256', 'sha384'],
            enabled: process.env.NODE_ENV === 'production',
        }),
    ],
});
```

## สรุป

`SRI` เป็นวิธีที่ยอดเยี่ยมในการช่วยให้แน่ใจว่าเนื้อหาของเราได้รับการปกป้องไม่ถูกแก้ไข ในกรณีที่ผู้ไม่หวังดีเข้ามาครอบงำไฟล์เว็บของเรา และพยายามใส่ malicious เข้าไป หากเบราว์เซอร์ของเรา compatible โดยใช้ Subresource integrity เบราว์เซอร์จะตรวจพบว่าไฟล์มีการเปลี่ยนแปลงและแฮชไม่ตรงกัน ดังนั้นแม้ว่าผู้โจมตีจะสามารถปล่อย malicious code ลงในไฟล์ได้ แต่ผู้เยี่ยมชมเว็บไซต์ก็จะไม่ได้รับอันตรายเนื่องจากไฟล์จะไม่โหลดเท่านั้นซึ่งจะช่วยเพิ่มความปลอดภัยและการป้องกันได้

#### Reference:

+ https://www.keycdn.com/support/subresource-integrity
+ https://medium.com/danaidesign/security-your-js-css-file-from-cdn-with-subresource-integrity-929a70152ea6
+ https://www.rahulpnath.com/blog/subresource-integrity-sri/

---

### Written by: Fareed Marnleb
