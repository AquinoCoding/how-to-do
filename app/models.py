from .db_settings import ConfigEngine

# Função para criar a tabela no banco de dados
def create_table():
    cursor = conn.cursor()

    query = """
    CREATE TABLE IF NOT EXISTS TO_DO (
        id SERIAL PRIMARY KEY,
        title VARCHAR(100) NOT NULL,
        sub_title VARCHAR(100),
        text TEXT,
        date_created TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
    """
    cursor.execute(query)

    conn.commit()
    conn.close()

# Função para inserir um novo registro na tabela
def insert_record(title: str, sub_title: str, text: str):
    conn = ConfigEngine().connection()
    cursor = conn.cursor()

    query = "INSERT INTO TO_DO (title, sub_title, text) VALUES (?, ?, ?);"
    cursor.execute(query, (title, sub_title, text))
    print(query)

    conn.commit()
    conn.close()

# Função para buscar todos os registros da tabela
def get_all_records():
    conn = ConfigEngine().connection()
    cursor = conn.cursor()

    query = "SELECT * FROM TO_DO;"
    cursor.execute(query)
    rows = cursor.fetchall()

    records = []
    for row in rows:
        record = {
            'id': row[0],
            'title': row[1],
            'sub_title': row[2],
            'text': row[3],
            'date_created': row[4]
        }
        records.append(record)

    conn.close()

    return records

# Função para excluir um registro da tabela pelo ID
def delete_record(record_id: id):
    conn = ConfigEngine().connection()
    cursor = conn.cursor()

    query = "DELETE FROM TO_DO WHERE id = %s;"
    cursor.execute(query, (record_id,))

    conn.commit()
    conn.close()

# Criar a tabela
#create_table(conn)

# Inserir um novo registro
insert_record("Título", "Subtítulo", "Texto")

# Buscar todos os registros
#all_records = get_all_records(conn)
#for record in all_records:
#    print(record)

# Excluir um registro
#delete_record(conn, 1)
