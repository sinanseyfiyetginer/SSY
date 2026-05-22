🌐 Meeting Translation Agent
=====================================

Online Toplantılar için İngilizce ↔ Türkçe Anlık Çeviri Ajanı

## 🎯 Ne Yapıyor?

- 🇬🇧 **İngilizce → Türkçe**: Toplantıda karşı tarafın söylediklerini anlamak
- 🇹🇷 **Türkçe → İngilizce**: Senin Türkçe cevaplarını İngilizceye çevir
- ⚡ **Anlık**: Hızlı ve doğru çeviri

---

## 📋 Kurulum

### Adım 1: Python Yüklü mü?

Windows/Mac/Linux'te terminali açıp şunu yazın:
```bash
python --version
```

Eğer `Python 3.8+` yazarsa, hazırsın! Yoksa [buradan yükle](https://www.python.org/downloads/)

### Adım 2: Gerekli Paketi Kur

Bu klasördeki terminalde (Windows: cmd, Mac/Linux: Terminal):

```bash
pip install -r requirements.txt
```

### Adım 3: Claude API Anahtarını Al

1. [Buraya git](https://console.anthropic.com/api/keys)
2. Hesap aç (ücretsiz)
3. **+ Create Key** butonuna tıkla
4. Anahtarı kopyala (bir daha görmeyeceksin!)

---

## 🚀 Nasıl Kullanırsın?

### Programı Başlat:

```bash
python translator.py YOUR_API_KEY_HERE
```

**Örnek:**
```bash
python translator.py sk-ant-v0-1234567890abcdefghijklmnopqrstuvwxyz
```

### Kullanım:

```
🌐 Meeting Translation Agent
==================================================
İngilizce ↔ Türkçe Çeviri Ajanı

Komutlar:
  'en' - İngilizce metni Türkçeye çevir
  'tr' - Türkçe metni İngilizceye çevir
  'exit' - Çıkış

📝 Mod seçin (en/tr/exit): en
🇬🇧 İngilizce metni gir: Can you send me the report?
⏳ Çeviriliyor...
🇹🇷 Türkçe:
Bana raporu gönderebilir misin?
```

---

## 💡 İpuçları

### ✅ Daha İyi Çeviri İçin:

1. **Kopyala-Yapıştır Yöntemi**:
   - Toplantıda "Copy Transcript" kullanırsan
   - Programın içine yapıştırabilirsin
   - Hızlı ve pratik

2. **Kısa ve Net Yazı**:
   - Uzun cümleler yerine
   - Kısa paragraflar gönder
   - Daha doğru çeviri alırsın

3. **Bağlam Ver**:
   - "Meeting hakkında: Proje planlaması"
   - "Teknik toplantı: Sistem mimarisi"
   - Daha bağlamsal çeviri yapar

---

## 💰 Maliyet

- **İlk ay**: Ücretsiz (100K token)
- **Sonrası**: Ayda ~5-10 dolar (az kullanırsan 2-3 dolar)
- **API Fiyatlandırması**: [Buradan bak](https://www.anthropic.com/pricing)

---

## ❓ Sorunlar?

### "API anahtarı geçersiz" hatası
→ Anahtarı doğru kopyaladığından emin ol

### "Module anthropic not found"
→ `pip install anthropic` yeniden çalıştır

### Çeviri yanlış çıkıyor
→ Daha kısa cümle dene veya bağlam ekle

---

## 🎓 Daha Gelişmiş Kullanım

Kod açık kaynak! İstediğin gibi değiştirebilirsin:
- Ses otomatikasyonu ekle
- Zoom/Teams entegrasyonu
- Kendi dilini ekle

Yazılımcıyla iletişime geç! 🚀

---

## 👤 Yazar

**Sinan Seyfi YETGİNER**
- 🐙 [GitHub](https://github.com/sinanseyfiyetginer)
- 💼 [LinkedIn](https://linkedin.com/in/sinanseyfiyetginer)
- 🐦 [Twitter](https://twitter.com/sinanseyfiyetginer)

---

## 📜 Lisans

Bu proje açık kaynak koddur. Özgürce kullanabilirsiniz.

---

**Hazırsa, başla!** 🎯

```bash
python translator.py YOUR_API_KEY_HERE
```

Good luck! 🍀
