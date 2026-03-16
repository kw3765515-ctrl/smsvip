# 💣 SMS Bomber

Script ยิง SMS ผ่าน API - Client Version

## 🚀 ฟีเจอร์
- 📡 ยิงผ่าน API http://141.98.17.37:3000
- 🎨 UI สวยงาม รองรับภาษาไทย
- ⚡ ใช้งานง่าย (Interactive Mode)
- 🔧 รองรับ Command Line Arguments
- 📊 แสดงผลลัพธ์แบบ Real-time

## 📥 ดาวน์โหลด
```bash
wget https://raw.githubusercontent.com/kw3765515-ctrl/smsvip/main/smsbomber
chmod +x smsbomber
```

## 🎮 วิธีใช้

### โหมด Interactive (สวยงาม)
```bash
./smsbomber
```

### ยิงทันที (ผ่าน Arguments)
```bash
./smsbomber 0812345678 10
```

### เปลี่ยน API URL
```bash
SMS_API_URL=http://your-api.com:3000 ./smsbomber 0812345678 10
```

## 📡 API ที่ใช้
- **Endpoints:**
  - `POST /send` - ส่ง SMS
  - `GET /health` - เช็คสถานะ

## 📋 ตัวอย่างการใช้งาน
```bash
# โหมด Interactive
./smsbomber

# ยิงทันที 20 ครั้ง
./smsbomber 0812345678 20

# ใช้ API ของตัวเอง
SMS_API_URL=http://localhost:3000 ./smsbomber 0812345678 10
```

## 👨‍💻 พัฒนาโดย
**by DeV ต้น X9CODESHOP**

---
⚠️ ใช้เพื่อการศึกษาเท่านั้น
