#!/bin/bash

# ═══════════════════════════════════════════════════════════════════════════════
# 💣 SMS Bomber Installer
# by DeV ต้น X9CODESHOP
# ═══════════════════════════════════════════════════════════════════════════════

set -e

REPO="https://raw.githubusercontent.com/kw3765515-ctrl/smsvip/main"
INSTALL_DIR="${INSTALL_DIR:-/usr/local/bin}"
RED='\033[0;31m'; GREEN='\033[0;32m'; YELLOW='\033[1;33m'
CYAN='\033[0;36m'; GRAY='\033[0;90m'; NC='\033[0m'

echo -e "${CYAN}💣 กำลังติดตั้ง SMS Bomber...${NC}"

# Check curl
if ! command -v curl &> /dev/null; then
    echo -e "${YELLOW}📦 กำลังติดตั้ง curl...${NC}"
    if command -v apt &> /dev/null; then
        apt-get update && apt-get install -y curl
    elif command -v yum &> /dev/null; then
        yum install -y curl
    elif command -v pacman &> /dev/null; then
        pacman -Sy curl
    else
        echo -e "${RED}❌ กรุณาติดตั้ง curl ก่อน${NC}"
        exit 1
    fi
fi

# Download
echo -e "${CYAN}📥 กำลังดาวน์โหลด...${NC}"
TMP_DIR=$(mktemp -d)
curl -fsSL "${REPO}/smsbomber" -o "${TMP_DIR}/smsbomber"

# Install
chmod +x "${TMP_DIR}/smsbomber"

# Try to install to system directory, fallback to home
if [ -w "$INSTALL_DIR" ] || [ "$EUID" -eq 0 ]; then
    mv "${TMP_DIR}/smsbomber" "${INSTALL_DIR}/smsbomber"
    INSTALLED_TO="${INSTALL_DIR}/smsbomber"
else
    mkdir -p "${HOME}/.local/bin"
    mv "${TMP_DIR}/smsbomber" "${HOME}/.local/bin/smsbomber"
    INSTALLED_TO="${HOME}/.local/bin/smsbomber"
    
    # Add to PATH if needed
    if [[ ":$PATH:" != *":${HOME}/.local/bin:"* ]]; then
        echo 'export PATH="${HOME}/.local/bin:${PATH}"' >> "${HOME}/.bashrc"
        echo -e "${YELLOW}⚠️  รัน 'source ~/.bashrc' หรือเปิด Terminal ใหม่เพื่อใช้คำสั่ง 'smsbomber'${NC}"
    fi
fi

rm -rf "$TMP_DIR"

echo ""
echo -e "${GREEN}✅ ติดตั้งสำเร็จ!${NC}"
echo ""
echo -e "${CYAN}🎮 วิธีใช้:${NC}"
echo -e "   ${GRAY}smsbomber          - โหมด Interactive${NC}"
echo -e "   ${GRAY}smsbomber เบอร์ จำนวน  - ยิงทันที${NC}"
echo ""
echo -e "${CYAN}📍 ติดตั้งที่:${NC} ${INSTALLED_TO}"
echo ""
echo -e "${GRAY}by DeV ต้น X9CODESHOP${NC}"
