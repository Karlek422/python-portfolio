import sqlite3
import os

# Спробуємо створити базу в тій же папці, де лежить сам скрипт
db_path = os.path.join(os.path.dirname(__file__), "social_network.db")
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# Вмикаємо підтримку зовнішніх ключів
cursor.execute("PRAGMA foreign_keys = ON;")

# USERS
cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    user_id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE NOT NULL,
    email TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL,
    date_of_birth TEXT,
    created_at TEXT DEFAULT CURRENT_TIMESTAMP
);
""")

# POSTS
cursor.execute("""
CREATE TABLE IF NOT EXISTS posts (
    post_id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    content TEXT NOT NULL,
    created_at TEXT DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(user_id)
);
""")

# COMMENTS
cursor.execute("""
CREATE TABLE IF NOT EXISTS comments (
    comment_id INTEGER PRIMARY KEY AUTOINCREMENT,
    post_id INTEGER,
    user_id INTEGER,
    content TEXT NOT NULL,
    created_at TEXT DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (post_id) REFERENCES posts(post_id),
    FOREIGN KEY (user_id) REFERENCES users(user_id)
);
""")

# LIKES
cursor.execute("""
CREATE TABLE IF NOT EXISTS likes (
    like_id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    post_id INTEGER,
    created_at TEXT DEFAULT CURRENT_TIMESTAMP,
    UNIQUE(user_id, post_id),
    FOREIGN KEY (user_id) REFERENCES users(user_id),
    FOREIGN KEY (post_id) REFERENCES posts(post_id)
);
""")

# FRIENDSHIPS
cursor.execute("""
CREATE TABLE IF NOT EXISTS friendships (
    user_id INTEGER,
    friend_id INTEGER,
    status TEXT DEFAULT 'pending',
    created_at TEXT DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (user_id, friend_id),
    FOREIGN KEY (user_id) REFERENCES users(user_id),
    FOREIGN KEY (friend_id) REFERENCES users(user_id)
);
""")

conn.commit()
print(f"База даних успішно створена/оновлена за шляхом: {os.path.abspath(db_path)}")
conn.close()