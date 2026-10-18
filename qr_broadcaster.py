import time
import qrcode as qr
import tkinter as tk
from PIL import ImageTk
root = tk.Tk()
root.geometry("500x500")
root.title("Qr Broadcaster")

def generate_qr():
    data = textbox.get("1.0", "end-1c")
    qr_config = qr.QRCode(
    version=1,
    box_size=18,
    border=4,
    )
    qr_config.add_data(data)
    qr_config.make(fit=True)
    qr_image = qr_config.make_image(fill_color="black", back_color="white")
    tk_image = ImageTk.PhotoImage(qr_image)
    qr_display_label.config(image=tk_image)
    qr_display_label.image = tk_image
label = tk.Label(root, text="Broadcast With QR", font=("Arial", 20))
label.pack(padx=22, pady=22)
textbox = tk.Text(root, height= 10, font=("Arial", 16))
textbox.pack(padx=20, pady=20)
button = tk.Button(root, text='Convert to Qr!', font=("Arial", 12), command=generate_qr)
button.pack(padx=12, pady=10)
qr_display_label = tk.Label(root)
qr_display_label.pack(pady=10)
    
root.mainloop()