const units = [
  { facility: 'Central Facility', type: 'Small', size: '2 m²', price: '$60/month', available: 8 },
  { facility: 'Central Facility', type: 'Medium', size: '5 m²', price: '$120/month', available: 4 },
  { facility: 'West Facility', type: 'Large', size: '10 m²', price: '$210/month', available: 3 }
];

const unitList = document.getElementById('unit-list');
const facility = document.getElementById('facility');
const unitType = document.getElementById('unitType');
const form = document.getElementById('reservation-form');
const result = document.getElementById('result');

const facilities = [...new Set(units.map(u => u.facility))];
const types = [...new Set(units.map(u => u.type))];

unitList.innerHTML = units.map(u => `
  <article class="unit">
    <h3>${u.facility} — ${u.type}</h3>
    <p>Size: ${u.size}</p>
    <p>Rental price: ${u.price}</p>
    <p>Available units: ${u.available}</p>
  </article>
`).join('');

facility.innerHTML = facilities.map(value => `<option value="${value}">${value}</option>`).join('');
unitType.innerHTML = types.map(value => `<option value="${value}">${value}</option>`).join('');

form.addEventListener('submit', event => {
  event.preventDefault();
  result.hidden = false;
  result.textContent = `Demo reservation submitted for ${facility.value}, ${unitType.value}, starting ${document.getElementById('startDate').value}, period ${document.getElementById('rentalPeriod').value}. No data is persisted.`;
});
