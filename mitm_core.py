#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# -------------------------------------------------------------------
# Project: MITM-Core Advanced Framework
# Version: 2.5.0 (Enterprise Stable)
# Author: canmitm | Instagram: @canmitm
# Description: Professional hybrid engine for automated Kali Linux 
#              repository integration and security toolchain deployment.
# -------------------------------------------------------------------

import os
import sys
import subprocess
import tempfile
import time

# --- INLINE C ENGINE SOURCE ---
# Bu blok, sistemin düşük seviyeli (low-level) yetki ve kernel denetimini sağlar.
C_CORE_MOTOR = r"""
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/utsname.h>
#include <string.h>

void execute_audit() {
    struct utsname sys_info;
    if (uname(&sys_info) == 0) {
        printf("[SYSTEM] OS: %s | Node: %s | Kernel: %s\n", 
               sys_info.sysname, sys_info.nodename, sys_info.release);
    }
}

int main(int argc, char *argv[]) {
    if (argc > 1 && strcmp(argv[1], "--audit") == 0) {
        execute_audit();
        return 0;
    }
    // Root check: Returns 1 if root, 0 otherwise
    return (getuid() == 0);
}
"""

class CoreBridge:
    """Python katmanı ile C-Binary motoru arasındaki hibrit iletişimi yönetir."""
    
    def __init__(self):
        self.bin_path = None
        self._initialize_core()

    def _initialize_core(self):
        """C kaynak kodunu geçici olarak derleyip binary haline getirir."""
        fd, c_file = tempfile.mkstemp(suffix=".c")
        self.bin_path = c_file.replace(".c", ".bin")
        
        try:
            with os.fdopen(fd, 'w') as f:
                f.write(C_CORE_MOTOR)
            
            # GCC derleme süreci
            compile_res = subprocess.run(
                ["gcc", c_file, "-o", self.bin_path],
                stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL
            )
            
            if compile_res.returncode != 0:
                print("\033[91m[!] Critical: GCC compiler not found or build error.\033[0m")
                sys.exit(1)
        finally:
            if os.path.exists(c_file):
                os.remove(c_file)

    def verify_auth(self):
        """Binary üzerinden root yetkisi doğrulaması yapar."""
        res = subprocess.run([self.bin_path], capture_output=True)
        return res.returncode == 1

    def system_audit(self):
        """C motorunu kullanarak sistem bilgilerini çeker."""
        subprocess.run([self.bin_path, "--audit"])

    def cleanup(self):
        """Oluşturulan binary dosyasını sistemden temizler."""
        if os.path.exists(self.bin_path):
            os.remove(self.bin_path)

class RepositoryEngine:
    """Repository ve GPG anahtar yönetim protokollerini yönetir."""
    
    def __init__(self):
        self.repo_list = "/etc/apt/sources.list.d/kali-rolling.list"
        self.gpg_key = "ED444FF07D8D0BF6"

    def deploy_repo(self):
        print("\033[94m[*] Phase 1: Injecting Kali Rolling Repository...\033[0m")
        line = "deb http://http.kali.org/kali kali-rolling main contrib non-free non-free-firmware"
        try:
            with open(self.repo_list, "w") as f:
                f.write(line)
            
            print("\033[94m[*] Phase 2: Synchronizing GPG Keychains...\033[0m")
            subprocess.run(["apt-key", "adv", "--keyserver", "keyserver.ubuntu.com", "--recv-keys", self.gpg_key], 
                           stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
            
            print("\033[94m[*] Phase 3: Updating System Package Index...\033[0m")
            os.system("apt update -y > /dev/null 2>&1")
            print("\033[92m[+] Integration Successful.\033[0m")
        except Exception as e:
            print(f"\033[91m[!] Deployment Error: {e}\033[0m")

    def remove_repo(self):
        if os.path.exists(self.repo_list):
            os.remove(self.repo_list)
            os.system("apt update -y > /dev/null 2>&1")
            print("\033[92m[+] System restored to original state.\033[0m")

class ToolDeployment:
    """Sızma testi araçlarının bağımlılık çözümlü kurulumunu sağlar."""
    
    def __init__(self):
        self.core_set = {
            "1": ("Metasploit-Framework", "metasploit-framework"),
            "2": ("Nmap Network Mapper", "nmap"),
            "3": ("Sqlmap API/Engine", "sqlmap"),
            "4": ("Burp Suite CE", "burpsuite"),
            "5": ("Aircrack-ng Suite", "aircrack-ng"),
            "6": ("Wireshark TShark", "wireshark")
        }

    def install_sequence(self, selection):
        if selection == "A":
            target_list = [v[1] for v in self.core_set.values()]
        else:
            target_list = [self.core_set[s.strip()][1] for s in selection.split(",") if s.strip() in self.core_set]

        for tool in target_list:
            print(f"\033[93m[*] Deploying: {tool}...\033[0m")
            os.system(f"apt install {tool} -y")

class MITM_Core_UI:
    """Framework terminal arayüzü ve ana döngü."""
    
    @staticmethod
    def banner():
        os.system("clear")
        print("\033[1;36m" + "="*65)
        print("   MITM-CORE ADVANCED FRAMEWORK | ENTERPRISE BUILD 2.5.0")
        print("   Lead Architect: canmitm | Auth Level: Administrative")
        print("="*65 + "\033[0m")

    def start(self):
        bridge = CoreBridge()
        if not bridge.verify_auth():
            print("\033[91m[FATAL] Administrative privileges (root) required.\033[0m")
            bridge.cleanup()
            sys.exit(1)

        repo = RepositoryEngine()
        tools = ToolDeployment()

        try:
            while True:
                self.banner()
                bridge.system_audit()
                print("\n [01] Integrate Kali Rolling Repository")
                print(" [02] Deploy Core Pentest Toolchain")
                print(" [03] Resolve Missing GPG PUBKEY")
                print(" [04] System De-provisioning (Cleanup)")
                print(" [00] Terminate Session")
                
                cmd = input("\n MITM-Core >> ").upper()
                
                if cmd == "01":
                    repo.deploy_repo()
                elif cmd == "02":
                    print("\n--- Available Toolsets ---")
                    for k, v in tools.core_set.items():
                        print(f" {k}) {v[0]}")
                    print(" A) Deploy All Tools")
                    choice = input("\n Selection: ").upper()
                    tools.install_sequence(choice)
                elif cmd == "03":
                    key = input("[?] Enter PUBKEY: ")
                    os.system(f"apt-key adv --keyserver keyserver.ubuntu.com --recv-keys {key}")
                elif cmd == "04":
                    repo.remove_repo()
                elif cmd == "00":
                    bridge.cleanup()
                    print("\n[*] Session terminated safely.")
                    break
                input("\nProcess Finished. Press Enter...")
        except KeyboardInterrupt:
            bridge.cleanup()
            sys.exit(0)

if __name__ == "__main__":
    app = MITM_Core_UI()
    app.start()
