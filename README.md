# 📘 Python MySQL CRUD Projesi

Bu proje, MySQL veritabanı üzerinde kullanıcı ekleme, listeleme, güncelleme ve silme işlemlerini yerine getiren basit ama profesyonel bir CRUD yapısı sunar. Kod yapısı tamamen modülerdir ve geliştirilmeye uygundur.

---

## 📂 Proje Klasör Yapısı

| 📁 Klasör / Dosya | 📝 Açıklama |
|------------------|-------------|
| **db.py** | MySQL veritabanı bağlantı fonksiyonu |
| **crud.py** | Create / Read / Update / Delete fonksiyonları |
| **main.py** | Terminal menüsü ve kullanıcı etkileşimi |
| **README.md** | Proje açıklama dosyası |

---

## 🧱 Kullanılan Teknolojiler

| Teknoloji | Açıklama |
|-----------|----------|
| 🐍 Python 3 | Projenin ana dili |
| 🗄 MySQL | Veri depolama |
| 🔌 mysql-connector-python | Python ↔ MySQL bağlantısı |

---

## 🚀 Özellikler

- Kullanıcı ekleme (Create)  
- Kullanıcıları listeleme (Read)  
- Kullanıcı güncelleme (Update)  
- Kullanıcı silme (Delete)  
- Otomatik tablo oluşturma  
- Hata yakalama (try-except)  
- Modüler ve temiz proje yapısı  
- Yeni özellik eklemeye uygun mimari  

---

## 🔧 Kurulum

### 1️⃣ Gerekli kütüphaneyi yükleyin
```bash
pip install mysql-connector-python

### 2️⃣ MySQL sunucunuzu başlatın

(MySQL Workbench, XAMPP veya WAMP kullanabilirsiniz.)

### 3️⃣ db.py içindeki veritabanı ayarlarını güncelleyin
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="pass",
    database="test"
)
### 4️⃣ Projeyi başlatın
python main.py

🖥 Menü Kullanımı
Başlangıç ekranı:

=== Kullanıcı Yönetim Sistemi ===
1) Kullanıcı ekle
2) Kullanıcıları listele
3) Kullanıcı güncelle
4) Kullanıcı sil
5) Çıkış

🧠 Bu Projeyle Öğrenilen Konular

MySQL ile Python arasında bağlantı kurma

SQL komutları kullanma

CRUD mantığı

Modüler proje mimarisi kurma

Terminal uygulaması geliştirme

Hata yakalama ve işlem kontrolü
