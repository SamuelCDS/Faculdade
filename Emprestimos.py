import psycopg2

conn = psycopg2.connect(user = "",
                        pasw = "",
                        host = "",
                        port = "",
                        bancodados = "")


cursor = conn.cursor()

try:
    cursor.execute("""
            INSERT INTO emprestimos (data_emprestimo, data_devolucao, status, userid, itemid) 
                   VALUES
                ('2023-01-01', '2023-01-15', 'Em andamento', 1, 101),
                ('2023-02-01', '2023-02-15', 'Concluído', 2, 102),
                ('2023-03-01', '2023-03-15', 'Em andamento', 3, 103),
                ('2023-04-01', '2023-04-08', 'emAndamento', 1, 104, 'materialDidatico'),
                ('2023-05-01', '2023-05-08', 'concluido', 2, 105, 'livro'),
                ('2023-06-01', '2023-06-08', 'emAndamento', 3, 106, 'materialDidatico'),
                ('2023-07-01', '2023-07-08', 'concluido', 1, 107, 'livro'),
                ('2023-08-01', '2023-08-08', 'emAndamento', 2, 108, 'materialDidatico'),
                ('2023-09-01', '2023-09-08', 'concluido', 3, 109, 'livro'),
                ('2023-10-01', '2023-10-08', 'emAndamento', 1, 110, 'materialDidatico'),
                ('2023-11-01', '2023-11-08', 'concluido', 2, 111, 'livro'),
                ('2023-12-01', '2023-12-08', 'emAndamento', 3, 112, 'materialDidatico'),
                ('2024-01-01', '2024-01-08', 'concluido', 1, 113, 'livro');
    """)
    conn.commit()

except Exception as err:
    print(f"Erro: {err}")
    conn.rollback()

finally:
    cursor.close()
    conn.close()
