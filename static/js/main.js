// Show spinner on submit
const form = document.querySelector('form');
const spinner = document.getElementById('loadingSpinner');
form.addEventListener('submit', () => { spinner.style.display = 'block'; });

// Temperature Unit Switch
const celsiusBtn = document.getElementById('celsiusBtn');
const fahrenheitBtn = document.getElementById('fahrenheitBtn');
let currentUnit = 'C';
function convertTemp(tempC) { return currentUnit === 'C' ? tempC : (tempC * 9 / 5 + 32).toFixed(1); }
function updateTemperatures() { document.querySelectorAll('.card h2, .forecast-card strong, .details-list b').forEach(el => { if (el.dataset.tempC) el.innerText = convertTemp(parseFloat(el.dataset.tempC)) + '°' + currentUnit; }); }
celsiusBtn.onclick = () => { currentUnit = 'C'; updateTemperatures(); };
fahrenheitBtn.onclick = () => { currentUnit = 'F'; updateTemperatures(); };
document.querySelectorAll('.card h2, .forecast-card strong, .details-list b').forEach(el => { el.dataset.tempC = parseFloat(el.innerText); });

// Search History
const historyDiv = document.getElementById('historyButtons');
const searchInput = document.querySelector('input[name="city"]');
let history = JSON.parse(localStorage.getItem('weatherHistory') || '[]');
function renderHistory() { historyDiv.innerHTML = ''; history.forEach(city => { const btn = document.createElement('button'); btn.className = 'btn btn-sm btn-outline-secondary me-1 mb-1'; btn.innerText = city; btn.onclick = () => { searchInput.value = city; searchInput.form.submit(); }; historyDiv.appendChild(btn); }); }
renderHistory();
form.addEventListener('submit', () => { const city = searchInput.value.trim(); if (!history.includes(city)) { history.unshift(city); if (history.length > 5) history.pop(); localStorage.setItem('weatherHistory', JSON.stringify(history)); } renderHistory(); });

// Refresh Button
document.getElementById('refreshBtn').onclick = () => { const city = searchInput.value.trim(); if (city) form.submit(); };


