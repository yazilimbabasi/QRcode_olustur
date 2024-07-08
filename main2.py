from tkinter import *
import webbrowser
from tkinter import filedialog
from PIL import Image, ImageTk
import qrcode
import uuid

# Pencereyi oluştur
window = Tk()
window.geometry("450x500")
window.title("QR Code Oluşturucu")
window.configure(bg="#D1E8E2")  # Daha sofistike bir arka plan rengi

# Simgeyi yükleyin (iconphoto)
window.iconphoto(True, PhotoImage(file="qr.png"))


def yapici():
    # QR kodunu oluştur
    qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=2)
    text = entry.get("1.0", "end-1c")  # Entry widget'ından metni al
    qr.add_data(text)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")

    # QR kodunu geçici olarak bellekte tut
    global qr_image, photo
    qr_image = img  # QR kodunu bellekte tutuyoruz

    # QR kodunu görüntüle
    img = img.convert("RGB")
    photo = ImageTk.PhotoImage(img.resize((150, 150)))

    # Eski Label'i güncelle
    if hasattr(yapici, 'la3'):
        yapici.la3.destroy()

    la3 = Label(image=photo)
    la3.image = photo
    la3.place(x=10, y=340)  # Sol alt köşeye yakın bir konuma taşıdık
    yapici.la3 = la3  # Yeni Label'i fonksiyon içinde saklayın


def kaydet():
    if 'qr_image' in globals():
        file_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])
        if file_path:
            qr_image.save(file_path)
def button_basıldı():
    website_url = "https://archive.org/download/blogger-image-279954257/blogger-image-279954257.jpg"
    webbrowser.open_new(website_url)

# Arayüz geliştirme kısmı
la1 = Label(text="QR Code Oluşturucu", font="Oswald 14", bg="#D1E8E2", fg="#374045")
la1.place(x=130, y=10)
la2 = Label(text="Metin Giriniz...", fg="#0D7377", font="Oswald 12", bg="#D1E8E2")
la2.place(x=5, y=50)
la3 = Label(text="Yazılımıcı: DebugHero",fg="#0D7377",font="Oswald 10",bg="#D1E8E2")
la3.place(x=305,y=460)

entry = Text(font="Oswald 10", wrap=WORD)  # Daha geniş bir alan ve satır sonunu otomatik yap
entry.place(x=0, y=80, width=450, height=200)  # Kenarlara sıfır olacak şekilde genişletildi
entry.focus()

# Oluştur butonu
bu1 = Button(text="OLUŞTUR", fg="#0D7377", bg="#374045", font="Oswald 10", command=yapici, width=10, height=2)
bu1.place(x=350, y=290)  # Sağ tarafa yakın

# İndir butonu
bu2 = Button(text="İNDİR", fg="#0D7377", bg="#374045", font="Oswald 10", command=kaydet, width=10, height=2)
bu2.place(x=350, y=340)  # Oluştur butonunun altına

bu3 = Button(text="communication", fg="#0D7377", bg="#374045", font="Oswald 7", command = button_basıldı, width=8, height=1)
bu3.place(x=385,y=480)

window.mainloop()
