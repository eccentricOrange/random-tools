CREATE TABLE IF NOT EXISTS providers (
    provider_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS chapters (
    lesson_id INTEGER PRIMARY KEY AUTOINCREMENT,
    provider_id INTEGER NOT NULL,
    subject_id TEXT NOT NULL,
    book_id INTEGER NOT NULL,
    name TEXT NOT NULL,
    FOREIGN KEY (provider_id) REFERENCES providers(provider_id),
    CONSTRAINT unique_lesson UNIQUE (provider_id, subject_id, book_id, name)
);

CREATE INDEX IF NOT EXISTS search_chapters_by_name
ON chapters (name);