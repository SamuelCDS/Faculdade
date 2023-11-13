import psycopg2
conn = psycopg2.connect(
    user = ""
    pasw = ""
    host = ""
    port = ""
    bancodados = ""
)
cursor = conn.cursor()
cursor.execute("""
        INSERT INTO emprestimos ()
        VALUES
            (),
            (),
            ();
""")
conn.commit()
cursor.close()
conn.close()