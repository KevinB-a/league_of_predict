DROP TABLE IF EXISTS user;  --supprime la table si elle existe
DROP TABLE IF EXISTS post;  --supprime la table si elle existe

CREATE TABLE user (  -- cree la table user qui comporte les attibuts suivant : id, username et password
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  username TEXT UNIQUE NOT NULL,
  password TEXT NOT NULL
);
