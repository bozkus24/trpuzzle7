# trpuzzle7 — Aradle 🎯

Betweenle tarzı Türkçe kelime bulmacası. Gizli **5 harfli** kelime, alfabetik sırada
**üstteki** ve **alttaki** kelimenin arasında. Tahmin ettikçe aralık daralır — kelimeyi
en az adımda bul!

## Özellikler

- Her gün yeni gizli kelime (deterministik) + 🎲 serbest mod
- Sınıra oturan tahminlerde **% yakınlık** ipucu, adım sayacı, yıldızlı puan (≤5 adım = 5⭐)
- Türk alfabesi sırası (ç, ğ, ı, i, ö, ş, ü dahil) ve Türkçe ekran klavyesi
- İstatistikler, seri takibi ve sonucu panoya kopyalayan paylaş butonu (tarayıcıda saklanır)
- Kelimeler `kelimehavuzu.txt` dosyasından okunur

## Çalıştırma

Tamamen statik bir site; herhangi bir web sunucusuyla açılır:

```bash
python3 -m http.server 8000
# → http://localhost:8000
```

GitHub Pages'e de doğrudan deploy edilebilir (Settings → Pages → bu dal, kök klasör).

## Kelime havuzu (iki katman)

Oyun iki listeden beslenir; ikisi de her satıra bir kelime, yalnızca **5 harfli**
ve Türk alfabesindeki harflerden oluşan satırlar kullanılır (küçük/büyük harf fark etmez):

- **`kelimehavuzu.txt`** — *cevap havuzu* (şu an 5585 kelime). Günün gizli kelimesi
  **buradan** seçilir. Ana kelime listesi budur.
- **`kabul.txt`** — *ek kabul edilen tahminler* (şu an 76 kelime). Cevap havuzunda
  olmayan ama tahmin olarak yazılabilen fazladan geçerli kelimeler. Gizli kelime
  olarak seçilmez.

Geçerli tahmin kümesi bu iki listenin birleşimidir (~5661 kelime). `kabul.txt`
yoksa oyun yalnızca `kelimehavuzu.txt` ile de sorunsuz çalışır. Her iki dosyayı
da kendi listenle değiştirebilirsin; oyun otomatik uyum sağlar.
