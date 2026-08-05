import streamlit as st

def arayuz_olustur():
    st.title("Sipariş Sonrası Talep Değerlendirme - Onay Ekranı")
    st.markdown("Yetkili kullanıcı öneriyi bu ekrandan onaylar, reddeder veya düzenler.")
    
    # Şimdilik örnek bir öneri nesnesi (mock data) üzerinden arayüzü çiziyoruz.
    oneri_ornek = {
        "recommendation_id": "uuid-1234-5678",
        "order_id": "ORD-1001",
        "action": "full_refund",
        "amount_percent": 100,
        "justification": "Müşteri, teslimattan sonraki 14 gün içinde kanıt sunarak kusurlu ürünler için iade talep etmiştir.",
        "evidence_quality": "high",
        "requires_escalation": False
    }

    st.subheader(f"Sipariş ID: {oneri_ornek['order_id']}")
    
    # Düzenlenebilir alanlar
    secilen_aksiyon = st.selectbox(
        "Önerilen Aksiyon", 
        ['store_credit', 'partial_refund', 'replacement', 'full_refund', 'escalate_to_human', 'no_action'],
        index=3
    )
    
    gerekce = st.text_area("Gerekçe", oneri_ornek['justification'])
    
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button("İşlemi Onayla", type="primary"):
            st.success(f"{oneri_ornek['order_id']} numaralı sipariş için {secilen_aksiyon} aksiyonu onaylandı. (İşlem Anahtarı oluşturulmak üzere yürütme birimine aktarılacak)")
            
    with col2:
        if st.button("İşlemi Reddet"):
            st.error("İşlem reddedildi. Sistem kayıtlarına işlendi.")

if __name__ == "__main__":
    arayuz_olustur()