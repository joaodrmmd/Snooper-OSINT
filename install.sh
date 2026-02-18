#!/bin/bash
# SNOOPER - Installation Script for Unix/Linux/MacOS
# Makes 'snooper' available as a global command

set -e  # Exit on error

# Colors
PURPLE='\033[95m'
GREEN='\033[92m'
YELLOW='\033[93m'
RED='\033[91m'
RESET='\033[0m'

echo -e "${PURPLE}"
echo "╔════════════════════════════════════════════════════════════════╗"
echo "║           SNOOPER v3.0 - Installation Script                   ║"
echo "║         'sudo make me a snooper' - Installation Wizard         ║"
echo "╚════════════════════════════════════════════════════════════════╝"
echo -e "${RESET}"

# Check if running as root for system-wide install
if [ "$EUID" -eq 0 ]; then 
    INSTALL_DIR="/usr/local/bin"
    echo -e "${GREEN}[+] Running as root - System-wide installation${RESET}"
else
    # User installation
    INSTALL_DIR="$HOME/.local/bin"
    echo -e "${YELLOW}[!] Running as user - Installing to $INSTALL_DIR${RESET}"
    echo -e "${YELLOW}[!] Make sure $INSTALL_DIR is in your PATH${RESET}"
    
    # Create directory if it doesn't exist
    mkdir -p "$INSTALL_DIR"
fi

# Get script directory
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

echo -e "\n${GREEN}[+] Installing snooper...${RESET}"

# Copy the main script
if [ -f "$SCRIPT_DIR/snooper.py" ]; then
    cp "$SCRIPT_DIR/snooper.py" "$INSTALL_DIR/snooper"
    chmod +x "$INSTALL_DIR/snooper"
    echo -e "${GREEN}[+] Installed to: $INSTALL_DIR/snooper${RESET}"
else
    echo -e "${RED}[-] Error: snooper.py not found in $SCRIPT_DIR${RESET}"
    exit 1
fi

# Check if install dir is in PATH
if [[ ":$PATH:" != *":$INSTALL_DIR:"* ]]; then
    echo -e "\n${YELLOW}[!] WARNING: $INSTALL_DIR is not in your PATH${RESET}"
    echo -e "${YELLOW}[!] Add this line to your ~/.bashrc or ~/.zshrc:${RESET}"
    echo -e "${PURPLE}    export PATH=\"\$PATH:$INSTALL_DIR\"${RESET}"
    echo -e "${YELLOW}[!] Then run: source ~/.bashrc (or ~/.zshrc)${RESET}"
fi

echo -e "\n${PURPLE}╔════════════════════════════════════════════════════════════════╗"
echo -e "║                   Installation Complete!                       ║"
echo -e "║                                                                ║"
echo -e "║  Run 'snooper' from anywhere to start the tool                ║"
echo -e "║                                                                ║"
echo -e "║  See you, Space Cowboy...                                     ║"
echo -e "╚════════════════════════════════════════════════════════════════╝${RESET}"
echo ""
