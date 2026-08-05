class DurumDogrulayici:
    def __init__(self):
        # Bu yapı ileride veritabanından güncel sipariş durumunu çekecek şekilde güncellenir.
        pass

    def durum_degisti_mi(self, siparis_id: str, onay_anindaki_durum: str, guncel_durum_sorgusu: str) -> bool:
        """
        Onay anı ile yürütme anı arasında sipariş durumunun değişip değişmediğini kontrol eder.
        Durum değişmişse True döner, bu durumda işlem durdurulmalı ve onaya dönmelidir.
        """
        # Güncel durum sorgusu veritabanından veya harici servisten gelir
        guncel_durum = guncel_durum_sorgusu 
        
        if onay_anindaki_durum != guncel_durum:
            return True
            
        return False