# Sistem Mimarisi

## Karar Akışı
Sistem aşağıdaki sıralı adımlardan oluşur[cite: 1]:
*   **Girdi toplama:** Müşteri mesajı, sipariş verisi, iade geçmişi ve güncel politika sürümü bir araya getirilir[cite: 1].
*   **Girdi doğrulama:** Talimat enjeksiyonu taraması ve veri ile talimatın birbirinden ayrılması yapılır[cite: 1].
*   **Karar üretimi:** Tanımlı veri yapısı dışında hiçbir alan içermeyen bir öneri oluşturulur[cite: 1].
*   **Çıktı doğrulama:** Veri yapısı uygunluğu, politika sınırı kontrolü ve güven değeri değerlendirilir[cite: 1].
*   **Onay:** Yetkili kullanıcı öneriyi onaylar, reddeder veya düzenler[cite: 1].
*   **Durum doğrulama:** Onay anı ile yürütme anı arasında sipariş durumunun değişip değişmediği kontrol edilir[cite: 1].
*   **Yürütme:** Onaylanan işlem, tek seferlik işlem anahtarı ile gerçekleştirilir[cite: 1].
*   **Kayıt:** Öneri, onay ve yürütme adımlarının tamamı denetim kaydına işlenir[cite: 1].

*Not:* Karar motoru hiçbir aşamada doğrudan yürütme yetkisine sahip değildir[cite: 1]. Öneri ile yürütme arasında daima bir onay adımı ve bir durum doğrulama adımı yer alır[cite: 1].