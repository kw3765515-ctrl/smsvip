#!/bin/bash

# ═══════════════════════════════════════════════════════════════════════════════
# ╔═════════════════════════════════════════════════════════════════════════════╗
# ║                    💣 SMS BOMBER - INSTALLER 💣                              ║
# ║                         by DeV ต้น X9CODESHOP                               ║
# ╚═════════════════════════════════════════════════════════════════════════════╝
# ═══════════════════════════════════════════════════════════════════════════════

set -e

REPO="https://raw.githubusercontent.com/kw3765515-ctrl/smsvip/main"
INSTALL_DIR="${INSTALL_DIR:-/usr/local/bin}"

# ─── Colors ───────────────────────────────────────────────────────────────────
RED='\033[0;31m'; GRN='\033[0;32m'; YLW='\033[1;33m'; BLU='\033[0;34m'
MGN='\033[0;35m'; CYN='\033[0;36m'; WHT='\033[1;37m'; GRY='\033[0;90m'
LGRN='\033[92m'; LYLW='\033[93m'; LBLU='\033[94m'; LMGN='\033[95m'
NC='\033[0m'; BOLD='\033[1m'

# ─── Banner ───────────────────────────────────────────────────────────────────
show_banner() {
    clear
    echo ""
    echo -e "${MGN}                              ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄                              ${NC}"
    echo -e "${MGN}                         ▄▄▄▄▀▀▀▀          ▀▀▀▀▄▄▄▄                         ${NC}"
    echo -e "${MGN}                     ▄▄▀▀                          ▀▀▄▄                     ${NC}"
    echo -e "${MGN}                  ▄█▀                                  ▀█▄                  ${NC}"
    echo -e "${MGN}                ▄█▀     ${CYN}███████╗███╗   ███╗███████╗${MGN}     ▀█▄                ${NC}"
    echo -e "${MGN}              ▄█▀       ${CYN}██╔════╝████╗ ████║██╔════╝${MGN}       ▀█▄              ${NC}"
    echo -e "${MGN}             ▄█         ${CYN}███████╗██╔████╔██║█████╗ ${MGN}         █▄             ${NC}"
    echo -e "${MGN}            ▄█          ${CYN}╚════██║██║╚██╔╝██║██╔══╝ ${MGN}          █▄            ${NC}"
    echo -e "${MGN}           ▐█           ${CYN}███████║██║ ╚═╝ ██║███████╗${MGN}           █▌           ${NC}"
    echo -e "${MGN}           ▐█           ${CYN}╚══════╝╚═╝     ╚═╝╚══════╝${MGN}           █▌           ${NC}"
    echo -e "${MGN}            █▄                                           ▄█            ${NC}"
    echo -e "${MGN}            ▀█▄                                         ▄█▀            ${NC}"
    echo -e "${MGN}              ▀█▄         ${RED}██████╗  ██████╗ ███╗   ███╗${MGN}         ▄█▀              ${NC}"
    echo -e "${MGN}               ▀█▄        ${RED}██╔══██╗██╔═══██╗████╗ ████║${MGN}        ▄█▀               ${NC}"
    echo -e "${MGN}                 ▀█▄      ${RED}██████╔╝██║   ██║██╔████╔██║${MGN}      ▄█▀                 ${NC}"
    echo -e "${MGN}                   ▀█▄    ${RED}██╔══██╗██║   ██║██║╚██╔╝██║${MGN}    ▄█▀                   ${NC}"
    echo -e "${MGN}                     ▀█▄  ${RED}██████╔╝╚██████╔╝██║ ╚═╝ ██║${MGN}  ▄█▀                     ${NC}"
    echo -e "${MGN}                       ▀█▄${RED}╚═════╝  ╚═════╝ ╚═╝     ╚═╝${MGN}▄█▀                       ${NC}"
    echo -e "${MGN}                         ▀█▄                        ▄█▀                         ${NC}"
    echo -e "${MGN}                           ▀█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█▀                           ${NC}"
    echo -e "${MGN}                              ▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀                              ${NC}"
    echo ""
    echo -e "${CYN}═══════════════════════════════════════════════════════════════════════════════${NC}"
    echo -e "              ${BOLD}⚡ ระบบติดตั้ง SMS BOMBER - AUTOMATIC INSTALLER ⚡${NC}"
    echo -e "${CYN}═══════════════════════════════════════════════════════════════════════════════${NC}"
    echo ""
}

# ─── Spinner ──────────────────────────────────────────────────────────────────
spinner() {
    local msg="$1"
    local pid=$2
    local spin='⣾⣽⣻⢿⡿⣟⣯⣷'
    local i=0
    
    while kill -0 $pid 2>/dev/null; do
        i=$(( (i+1) % 8 ))
        printf "\r  ${CYN}${spin:$i:1}${NC} ${msg}"
        sleep 0.1
    done
    printf "\r  ${LGRN}✓${NC} ${msg} ${GRY}เสร็จสิ้น${NC}\n"
}

# ─── Main ─────────────────────────────────────────────────────────────────────
show_banner

# Check curl
echo -e "  ${YLW}🔍 กำลังตรวจสอบระบบ...${NC}"
if ! command -v curl &> /dev/null; then
    echo -e "  ${RED}✗ ไม่พบ curl${NC}"
    
    # Try to install curl
    echo -e "  ${YLW}📦 กำลังติดตั้ง curl...${NC}"
    if command -v apt &> /dev/null; then
        apt-get update -qq && apt-get install -y -qq curl
    elif command -v yum &> /dev/null; then
        yum install -y -q curl
    elif command -v pacman &> /dev/null; then
        pacman -Sy --noconfirm curl
    elif command -v pkg &> /dev/null; then
        pkg install -y curl
    else
        echo -e "  ${RED}✗ ไม่สามารถติดตั้ง curl อัตโนมัติได้${NC}"
        echo -e "  ${GRY}กรุณาติดตั้ง curl ด้วยตนเอง${NC}"
        exit 1
    fi
fi
echo -e "  ${LGRN}✓ ระบบพร้อมใช้งาน${NC}"
echo ""

# Download
echo -e "  ${YLW}📥 กำลังดาวน์โหลด SMS Bomber...${NC}"
TMP_DIR=$(mktemp -d)
(curl -fsSL "${REPO}/smsbomber" -o "${TMP_DIR}/smsbomber" &)
spinner "กำลังดาวน์โหลด" $!

chmod +x "${TMP_DIR}/smsbomber"

# Install
if [ -w "$INSTALL_DIR" ] || [ "$EUID" -eq 0 ]; then
    mv "${TMP_DIR}/smsbomber" "${INSTALL_DIR}/smsbomber"
    INSTALLED_TO="${INSTALL_DIR}/smsbomber"
else
    mkdir -p "${HOME}/.local/bin"
    mv "${TMP_DIR}/smsbomber" "${HOME}/.local/bin/smsbomber"
    INSTALLED_TO="${HOME}/.local/bin/smsbomber"
    
    if [[ ":$PATH:" != *":${HOME}/.local/bin:"* ]]; then
        echo 'export PATH="${HOME}/.local/bin:${PATH}"' >> "${HOME}/.bashrc"
        export PATH="${HOME}/.local/bin:${PATH}"
    fi
fi

rm -rf "$TMP_DIR"

echo ""
echo -e "${GRN}═══════════════════════════════════════════════════════════════════════════════${NC}"
echo -e "                        ${LGRN}${BOLD}✓ ติดตั้งสำเร็จ!${NC}"
echo -e "${GRN}═══════════════════════════════════════════════════════════════════════════════${NC}"
echo ""
echo -e "  ${CYN}📍 ติดตั้งที่:${NC} ${WHT}${INSTALLED_TO}${NC}"
echo -e "  ${GRY}   by DeV ต้น X9CODESHOP${NC}"
echo ""
echo -e "${CYN}═══════════════════════════════════════════════════════════════════════════════${NC}"
echo ""

# Run immediately
echo -e "  ${YLW}🚀 เริ่มใช้งานเลย...${NC}"
echo ""
sleep 1
"${INSTALLED_TO}"
