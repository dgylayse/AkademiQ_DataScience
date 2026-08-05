import hashlib

class YurutmeBirimi:
    def __init__(self):
        # Şimdilik kullanılan anahtarları bellekte tutuyoruz, 
        # ileride kalıcı bir veritabanına eklenebilir.
        self.kullanilan_anahtarlar = set()

    def islem_anahtari_uret(self, siparis_id: str, oneri_id: str) -> str:
        """
        Sipariş kimliği ve öneri kimliğinden türetilen tek seferlik bir işlem anahtarı oluşturur.
        """
        veri = f"{siparis_id}-{oneri_id}".encode('utf-8')
        return hashlib.sha256(veri).hexdigest()

    def islemi_yurut(self, siparis_id: str, oneri_id: str, aksiyon: str) -> dict:
        """
        Onaylanan işlemi tek seferlik anahtar kontrolü ile çalıştırır.
        """
        islem_anahtari = self.islem_anahtari_uret(siparis_id, oneri_id)
        
        if islem_anahtari in self.kullanilan_anahtarlar:
            return {
                "basari": False, 
                "mesaj": "Reddedildi: Bu işlem anahtarı daha önce kullanılmış (Tekrarlanan İşlem)."
            }
        
        # Anahtar kullanılmamışsa, işlemi simüle et ve anahtarı kaydederek tüket
        self.kullanilan_anahtarlar.add(islem_anahtari)
        
        return {
            "basari": True, 
            "mesaj": f"İşlem başarılı. {aksiyon} yürütüldü.", 
            "islem_anahtari": islem_anahtari
        }