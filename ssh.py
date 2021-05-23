#DontRecodePlease
#Anon66Exp3rt
import os

def menu():

    print("""                                                             
 ____ ____  _   _   _     _                   ___           _        _ _ 
/ ___/ ___|| | | | | |   (_)_ __  _   ___  __ |_ _|_ __  ___| |_ __ _| | |
\___ \___ \| |_| | | |   | | '_ \| | | \ \/ /  | || '_ \/ __| __/ _` | | |
 ___) |__) |  _  | | |___| | | | | |_| |>  <   | || | | \__ \ || (_| | | |
|____/____/|_| |_| |_____|_|_| |_|\__,_/_/\_\ |___|_| |_|___/\__\__,_|_|_|

Developed by : Anon666Exp3rt
Team         : AnXsec Syndicate
github       : https://github.com/anon666exp3rt                                                                                                           
==========================================
This is a List of available Linux SSH
------------------------------------------
1. Install SSH Alpine Linux 3.13.1
2. Install SSH Arch Linux
3. Install SSH Debian 10 (Buster)
4. Install SSH Fedora 33
5. Install SSH Kali Nethunter
6. Install SSH Parrot OS (LTS)
7. Install SSH Ubuntu 18.04
8. Install SSH Ubuntu 20.04

------------------------------------------
99. Exit
==========================================
""")

loop = True

while loop:
    menu()
    what = input("root@anon~#, ")
    if what == "1":
        os.system("cd /data/data/com.termux/files/home")
        os.system("pkg update -y")
        os.system("pkg upgrade -y")
        os.system("pkg install -y proot-distro")
        os.system("proot-distro install alpine")
        os.system("cd /data/data/com.termux/files/home")
        print("==================================================")
        print("[+] Alpine Linux 3.13.1 installed successfully :)")
        print("[+] Do update && upgrade after login ssh")
        print("==================================================")
        rmenu = input("[?] Back to Menu? (y/n): ")
        if rmenu == "y":
            menu()
        else:
            break
    elif what == "2":
        os.system("cd /data/data/com.termux/files/home")
        os.system("pkg update -y")
        os.system("pkg upgrade -y")
        os.system("pkg install -y proot-distro")
        os.system("proot-distro install archlinux")
        os.system("cd /data/data/com.termux/files/home")
        print("==================================================")
        print("[+] Arch Linux installed successfully :)")
        print("[+] Do update && upgrade after login ssh")
        print("==================================================")
        rmenu = input("[?] Back to Menu? (y/n): ")
        if rmenu == "y":
            menu()
        else:
            break
    elif what == "3":
        os.system("cd /data/data/com.termux/files/home")
        os.system("pkg update -y")
        os.system("pkg upgrade -y")
        os.system("pkg install proot-distro")
        os.system("proot-distro install debian-buster")
        os.system("cd /data/data/com.termux/files/home")
        print("==================================================")
        print("[+] Alpine Linux 3.13.1 installed successfully :)")
        print("[+] Do update && upgrade after login ssh")
        print("==================================================")
        rmenu = input("[?] Back to Menu? (y/n): ")
        if rmenu == "y":
            menu()
        else:
            break
    elif what == "4":
        os.system("pkg update -y")
        os.system("pkg upgrade -y")
        os.system("pkg install -y proot-distro")
        os.system("proot-distro install fedora-33")
        os.system("cd /data/data/com.termux/files/home")
        print("==================================================")
        print("[+] Fedora 33 installed successfully :)")
        print("[+] Do update && upgrade after login ssh")
        print("==================================================")
        rmenu = input("[?] Back to Menu? (y/n): ")
        if rmenu == "y":
            menu()
        else:
            break
    elif what == "5":
        os.system("pkg update -y")
        os.system("pkg upgrade -y")
        os.system("pkg install -y proot-distro")
        os.system("proot-distro install nethunter")
        os.system("cd /data/data/com.termux/files/home")
        print("==================================================")
        print("[+] Nethunter installed successfully :)")
        print("[+] Do update && upgrade after login ssh")
        print("==================================================")
        rmenu = input("[?] Back to Menu? (y/n): ")
        if rmenu == "y":
            menu()
        else:
            break
    elif what == "6":
        os.system("pkg update -y")
        os.system("pkg upgrade -y")
        os.system("pkg install proot-distro -y")
        os.system("proot-distro install parrot-lts")
        print("====================================")
        print("[+] Parrot OS (LTS) installed successfully :)")
        print("[+] Do update && upgrade after login ssh")
        print("====================================")
        rmenu = input("[?] Back to Menu? (y/n): ")
        if rmenu == "y":
            menu()
        else:
            break
    elif what == "7":
        os.system("pkg update -y")
        os.system("pkg upgrade -y")
        os.system("pkg install proot-distro -y")
        os.system("proot-distro install ubuntu-18.04")
        print("====================================")
        print("[+] Ubuntu 18.04 installed successfully :)")
        print("[+] Do update && upgrade after login ssh")
        print("====================================")
        rmenu = input("[?] Back to Menu? (y/n): ")
        if rmenu == "y":
            menu()
        else:
            break
    elif what == "8":
        os.system("pkg update -y")
        os.system("pkg upgrade -y")
        os.system("pkg install proot-distro -y")
        os.system("proot-distro install ubuntu-20.04")
        print("====================================")
        print("[+] Ubuntu 20.04 installed successfully :)")
        print("[+] Do update && upgrade after login ssh")
        print("====================================")
        rmenu = input("[?] Back to Menu? (y/n): ")
        if rmenu == "y":
            menu()
        else:
            break
    elif what == "99":
        print("""
 Enjoy And Happy Hacking :D
""")
        break