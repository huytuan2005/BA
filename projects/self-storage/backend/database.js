const { DatabaseSync } = require('node:sqlite');
const path = require('node:path');

const db = new DatabaseSync(path.join(__dirname, 'self-storage.sqlite'));

db.exec(`
  PRAGMA foreign_keys = ON;
  CREATE TABLE IF NOT EXISTS facilities (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    address TEXT NOT NULL
  );
  CREATE TABLE IF NOT EXISTS units (
    id INTEGER PRIMARY KEY,
    facility_id INTEGER NOT NULL,
    unit_type TEXT NOT NULL,
    size_sqft INTEGER NOT NULL,
    rental_price_monthly INTEGER NOT NULL,
    available INTEGER NOT NULL CHECK (available IN (0,1)),
    FOREIGN KEY (facility_id) REFERENCES facilities(id)
  );
  CREATE TABLE IF NOT EXISTS reservations (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    facility_id INTEGER NOT NULL,
    unit_id INTEGER NOT NULL,
    start_date TEXT NOT NULL,
    rental_period_months INTEGER NOT NULL,
    status TEXT NOT NULL,
    created_at TEXT NOT NULL,
    FOREIGN KEY (facility_id) REFERENCES facilities(id),
    FOREIGN KEY (unit_id) REFERENCES units(id)
  );
`);

const count = db.prepare('SELECT COUNT(*) AS c FROM facilities').get().c;
if (count === 0) {
  db.prepare('INSERT INTO facilities (id, name, address) VALUES (?, ?, ?)').run(1, 'Sunrise Storage', 'District 7, Ho Chi Minh City');
  db.prepare('INSERT INTO facilities (id, name, address) VALUES (?, ?, ?)').run(2, 'Riverside Storage', 'Thu Duc City, Ho Chi Minh City');
  db.prepare('INSERT INTO units (id, facility_id, unit_type, size_sqft, rental_price_monthly, available) VALUES (?, ?, ?, ?, ?, ?)').run(101, 1, 'Small', 25, 800000, 1);
  db.prepare('INSERT INTO units (id, facility_id, unit_type, size_sqft, rental_price_monthly, available) VALUES (?, ?, ?, ?, ?, ?)').run(102, 1, 'Medium', 50, 1400000, 1);
  db.prepare('INSERT INTO units (id, facility_id, unit_type, size_sqft, rental_price_monthly, available) VALUES (?, ?, ?, ?, ?, ?)').run(201, 2, 'Small', 25, 750000, 1);
}

module.exports = { db };
