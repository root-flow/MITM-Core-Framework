# MITM-Core Advanced Framework (v2.5.0)

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Build: Success](https://img.shields.io/badge/Build-Stable-green.svg)]()
[![Author: canmitm](https://img.shields.io/badge/Author-canmitm-blue.svg)](https://instagram.com/canmitm)

## 0x01. Overview
MITM-Core, Debian tabanlı Linux dağıtımlarını (Ubuntu, Mint, Debian vb.) tam donanımlı bir sızma testi platformuna dönüştürmek için tasarlanmış hibrit bir otomasyon framework'üdür. Standart scriptlerin aksine, sistem güvenliğini doğrulamak için çalışma anında (runtime) derlenen düşük seviyeli bir **C çekirdeği** kullanır.

## 0x02. Technical Architecture
Framework iki ana katmandan oluşur:
1.  **Low-Level Core (C):** Donanım kimliği doğrulama, kernel sürüm denetimi ve idari (Root) yetki validasyonu.
2.  **Logic Engine (Python):** GPG anahtar yönetimi, izole repo konfigürasyonu ve bağımlılık çözümlü araç kurulum modülleri.



## 0x03. Key Features
- **Secure Repository Injection:** `/etc/apt/sources.list.d/` dizini üzerinden izole Kali Rolling entegrasyonu.
- **Automated GPG Keychain Sync:** Eksik anahtarların `keyserver.ubuntu.com` üzerinden otomatik onarımı.
- **Core Pentest Deployment:** Metasploit, Nmap, Sqlmap ve Wireshark gibi kritik araçların tek tıkla yapılandırılması.
- **Resource Cleaning:** İstenildiğinde tüm repo ve geçici binary dosyalarının sistemden tam temizliği (De-provisioning).

## 0x04. Installation & Deployment

### Prerequisites
Sistemin hibrit motorunu derleyebilmesi için GCC derleyicisi gereklidir:
```bash
sudo apt update && sudo apt install gcc python3-pip -y
