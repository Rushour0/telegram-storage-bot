import sqlite3
db_name = "files.db"


def create_table():
    # Connect to the database (it will be created if it doesn't exist)
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

    # Create the table if it doesn't exist
    cursor.execute('''CREATE TABLE IF NOT EXISTS files_key (
                        id INTEGER PRIMARY KEY,
                        file_name TEXT UNIQUE,
                        message_id TEXT UNIQUE
                    )''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS admins (
                        id INTEGER PRIMARY KEY,
                        user_id TEXT UNIQUE,
                        chat_id TEXT UNIQUE
                    )''')

    # Commit the changes and close the connection
    conn.commit()
    conn.close()


def insert_data(file_name, message_id):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

    try:
        # Insert the data into the table
        cursor.execute(
            '''INSERT INTO files_key (file_name, message_id) VALUES (?, ?)''', (file_name, message_id))
        conn.commit()
        print("Data inserted successfully!")
    except sqlite3.IntegrityError as e:
        print(
            f"Error: {e}. The file_name or message_id already exists in the database.")
    finally:
        conn.close()


def retrieve_file_id_by_file_name(file_name):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

    # Retrieve the message_id associated with the given file_name
    cursor.execute(
        '''SELECT message_id FROM files_key WHERE file_name = ?''', (file_name,))
    message_id = cursor.fetchone()

    conn.close()
    return message_id[0] if message_id else None


def retrieve_admins_by_chat_id(chat_id):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

    # Retrieve the message_id associated with the given file_name
    cursor.execute(
        '''SELECT user_id FROM admins WHERE chat_id = ?''', (chat_id,))
    user_id = cursor.fetchall()

    conn.close()
    return user_id if user_id else None
