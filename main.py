import logging

# Security Audit Log Yapılandırması
logging.basicConfig(
    filename='security_audit.log',
    level=logging.INFO,
    format='%(asctime)s - [%(levelname)s] - %(message)s'
)

class ERPSecurityEngine:
    def __init__(self):
        # Görevler Ayrılığı (SoD) Çakışma Matrisi
        self.sod_rules = [
            {"conflict": ("CREATE_PO", "APPROVE_PO"), "risk": "HIGH", "desc": "Siparişi açan kişi onaylayamaz."},
            {"conflict": ("CREATE_VENDOR", "PAY_INVOICE"), "risk": "CRITICAL", "desc": "Tedarikçi ekleyen kişi ödeme yapamaz."}
        ]
        self.user_roles = {}

    def assign_permissions(self, user_id, permissions):
        """Kullanıcıya yetki atarken SoD kural motorunu çalıştırır."""
        for rule in self.sod_rules:
            perm1, perm2 = rule["conflict"]
            if perm1 in permissions and perm2 in permissions:
                alert_msg = f"[SoD İHLALİ] Kullanıcı: {user_id} -> Çakışan Yetkiler: {perm1} & {perm2} | Risk: {rule['risk']}"
                print(f"❌ {alert_msg}")
                logging.warning(alert_msg)
                return False

        self.user_roles[user_id] = permissions
        success_msg = f"[GÜVENLİ] Kullanıcı: {user_id} yetkileri başarıyla tanımlandı: {permissions}"
        print(f"✅ {success_msg}")
        logging.info(success_msg)
        return True

if __name__ == "__main__":
    engine = ERPSecurityEngine()
    print("--- ERP Güvenlik ve SoD Denetim Motoru Çalıştırılıyor ---\n")
    
    # Test 1: Güvenli Yetki Ataması
    engine.assign_permissions("user_satinalma_uzmani", ["CREATE_PR", "CREATE_PO"])
    
    # Test 2: SoD İhlali (Fraud Risk)
    engine.assign_permissions("user_kidemli_uzman", ["CREATE_PO", "APPROVE_PO"])
