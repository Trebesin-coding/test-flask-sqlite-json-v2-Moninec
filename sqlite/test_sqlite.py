import sqlite3

# Proč je connection podtržené? Oprav chybu
connection = sqlite3.connect("filmy.db")

cursor = connection.cursor()

# Co tu chybí?



# Oprav vytváření tabulky - hodnocení je číselné
cursor.execute(
    """CREATE TABLE IF NOT EXISTS hodnoceni (
        id INTEGER PRIMARY KEY,
        nazev_filmu TEXT,
        hodnoceni INTEGER
    )
    """
)

# Zapsání do databáze
cursor.execute("INSERT INTO hodnoceni(id, nazev_filmu, hodnoceni) VALUES (1, 'Babovresky', 5)")
# tady by měl vepsat hodnocení do databáze - není potřeba využívat input, stačí zapsat statický údaj
# cursor.???

connection.commit()


# Vypisování hodnocení

cursor.execute("SELECT * FROM hodnoceni")

rows = cursor.fetchall()

# tady printne hodnocení filmu z databáze

print("hodnoceni: ", rows[0][2])

connection.close()
