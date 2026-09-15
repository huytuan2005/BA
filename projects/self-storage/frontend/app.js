const facilityEl = document.getElementById('facility');
const unitEl = document.getElementById('unit');
const unitInfo = document.getElementById('unitInfo');
const result = document.getElementById('result');

async function loadFacilities() {
  const facilities = await fetch('/api/facilities').then(r => r.json());
  facilityEl.innerHTML = facilities.map(f => `<option value="${f.id}">${f.name} — ${f.address}</option>`).join('');
  await loadUnits();
}

async function loadUnits() {
  const units = await fetch(`/api/facilities/${facilityEl.value}/units`).then(r => r.json());
  const available = units.filter(u => u.available === 1);
  unitEl.innerHTML = available.map(u => `<option value="${u.id}">${u.unit_type} — ${u.size_sqft} sqft — ${u.rental_price_monthly.toLocaleString()} VND/month</option>`).join('');
  unitInfo.textContent = available.length ? 'Select an available unit.' : 'No available units.';
}

facilityEl.addEventListener('change', loadUnits);

document.getElementById('reserve').addEventListener('click', async () => {
  const payload = {
    facilityId: Number(facilityEl.value),
    unitId: Number(unitEl.value),
    startDate: document.getElementById('startDate').value,
    rentalPeriodMonths: Number(document.getElementById('months').value)
  };
  const response = await fetch('/api/reservations', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(payload)
  });
  const data = await response.json();
  result.textContent = response.ok
    ? `Reservation created: #${data.id} — ${data.status}`
    : `Error: ${data.error}`;
});

loadFacilities();
