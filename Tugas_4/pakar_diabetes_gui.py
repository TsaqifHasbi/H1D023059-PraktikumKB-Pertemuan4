import tkinter as tk
from pyswip import Prolog
from tkinter import messagebox
from tkinter import ttk

# Setup GUI
root = tk.Tk()
root.title("Sistem Pakar Diagnosa Diabetes")

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(tk.N, tk.W, tk.E, tk.S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

ttk.Label(mainframe, text="Aplikasi Diagnosa Penyakit Diabetes", font=("Arial", 16)).grid(column=0, row=0, columnspan=3)
ttk.Label(mainframe, text="Kolom Pertanyaan:").grid(column=0, row=1)
kotak_pertanyaan = tk.Text(mainframe, height=4, width=50, state=tk.DISABLED)
kotak_pertanyaan.grid(column=0, row=2, columnspan=3)
no_btn = ttk.Button(mainframe, text="Tidak", state=tk.DISABLED, command=lambda: jawaban(False))
no_btn.grid(column=1, row=3, sticky=(tk.W, tk.E))
yes_btn = ttk.Button(mainframe, text="Ya", state=tk.DISABLED, command=lambda: jawaban(True))
yes_btn.grid(column=2, row=3, sticky=(tk.W, tk.E))

for widget in mainframe.winfo_children():
    widget.grid_configure(padx=5, pady=5)

prolog = Prolog()
prolog.consult("pakar_diabetes_gui.pl")
penyakit = []
gejala = {}
index_penyakit = 0
index_gejala = 0
current_penyakit = ""
current_gejala = ""

def mulai_diagnosa():
    global penyakit, gejala, index_penyakit, index_gejala
    prolog.retractall("gejala_pos(_)") 
    prolog.retractall("gejala_neg(_)") 
    start_btn.configure(state=tk.DISABLED)
    yes_btn.configure(state=tk.NORMAL)
    no_btn.configure(state=tk.NORMAL)

    penyakit = [p["X"].decode() for p in list(prolog.query("penyakit(X)"))]
    for p in penyakit:
        gejala[p] = [g["X"] for g in list(prolog.query(f'gejala(X, "{p}")'))]
    index_penyakit = 0
    index_gejala = -1
    pertanyaan_selanjutnya()

start_btn = ttk.Button(mainframe, text="Mulai Diagnosa", command=mulai_diagnosa)
start_btn.grid(column=1, row=4, columnspan=2, sticky=(tk.W, tk.E))

def pertanyaan_selanjutnya(ganti_penyakit=False):
    global current_penyakit, current_gejala, index_penyakit, index_gejala
    if ganti_penyakit:
        index_penyakit += 1
        index_gejala = -1
        if index_penyakit >= len(penyakit):
            hasil_diagnosa()
            return
    current_penyakit = penyakit[index_penyakit]
    index_gejala += 1
    if index_gejala >= len(gejala[current_penyakit]):
        hasil_diagnosa(current_penyakit)
        return
    current_gejala = gejala[current_penyakit][index_gejala]
    if list(prolog.query(f"gejala_pos({current_gejala})")):
        pertanyaan_selanjutnya()
        return
    elif list(prolog.query(f"gejala_neg({current_gejala})")):
        pertanyaan_selanjutnya(ganti_penyakit=True)
        return
    pertanyaan = list(prolog.query(f"pertanyaan({current_gejala}, Y)"))[0]["Y"].decode()
    tampilkan_pertanyaan(pertanyaan)

def tampilkan_pertanyaan(pertanyaan):
    kotak_pertanyaan.configure(state=tk.NORMAL)
    kotak_pertanyaan.delete(1.0, tk.END)
    kotak_pertanyaan.insert(tk.END, pertanyaan)
    kotak_pertanyaan.configure(state=tk.DISABLED)

def jawaban(jwb):
    if jwb:
        prolog.assertz(f"gejala_pos({current_gejala})")
        pertanyaan_selanjutnya()
    else:
        prolog.assertz(f"gejala_neg({current_gejala})")
        pertanyaan_selanjutnya(ganti_penyakit=True)

def hasil_diagnosa(penyakit=""):
    if penyakit:
        messagebox.showinfo("Hasil Diagnosa", f"Anda kemungkinan menderita {penyakit}.")
    else:
        messagebox.showinfo("Hasil Diagnosa", "Tidak terdeteksi jenis diabetes dari gejala Anda.")
    yes_btn.configure(state=tk.DISABLED)
    no_btn.configure(state=tk.DISABLED)
    start_btn.configure(state=tk.NORMAL)

root.mainloop()
