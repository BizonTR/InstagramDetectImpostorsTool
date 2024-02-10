import tkinter as tk
from ResultMethods import FindLastFollowDate
from GetData import InstagramTool

def FindImpostorsButtonClick():
    output_text = "İmpostorlar:\n\n"
    for item in FindLastFollowDate():
        output_text += item + "\n"

    output_textbox.delete(1.0, tk.END)  # Çıktı alanını temizle
    output_textbox.insert(tk.END, output_text)  # Yeni metni 
    
def ScanButtonClick():
    userName = textbox1.get("1.0", "end-1c").strip()
    password = textbox2.get().strip()
    output_text = "Scan is starting...\n"
    output_textbox.delete(1.0, tk.END)  # Çıktı alanını temizle
    output_textbox.insert(tk.END, output_text)  # Yeni metni ekle

    instagramTool = InstagramTool(userName=userName,password=password)
    ScanFinished(instagramTool.Scan())

def ScanFinished(folder):
    output_text = f"Scan Finished.{folder} Folder Created.\n"
    output_textbox.insert(tk.END, output_text)  # Yeni metni ekle

def LoginIncorrectMessage():
    output_textbox.insert(tk.END, "Username or Password Incorrect.")  # Yeni metni ekle

def LoginCorrectMessage():
    output_textbox.insert(tk.END, "Login Successful.")  # Yeni metni ekle

# Ana pencere oluşturma
root = tk.Tk()
root.title("Instagram Tool")
root.geometry("500x400")  # Pencere boyutunu belirle

# Buton oluşturma

frame = tk.Frame(root)
frame.pack(padx=10, pady=10)
# Create textbox 1
global textbox1
label1 = tk.Label(frame, text="Username")
label1.grid(row=0, column=0, padx=5, pady=5)
textbox1 = tk.Text(frame, height=1, width=22)
textbox1.grid(row=0, column=1, padx=5, pady=5)
# Create textbox 2
global textbox2
label2 = tk.Label(frame, text="Password")
label2.grid(row=1, column=0, padx=5, pady=5)
textbox2 = tk.Entry(frame, show="*", width=30)
textbox2.grid(row=1, column=1, padx=5, pady=5)

button = tk.Button(root, text="Scan", command=ScanButtonClick) #klasör oluşturma işlemi
button.pack(pady=10)
button = tk.Button(root, text="Find Impostors", command=FindImpostorsButtonClick)
button.pack(pady=10)

# Frame oluşturma
frame = tk.Frame(root)
frame.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

# Scrollbar oluşturma
scrollbar = tk.Scrollbar(frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

# Çıktı ekranı oluşturma
output_textbox = tk.Text(frame, wrap="word", yscrollcommand=scrollbar.set, height=10, width=50)  # Çıktı ekranı için Text widget'ı oluştur
output_textbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

# Scrollbar ile çıktı ekranını bağlama
scrollbar.config(command=output_textbox.yview)


# Ana döngüyü başlatma
root.mainloop()
