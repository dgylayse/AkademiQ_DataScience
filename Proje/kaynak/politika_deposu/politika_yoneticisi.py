class PolitikaYoneticisi:
    def __init__(self):
        # Şimdilik veritabanı yerine bellek içi (in-memory) bir sözlük kullanıyoruz.
        # İleride SQLite'a bağlanabilir.
        self.politikalar = {
            "v1.0": "Müşteriler 30 gün içinde koşulsuz iade yapabilir.",
            "v1.2": "Müşteriler, teslimattan sonraki 14 gün içinde kanıt sunarak kusurlu ürünler için tam iade talep edebilir. Hasarlı veya çalışmayan ürünler için görsel kanıt zorunludur."
        }
        self.guncel_surum = "v1.2"

    def politika_getir(self, talep_edilen_surum: str = None) -> dict:
        """
        İstenen sürümü getirir. Sürüm belirtilmezse güncel sürümü döner.
        Eğer eski/farklı bir sürüm talep edildiyse çelişki bayrağını (conflict) True yapar.
        """
        surum = talep_edilen_surum if talep_edilen_surum else self.guncel_surum
        
        if surum not in self.politikalar:
            return {"hata": f"Sürüm {surum} bulunamadı."}

        conflict = surum != self.guncel_surum
        
        return {
            "surum": surum,
            "metin": self.politikalar[surum],
            "guncel_mi": not conflict,
            "celiski_tespit_edildi": conflict
        }