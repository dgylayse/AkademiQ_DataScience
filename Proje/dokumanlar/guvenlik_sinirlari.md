# Güvenlik Sınırları

Sistemin karşılaması gereken temel risk alanları ve bunlara karşılık gelen kontrol mekanizmaları şunlardır[cite: 1]:

*   **Eski veya çelişen politika kaynağı:** Politika belgesi merkezi bir depodan sürüm numarası ile çekilir[cite: 1]. Girdilerde sürüm uyuşmazlığı tespit edilirse işlem otomatik olarak insan onayına yönlendirilir[cite: 1].
*   **Talimat enjeksiyonu:** Müşteri mesajı ve politika metni ayrı ve açıkça işaretlenmiş bloklar halinde işlenir[cite: 1]. Müşteri mesajı hiçbir zaman politika kuralını geçersiz kılacak şekilde yorumlanmaz[cite: 1]. Çıktı, koddan bağımsız olarak politika sınırlarına karşı ayrıca doğrulanır[cite: 1].
*   **Onay sonrası sipariş durumunun değişmesi:** Yürütme öncesinde sipariş durumu yeniden sorgulanır ve onay anındaki durumla karşılaştırılır[cite: 1]. Uyuşmazlık tespit edilirse işlem durdurulur ve yeniden onaya sunulur[cite: 1].
*   **Aynı işlemin birden fazla kez yürütülmesi:** Her onaylanmış işlem, sipariş kimliği ve öneri kimliğinden türetilen tek seferlik bir işlem anahtarı ile yürütülür[cite: 1]. Aynı anahtarla yapılan ikinci bir çağrı reddedilir[cite: 1].
*   **Düşük kaliteli veya yetersiz kanıt:** Kanıt kalitesi alanı zorunludur[cite: 1]. Düşük veya belirsiz kanıt içeren öneriler otomatik onaya alınmaz ve insan değerlendirmesine bırakılır[cite: 1].
*   **Şema dışı veya beklenmeyen çıktı:** Tanımlı veri yapısına uymayan her çıktı geçersiz sayılır ve otomatik olarak insan onayına yönlendirilir[cite: 1]. Üretilen çıktı hiçbir zaman doğrudan komut olarak çalıştırılmaz[cite: 1].