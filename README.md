# Simple-RSA-via-Python
Python ile temel RSA şifreleme ve deşifreleme algoritması.
# Simple RSA Implementation in Python 🔐

Bu proje, RSA (Rivest–Shamir–Adleman) şifreleme algoritmasının temel mantığını anlamak ve Python ile simüle etmek için geliştirilmiştir. Eğitim amaçlı bir çalışmadır.

## 🚀 Özellikler
- **Asal Sayı Tabanlı:** Seçilen `p` ve `q` asalları üzerinden anahtar üretimi.
- **EBOB Hesaplama:** Öklid algoritması kullanılarak `gcd` (En Büyük Ortak Bölen) hesabı.
- **Şifreleme:** Metin karakterlerini ASCII değerlerine dönüştürüp $c = m^e \pmod{n}$ formülüyle şifreleme.
- **Deşifreleme:** Şifreli sayıları modüler üs alma yöntemiyle tekrar karaktere dönüştürme.

## 🛠 Kullanım
Projeyi bilgisayarınıza klonlayın veya `.py` dosyasını indirin:

1. Terminali açın.
2. Dosyanın olduğu dizine gidin.
3. Şu komutu çalıştırın:
   ```bash
   python rsa_script.py

  ⚠️  Önemli Not
Bu uygulama eğitim amaçlıdır. Gerçek dünya güvenliği için küçük asal sayılar (bu projede kullanılanlar gibi) yeterli değildir. Profesyonel projelerde cryptography gibi kütüphaneler ve en az 2048-bit anahtarlar kullanılmalıdır.

  📄 Lisans
Bu proje MIT License ile lisanslanmıştır.
