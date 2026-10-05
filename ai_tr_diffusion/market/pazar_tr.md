# Pazar çalışması: P1 (Gediz sulak alan veri seti) ve P2 (ÇED biyoçeşitlilik ön taraması) için ürün modelleri

Tarih: 5 Ekim 2026. Bu metin `market_en.md` dosyasının sadeleştirilmiş Türkçe karşılığıdır; dört araştırma kolunun (R1–R4) sentezidir, yeni arama içermez. [R3-012] gibi kodlar `sources_market.csv` kaynak numaralarıdır.

- Sayıların hepsi "arama sonucundan" gelir; çoğu sayfa baştan sona okunmadı, bazıları arama özetidir. Dış kullanımdan önce birincil sayfadan doğrulayın.
- **"Kaynaklı"** fiyat bir kaynağa dayanır (5 Ekim 2026'da, orijinal para biriminde). **"Tahmin"** arkasında kaynak olmayan kanaattir. Türkiye'ye ait hiçbir ödeme isteği rakamı kaynaklı değildir.
- Sizin kısıtlarınız (BRIEF §7): tek araştırmacı (Ege Üniversitesi, sulak alan ekolojisi; herpetofauna, Odonata, bitki örtüsü, uzaktan algılama) ve fatura kesip hibe alabilen bir kooperatif. ÇED Yeterlik Belgeniz yok; ÇED raporunu yalnızca belgeli firmalar hazırlayabilir [R3-020]. Bu yüzden P2'de ÇED yazarı değil, belgeli firmalara, geliştiricilere ve kredi verenlere tedarikçi olursunuz. Ürünler, ajan hatlarıyla üretilen standart dosyalar (XLSX, DOCX/PDF, GeoPackage) olmalı. Ekim'de başlayan pencere Odonata ve kurbağa mevsiminin dışında kalır; ilk ürünler eldeki veriye dayanır, yeni saha işi 2027 baharındadır.

---

## 1. Kanıt ne diyor

**P1 (sahada etiketlenmiş sulak alan verisi)**

| Konu | Olgu |
|---|---|
| Etiket için ödeyen | Kimse. Başlıca ölçüt veri setleri açık lisanslı; temel model (FM: büyük genel amaçlı yapay zekâ modeli) ekipleri bedava kullanır [R1-011][R1-030][R1-006]. |
| Tek nakit alıcı | Orman karbonu ölçüm-doğrulama (MRV) firmaları, yalnızca orman biyokütlesi için; Sylvera 10 milyon dolardan fazla harcadığını söylüyor. Sulak alan veya fauna etiketi için ödeme yok [R1-082][R1-079]. |
| Doğrulama ihtiyacı | Gerçek. WorldCover otsu sulak alanda zayıf [R1-015]; Copernicus HRL geçici ıslak alanda zayıf [R2-058]; MWO/Tour du Valat haritalarını yerel envanterle doğruluyor, Türkiyeli ortağı yok [R2-053]. |
| Konsorsiyum iş paketi ve ölçek | BiodivMon 33 proje [R2-036], BiodivConnect 36 proje [R2-031]; TÜBİTAK 1071 proje başına en çok 160 bin € (kaynaklı) [R2-034]. |
| Türkiye'de veri alımı | Etiketli veri için satın alma, lisans veya ihale bulunmadı. Para DKMP il envanter ihalelerinden [R2-011] ve hibelerden geçiyor. |

**P2 (ÇED biyoçeşitlilik ön taraması)**

| Konu | Olgu |
|---|---|
| ÇED hacmi | 2025: 716 olumlu, 3.056 "gerekli değildir", 304 olumsuz; olumluların 422'si enerji. Toplamlar tutmuyor, doğrulanmalı [R3-004]. |
| 2026 değişikliği | 05.03.2026'da "gerekli değildir" sonucu kaldırıldı [R3-011]; tam rapor sayısının artması beklenir. DKMP rüzgar ve madende ekosistem, RES/GES'te ornitolojik rapor (ODR) istiyor [R3-018][R3-019]. 05.09.2026 sulak alan değişikliği sürdürülebilir kullanım bölgelerinde yenilenebilire izin veriyor [R3-013]. |
| Mahkeme | Gaia RES'in olumlu kararı flora ve kuş izlemesi yetersiz diye iptal edildi; türbinler dikildikten sonra yeniden verildi [R3-053][R3-054]. Germencik bilirkişi heyeti 6 amfibi ve 6 sürüngen listelenmiş buldu; literatür çok daha fazlasını gösteriyordu [R3-055]. |
| IBAT fiyatları | IBAT: küresel ücretli ön tarama aracı. Abonelik yılda 0–35 bin dolar; tek rapor 750 (yakınlık), 1.250 (PS6), 5.000 dolar (çok alan), kaynaklı [R4-001][R4-004]. Yalnızca küresel ve "ön tarama" konumlu [R4-010]. |
| Kredi verenler | IFC PS6 (biyoçeşitlilik standardı) bölgesel deneyimli dış uzman şart koşuyor [R4-012]. Enerjisa'nın 750 MW rüzgar portföyünün kritik habitat değerlendirmelerini (CHA) Mott MacDonald ve ERM yazmış [R4-051][R3-028][R3-029]. |
| Türkçe araç ve veri | Türkiye için ön tarama aracı bulunamadı; küresel araçların Türkçe çıktısı yok [R4-015]. Nuh'un Gemisi'nde (yaklaşık 2 milyon kayıt) **Odonata yok** [R4-060]. |
| Ücret verisi | Flora-fauna raporu için kamuya açık fiyat yok; bir danışmanlık ODR için 140–176 bin TL yazıyor (kaynaklı, doğrulanmadı) [R2-085]. Yabancı şablon bng.ai £249–1.999 (kaynaklı) [R4-022]. |

**Yokluklar** (yaklaşık 160 aramaya dayanır, pazar denetimine değil): etiket için nakit alıcı, Türkiye'de ücret veya ödeme isteği rakamı, kamuya açık CHA ücreti, belgeli firma sayısı, Nuh'un Gemisi yeniden kullanım şartı.

---

## 2. Ürün modelleri

On bir model, on bir ayrı amaçtır; hiçbiri diğerinin "varyantı" değildir (tek birleştirme: brifteki "poligon başına rapor" ile "uzman doğrulamalı kademe" aynı ürünün kademeleri olduğundan P2-1'dedir). Kanıt gücü yalnızca talebi derecelendirir, uygulanabilirliği değil.

### P1: etiketli veri tarafı

**P1-1 Açık ölçüt + ticari lisans (çift lisans)**
1. *Amaç:* Gediz'i Akdeniz sulak alanları için başvuru test seti yapmak; ticari temiz etiket isteyenden lisans almak.
2. *Kim öder, neden:* ticari FM, ses modeli ve MRV ekipleri; BirdNET modelleri ticari olmayan lisanslı [R1-051], Maxar açık verisi de [R1-070]. Ödeyen kanıtı yok [R1-006][R1-082].
3. *Girdi → çıktı; olmazsa olmaz:* uydu parçaları, drone, habitat poligonları, pasif akustik kayıt (PAM), Odonata/herp fotoğrafı → veri kartı, sabit bölmeler, başlangıç skorları (Zenodo). Gözlemci/tarih kayıtlı etiket, ayrılmış test alanı, lisans ayrımı.
4. *Fiyat:* çapa yok; pazar yeri veri setleri 5–500 dolar (kaynaklı) [R1-077]. Ticari lisans yılda 3–10 bin € (tahmin); ilk yıl geliri sıfıra yakın.
5. *90 gün:* eldeki tez ve ortak verisinden v0 yayını, DOI, bir başlangıç skoru, veri makalesi taslağı.
6. *Savunulabilirlik:* açık yayında veri hendeği zayıf; kalıcı olan zaman serisi ve yeniden etiketleyen ekip. *Risk:* açık yayın ücretli lisansı yer; veri hakları (üniversite, DKMP izni) belirsiz. *Kanıt:* zayıf.

**P1-2 Doğrulama ortağı (iş paketi olarak saha doğrulaması)**
1. *Amaç:* veri değil, bağımsız harita doğruluk değerlendirmesi satmak (MWO, Copernicus HRL, Global Wetland Watch, SAYBİS/DKMP envanterleri).
2. *Kim öder, neden:* hibe bütçeli konsorsiyumlar; "güzel görünen haritalar yanlış olabilir" [R2-054][R1-025]; saha doğrulaması "hayati" [R1-022].
3. *Girdi → çıktı; olmazsa olmaz:* ortağın haritası ve sınıfları → sınıfa göre tabakalı örnekleme, saha ve drone referansı, hata matrisi ve güven aralıkları, hata haritası, PDF rapor, referans set DOI'si. Geçici ıslak alan protokolü [R1-104]; hataların ekolojik teşhisi; birden çok ürüne yeniden kullanılabilen referans set.
4. *Fiyat:* TÜBİTAK 1071 tavanı (kaynaklı) [R2-034]. İş paketi başına 25–80 bin € (tahmin); tek ürün tek alan doğrulaması 8–20 bin € (tahmin).
5. *90 gün:* eldeki Gediz noktalarıyla 2–3 açık ürünü doğrulayıp 6 sayfalık "Gediz doğrulama notu" yazmak; kooperatife AB katılımcı kodu (PIC) almak; hazırlanan bir teklife ortak olmak.
6. *Savunulabilirlik:* Tour du Valat ilişkisi, saha izni, mevsimlik sulak alan bilgisi, DKMP ile Türkçe iletişim. *Risk:* para çağrıdan 12–18 ay sonra ve yalnızca kazanılırsa gelir; akademik ortaklar öğrenciyle bedava yapabilir. *Kanıt:* orta (ihtiyaç ve hibe belgeli; dışarıdan doğrulayıcıya ödeme örneği yok).

**P1-3 Ölçüt dahil edilmesi / yarışma kolu (akademik sermaye)**
1. *Amaç:* Gediz görevlerini model ekiplerinin kullandığı yerlere (PANGAEA, BEANS, BirdCLEF tarzı yarışma) koyup atıf ve "bölgesel uzman" itibarı kazanmak; P1-2 ve P2-2'yi besler.
2. *Kim öder, neden:* kimse. BirdCLEF+ 2025 ödülü 50 bin dolar (kaynaklı), 9.636 katılımcı [R1-056]; açık amfibi sınıflandırıcıları "büyük ölçüde yok" [R1-101].
3. *Girdi → çıktı; olmazsa olmaz:* güçlü, zaman damgalı kurbağa etiketi → gizli etiketli test seti, görev tanımı, başlangıç notebook'u, veri makalesi. Gizli test etiketi, BirdSet/BEANS uyumu, CC-BY.
4. *Fiyat:* yok; maliyeti siz taşırsınız.
5. *90 gün:* PANGAEA ve BEANS'e tek sayfalık görev tanımı (GitHub issue) [R1-002][R1-036]; eldeki kayıtlardan "Gediz-Anura v0" (10–20 saat etiketli klip, tahmin).
6. *Savunulabilirlik:* Doğu Akdeniz için ilk hareket avantajı. *Risk:* gelir yok, bakımcılar reddedebilir, tez zamanıyla yarışır. *Kanıt:* kullanım için güçlü, nakit için yok.

**P1-4 Gediz yaşayan laboratuvar (ücretli referans alan)**
1. *Amaç:* kalıcı parsel, PAM ağı, tekrarlı drone ve etiketli zaman serisi olan izinli bir test alanı sunmak.
2. *Kim öder, neden:* Akdeniz pilot alanı arayan AB projeleri, sensör satıcıları [R4-045][R4-048]; belediye Gediz izlemesini 2020'den beri destekliyor [R2-080][R2-082]. Alan erişimine ödeme yapıldığına dair kanıt yok.
3. *Girdi → çıktı; olmazsa olmaz:* alan paketi → kampanya verisi ve doğrulama raporu. Kalıcı parseller, zaman damgalı PAM, izin ve lojistik, veri paylaşım şablonu.
4. *Fiyat:* çapa yok; pilot kampanya başına 10–30 bin € (tahmin).
5. *90 gün:* tek sayfalık teklif, alan haritası, veri envanteri, belediyeden destek mektubu; bir teklifte gösterim alanı olarak yer almak.
6. *Savunulabilirlik:* fiziksel ve izne dayalı, kopyalaması en zor model. *Risk:* talep kanıtı yok; sabit maliyet yüksek (hırsızlık, bakım, kuş üremesine rahatsızlık). *Kanıt:* zayıf.

**P1-5 Envanter ihalelerinde alt yüklenicilik (yapay zekâ destekli etiketleme)**
1. *Amaç:* devletin zaten finanse ettiği envanterlerden kazanmak: ihale kazananlara herp, Odonata ve PAM modülü sunmak; yapay zekâ ön etiketini (BirdNET/Perch) siz kontrol edersiniz.
2. *Kim öder, neden:* DKMP il envanteri (Muğla 540 gün, Ankara 730 gün) [R2-010][R2-011] ve ÇŞB ihaleleri [R2-016]; kazananlar danışmanlıklar ve üniversiteler [R2-014][R2-015]. Çok taksonlu şartname herp/Odonata uzmanı ister.
3. *Girdi → çıktı; olmazsa olmaz:* şartname → saha ve PAM verisi, Nuh'un Gemisi biçiminde CSV, haritalar, Türkçe rapor bölümleri. Ön etiket günlüğü, Odonata modülü, ses/fotoğraf kanıtı.
4. *Fiyat:* ihale tutarı bulunamadı. Büyüklük çapası: bir firmanın ODR'si, 140–176 bin TL (kaynaklı, doğrulanmadı) [R2-085]. Takson modülü başına, il başına 150–400 bin TL (tahmin).
5. *90 gün:* ajanlarla 2024–26 envanter ihalelerini ve kazananlarını EKAP'tan listelemek; üç kazananla görüşmek; fiyat listesi; kooperatifin yeterlilik belgesi ve üniversitenin dış iş kurallarını kontrol etmek.
6. *Savunulabilirlik:* zor taksonlarda uzmanlık, bölgesel varlık. *Risk:* verinin sahibi DKMP, P1'de yeniden kullanımı engelleyebilir; marj düşük. *Kanıt:* orta (harcama gerçek; tutarlar ve alt yüklenici isteği doğrulanmadı).

### P2: ÇED ön tarama tarafı

**P2-1 Kademeli poligon ön taraması (otomatik + uzman doğrulamalı)**
1. *Amaç:* arazi kiralamadan, YEKA teklifinden veya ÇED dosyasından önce "bu alan hangi biyoçeşitlilik sorunlarını çıkarır?" sorusuna hızlı, ucuz, kaynaklı yanıt.
2. *Kim öder, neden:* RES/GES/JES geliştiricileri (enerji, olumlu kararların yaklaşık yarısı veya fazlası [R3-004]) ve ön kapsam çalışan danışmanlıklar. Kaçırılan tür aylara mal olur [R3-053][R3-054]. Fiyat modeli yurtdışında kanıtlı [R4-001][R4-022].
3. *Girdi → çıktı; olmazsa olmaz:* poligon ve proje türü → TR/EN 8–15 sayfa PDF, XLSX tür tablosu, GeoPackage, kaynak günlüğü; uzman kademesinde imzalı beyan. Türkiye katmanları (Nuh'un Gemisi [R4-060], Amfibi veri tabanı [R2-072], CC0/CC-BY GBIF [R1-065], Ramsar/SAYBİS [R2-021], ÇED Ek-5 [R3-012], Emerald [R4-069]); satır bazında kaynak; adıyla anılan uzman.
4. *Fiyat:* üç kademe, TL. Yapı bng.ai'yi izler (£249 / £1.499 / £1.999, kaynaklı) [R4-022], IBAT yakınlık raporunun 750 dolarının altında (kaynaklı) [R4-001]; £1.250 ara çapa (kaynaklı) [R4-021]. Otomatik 150–350 €, uzman doğrulamalı 700–1.500 €, saha ziyaretli 1.500–3.000 € (hepsi tahmin).
5. *90 gün:* ajan hattını kurmak; Germencik'te geriye dönük test: hat, heyetin eksik bulduğu amfibi/sürüngenleri işaretliyor mu [R3-055]? Gaia'da aynı test; Ege'deki danışmanlık ve geliştiricilere 10 ücretsiz rapor; anonim örnek yayımlamak.
6. *Savunulabilirlik:* Türkçe katmanlar, kendi Ege kayıtlarınız, bölgesel uzman; IBAT bölgesel uzman olarak imza atamaz [R4-012]. *Risk:* veri lisansı (Nuh'un Gemisi şartı bilinmiyor; WDPA/KBA/IUCN ticari kullanımı kısıtlı olabilir, genel bilgi, doğrulayın), Türkiye'de ödeme isteği bilinmiyor, kaçırılan türün sorumluluğu. *Kanıt:* orta.

**P2-2 Kredi verenlere uygun PS6/PR6 kritik habitat taraması + anket tasarımı**
1. *Amaç:* CHA'nın ilk iki adımını (ulusal veriyle tetikleyici taraması, kredi verenin kabul edeceği temel anket tasarımı) baş danışmanın CHA'sına konabilecek biçimde teslim etmek.
2. *Kim öder, neden:* uluslararası finans arayan geliştiriciler (Enerjisa örüntüsü) [R4-051][R2-086]; bölgesel uzman çağırmak zorunda olan Mott MacDonald ve ERM [R4-012][R3-028][R3-029]; Türk Ekvator bankaları [R3-049]. IBAT'ın PS6 raporu yalnızca ön tarama [R4-004].
3. *Girdi → çıktı; olmazsa olmaz:* alan ve proje tanımı → İngilizce tarama notu (özellik × PS6 ölçütü tablosu [R4-011]), analiz alanı (EAAA) haritaları, uzman beyanları, anket tasarımı, GIS paketi. Eşikli ölçüt matrisi; herp/Odonata için imzalı uzman beyanı, kuş ve yarasa için adıyla anılan ortak.
4. *Fiyat:* taban IBAT PS6 raporu 1.250 dolar (kaynaklı) [R4-004]; kamuya açık CHA ücreti yok [R4-059]. Alan başına 4–12 bin € veya gün ücreti 350–600 € (tahmin); referans: Birleşik Krallık kıdemli ekolog £280–450/gün (kaynaklı) [R4-076].
5. *90 gün:* herkese açık Enerjisa CHA'larından şablon (Ihlamur: 6 kuş, 3 bitki, 13 memeli, 1 sürüngen [R3-044]); açıklanmış bir proje için kör "gölge tarama" yapıp yayımlanmış CHA ile karşılaştırmak; Mott MacDonald Türkiye ve ERM'ye sunmak.
6. *Savunulabilirlik:* bölgesel uzman şartı, ulusal veri, yayın geçmişi. *Risk:* pazar 2–3 danışmanlıkta ve yavaş; rüzgarda kuş/yarasa baskın, herp küçük kalabilir (23 özellikten 1 sürüngen [R3-044]). *Kanıt:* orta.

**P2-3 ÇED biyoçeşitlilik bölümlerinin dava riski denetimi**
1. *Amaç:* taslak veya sunulmuş flora-fauna bölümünde boşluk analizi: listelenen türler ile beklenenler, anket zamanı ile takson mevsimselliği.
2. *Kim öder, neden:* iki taraf var ve **kooperatif birini seçmek zorunda.** Savunma tarafı: geliştirici ve danışmanlıklar [R3-053]. Karşı taraf: belediye, dernek, baro, hukuk büroları [R3-055][R3-031][R3-058]. Danıştay kararları iki yöne de gidiyor [R3-057].
3. *Girdi → çıktı; olmazsa olmaz:* ÇED raporu (PDF) ve poligon → boşluk matrisi, risk derecesi, imzalı Türkçe not. PDF'den tür çıkarımı, P2-1 motorundan beklenen liste, mevsim/yöntem denetleyicisi.
4. *Fiyat:* bilirkişi ücreti için kaynak yok. Denetim başına 1.000–3.000 € (tahmin); dernek işi hibeyle.
5. *90 gün:* 5 kamuya açık Ege RES/GES ÇED raporu ve Germencik dosyasını denetleyip anonim yöntem notu yayımlamak.
6. *Savunulabilirlik:* herp/Odonata derinliği. *Risk:* **çıkar çatışması**: dernek tarafı P2-1, P2-2 ve P2-4 satışını zedeler (tersi de); ücretli taraf işi bilirkişi atanmasıyla bağdaşmayabilir. *Kanıt:* ihtiyaç orta, ödeme isteği zayıf.

**P2-4 Danışmanlıklar için beyaz etiketli ÇED bölümü taslağı**
1. *Amaç:* danışmanlığın markasıyla, mevzuat biçiminde (Ek-3/Ek-4 [R3-010]) flora-fauna bölümü taslağı; saha doğrulama ve imza danışmanlığın biyologlarında. Çıktısı tarama raporu değil, bölümün kendisidir.
2. *Kim öder, neden:* Yeterlik belgeli firmalar (sayısı bilinmiyor) [R3-020][R3-021]; orta ölçekli firmalar bu raporları pazarlıyor [R3-026][R3-027]. Yurtdışında ERM IBAT kullanıyor [R4-008]; Türkiye kanıtı yok.
3. *Girdi → çıktı; olmazsa olmaz:* poligon → düzenlenebilir Türkçe DOCX bölüm, GeoPackage, saha doğrulama listesi. ÇED biçimine uygun şablon, otomatik statü sütunları, doğrulanmamış satır işareti.
4. *Fiyat:* IBAT Basic yılda 5 bin, Pro 15 bin dolar (kaynaklı) [R4-001]; NatureServe kullanıcı başına yılda 600 dolar (kaynaklı) [R4-017]. Bölüm başına 150–400 € veya firma başına yılda 2–5 bin € (tahmin).
5. *90 gün:* 3 danışmanlıkta canlı projelere taslak yazıp kazanılan masa başı saati ölçmek.
6. *Savunulabilirlik:* zayıf; şablonu genel bir dil modeliyle taklit etmek kolay, kalıcı olan herp/Odonata içeriği. *Risk:* sıradanlaşma, imzalı raporda sorumluluk, eleştirilen kopya tür listelerini hızlandırma [R3-031]. *Kanıt:* zayıf.

**P2-5 Yenilenebilir enerji için sulak alan bölgesi ve kümülatif etki değerlendirmesi**
1. *Amaç:* 05.09.2026 değişikliği sonrası sulak alan içinde veya yakınındaki enerji projelerini değerlendirmek (çevresel akış ve kümülatif etki şartları [R3-013][R3-014]): su baskını, habitat, sulak alana bağımlı herp, Odonata ve su kuşları, kümelenmiş projelerin toplam ayak izi.
2. *Kim öder, neden:* sulak alan bölgesinde izin arayan geliştiriciler; denetleyici olarak komisyonlar ve DKMP. Bağlam: yoğun Ege rüzgarı [R3-007], 14 Ramsar alanı [R2-021], SAYBİS'te 6.418 sulak alan [R2-018]. Kural yeni; tedarikçi bulunmadı (çıkarım, alıcı kanıtı yok).
3. *Girdi → çıktı; olmazsa olmaz:* proje ve sulak alan sınırı → Türkçe rapor, Sentinel su baskını zaman serisi, habitat haritası, komşu projeler haritası [R3-006][R3-063], çevresel akış işaretleri. Koruma bölgesi kontrolü, uzman imzası.
4. *Fiyat:* çapa yok; proje başına 3–8 bin € (tahmin).
5. *90 gün:* Ege sulak alanları için herkese açık "yenilenebilir × sulak alan bölgeleri" atlası; hem talep testi hem tanıtım kartı.
6. *Savunulabilirlik:* tam sizin profiliniz (sulak alan uzaktan algılaması, delta ekolojisi, Tour du Valat yöntemleri). *Risk:* kural tartışmalı; koruma ortakları karşı çıkabilir, itibar riski; hacim bilinmiyor. *Kanıt:* zayıf–orta (mevzuat dayanağı belgeli, alıcı değil).

**P2-6 Türkiye herpetofauna/Odonata referans katmanı (veri/API)**
1. *Amaç:* amfibi, sürüngen ve Odonata için uzman doğrulamalı kayıt ve dağılım katmanı; Nuh'un Gemisi'ndeki Odonata boşluğunu doldurur [R4-060].
2. *Kim öder, neden:* doğa-risk platformları [R4-036][R4-031], Türkiye CHA'sı yazan danışmanlıklar, DKMP. IBAT küresel menzil haritası kullanıyor [R4-006]; 38 herp türü değerlendirilmemiş (arama özeti) [R4-066]. Alıcı bulunmadı.
3. *Girdi → çıktı; olmazsa olmaz:* literatür, açık lisanslı kayıtlar, Amfibi veri tabanı [R2-072], kendi kayıtlarınız → kayıt tablosu, 1 km dağılım modeli rasterleri, statü tablosu, sürümlü DOI. Güven işaretli kayıt, Odonata dahil, kaba katman açık/ince katman ücretli, hassas türlerde konum bulanıklaştırma.
4. *Fiyat:* NatureServe veri lisansı en az 10 bin dolardan bölgesel 100 bin dolara (kaynaklı) [R4-016]. Ticari lisans sahibi başına yılda 5–15 bin € (tahmin); araştırmaya ücretsiz.
5. *90 gün:* literatür, CC-BY iNaturalist ve kendi kayıtlarınızdan "Batı Anadolu Odonataları v0" ve veri makalesi taslağı; DKMP'ye katkı olarak sunmak.
6. *Savunulabilirlik:* ihmal edilmiş taksonda uzman doğrulaması. *Risk:* çok küçük alıcı havuzu; kaynak kayıtlar ticari olmayan lisanslı olabilir [R1-067]; konum sızıntısı hassas türlere zarar verebilir. *Kanıt:* zayıf.

---

## 3. Tasarım taslakları

Uzmanın (sizin) imza attığı yerler **koyu** işaretlidir.

### 3A. P2-1 kademeli ön tarama (P2-1, P2-2, P2-3 ve P2-4'ün ortak motoru)

**Alım.** MVP'de web uygulaması yok; form veya e-posta. Müşteri poligon, proje türü, aşama (alan seçimi, ÇED dosyası, finansman), kademe ve dili bildirir.

**Hat (ajan aşamaları):**
1. Geometri: dosyayı doğrular, 1/5/10 km tampon çıkarır.
2. Bağlam: idari birimler, arazi örtüsü, ıslak alan göstergeleri; Ramsar/SAYBİS, Ek-5, Emerald ve KBA ile örtüşme (her katmanda lisans işareti).
3. Kayıtlar: Nuh'un Gemisi il çıktısı, CC0/CC-BY GBIF, Amfibi veri tabanı, iNaturalist ve sizin kayıtlarınız; tekrarları ayıklar, en yakın kayıt mesafesini hesaplar.
4. Literatür: DergiPark makaleleri ve tezler; tür-yer iddiaları sayfa atıflı çıkarılır.
5. Olasılık: kayıt mesafesi, habitat ve mevsimden Yüksek/Orta/Düşük/Bilinmiyor; kurallar sürümlü ve raporda basılı.
6. Statü: IUCN, Bern, CITES, ulusal liste, endemizm.
7. Boşluk ve anket: takson × ay takvimi, yöntem ve çaba.
8. Derleyici: TR/EN PDF, XLSX, GeoPackage.
9. Kalite: her satırın kaynağı olmalı; PDF, XLSX ve GeoPackage sayıları tutmalı.

**Uzman, 8. ve 9. aşama arasında (yalnızca uzman kademelerinde).** XLSX'te her tür satırını "kabul, düşür, ekle, yorum" diye işaretlersiniz (rapor başına 30–90 dakika, tahmin); **kapsam ve sınırları belirten beyanı imzalarsınız**; isteğe bağlı saha ziyareti eklenir.

**Alıcının gördüğü PDF:** (1) tek sayfalık özet ve trafik ışıkları; (2) harita; (3) korunan ve hassas alanlar; (4) tür-olasılık tablosu; (5) veri boşlukları; (6) mevsime göre anket programı; (7) "mahkeme bilirkişisinin görmeyi bekleyeceği türler" (Germencik dersi); (8) kaynaklar; (9) **uzman beyanı** ve sınırlar: bu bir ön taramadır, ÇED raporu veya CHA değildir.

### 3B. P2-2 kredi veren paketi (3A'ya eklenir)

Ek aşamalar: 10. PS6/PR6 (her özelliği ölçüt 1–5 ve PR6'ya eşler [R4-011]); 11. analiz alanı (EAAA) sınırı, takson grubuna göre; 12. uzlaştırma (müşteri IBAT raporu verirse ulusal kayıtlarla karşılaştırır).

**Uzman rolü en ağır adım:** herp/Odonata tetikleyicileri için tür uzmanı beyanlarını **siz yazıp imzalarsınız**; kuş ve yarasayı ortak üstlenir. Alan başına yaklaşık 1–2 gün (tahmin). Teslim İngilizce: yönetici özeti, PS6 tetikleyici matrisi, EAAA haritaları, uzman beyanları, denetlenebilir anket tasarımı, veri eki ve "CHA baş danışmanın belgesidir" ifadesi.

### 3C. P1-2 doğrulama iş paketi

Çerçeve: ortağın teklifine yazılan "İP-x: Doğu Akdeniz için bağımsız saha doğrulaması". Hat: (1) ortağın haritası alınır; (2) ajanlar tabakalı örnekleme tasarlar; (3) mevsime göre saha ve drone planı; (4) QField/ODK ile veri girişi, GeoPackage çıktısı; (5) ajanlar doğruluk ve alan tahminini hesaplar; (6) habitat bazında hata teşhisi; (7) rapor ve referans set yayını (DOI).

**Uzman:** her referans birimini siz etiketler veya doğrularsınız, belirsiz birimlerin gerekçesini **kayda geçirir, raporu imzalarsınız** (4. ve 6. aşama). Ortak; rapor, hata atlası, açık referans set ve ortak yazarlı makale alır. İkinci ürünü aynı referansla doğrulamak yalnızca 1., 5. ve 6. aşamayı gerektirir.

---

## 4. Sıralama ve gerekçe

Planlayıcı dört ölçütü bu sırayla tarttı: birinin ödeyeceği gösterilmiş mi; ilk fatura ne kadar hızlı gelir; model sizin avantajınızı (Ege kayıtları, herp/Odonata uzmanlığı, Tour du Valat, çok ajanlı hatlar) ne kadar kullanıyor; bir sonraki modelin ihtiyaç duyduğu varlığı üretiyor mu.

**1. P2-1 kademeli poligon ön taraması.** Hacim, mevzuat baskısı, belgeli başarısızlık maliyeti ve fiyatı bilinen yabancı şablon yalnızca bu modelde bir arada: yılda yaklaşık 3.800 ÇED kararı ve enerjinin yarısı civarı, Mart 2026 değişikliği, eksik herp ve kuş verisine dayanan iki mahkeme vakası, IBAT'ın 750 doları ve Birleşik Krallık uzman kademesi £1.250–1.999 (ikisi de kaynaklı). Türkiye'de bunu yapan yok; küresel araçlar Türkçe çıktı vermiyor, Odonata içermiyor. Diğer tüm P2 modellerinin motorunu da kurar. Eksik tek şey Türkiye'de ödeme isteği; 90 günde on ücretsiz raporla sınanır. **Önce bunu yapın; Germencik geriye dönük testi devam/dur kararıdır.**

**2. P1-2 iş paketi olarak doğrulama ortağı.** Veri seti fikrinin doğru biçimi. Araştırma saf sürümü öldürdü: model ekipleri etikete ödemiyor, tek nakit alıcı orman karbonu firmaları. Ama doğrulama ihtiyacı belgeli ve konsorsiyumlar bunu TÜBİTAK 1071 ölçeğinde (proje başına yaklaşık 160 bin €, kaynaklı) iş paketi olarak ödüyor. Aynı saha işi, P2-1'in kayıtlarını ve IFC PS6'nın aradığı "bölgesel uzman" geçmişini üretir. Bunu ürün olarak değil, Tour du Valat ve bir sonraki Biodiversa+ çağrısı üzerinden yürütün.

**3. P2-2 PS6/PR6 tarama ve anket tasarımı.** Alıcılar az ama başka bir para biriminde ödüyor: Enerjisa'nın 750 MW'lık Ege paketinin uluslararası danışmanlık yazımı CHA'ları var, IFC bölgesel uzman şart koşuyor, TSKB ve Garanti BBVA Ekvator tipi kurallar uyguluyor. P2-1 motoruna ve görünür bir uzman geçmişine dayandığı için takipçidir. Geliştiriciye doğrudan değil, Mott MacDonald ve ERM'ye alt yüklenici modülü olarak sunun.

**Yanınızda taşıyın, öne çıkarmayın.** P1-3 ucuzdur ve atıf almanın en ucuz yoludur; 2027 saha sezonunun yan ürünü yapın. P1-5, bir ihale kazananı herp veya Odonata isterse bir teklife değer; Ankara ihalesi 16 Ekim 2026'da kapanıyor, çok yakın, bir sonrakini hedefleyin. P2-6, P2-1 kayıtlarından kendiliğinden doğar, ayrıca kurulmaz.

**Şimdilik reddedilenler.** P2-3 (dernekler için dava denetimi): ihtiyaç gerçek, ödeyen yok ve çıkar çatışmasıyla P2-1 ile P2-2'yi kapatır; kooperatif dernek tarafını seçerse bu lider ürün olur, P2-1 bırakılır. P2-4: danışmanlıklar isteyene kadar bekleyin. P1-1 ticari lisans: ödeyen kanıtı yok; açık yayınlayıp seçeneği saklayın. P1-4: yalnızca finanse edilmiş bir proje içinde. P2-5: 05.09.2026 yönetmeliğini izleyin, pilot görüşmelerden sonra yeniden bakın.

**Başlamadan önce vereceğiniz karar: kooperatif ÇED masasının hangi tarafında?** Geliştiriciler ve danışmanlıklar öder; belediyeler ve dernekler ödemez. Sıralama ödeyen tarafı varsayar ve ürünü etki hükmüyle değil, ön tarama ile anket tasarımıyla sınırlı tutar. Sonra inşadan önce üç ucuz kontrol: örnek raporla Ege danışmanlıklarına beş telefon; DKMP'ye Nuh'un Gemisi şartları için bir e-posta; üniversite hukuk ofisine kooperatif üzerinden ücretli iş için bir telefon.

---

## 5. İlk 90 gün (Ekim–Aralık 2026)

Tarihler §4 sıralamasından ve §7 planlayıcı sıralamasından türetilmiş önerilerdir; yalnızca 16 Ekim ihale açılışı kaynaklı bir tarihtir [R2-011].

**5–16 Ekim**
- [ ] Taraf kararı (geliştirici/danışmanlık tarafı) yazılı not.
- [ ] Üç ucuz kontrolü başlatın: üniversite hukuk ofisi, DKMP e-postası, beş danışmanlık listesi.
- [ ] Nuh'un Gemisi portalında herhangi bir Odonata türünü sorgulayın (5 dakika).
- [ ] 16 Ekim: Ankara IKN 2026/1788766 açılışı; sonra EKAP kaydını okuyun [R2-011].
- [ ] 2025 ÇED tablolarını Bakanlık sayfasından indirip toplamları düzeltin [R3-001].

**19–31 Ekim**
- [ ] P2-1 hattının 1–9. aşamalarını kurun; Germencik ve Gaia poligonlarını toplayın.
- [ ] PANGAEA ve BEANS'e tek sayfalık görev tanımını GitHub issue olarak gönderin [R1-002][R1-036].
- [ ] Tour du Valat'taki kişiyle görüşme isteyin.

**2–13 Kasım**
- [ ] Germencik geriye dönük test; sonra Gaia [R3-055]. Devam/dur kararı.
- [ ] Kooperatif için AB PIC başvurusu.

**16–30 Kasım**
- [ ] Ege danışmanlık ve geliştiricilerine 10 ücretsiz P2-1 raporu üretmeye başlayın; bir anonim örnek yayımlayın.
- [ ] Eldeki Gediz noktalarıyla WorldCover [R1-015] ve GWL_FCS30 [R1-024] doğrulamasını başlatın.
- [ ] EKAP'ta 2024–26 envanter ihalelerini listeleyin (P1-5, sonraki ihale için).

**1–11 Aralık**
- [ ] Beş danışmanlık telefonu: örnek rapor ve üç fiyat noktasıyla (§6'daki 1. ve 2. soru).
- [ ] 6 sayfalık "Gediz doğrulama notu"nu Tour du Valat ve Global Wetland Watch'a gönderin.
- [ ] Hazırlanan bir teklife (Biodiversa+, Horizon Küme 6 veya TÜBİTAK 1071 ulusal ayağı) ortak olarak eklenmeyi görüşün.

**14–31 Aralık**
- [ ] P2-2 gölge tarama taslağı (kamuya açık bir Enerjisa CHA'sına karşı).
- [ ] 10 raporun geri bildirimini ve fiyat görüşmelerini derleyin; ücretli P2-1 için devam/dur notu yazın.
- [ ] 2027 bahar saha planı (PAM, Odonata, drone) ve P1-3/P1-1 veri yayını taslağı.

---

## 6. Önce doğrulanacak sorular

| # | Soru | En ucuz doğrulama |
|---|---|---|
| 1 | Ege ÇED danışmanlıkları ve RES/GES geliştiricileri masa başı ön tarama için ödeyecek mi, ne kadar? | Örnek rapor ve üç fiyatla beş telefon (örneğin [R3-019][R3-026][R3-027][R3-018] arkasındaki firmalar). |
| 2 | Türkiye'de flora-fauna, ekosistem ve ODR raporları ile biyolog günü gerçekte ne tutuyor? | EKAP'ta sonuçlanmış "ekosistem değerlendirme raporu" ve "biyolojik çeşitlilik envanter" ihalelerinin yaklaşık maliyet ve bedellerini okuyun; aynı soruyu 1. sorudaki telefonlarda sorun. |
| 3 | Nuh'un Gemisi verisi, WDPA/KBA poligonları ve IUCN menzilleri ücretli raporda kullanılabilir mi? | DKMP'ye bir e-posta; IBAT/UNEP-WCMC üzerinden bir veri talep formu [R4-008]. |
| 4 | Yeterlik belgesiz kooperatif, ÇED ekine giren uzman imzalı içerik satabilir mi? Üniversite kooperatif üzerinden ücretli dış işe izin veriyor mu, yoksa döner sermaye mi şart? | Üniversite hukuk/teknoloji transfer ofisine bir telefon; Yeterlik Tebliği personel kurallarını okuyun [R3-020]. |
| 5 | DKMP envanter kazananları herp/Odonata işini alt yükleniciye veriyor mu, hangi tutarla? Veri kimin? | 16 Ekim 2026 açılışından sonra Ankara IKN 2026/1788766 EKAP kaydı [R2-011], ardından kazanana telefon. |
| 6 | Mott MacDonald Türkiye ve ERM bölgesel herp/Odonata uzman günü alıyor mu, hangi ücretle? | Türkiye biyoçeşitlilik sorumlularına telefon veya LinkedIn mesajı, gölge taramayla birlikte. |
| 7 | Tour du Valat/MWO veya Global Wetland Watch'ın sonraki döngüde Doğu Akdeniz doğrulama ortağı için bütçesi var mı? | Mevcut Tour du Valat kişisiyle bir görüşme. |
| 8 | 2025 ÇED sayıları, Ege payı ve RES/GES ayrımı gerçekte nedir? | Bakanlık tablolarını indirin [R3-001]. |
| 9 | Nuh'un Gemisi'nde Odonata gerçekten yok mu; veri tabanı dışarıdan kayıt kabul ediyor mu? | Portalda bir Odonata türünü sorgulayın (5 dakika), sonra DKMP'ye e-posta. |
| 10 | PANGAEA/GEO-Bench-2 veya BEANS bakımcıları bir Gediz görevini kabul eder mi? | Her bakımcıya tek sayfalık görev tanımıyla GitHub issue [R1-002][R1-036]. |

**Sınırlar.** ODR ücreti, 2025 ÇED sayıları, 38 değerlendirilmemiş herp türü ve NatureMetrics platform fiyatı arama özetidir; dış kullanımdan önce birincil sayfada kontrol edin. Belediye ortağının İzmir BB olduğu varsayımı doğrulanmamıştır.
