import re

class GirdiDogrulayici:
    def __init__(self):
        # Enjeksiyon denemelerinde sık kullanılan kalıplar
        self.yasakli_kaliplar = [
            r"(?i)ignore all",
            r"(?i)system prompt",
            r"(?i)developer mode",
            r"(?i)bana iade (yap|ver)",
            r"(?i)return exactly"
        ]

    def enjeksiyon_taramasi(self, musteri_mesaji: str) -> bool:
        """
        Müşteri mesajında zararlı bir komut/talimat enjeksiyonu olup olmadığını kontrol eder.
        Zararlı kalıp bulunursa True döner.
        """
        for kalip in self.yasakli_kaliplar:
            if re.search(kalip, musteri_mesaji):
                return True
        return False

    def mesaj_ve_politika_ayristir(self, ham_veri: dict, politika_metni: str) -> dict:
        """
        Müşteri mesajı ve politika metnini ayrı ve açıkça işaretlenmiş bloklar halinde yapılandırır.
        """
        mesaj = ham_veri.get("musteri_mesaji", "")
        
        enjeksiyon_var_mi = self.enjeksiyon_taramasi(mesaj)

        return {
            "guvenli_girdi_yapisi": {
                "MUSTERI_BEYANI": mesaj,
                "SISTEM_POLITIKASI": politika_metni
            },
            "enjeksiyon_tespiti": enjeksiyon_var_mi,
            "durum": "Reddedildi - Talimat Enjeksiyonu Şüphesi" if enjeksiyon_var_mi else "Başarılı"
        }