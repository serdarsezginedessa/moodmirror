# MoodMirror 😌🪞

**MoodMirror**, kullanıcıların ruh halini anlayarak onlara uygun öneriler sunan yapay zekâ destekli bir tavsiye API’sidir.

## Özellikler

- Ruh haline göre film, kitap, müzik, egzersiz önerisi
- Flask ile çalışan REST API
- Basit ve genişletilebilir Python altyapısı
- (İleride) NLP ile ruh hali tahmini, Flutter arayüz

## Kullanım

```bash
# API'yi başlat
python app.py

POST
{
  "durum": "bugün biraz stresliyim"
}
Yanıt

{
  "tavsiye": "5 dakikalık meditasyon yap."
}

Kurulum

git clone https://github.com/serdarsezginedessa/MoodMirror.git
cd MoodMirror
pip install -r requirements.txt
python app.py

Lisans
MIT License

markdown

```
