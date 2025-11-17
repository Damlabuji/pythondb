from crud import *

create_table()

def menu():
    while True:
        print("\n=== Kullanıcı Yönetim Sistemi ===")
        print("1) Kullanıcı ekle")
        print("2) Kullanıcıları listele")
        print("3) Kullanıcı güncelle")
        print("4) Kullanıcı sil")
        print("5) Çıkış")

        secim = input("Seçiminiz: ")

        if secim == "1":
            isim = input("İsim: ")
            email = input("Email: ")
            insert_user(isim, email)

        elif secim == "2":
            get_users()

        elif secim == "3":
            numara = input("Güncellenecek ID: ")
            isim = input("Yeni isim: ")
            email = input("Yeni email: ")
            update_user(numara, isim, email)

        elif secim == "4":
            numara = input("Silinecek ID: ")
            delete_user(numara)

        elif secim == "5":
            print("Programdan çıkılıyor...")
            break

        else:
            print("❗ Geçersiz seçim, tekrar deneyin.")


menu()
