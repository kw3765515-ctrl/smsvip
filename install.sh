#!/bin/bash

# SMS Bomber Installer - Simple & Working Version
# by DeV ต้น X9CODESHOP

REPO="https://raw.githubusercontent.com/kw3765515-ctrl/smsvip/main"

# Colors
RED='\033[0;31m'
GRN='\033[0;32m'
YLW='\033[1;33m'
CYN='\033[0;36m'
WHT='\033[1;37m'
NC='\033[0m'

# Clear screen
clear

echo ""
echo -e "${CYN}╔══════════════════════════════════════════════════════════════╗${NC}"
echo -e "${CYN}║${NC}                                                              ${CYN}║${NC}"
echo -e "${CYN}║${NC}   ${YLW}💣 SMS BOMBER INSTALLER${NC}                                    ${CYN}║${NC}"
echo -e "${CYN}║${NC}   ${GRN}by DeV ต้น X9CODESHOP${NC}                                      ${CYN}║${NC}"
echo -e "${CYN}║${NC}                                                              ${CYN}║${NC}"
echo -e "${CYN}╚══════════════════════════════════════════════════════════════╝${NC}"
echo ""

# Check curl
echo -e "${CYN}[1/3]${NC} ตรวจสอบ curl..."
if ! command -v curl &> /dev/null; then
    echo -e "${RED}✗ ไม่พบ curl${NC}"
    echo "กรุณาติดตั้ง curl ก่อน:"
    echo "  pkg install curl  (สำหรับ Termux)"
    echo "  apt install curl  (สำหรับ Debian/Ubuntu)"
    exit 1
fi
echo -e "${GRN}✓ พบ curl${NC}"
echo ""

# Determine install location
echo -e "${CYN}[2/3]${NC} กำลังเตรียมติดตั้ง..."

INSTALL_DIR=""
if [ -w "/usr/local/bin" ]; then
    INSTALL_DIR="/usr/local/bin"
elif [ -d "$HOME/.local/bin" ] && [ -w "$HOME/.local/bin" ]; then
    INSTALL_DIR="$HOME/.local/bin"
else
    INSTALL_DIR="$HOME/.local/bin"
    mkdir -p "$INSTALL_DIR"
fi

echo -e "${GRN}✓ จะติดตั้งที่: $INSTALL_DIR${NC}"
echo ""

# Download
echo -e "${CYN}[3/3]${NC} กำลังดาวน์โหลด smsbomber..."
echo ""

TARGET="${INSTALL_DIR}/smsbomber"

# Download with progress
curl -fSL --progress-bar "${REPO}/smsbomber" -o "$TARGET" 2>&1

if [ $? -ne 0 ] || [ ! -f "$TARGET" ]; then
    echo ""
    echo -e "${RED}✗ ดาวน์โหลดล้มเหลว!${NC}"
    echo ""
    echo "ลองติดตั้งด้วยตนเอง:"
    echo "  curl -fsSL ${REPO}/smsbomber -o ~/smsbomber"
    echo "  chmod +x ~/smsbomber"
    echo "  ~/smsbomber"
    exit 1
fi

chmod +x "$TARGET"

echo ""
echo -e "${GRN}✓ ดาวน์โหลดเสร็จสิ้น${NC}"
echo ""

# Add to PATH if needed
if [[ ":$PATH:" != *":$INSTALL_DIR:"* ]]; then
    echo 'export PATH="'$INSTALL_DIR':${PATH}"' >> "$HOME/.bashrc"
    export PATH="$INSTALL_DIR:${PATH}"
fi

# Success message
echo ""
echo -e "${GRN}╔══════════════════════════════════════════════════════════════╗${NC}"
echo -e "${GRN}║${NC}                   ${GRN}✓ ติดตั้งสำเร็จ!${NC}                         ${GRN}║${NC}"
echo -e "${GRN}╚══════════════════════════════════════════════════════════════╝${NC}"
echo ""
echo -e "📍 ติดตั้งที่: ${WHT}$TARGET${NC}"
echo ""
echo -e "${YLW}🚀 กำลังเริ่มใช้งาน...${NC}"
echo ""
sleep 2

# Run
echo -e "${CYN}══════════════════════════════════════════════════════════════${NC}"
echo ""
"$TARGET"
