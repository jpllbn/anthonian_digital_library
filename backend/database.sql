-- SQL script to create the database schema for the Anthonian Digital Library

-- Create the "users" table
CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    lrn INTEGER NOT NULL UNIQUE,
    email TEXT NOT NULL UNIQUE,
    hashed_password TEXT NOT NULL,
    is_active BOOLEAN DEFAULT 1
);