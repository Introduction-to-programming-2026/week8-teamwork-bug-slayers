import sqlite3

# Veritabanına bağlan (yoksa oluşturur)
conn = sqlite3.connect("favorites.db")
c = conn.cursor()

# favorites tablosunu oluştur
c.execute("""
CREATE TABLE IF NOT EXISTS favorites (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    language TEXT NOT NULL
)
""")

# Örnek veriler ekle
c.execute("INSERT INTO favorites (name, language) VALUES (?, ?)", ("Alice", "Python"))
c.execute("INSERT INTO favorites (name, language) VALUES (?, ?)", ("Bob", "JavaScript"))
c.execute("INSERT INTO favorites (name, language) VALUES (?, ?)", ("Charlie", "Python"))

conn.commit()
conn.close()

print("favorites.db veritabanı oluşturuldu ve örnek veriler eklendi.")
+
