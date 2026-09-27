![Python](https://img.shields.io/badge/Python-3.10%2B-blue?style=for-the-badge&logo=python)
![Security](https://img.shields.io/badge/Security-RBAC%20%2F%20SoD-red?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Completed%20PoC-orange?style=for-the-badge)

# ERP Security, RBAC & Segregation of Duties (SoD) Engine

## Proje Kapsamı ve Kurumsal Güvenlik Mimarisi
Kurumsal ERP sistemlerinde (KOVAN, SAP, Oracle) veri güvenliği kadar **İç Denetim (Internal Audit)** ve **Görevler Ayrılığı (Segregation of Duties - SoD)** ilkeleri kritiktir. Bir kullanıcının sistemde sahip olduğu yetkilerin çakışması (örneğin hem Satın Alma Siparişi açma hem de kendi açtığı siparişi onaylama yetkisinin tek kişide olması) ciddi bir iç denetim ihlalidir (Fraud Risk).

Bu proje; Role-Based Access Control (RBAC) yetkilendirme mimarisi üzerinden sistemdeki SoD çakışmalarını ve yetki suistimallerini otomatik tespit eden bir **Proof of Concept (PoC)** çalışmasıdır.

### Öne Çıkan Özellikler
- **Role-Based Access Control (RBAC):** Modül ve fonksiyon bazlı dinamik rol matrisi.
- **SoD Conflict Detection Engine:** Çakışan yetkilerin (`CREATE_PO` + `APPROVE_PO`) aynı kullanıcıya atanmasını engelleyen kural motoru.
- **Audit Log & Traceability:** Yetkisiz erişim ve yetki ihlali denemelerinin `security_audit.log` dosyasına kaydedilmesi.

### Kullanılan Teknolojiler
- **Dil:** Python 3.x
- **Kütüphaneler:** Logging, JSON
- **Veritabanı:** SQLite / SQL
