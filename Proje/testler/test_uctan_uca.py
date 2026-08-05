import json
import pytest
import os
from kaynak.dogrulama.girdi_dogrulama import GirdiDogrulayici
from kaynak.yurutme_birimi.yurutme import YurutmeBirimi

# Örnek senaryoların bulunduğu dizin (Alt çizgi ile güncellendi)
SENARYO_DIZINI = os.path.join(os.path.dirname(__file__), '..', 'veri', 'ornek_senaryolar')

def senaryo_yukle(dosya_adi):
    with open(os.path.join(SENARYO_DIZINI, dosya_adi), 'r', encoding='utf-8') as f:
        return json.load(f)

def test_talimat_enjeksiyonu_tespiti():
    """Talimat enjeksiyonu senaryosunun başarıyla yakalandığını test eder."""
    senaryo = senaryo_yukle("02_talimat_enjeksiyonu.json")
    dogrulayici = GirdiDogrulayici()
    
    sonuc = dogrulayici.enjeksiyon_taramasi(senaryo["musteri_mesaji"])
    assert sonuc is True, "Talimat enjeksiyonu yakalanamadı!"

def test_tekrarlanan_islem_engelleme():
    """İşlemin birden fazla kez yürütülmeye çalışılması senaryosunu test eder."""
    senaryo = senaryo_yukle("05_tekrarlanan_islem.json")
    yurutme = YurutmeBirimi()
    
    siparis_id = senaryo["siparis_verisi"]["order_id"]
    oneri_id = "test-oneri-id-123"
    
    # İlk yürütme başarılı olmalı
    ilk_islem = yurutme.islemi_yurut(siparis_id, oneri_id, "full_refund")
    assert ilk_islem["basari"] is True
    
    # Aynı sipariş ve öneri ile ikinci yürütme reddedilmeli
    ikinci_islem = yurutme.islemi_yurut(siparis_id, oneri_id, "full_refund")
    assert ikinci_islem["basari"] is False
    assert "Reddedildi" in ikinci_islem["mesaj"]