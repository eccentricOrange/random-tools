from sqlite3 import connect
from pathlib import Path

SCHEMA_PATH = Path("schema.sql")
DATABASE_PATH = Path("index.db")

def init():
    with connect(DATABASE_PATH) as connection, SCHEMA_PATH.open('r') as schema:
        connection.executescript(schema.read())
        connection.commit()



def read_data():
    provider = input("Enter the name of the provider: ").strip()
    subject = input("Enter the subject: ").strip()
    book = int(input("Enter the number of the book: ").strip())

    while True:
        print(f"{provider=} {subject=} {book=}")

        name = input("\nEnter the lesson: ").strip()

        if name == "":
            new_provider = input("Enter the name of the provider: ").strip()
            if new_provider != "":
                provider = new_provider
                continue

            new_subject = input("Enter the subject: ").strip()
            if new_subject != "":
                subject = new_subject
                continue

            new_book = input("Enter the number of the book: ").strip()
            if new_book != "":
                book = int(new_book)
                continue

            break

        insert_one_value((provider.lower(), subject.lower(), book, name.capitalize()))
        print(f"Added {name=} to {provider=} {subject=} {book=}.\n")

def insert_one_value(data):
    with connect(DATABASE_PATH) as connection:
        cursor = connection.cursor()
        cursor.execute("INSERT INTO chapters (provider_id, subject_id, book_id, name) VALUES (?, ?, ?, ?)", data)
        connection.commit()


def main():
    init()
    read_data()

if __name__ == "__main__":
    main()

