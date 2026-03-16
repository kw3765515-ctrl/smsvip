#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
╔═══════════════════════════════════════════════════════════════════════════════╗
║                                                                               ║
║   💣 SMS BOMBER INSTALLER - Python Edition                                    ║
║   ติดตั้งอัตโนมัติสำหรับทุกระบบ (Windows, Linux, Mac, Termux)                  ║
║                                                                               ║
║   by DeV ต้น X9CODESHOP                                                       ║
║                                                                               ║
╚═══════════════════════════════════════════════════════════════════════════════╝
"""

import os
import sys
import urllib.request
import urllib.error
import platform
import shutil
from pathlib import Path

# Colors for terminal
class Colors:
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    MAGENTA = '\033[95m'
    CYAN = '\033[96m'
    WHITE = '\033[97m'
    BOLD = '\033[1m'
    DIM = '\033[2m'
    END = '\033[0m'

def clear_screen():
    """Clear terminal screen"""
    os.system('cls' if os.name == 'nt' else 'clear')

def print_banner():
    """Print beautiful banner"""
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
              {Colors.BOLD}⚡ ระบบติดตั้ง SMS BOMBER - PYTHON INSTALLER ⚡{Colors.END}
{Colors.CYAN}═══════════════════════════════════════════════════════════════════════════════{Colors.END}
"""
    print(banner)

def print_step(step_num, total, message):
    """Print step progress"""
    print(f"{Colors.CYAN}[{step_num}/{total}]{Colors.END} {message}")

def print_success(message):
    """Print success message"""
    print(f"{Colors.GREEN}  ✓ {message}{Colors.END}")

def print_error(message):
    """Print error message"""
    print(f"{Colors.RED}  ✗ {message}{Colors.END}")

def print_info(message):
    """Print info message"""
    print(f"{Colors.YELLOW}  ℹ {message}{Colors.END}")

def get_install_dir():
    """Get appropriate installation directory"""
    system = platform.system()
    
    # Try system directories first (if writable)
    if system != "Windows":
        # Linux/Mac/Termux
        if os.access("/usr/local/bin", os.W_OK):
            return "/usr/local/bin"
        if os.access("/usr/bin", os.W_OK):
            return "/usr/bin"
    
    # User local bin
    local_bin = Path.home() / ".local" / "bin"
    local_bin.mkdir(parents=True, exist_ok=True)
    return str(local_bin)

def download_file(url, destination, show_progress=True):
    """Download file with progress bar"""
    try:
        if show_progress:
            print(f"{Colors.DIM}", end="")
        
        # Create request with headers
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }
        req = urllib.request.Request(url, headers=headers)
        
        # Download
        with urllib.request.urlopen(req, timeout=30) as response:
            total_size = int(response.headers.get('Content-Length', 0))
            block_size = 8192
            downloaded = 0
            
            with open(destination, 'wb') as f:
                while True:
                    chunk = response.read(block_size)
                    if not chunk:
                        break
                    f.write(chunk)
                    downloaded += len(chunk)
                    
                    if show_progress and total_size > 0:
                        percent = (downloaded / total_size) * 100
                        bar_length = 30
                        filled = int(bar_length * downloaded / total_size)
                        bar = '█' * filled + '░' * (bar_length - filled)
                        print(f"\r  {Colors.CYAN}↓{Colors.END} [{bar}] {percent:.1f}%", end='', flush=True)
        
        if show_progress:
            print(f"{Colors.END}")
        
        return True
        
    except Exception as e:
        if show_progress:
            print(f"{Colors.END}")
        print_error(f"Download failed: {str(e)}")
        return False

def add_to_path(directory):
    """Add directory to PATH"""
    shell_rc = None
    
    if os.name == 'posix':
        # Linux/Mac
        shell = os.environ.get('SHELL', '').split('/')[-1]
        if shell == 'bash':
            shell_rc = Path.home() / '.bashrc'
        elif shell == 'zsh':
            shell_rc = Path.home() / '.zshrc'
    
    if shell_rc and shell_rc.exists():
        with open(shell_rc, 'a') as f:
            f.write(f'\n# SMS Bomber PATH\nexport PATH="{directory}:$PATH"\n')
        return True
    return False

def main():
    """Main installer function"""
    clear_screen()
    print_banner()
    
    REPO = "https://raw.githubusercontent.com/kw3765515-ctrl/smsvip/main"
    
    # Step 1: Check Python version
    print_step(1, 4, "ตรวจสอบ Python...")
    if sys.version_info < (3, 6):
        print_error("ต้องการ Python 3.6 ขึ้นไป")
        sys.exit(1)
    print_success(f"Python {sys.version.split()[0]}")
    print()
    
    # Step 2: Determine install location
    print_step(2, 4, "กำลังเตรียมติดตั้ง...")
    install_dir = get_install_dir()
    target_file = os.path.join(install_dir, "smsbomber")
    
    # Windows needs .py extension
    if platform.system() == "Windows":
        target_file += ".py"
    
    print_success(f"ติดตั้งที่: {install_dir}")
    print()
    
    # Step 3: Download
    print_step(3, 4, "กำลังดาวน์โหลด smsbomber...")
    print()
    
    download_url = f"{REPO}/smsbomber"
    
    # Try downloading main script
    if not download_file(download_url, target_file):
        print()
        print_error("ดาวน์โหลดล้มเหลว!")
        print()
        print_info("ลองติดตั้งด้วยตนเอง:")
        print(f"  curl -o ~/smsbomber {download_url}")
        print(f"  chmod +x ~/smsbomber")
        print(f"  ~/smsbomber")
        sys.exit(1)
    
    print()
    print_success("ดาวน์โหลดเสร็จสิ้น")
    print()
    
    # Step 4: Setup
    print_step(4, 4, "กำลังตั้งค่า...")
    
    # Make executable (Unix-like systems)
    if os.name == 'posix':
        os.chmod(target_file, 0o755)
    
    # Add to PATH if needed
    if install_dir not in os.environ.get('PATH', ''):
        if add_to_path(install_dir):
            print_success("เพิ่ม PATH แล้ว")
    
    print_success("ตั้งค่าเสร็จสิ้น")
    print()
    
    # Success message
    print(f"{Colors.GREEN}{'═'*79}{Colors.END}")
    print(f"{Colors.GREEN}{' '*25}✓ ติดตั้งสำเร็จ!{Colors.END}")
    print(f"{Colors.GREEN}{'═'*79}{Colors.END}")
    print()
    print(f"📍 ติดตั้งที่: {Colors.WHITE}{target_file}{Colors.END}")
    print()
    print(f"{Colors.DIM}by DeV ต้น X9CODESHOP{Colors.END}")
    print()
    print(f"{Colors.CYAN}{'═'*79}{Colors.END}")
    print()
    print(f"{Colors.YELLOW}🚀 กำลังเริ่มใช้งาน...{Colors.END}")
    print()
    
    import time
    time.sleep(2)
    
    # Run the installed script
    if os.name == 'posix':
        os.execv(target_file, [target_file])
    else:
        # Windows
        os.system(f'python "{target_file}"')

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print()
        print(f"\n{Colors.YELLOW}⚠ ยกเลิกการติดตั้ง{Colors.END}")
        sys.exit(0)
    except Exception as e:
        print()
        print_error(f"เกิดข้อผิดพลาด: {str(e)}")
        sys.exit(1)
