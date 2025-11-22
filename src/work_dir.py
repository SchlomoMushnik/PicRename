import tkinter as tk
from tkinter import filedialog
from typing import Optional


def select_working_directory() -> Optional[str]:
    """
    Öffnet ein GUI-Fenster zur Auswahl eines Arbeitsverzeichnisses.
    
    Returns:
        Optional[str]: Der Pfad zum ausgewählten Verzeichnis oder None, wenn der Benutzer Abbrechen klickt.
    """
    # Versteckes Root-Fenster erstellen (wird nicht angezeigt)
    root = tk.Tk()
    root.withdraw()  # Fenster ausblenden
    
    # Dialog für Verzeichnisauswahl öffnen
    directory_path = filedialog.askdirectory(
        title="Arbeitsverzeichnis auswählen",
        initialdir="~"
    )
    
    # Root-Fenster schließen
    root.destroy()
    
    # Leeren String in None konvertieren (wenn Abbrechen gedrückt wurde)
    return directory_path if directory_path else None


if __name__ == "__main__":
    # Test-Funktion
    selected_dir = select_working_directory()
    if selected_dir:
        print(f"Ausgewähltes Verzeichnis: {selected_dir}")
    else:
        print("Keine Verzeichnis ausgewählt oder Abbrechen gedrückt")
