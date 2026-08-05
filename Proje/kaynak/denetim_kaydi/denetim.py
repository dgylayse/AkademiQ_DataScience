import json
from datetime import datetime
import os

class DenetimKaydi:
    def __init__(self, dosya_yolu="denetim_kayitlari.jsonl"):
        self.dosya_yolu = dosya_yolu

    def kayit_ekle(self, asama: str, veri: dict):
        """
        Denetim kayıtlarını değiştirilemez (yalnızca eklenebilir) şekilde tutar.
        Her kayıt JSON Formatında yeni bir satıra eklenir (JSON Lines).
        """
        kayit = {
            "zaman_damgasi": datetime.utcnow().isoformat(),
            "asama": asama,  # Öneri, Onay veya Yürütme
            "detaylar": veri
        }
        
        # 'a' (append) kipi ile dosyayı açarak sadece sonuna ekleme yapıyoruz.
        with open(self.dosya_yolu, "a", encoding="utf-8") as dosya:
            dosya.write(json.dumps(kayit, ensure_ascii=False) + "\n")