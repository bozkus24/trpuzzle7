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

## Kelime havuzu

`kelimehavuzu.txt` — her satıra bir kelime. Oyun yalnızca **5 harfli** ve Türk
alfabesindeki harflerden oluşan satırları kullanır (küçük/büyük harf fark etmez,
şu an 835 kelime). Dosyayı kendi listenle değiştirmen yeterli; oyun otomatik uyum sağlar.
