import calendar

# Funktion zum Erstellen eines Jahreskalenders 
def create_year_calendar(year):
    # Erstelle ein TextCalendar-Objekt das die Woche mit dem Sonntag beginnt
    cal = calendar.TextCalendar(calendar.SUNDAY)
    
    #Erhalte den Kalender für das gesamte Jahr im Textformat
    year_calendar = cal.formatyear(year)
    
    #Ausgabe des Kalenders für das angegebene Jahr
    print(f"\nKalender für das Jahr {year}: \n")
    print(year_calendar)
    
    #Ausgabe Kalender für den Monat Febraur 2025
    year = 2025
    print("Erstelle Jahreskalender...\n")
    create_year_calendar(year) # Kalender für das Jahr 2025
    # Zeigt den Kalender für den Februar 2025 an
    print("\nErstelle Monatskalender für Februar 2025/n")
    create_month_calendar(year, 2) # Kalender für Februar 2025
    
    #Ausgabe Kalender für den Monat März 2025
    print("\nErstelle Monatskalender für März 2025/n")
    create_month_calendar(year,3) # Kalender für März 2025
   
   #Ausgabe Kalender für den Monat April 2025
    print("\nErstelle Monatskalender für April 2025/n")
    create_month_calendar(year, 4) # Kalender für April 2025
    
    #Ausgabe Kalender für den Monat Mai 2025
    print("\nErstelle Monatskalender für Mai 2025/n")
    create_month_calendar(year, 5) # Kalender für  Mai 2025 
    
    #Ausgabe Kalender für den Monat Juni 2025
    print("\nErstelle Monatskalender für Juni 2025/n")
    create_month_calendar(year, 6) # Kalender für  Juni 2025
    
    #Ausgabe Kalender für den Monat Juli 2025
    print("\nErstelle Monatskalender für Juli 2025/n")
    create_month_calendar(year, 7) # Kalender für Juli 2025
    
    #Ausgabe Kalender für den Monat August 2025
    print("\nErstelle Monatskalender für August 2025/n")
    create_month_calendar(year, 8) # Kalender für August 2025
    
    #Ausgabe Kalender für den Monat September 2025
    print("\nErstelle Monatskalender für September 2025/n")
    create_month_calendar(year, 9) # Kalender für September 2025
    
    #Ausgabe Kalender für den Monat Oktober 2025
    print("\nErstelle Monatskalender für Oktober 2025/n")
    create_month_calendar(year, 10) #Kalender für Oktober 2025 
    
    #Ausgabe Kalender für den Monat November 2025
    print("\nErstelle Monatskalender für November 2025/n")
    create_month_calendar(year, 11) # Kalender für November 2025
    
    #Ausgabe Kalender für den Monat Dezember 2025
    print("\nErstelle Monatskalender für Dezember 2025/n")
    create_month_calendar(year, 12) # Kalender für Dezember 2025
