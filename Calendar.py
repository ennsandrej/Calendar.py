import calendar
import tkinter as tk
from tkinter import ttk
from tkinter.scrolledtext import ScrolledText

# Funktion zum Erstellen des Monatskalenders
def create_month_calendar(year, month):
    cal = calendar.TextCalendar(calendar.SUNDAY)
    return cal.formatmonth(year, month)

# Funktion zum Erstellen des Jahreskalenders
def create_year_calendar(year):
    cal = calendar.TextCalendar(calendar.SUNDAY)
    return cal.formatyear(year)

# Funktion, um Kalender in der Textbox anzuzeigen
def show_calendar():
    try:
        year = int(year_entry.get())
        view = view_option.get()
        
        if view == "Jahreskalender":
            result = create_year_calendar(year)
        else:
            month = month_combo.current() + 1  # Januar = 0 → +1
            result = create_month_calendar(year, month)

        text_box.delete('1.0', tk.END)
        text_box.insert(tk.END, result)
    except ValueError:
        text_box.delete('1.0', tk.END)
        text_box.insert(tk.END, "Bitte eine gültige Jahreszahl eingeben.")

# Hauptfenster
root = tk.Tk()
root.title("Kalenderanzeige")

# Jahres-Eingabe
tk.Label(root, text="Jahr:").grid(row=0, column=0, padx=5, pady=5, sticky="e")
year_entry = tk.Entry(root)
year_entry.grid(row=0, column=1, padx=5, pady=5)

# Monats-Auswahl
tk.Label(root, text="Monat:").grid(row=1, column=0, padx=5, pady=5, sticky="e")
month_combo = ttk.Combobox(root, values=[
    "Januar", "Februar", "März", "April", "Mai", "Juni",
    "Juli", "August", "September", "Oktober", "November", "Dezember"
])
month_combo.current(0)
month_combo.grid(row=1, column=1, padx=5, pady=5)

# Auswahl Jahres- oder Monatskalender
view_option = ttk.Combobox(root, values=["Monatskalender", "Jahreskalender"])
view_option.current(0)
view_option.grid(row=2, column=1, padx=5, pady=5)

# Button zur Anzeige
show_btn = tk.Button(root, text="Kalender anzeigen", command=show_calendar)
show_btn.grid(row=3, column=0, columnspan=2, pady=10)

# Textfeld zur Anzeige des Kalenders
text_box = ScrolledText(root, width=60, height=20)
text_box.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

# Hauptloop
root.mainloop()
