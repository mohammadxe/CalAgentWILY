#!/usr/bin/env python3
"""
Helper script to find MacBook's IP address
"""

import socket
import subprocess
import platform
import re

def get_ip_address():
    """Get the local IP address"""
    try:
        # Create a socket connection to get local IP
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        # Doesn't actually connect, just gets local IP
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        s.close()
        return ip
    except Exception:
        return None

def get_all_ips():
    """Get all network IP addresses"""
    ips = []
    system = platform.system()
    
    if system == "Darwin":  # macOS
        try:
            result = subprocess.run(
                ["ifconfig"],
                capture_output=True,
                text=True,
                check=True
            )
            # Parse ifconfig output
            for line in result.stdout.split('\n'):
                if 'inet ' in line and '127.0.0.1' not in line:
                    match = re.search(r'inet (\d+\.\d+\.\d+\.\d+)', line)
                    if match:
                        ip = match.group(1)
                        if ip not in ips:
                            ips.append(ip)
        except Exception as e:
            print(f"Error getting IPs: {e}")
    elif system == "Linux":
        try:
            result = subprocess.run(
                ["hostname", "-I"],
                capture_output=True,
                text=True,
                check=True
            )
            ips = result.stdout.strip().split()
        except Exception:
            pass
    
    return ips

def main():
    print("Finding your MacBook's IP address...")
    print()
    
    # Get primary IP
    primary_ip = get_ip_address()
    if primary_ip:
        print(f"Primary IP Address: {primary_ip}")
        print(f"Use this in App.tsx: http://{primary_ip}:8000")
        print()
    
    # Get all IPs
    all_ips = get_all_ips()
    if all_ips:
        print("All Network IP Addresses:")
        for ip in all_ips:
            if ip != '127.0.0.1':
                print(f"  - {ip}")
        print()
    
    if primary_ip:
        print(f"Update frontend/App.tsx with:")
        print(f"  const API_BASE_URL = __DEV__")
        print(f"    ? 'http://{primary_ip}:8000'")
        print(f"    : 'http://your-server.com:8000';")
    else:
        print("Could not determine IP address automatically.")
        print("Please find it manually:")
        print("  macOS: System Preferences > Network > Wi-Fi > Advanced > TCP/IP")
        print("  Or run: ifconfig | grep 'inet ' | grep -v 127.0.0.1")

if __name__ == "__main__":
    main()

