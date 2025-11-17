🗄️ Python + MySQL CRUD Uygulaması

Bu proje, Python kullanarak MySQL üzerinde CRUD işlemleri (Create, Read, Update, Delete) yapan basit ve anlaşılır bir örnek uygulamadır.

MySQL veritabanına bağlanır, tabloyu oluşturur, kullanıcı ekler, günceller, siler ve tüm kullanıcıları listeler.

📌 Özellikler

MySQL veritabanına bağlanma

Tablo otomatik oluşturma (CREATE TABLE IF NOT EXISTS)

Kullanıcı ekleme (INSERT)

Kullanıcıları listeleme (SELECT)

Kullanıcı güncelleme (UPDATE)

Kullanıcı silme (DELETE)

📦 Gereksinimler

Makinenizde aşağıdakiler kurulu olmalıdır:

Python 3.8+

MySQL Server

mysql-connector-python kütüphanesi

Kurulum:

pip install mysql-connector-python

🏗️ Veritabanı Ayarları

Kod şu MySQL bilgilerini kullanır:

host="localhost"
user="root"
password="pass"
database="test"


Farklıysa kendi bilgilerinize göre güncelleyin.

▶️ Nasıl Çalıştırılır?
python main.py


Çalışınca:

users tablosu otomatik oluşur

"ugur" adlı kullanıcı veritabanına eklenir

Tüm kullanıcılar terminalde listelenir

🔧 Örnek Çıktı
Kullanıcılar:
(1, 'ugur', 'ugur@hotmail.com')

📝 Notlar

email alanı benzersiz (UNIQUE).

Aynı email tekrar eklenirse MySQL hata verir.

Kod tamamen modülerdir ve geliştirilmeye uygundur.

🧑‍💻 Geliştirme Önerileri

GUI ekleme (Tkinter, PyQt, Flask)

Şifre alanı ekleme

Loglama sistemi ekleme

Prepared statements + try/except blokları ekleme
