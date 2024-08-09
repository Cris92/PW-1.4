
# Hotel Pegaso - Sistema di Prenotazione

Questo progetto implementa un sistema di prenotazione per l'Hotel Pegaso utilizzando Django come framework backend.

## Strumenti Utilizzati

 - Visual Studio Code
 - Git
 - WinGet


## Altre Info

### Conventional Commit

Il progetto viene gestito seguendo le indicazioni di [conventional commit](https://www.conventionalcommits.org/en/v1.0.0/) 
Per utilizzare al meglio le convenzioni ho utilizzato cz-commit.
Per installarlo prima di tutto ci serve NPM
```cmd
winget install Node.js
```

Successivamente installo il tool utilizzando 

```cmd
npm i cz-customizable -g
```

Successivamente creo un file .cz-config.js nella root di progetto e copio il contenuto di https://github.com/leoforfree/cz-customizable/blob/master/.cz-config.js al suo interno.
Dopodichè invece che eseguire le commit, successivamente al git add, eseguo
 
```cmd
cz-cust
```

e avrò degli step interattivi per eseguire una commit secondo le convenzioni

## Struttura del Progetto

- **hotel_pegaso/**: Contiene l'app principale del progetto.
  - **booking/**: Contiene i dati relativi alla Django app booking.
  - **hotel_pegaso/**: Contiene i file di configurazione del Django Project.
    - **manage.py**: Script di gestione del progetto Django.

## Sviluppo

### Prerequisiti

- **Python 3.x** deve essere installato sul sistema.
- **virtualenv** per creare un ambiente virtuale (opzionale ma raccomandato).

### Configurazione dell'Ambiente di Sviluppo

**Creo un ambiente virtuale** (opzionale ma raccomandato):

```bash
python -m venv myenv
```

**Attivo l'ambiente virtuale**:
  
```bash
myenv\Scripts\activate
```

**Installo Django**:

   Con l'ambiente virtuale attivato, esegui:

```bash
pip install django
```

**Creo un nuovo progetto Django**:

```bash
django-admin startproject hotel_pegaso
cd hotel_pegaso
```

**Creo una nuova app Django**:

```bash
python manage.py startapp booking
```

**Configuro il progetto**:

   - Aggiungi `booking` a `INSTALLED_APPS` in `settings.py`.
```bash
   INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    #Aggiungi qui
    'booking',
]
```

**Eseguo le migrazioni iniziali**:

```bash
python manage.py migrate
```

**Creo un superutente** (facoltativo):

```bash
python manage.py createsuperuser
```

**Avvio il server di sviluppo**:

```bash
python manage.py runserver
```
**Verifico corretta installazione**:

```bash
curl http://127.0.0.1:8000
```
Se tutto è stato installato correttamente dovreste avere una response, altrimenti se navigate tramite browser, vedrete questo:

![alt text](django_install_success.png)