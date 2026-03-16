# 💣 SMS Bomber

ยิง SMS ผ่าน API - รองรับทุกระบบ (Python Edition)

## 🚀 วิธีติดตั้ง (เลือกใดวิธีหนึ่ง)

### วิธีที่ 1: ติดตั้งอัตโนมัติ (แนะนำ)
```bash
# ใช้ Python ติดตั้ง
python3 <(curl -Ls https://raw.githubusercontent.com/kw3765515-ctrl/smsvip/main/install.py)
```

```bash
# หรือใช้ Shell ติดตั้ง
bash <(curl -Ls https://raw.githubusercontent.com/kw3765515-ctrl/smsvip/main/install.sh)
```

### วิธีที่ 2: ดาวน์โหลดไฟล์ Python โดยตรง
```bash
# ดาวน์โหลด
wget https://raw.githubusercontent.com/kw3765515-ctrl/smsvip/main/smsbomber.py

# รัน
python3 smsbomber.py
```

### วิธีที่ 3: ดาวน์โหลดไฟล์ Shell
```bash
wget https://raw.githubusercontent.com/kw3765515-ctrl/smsvip/main/smsbomber
chmod +x smsbomber
./smsbomber
```

## 🎮 วิธีใช้งาน

### โหมด Interactive (แนะนำ)
```bash
smsbomber
# หรือ
python3 smsbomber.py
```

### โหมดเร็ว (ผ่าน Arguments)
```bash
smsbomber 0812345678 10
# หรือ
python3 smsbomber.py 0812345678 10
```

### เปลี่ยน API
```bash
export SMS_API_URL=http://your-api.com:3000
smsbomber
```

## 📁 ไฟล์ใน Repository

| ไฟล์ | คำอธิบาย |
|------|---------|
| `smsbomber.py` | 🐍 Python Script (แนะนำ) |
| `install.py` | 📥 Python Installer |
| `smsbomber` | 📜 Shell Script |
| `install.sh` | 📥 Shell Installer |

## 💻 รองรับระบบ

- ✅ Linux (Ubuntu, Debian, CentOS, etc.)
- ✅ macOS
- ✅ Windows (ใช้ Python)
- ✅ Termux (Android)
- ✅ WSL (Windows Subsystem for Linux)

## 🐍 ความต้องการ

- Python 3.6+ (สำหรับใช้ .py)
- หรือ Bash (สำหรับใช้ .sh)

## 👨‍💻 พัฒนาโดย

**by DeV ต้น X9CODESHOP**

---
⚠️ ใช้เพื่อการศึกษาเท่านั้น
