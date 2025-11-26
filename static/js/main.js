document.getElementById('expenseForm').addEventListener('submit', async function(e) {
    e.preventDefault();
    let form = e.target;
    let data = {
        amount: form.amount.value,
        category: form.category.value,
        note: form.note.value
    };

    let response = await fetch('/add', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(data)
    });

    let expense = await response.json();

    // Append new expense to the table
    let table = document.getElementById('expenseTable').querySelector('tbody');
    let row = table.insertRow();
    row.insertCell(0).innerText = expense.id;
    row.insertCell(1).innerText = expense.amount;
    row.insertCell(2).innerText = expense.category;
    row.insertCell(3).innerText = expense.note;

    form.reset();
});
