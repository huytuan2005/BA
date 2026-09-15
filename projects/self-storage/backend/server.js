const http = require('node:http');
const fs = require('node:fs');
const path = require('node:path');
const { db } = require('./database');

const PORT = 3010;
const frontendDir = path.join(__dirname, '..', 'frontend');

function json(res, status, payload) {
  const body = JSON.stringify(payload);
  res.writeHead(status, { 'Content-Type': 'application/json; charset=utf-8', 'Access-Control-Allow-Origin': '*' });
  res.end(body);
}

function sendFile(res, filePath, contentType) {
  res.writeHead(200, { 'Content-Type': contentType });
  res.end(fs.readFileSync(filePath));
}

function readBody(req) {
  return new Promise((resolve, reject) => {
    let data = '';
    req.on('data', chunk => { data += chunk; });
    req.on('end', () => {
      try { resolve(data ? JSON.parse(data) : {}); }
      catch (err) { reject(err); }
    });
    req.on('error', reject);
  });
}

const server = http.createServer(async (req, res) => {
  try {
    const url = new URL(req.url, `http://${req.headers.host}`);

    if (req.method === 'GET' && url.pathname === '/api/facilities') {
      const facilities = db.prepare('SELECT id, name, address FROM facilities ORDER BY id').all();
      return json(res, 200, facilities);
    }

    const unitMatch = url.pathname.match(/^\/api\/facilities\/(\d+)\/units$/);
    if (req.method === 'GET' && unitMatch) {
      const facilityId = Number(unitMatch[1]);
      const units = db.prepare('SELECT id, facility_id, unit_type, size_sqft, rental_price_monthly, available FROM units WHERE facility_id = ? ORDER BY id').all(facilityId);
      return json(res, 200, units);
    }

    if (req.method === 'POST' && url.pathname === '/api/reservations') {
      const body = await readBody(req);
      const facilityId = Number(body.facilityId);
      const unitId = Number(body.unitId);
      const startDate = String(body.startDate || '');
      const rentalPeriodMonths = Number(body.rentalPeriodMonths);
      if (!facilityId || !unitId || !startDate || !Number.isInteger(rentalPeriodMonths) || rentalPeriodMonths < 1) {
        return json(res, 400, { error: 'facilityId, unitId, startDate and rentalPeriodMonths are required' });
      }
      const unit = db.prepare('SELECT id, facility_id, available FROM units WHERE id = ?').get(unitId);
      if (!unit || unit.facility_id !== facilityId) return json(res, 400, { error: 'Unit does not belong to facility' });
      if (!unit.available) return json(res, 409, { error: 'Unit is not available' });
      const createdAt = new Date().toISOString();
      const result = db.prepare('INSERT INTO reservations (facility_id, unit_id, start_date, rental_period_months, status, created_at) VALUES (?, ?, ?, ?, ?, ?)').run(facilityId, unitId, startDate, rentalPeriodMonths, 'REQUESTED', createdAt);
      const reservation = db.prepare('SELECT id, facility_id, unit_id, start_date, rental_period_months, status, created_at FROM reservations WHERE id = ?').get(result.lastInsertRowid);
      return json(res, 201, reservation);
    }

    const reservationMatch = url.pathname.match(/^\/api\/reservations\/(\d+)$/);
    if (req.method === 'GET' && reservationMatch) {
      const id = Number(reservationMatch[1]);
      const reservation = db.prepare('SELECT id, facility_id, unit_id, start_date, rental_period_months, status, created_at FROM reservations WHERE id = ?').get(id);
      if (!reservation) return json(res, 404, { error: 'Reservation not found' });
      return json(res, 200, reservation);
    }

    if (req.method === 'GET' && url.pathname === '/') return sendFile(res, path.join(frontendDir, 'index.html'), 'text/html; charset=utf-8');
    if (req.method === 'GET' && url.pathname === '/app.js') return sendFile(res, path.join(frontendDir, 'app.js'), 'text/javascript; charset=utf-8');
    if (req.method === 'GET' && url.pathname === '/styles.css') return sendFile(res, path.join(frontendDir, 'styles.css'), 'text/css; charset=utf-8');

    json(res, 404, { error: 'Not found' });
  } catch (err) {
    console.error(err);
    json(res, 500, { error: 'Internal server error' });
  }
});

server.listen(PORT, () => console.log(`Self-Storage MVP running at http://localhost:${PORT}`));
