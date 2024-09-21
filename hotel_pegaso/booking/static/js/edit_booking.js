document.getElementById('edit-booking-form').addEventListener('submit', function (e) {
    e.preventDefault();
    const formData = new FormData(this);
    const actionUrl = this.getAttribute('action');

    fetch(actionUrl, {
        method: 'POST',
        body: formData
    })
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok ' + response.statusText);
            }
            return response.json();
        })
        .then(data => {
            if (data.status === 'success') {
                let message = '';
                if (data.action === 'deleted') {
                    message = 'La prenotazione è stata cancellata con successo.';
                } else if (data.action === 'updated') {
                    message = 'La prenotazione è stata aggiornata con successo.';
                    message += ` <a href="${data.pdf_url}" target="_blank">Scarica il nuovo PDF</a>`;
                }
                document.getElementById('resultMessage').innerHTML = message;
                new bootstrap.Modal(document.getElementById('resultModal')).show();
            } else if (data.status === 'error') {
                document.getElementById('resultMessage').innerText = data.message;
                new bootstrap.Modal(document.getElementById('resultModal')).show();
            }
        })
        .catch(error => {
            console.error('There has been a problem with your fetch operation:', error);
        });
});
