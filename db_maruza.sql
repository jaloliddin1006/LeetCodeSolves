--  Jaloliddin Mamatmusayev Ma'lumotlar Bazasi fanidan 
-- "SQL da indexlardan foydalanish" mavzusida tayyorlagan
--                  mustaqil ishi 


-- PostgreSQL-da indexlar ma'lumotlar ustida tezkor qidirishni 
    -- optimallashtirish uchun ishlatiladi. 
-- Quyidagi misollar indexlar bilan ishlashni to'liq tushuntiradi:


-- Indeks yaratish:

CREATE INDEX myindex ON users (first_name);


-- Indeksga murojaat qilish:
SELECT * FROM users WHERE gender = 'Female';


-- Indeksga murojaat qilishning ikki joyida (AND operatori):
SELECT * FROM users WHERE gender = 'Female' AND first_name LIKE 'K%';


-- Indeksni foydalanishning hammasi (AND, OR operatorlari):
SELECT * FROM users WHERE gender = 'Female' OR first_name LIKE 'K%';



-- Bitta ustunga ikki indeks yaratish:
CREATE INDEX myidnex_name ON users (first_name);
CREATE INDEX my_index_country ON users (country);



-- Unikal indeks yaratish:
CREATE UNIQUE INDEX index_email ON users (email);


-- Beshlik (B-tree) indeks yaratish:
CREATE INDEX index_country ON users USING BTREE (country);

-- Bu misolda users jadvalidagi country ustuniga Beshlik (B-tree) indeksi yaratiladi. 
-- Beshlik indeks yo'qotish va katta ma'lumotlar ustida ishlashda yaxshi natijalarni beradi.


-- Indeksdan foydalanishning natijalarini ko'rish:
EXPLAIN ANALYZE SELECT * FROM users WHERE email like 'O%';


-- Indekslarni o'chirish:
DROP INDEX myindex;



-- Indekslarni monitoring qilish:
SELECT * FROM pg_indexes WHERE tablename = 'users';

-- Bu so'rov users jadvalidagi indekslarni ko'rsatadi.

-- Indeks yaratish, uni foydalanish va o'chirish bilan PostgreSQL ma'lumotlar 
    -- qidirish jarayonlarini tezlashtirishga imkon beradi. 

-- Indeksni ma'lumotlar ustida moslashtirishni, so'rovlar birlashmasini
    -- optimallashtirishni va iste'molchilarga tezlikni ta'minlashni o'z ichiga oladi.