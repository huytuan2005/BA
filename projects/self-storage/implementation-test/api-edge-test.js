const assert = require('node:assert/strict');
const { spawn } = require('node:child_process');

function sleep(ms) {
  return new Promise(resolve => setTimeout(resolve, ms));
}

async function waitForServer(base, attempts = 30) {
  for (let i = 0; i < attempts; i += 1) {
    try {
      const response = await fetch(`${base}/api/facilities`);
      if (response.ok) return;
    } catch (_) {}
    await sleep(200);
  }
  throw new Error('server did not become ready');
}

async function run() {
  const base = 'http://127.0.0.1:3010';
  const server = spawn(process.execPath, ['backend/server.js'], { cwd: __dirname + '/..', stdio: 'ignore' });
  try {
    await waitForServer(base);

    const missingUnit = await fetch(`${base}/api/facilities/999/units`);
    assert.equal(missingUnit.status, 200);
    assert.deepEqual(await missingUnit.json(), []);

    const missingReservation = await fetch(`${base}/api/reservations/999999`);
    assert.equal(missingReservation.status, 404);

    const malformed = await fetch(`${base}/api/reservations`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ facilityId: 1, unitId: 101, startDate: '', rentalPeriodMonths: 0 })
    });
    assert.equal(malformed.status, 400);

    const wrongFacility = await fetch(`${base}/api/reservations`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ facilityId: 2, unitId: 101, startDate: '2026-10-01', rentalPeriodMonths: 1 })
    });
    assert.equal(wrongFacility.status, 400);

    console.log('MVP API edge-case test: PASS');
  } finally {
    server.kill();
  }
}

run().catch(err => {
  console.error(err);
  process.exit(1);
});
