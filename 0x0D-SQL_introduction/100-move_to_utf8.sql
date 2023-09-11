-- Converts hbtn_0c_0 database to UTF8 (utf8mb4, collate utf8mb4_unicode_ci) in your MySQL server
-- db
USE hbtn_0c_0;
-- db to utf-8mb4
ALTER DATABASE hbtn_0c_0
CHARACTER SET utf8mb4
COLLATE utf8mb4_unicode_ci;

-- table to utf
ALTER TABLE first_table
CONVERT TO CHARACTER SET utf8mb4
COLLATE utf8mb4_unicode_ci;

-- frst to utf
ALTER TABLE first_table
MODIFY name VARCHAR(256)
CHARACTER SET utf8mb4
COLLATE utf8mb4_unicode_ci;