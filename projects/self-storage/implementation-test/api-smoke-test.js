const assert = require('node:assert/strict');

async function run() {
  const base = 'http://127.0.0.1:3010';
  const facilities = await fetch(`${base}/api/facilities`).then(r => r.json());
  assert.ok(facilities.length >= 1, 'facilities should exist');

  const units = await fetch(`${base}/api/facilities/${facilities[0].id}/units`).then(r => r.json());
  const available = units.find(u => u.available === 1);
  assert.ok(available, 'an available unit should exist');

  const create = await fetch(`${base}/api/reservations`, {
    method: 'POST', headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ facilityId: facilities[0].id, unitId: available.id, startDate: '2026-10-01', rentalPeriodMonths: 3 })
  });
  assert.equal(create.status, 201);
  const reservation = await create.json();
  assert.equal(reservation.status, 'REQUESTED');

  const read = await fetch(`${base}/api/reservations/${reservation.id}`);
  assert.equal(read.status, 200);
  const loaded = await read.json();
  assert.equal(loaded.id, reservation.id);
  assert.equal(loaded.rental_period_months, 3);

  console.log('MVP API smoke test: PASS');
}

run().catch(err => { console.error(err); process.exit(1); });
