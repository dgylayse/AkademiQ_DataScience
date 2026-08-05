# Sipariş Sonrası Talep Değerlendirme Sistemi 🛡️

Bu proje, müşteri taleplerini, sipariş geçmişini ve şirket kurallarını analiz ederek **yalnızca yapılandırılmış bir öneri nesnesi** üreten, güvenlik odaklı (secure by design) bir karar destek sistemidir. 

Adli bilişim ve siber güvenlik prensipleri gözetilerek tasarlanan bu mimaride, yapay zeka ve karar motorları hiçbir zaman doğrudan işlem yapma yetkisine sahip değildir. Üretilen her öneri, katı bir doğrulama katmanından geçer ve nihai yürütme için her zaman **insan onayına (human-in-the-loop)** ihtiyaç duyar.

## 🚀 Temel Özellikler ve Güvenlik Sınırları

*   **Talimat Enjeksiyonu (Prompt Injection) Savunması:** Müşteri mesajı içine gizlenmiş sistem komutlarını geçersiz kılmaya yönelik manipülasyon saldırıları, girdi katmanında regex ve kalıp analizi ile tespit edilip engellenir.
*   **Tekrarlanan İşlem (Replay Attack) Koruması:** Her onaylanmış işlem, sipariş ve öneri kimliğinden türetilen "tek seferlik işlem anahtarı" (SHA-256 hash) ile yürütülür. Aynı anahtarla yapılan mükerrer çağrılar yürütme birimi tarafından reddedilir.
*   **Değiştirilemez Denetim Kaydı (Immutable Audit Logs):** Sistemdeki tüm girdi, onay ve yürütme adımları, SOC analizlerine ve geriye dönük iz sürmeye uygun şekilde, yalnızca eklenebilir (append-only) JSONL formatında kaydedilir.
*   **Katı Şema Doğrulaması:** Karar motorunun, tanımlı veri yapısı (Pydantic) dışında hiçbir çıktı üretmesine izin verilmez. Şema dışı üretilen her yanıt, sistem tarafından geçersiz sayılarak otomatik olarak insana eskalasyon (escalate_to_human) sürecine sokulur.
*   **Durum ve Sürüm Kontrolü:** Yürütme anı ile onay anı arasındaki olası veri değişimleri ve eski politika sürümü kullanımları otomatik olarak yakalanır.

## 🛠️ Kullanılan Teknolojiler

*   **Dil:** Python 3.10+
*   **Şema Doğrulama & Veri Yapıları:** Pydantic
*   **Arayüz (İnsan Onay Katmanı):** Streamlit
*   **Test & Doğrulama:** pytest
*   **Sürekli Entegrasyon (CI/CD):** GitHub Actions
*   **Kriptografi & Loglama:** Hashlib, JSON, OS (Standart Kütüphaneler)

## 📂 Proje Dizini

```text
├── dokumanlar/                 # Mimari ve güvenlik sınırları belgeleri
├── kaynak/                     
│   ├── denetim_kaydi/          # Append-only loglama birimi
│   ├── dogrulama/              # Girdi, çıktı ve durum doğrulama katmanları
│   ├── karar_motoru/           # Pydantic yapılandırılmış karar şeması
│   ├── onay_arayuzu/           # Streamlit tabanlı yetkili onay ekranı
│   ├── politika_deposu/        # Sürüm kontrollü kural deposu
│   └── yurutme_birimi/         # Tek seferlik islem anahtarı ve yürütme
├── testler/                    # Sızma ve uçtan uca senaryo testleri
└── veri/ornek_senaryolar/      # Enjeksiyon ve çelişki barındıran JSON test verileri
