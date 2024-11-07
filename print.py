import tkinter as tk
from tkinter import messagebox

polish_alphabet = "AĄBCĆDEĘFGHIJKLŁMNŃOÓPRSŚTUWYZŹŻ"

def caesar_cipher(text, shift):
    result = ""
    for char in text:
        if char.upper() in polish_alphabet:
            is_upper = char.isupper()
            index = polish_alphabet.index(char.upper())
            shifted_index = (index + shift) % len(polish_alphabet)
            shifted_char = polish_alphabet[shifted_index]
            result += shifted_char if is_upper else shifted_char.lower()
        else:
            result += char
    return result

def encrypt_text():
    text = entry_text.get()
    try:
        shift = int(entry_shift.get())
        encrypted_text = caesar_cipher(text, shift)
        result_text.config(state="normal")  # Делаем текстовое поле активным для записи
        result_text.delete(1.0, "end")  # Очищаем текстовое поле
        result_text.insert("end", encrypted_text)  # Вставляем зашифрованный текст
        result_text.config(state="disabled")  # Делаем текстовое поле неактивным для редактирования
    except ValueError:
        messagebox.showerror("Błąd", "Wprowadź liczbę dla przesunięcia")

def decrypt_text():
    text = entry_text.get()
    try:
        shift = int(entry_shift.get())
        decrypted_text = caesar_cipher(text, -shift)
        result_text.config(state="normal")
        result_text.delete(1.0, "end")
        result_text.insert("end", decrypted_text)
        result_text.config(state="disabled")
    except ValueError:
        messagebox.showerror("Błąd", "Wprowadź liczbę dla przesunięcia")

root = tk.Tk()
root.title("Szyfr Cezara")

tk.Label(root, text="Wprowadź tekst do zaszyfrowania/odszyfrowania:").pack(pady=5)
entry_text = tk.Entry(root, width=50)
entry_text.pack(pady=5)

tk.Label(root, text="Wprowadź wielkość przesunięcia:").pack(pady=5)
entry_shift = tk.Entry(root, width=5)
entry_shift.pack(pady=5)

button_encrypt = tk.Button(root, text="Zaszyfruj", command=encrypt_text)
button_encrypt.pack(pady=5)

button_decrypt = tk.Button(root, text="Odszyfruj", command=decrypt_text)
button_decrypt.pack(pady=5)

tk.Label(root, text="Wynik:").pack(pady=5)
result_text = tk.Text(root, height=2, width=50, font=("Arial", 12))
result_text.pack(pady=5)
result_text.config(state="disabled")  # Делаем текстовое поле неактивным для редактирования

root.mainloop()
