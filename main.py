import tkinter as tk
from tkinter import messagebox

class MenuPOSApp:
    def __init__(self, root):
        self.root = root
        self.root. title("Menü POS Sistemi")
        self.root.geometry("600x400")
        self.root.configure(bg="#2C3E50")
        
        # Başlık
        title_label = tk.Label(
            root, 
            text="🍽️ Menü POS Sistemi", 
            font=("Arial", 24, "bold"),
            bg="#2C3E50",
            fg="white"
        )
        title_label.pack(pady=20)
        
        # Butonlar Frame
        button_frame = tk. Frame(root, bg="#2C3E50")
        button_frame.pack(pady=30)
        
        # Sipariş butonu
        order_btn = tk.Button(
            button_frame,
            text="📋 Yeni Sipariş",
            font=("Arial", 14),
            bg="#27AE60",
            fg="white",
            width=15,
            height=2,
            command=self.new_order
        )
        order_btn.grid(row=0, column=0, padx=10, pady=10)
        
        # Menü butonu
        menu_btn = tk.Button(
            button_frame,
            text="🍕 Menü",
            font=("Arial", 14),
            bg="#3498DB",
            fg="white",
            width=15,
            height=2,
            command=self.show_menu
        )
        menu_btn.grid(row=0, column=1, padx=10, pady=10)
        
        # Ayarlar butonu
        settings_btn = tk.Button(
            button_frame,
            text="⚙️ Ayarlar",
            font=("Arial", 14),
            bg="#E67E22",
            fg="white",
            width=15,
            height=2,
            command=self.show_settings
        )
        settings_btn.grid(row=1, column=0, padx=10, pady=10)
        
        # Çıkış butonu
        exit_btn = tk.Button(
            button_frame,
            text="❌ Çıkış",
            font=("Arial", 14),
            bg="#E74C3C",
            fg="white",
            width=15,
            height=2,
            command=self.exit_app
        )
        exit_btn.grid(row=1, column=1, padx=10, pady=10)
        
        # Versiyon
        version_label = tk.Label(
            root,
            text="v1.0.0 - GitHub Actions Build",
            font=("Arial", 10),
            bg="#2C3E50",
            fg="#BDC3C7"
        )
        version_label.pack(side="bottom", pady=10)
    
    def new_order(self):
        messagebox.showinfo("Sipariş", "Yeni sipariş ekranı açılıyor...")
    
    def show_menu(self):
        messagebox.showinfo("Menü", "Menü listesi:\n\n🍕 Pizza - 50 TL\n🍔 Burger - 40 TL\n🥗 Salata - 30 TL")
    
    def show_settings(self):
        messagebox. showinfo("Ayarlar", "Ayarlar menüsü")
    
    def exit_app(self):
        if messagebox.askyesno("Çıkış", "Programdan çıkmak istediğinize emin misiniz?"):
            self.root.quit()

if __name__ == "__main__":
    root = tk.Tk()
    app = MenuPOSApp(root)
    root.mainloop()
