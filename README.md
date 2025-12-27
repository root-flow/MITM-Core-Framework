# 🛡️ MITM-Core Advanced Framework

![Version](https://img.shields.io/badge/Version-2.5.0-blue.svg?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-green.svg?style=for-the-badge)
![Platform](https://img.shields.io/badge/Platform-Debian--Based-orange.svg?style=for-the-badge)
![Build](https://img.shields.io/badge/Build-Stable-brightgreen.svg?style=for-the-badge)

**MITM-Core**, standart Debian tabanlı Linux dağıtımlarını profesyonel bir sızma testi platformuna dönüştürmek için tasarlanmış, hibrit mimarili bir otomasyon motorudur. 

---

## 💎 Proje Özeti
Sıradan betiklerin aksine **MITM-Core**, düşük seviyeli sistem doğrulamasını sağlamak için çalışma anında derlenen bir **C Çekirdeği (C-Core)** kullanır. Python tabanlı mantıksal katmanı ile sızma testi araçlarının yapılandırmasını ve depo entegrasyonunu hatasız yönetir.

> **Developer Note:** Bu proje, kurumsal standartlarda beyaz şapkalı güvenlik uzmanları için optimize edilmiştir.

---

## 🏗️ Teknik Mimari

### 🖇️ Hibrit Motor Yapısı
Sistem iki katmanlı bir doğrulama protokolü üzerinden çalışır:
* **Layer 1 (Hardware/Privilege):** `system_core.c` modülü üzerinden kernel validasyonu ve idari yetki denetimi.
* **Layer 2 (Orchestration):** Python Wrapper üzerinden dinamik repository enjeksiyonu ve bağımlılık çözümü.

### ✨ Temel Özellikler
| Özellik | Açıklama |
| :--- | :--- |
| **Hybrid Auth** | C-Binary handshake ile yüksek güvenlikli root doğrulaması. |
| **Repo Isolation** | `/etc/apt/sources.list.d/` altında izole ve temiz depo yönetimi. |
| **Auto-GPG** | Key-server üzerinden otomatik anahtar senkronizasyonu. |
| **Core Deploy** | Metasploit, Nmap, Sqlmap gibi araçların tek tıkla kurulumu. |
| **Clean Wipe** | Sistemde iz bırakmadan tüm konfigürasyonları geri alabilme. |

---

## 🚀 Kurulum ve Kullanım

### 1. Ön Hazırlık
Hibrit motorun derlenebilmesi için sisteminizde GCC bulunmalıdır:
```bash
sudo apt update && sudo apt install gcc python3 -y
