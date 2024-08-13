
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

![alt text](docs/img/django_install_success.png)

**Generazione file statici**

Vado a creare la cartella che conterra i templates e ad inserire il codice

```bash
   mkdir templates/
   mkdir static/
```

e vado a creare i file che comporranno le pagine

#### index.html
```html
{% load static %}

<!DOCTYPE html>
<html lang="it">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Hotel Pegaso - Homepage</title>
    <!--Importo i css necessari online -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css">
    <link href="https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;700&display=swap" rel="stylesheet">
    <!-- Stili personalizzati -->
    <link rel="stylesheet" href="{% static 'css/style.css' %}">
</head>

<body>
    <!--Includo con templating la navbar-->
    {% include 'booking/_navbar.html' %}

    <!-- Gestione del carosello -->
    <div id="hotelCarousel" class="carousel slide mt-4" data-bs-ride="carousel" data-bs-interval="3000">
        <div class="carousel-indicators">
            <button type="button" data-bs-target="#hotelCarousel" data-bs-slide-to="0" class="active"
                aria-current="true" aria-label="Slide 1"></button>
            <button type="button" data-bs-target="#hotelCarousel" data-bs-slide-to="1" aria-label="Slide 2"></button>
            <button type="button" data-bs-target="#hotelCarousel" data-bs-slide-to="2" aria-label="Slide 3"></button>
        </div>
        <div class="carousel-inner">
            <div class="carousel-item active">
                <img src="../static/img/carousel_1.jpg" class="d-block w-100" alt="Hotel Pegaso">
            </div>
            <div class="carousel-item">
                <img src="../static/img/carousel_2.jpg" class="d-block w-100" alt="Camere di Lusso">
            </div>
            <div class="carousel-item">
                <img src="../static/img/carousel_3.jpg" class="d-block w-100" alt="Spa e Benessere">
            </div>
        </div>
        <button class="carousel-control-prev" type="button" data-bs-target="#hotelCarousel" data-bs-slide="prev">
            <span class="carousel-control-prev-icon" aria-hidden="true"></span>
            <span class="visually-hidden">Precedente</span>
        </button>
        <button class="carousel-control-next" type="button" data-bs-target="#hotelCarousel" data-bs-slide="next">
            <span class="carousel-control-next-icon" aria-hidden="true"></span>
            <span class="visually-hidden">Successivo</span>
        </button>
    </div>

    <div class="container mt-5">
        <div class="row">
            <div class="col-md-12">
                <h1 class="text-center">Benvenuti a Hotel Pegaso</h1>
                <p class="lead text-center">Goditi un soggiorno di lusso con i nostri servizi esclusivi.</p>
            </div>
        </div>

        <div class="container mt-5">
            <div class="row">
                <!-- Colonna per Chi Siamo -->
                <div class="col-md-6">
                    <h2>Chi Siamo</h2>
                    <p>Hotel Pegaso è il luogo ideale per rilassarsi e rigenerarsi. Offriamo un'esperienza unica con
                        camere
                        lussuose, ristoranti gourmet e un servizio impeccabile.</p>
                </div>
                <!-- Colonna per Contatti -->
                <div class="col-md-6 text-end">
                    <h2>Contatti</h2>
                    <p>Email: info@hotelpegaso.com</p>
                    <p>Telefono: +39 0123 456789</p>
                </div>
            </div>
        </div>
    </div>
</body>
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>

</html>
```

#### navbar.html
```html
{% load static %}

<nav class="navbar navbar-expand-lg navbar-light bg-light">
    <div class="container">
        <a class="navbar-brand" href="{% url 'index' %}">
            <i class="fas fa-leaf"></i> Hotel Pegaso
        </a>
        <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav"
            aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
            <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarNav">
            <ul class="navbar-nav ms-auto">
                <li class="nav-item">
                    <a class="nav-link {% if request.resolver_match.url_name == 'index' %}active{% endif %}"
                        href="{% url 'index' %}">Home</a>
                </li>
                <li class="nav-item">
                    <a class="nav-link {% if request.resolver_match.url_name == 'booking' %}active{% endif %}"
                        href="{% url 'booking' %}">Prenotazione</a>
                </li>
                <li class="nav-item">
                    <a class="nav-link {% if request.resolver_match.url_name == 'rooms' %}active{% endif %}"
                        href="{% url 'rooms' %}">Camere Disponibili</a>
                </li>
                <li class="nav-item">
                    <a class="nav-link {% if request.resolver_match.url_name == 'manage_booking' %}active{% endif %}"
                        href="{% url 'manage_booking' %}">Gestisci Prenotazione</a>
                </li>
            </ul>
        </div>
    </div>
</nav>
```

Come si può vedere dal codice, abbiamo alcuni elementi esclusivi della gestione django/jinja.

Innanzitutto il:

*{% load static %}*

Che ci permette di utilizzare i file statici definiti.

Poi abbiamo

*{% include 'navbar.html' %}*

Che ci permette di includere all'interno dei nostri template django dei sottotemplate, in modo da poter centralizzare la gestione di elementi comuni a tutte le pagine(in futuro andremo anche a sviluppare footer.html)

All'interno del file navbar.html abbiamo poi questi blocchi

```html
<a class="nav-link {% if request.resolver_match.url_name == 'manage_booking' %}active{% endif %}"
```

Questa sintassi ci permette di utilizzare una logica all'interno dei template.
Qui nello specifico andiamo a differenziare l'elemento active, in base al valore dell'url su cui ci troviamo

Infine vado a modificare il file settings.py per indicare a django dove sono questi file
```python
from django.db import models

# Modello per le stanze dell'hotel
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        #Aggiungo questa riga
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

...
...
...

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

#Verifivo la correttezza di questa riga
STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field
   ```

### Configurazione URLs e Path

Adesso vado a configurare i render delle views andando creare il file urls.py in booking
```python

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('booking/', views.booking_view, name='booking'),
    path('rooms/', views.rooms, name='rooms'),
    path('manage-booking/', views.manage_booking, name='manage_booking'),
]
```

in questo modo andiamo a definire le route della django app.

Andiamo poi a configurare a quale view corrispondono le singole pagine modificando views.py

```python
from django.shortcuts import render

# View per la homepage
def index(request):
    return render(request, 'index.html')

# View per la pagina di prenotazione
def booking_view(request):
    return render(request, 'booking.html')

# View per la pagina delle camere disponibili
def rooms(request):
    return render(request, 'rooms.html')

# View per la gestione delle prenotazioni
def manage_booking(request):
    return render(request, 'manage-booking.html')

```


Adesso andiamo invece ad includere i path di booking all'interno della main app andando a modificare il file urls.py nella cartella padre

```python
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('booking.urls')),  # Include le URL definite nell'app `booking`
]
```

Adesso in caso il server fosse ancora running chiudiamo il processo e lo riavviamo tramite

```bash
python manage.py runserver
```

Andando ora su http://127.0.0.1:8000/ ci troveremo davanti la nostra homepage

![alt text](homepage_1.png)

### Test Deploy su Azure

Adesso andiamo ad inizializzare il deploy dell'applicazione sulla nostra infrastruttura Azure.
Prima di tutto, andiamo a modificare il file settings.py andando a settare i valori per il nostro database in modo da usare quello in remoto invece di quello locale


```python

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('DB_NAME'),          
        'USER': os.getenv('DB_USER'),          
        'PASSWORD': os.getenv('DB_PASSWORD'),  
        'HOST': os.getenv('DB_HOST'),          
        'PORT': '5432',                        
    }
}


```

Avendo settato con app settings le variabili di ambiente, dall'app andiamo a prelevare i valori tramite os.getenv()
Andiamo a creare il requirements.txt andando ad aggiungere oltre a Django, anche le librerie di gestione del container wsgi, e della gestione di postgresql.

Andiamo adesso a lanciare la pipeline definita in Pipeline Deploy WebApp


## Infrastruttura
L'infrastruttura per il progetto consiste in una Service App deployata su Azure su cui girerà la nostra applicazione Django
Il tutto verrà gestito in modalità zero-touch, quindi sfruttando un linguaggio IaC, nello specifico terraform, andremo a gestire la creazione degli oggetti necessari.
In seguito la fase di deploy avverrà tramite github actions


[Naming Convention](https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/ready/azure-best-practices/resource-naming)

Voglio utilizzare come backend terraform uno storage account, quindi come prima cosa mi creo la subscription dove lavorerò, in seguito vado a creare all'interno uno storage account usando temporaneamente il backend local.

Quindi primo passo, installazione di azcli in locale, come da [documentazione](https://learn.microsoft.com/en-us/cli/azure/install-azure-cli-windows?tabs=winget#install-or-update)

```bash
winget install -e --id Microsoft.AzureCLI
```

Successivamente passiamo alla definizione del provider.tf


```terraform
terraform {
  required_providers {
    azurerm = {
      source  = "hashicorp/azurerm"
      version = "~> 3.0"
    }
  }
}

provider "azurerm" {
  features = {}

  # Se vuoi specificare la subscription manualmente
  subscription_id = "24174a6a-0206-4456-9d93-343680d2962b" 
}
```

E andiamo a definire il file che creerà lo storage account dedicato ad ospitare i tf statefiles

```terraform
resource "azurerm_resource_group" "main" {
  name     = "rg-terraform-states-001"
  location = "West Europe"
}

resource "azurerm_storage_account" "terraform" {
  name                     = "satfcrosswesteu001"
  resource_group_name      = azurerm_resource_group.main.name
  location                 = azurerm_resource_group.main.location
  account_tier             = "Standard"
  account_replication_type = "LRS"

  tags = {
    environment = "Cross"
  }
}

resource "azurerm_storage_container" "terraform" {
  name                  = "tfstate"
  storage_account_name  = azurerm_storage_account.terraform.name
  container_access_type = "private"
}

resource "azurerm_storage_account_network_rules" "terraform" {
  storage_account_id = azurerm_storage_account.terraform.id

  default_action = "Allow"
  bypass         = ["AzureServices"]

  ip_rules = []
}
```

Andiamo quindi prima ad effettuare l'az login per connetterci al nostro account azure


```bash
az login --tenant xxxxxxxxxxxxx
```

 e successivamente lanciamo

```bash
terraform init
terraform plan
```

A questo punto, se dal log otteniamo la creazione del solo storage account, procediamo con


```bash
terraform apply
```

Se tutto è stato eseguito correttamente, sul portale avremo un resource group con all'interno lo storage

![alt text](docs/img/portal_after_terraform_1.png)


Adesso, andiamo a configurare lo storage come remote backend in modo da svincolarci dallo sviluppo in locale.
Per far ciò, creiamo 3 cartelle in /terraform, e andiamo a creare i provider per i 3 ambienti


```terraform
terraform {
  backend "azurerm" {
    resource_group_name   = "rg-terraform-states-001"
    storage_account_name  = "satfcrosswesteu001"
    container_name        = "tfstate"
    #Cambiamo questo nome in base all'ambiente
    key                   = "developement.tfstate"  # Puoi personalizzare il nome del file di stato
  }

  required_providers {
    azurerm = {
      source  = "hashicorp/azurerm"
      version = "~> 3.0"
    }
  }
}

provider "azurerm" {
  features = {}
}
```

Rieffettuiamo
```bash
terraform init
```


e ora vedremo che all'interno del nostro container sono presenti i 3 file di gestione degli state

![alt text](docs/img/portal_after_terraform_2.png)

**⚠️ ATTENZIONE:** In caso doveste committare a questo punto, è necessario aggiungere al .gitignore terraform/*/.terraform/

### Gestione CI/CD

Per la gestione del lancio del terraform quando viene modificato il codice sul repository, andiamo ad utilizzare le Github Actions.

Il primo step sarà quello di creare un Service Principal su azure, che ci permetta di configurare le Actions, in modo che possano apportare modifiche al nostro portale.

Andiamo ad eseguire

```bash
ad sp create-for-rbac --name "sp-terraform-github-westeu-001" --role="Contributor" --scopes="/subscriptions/xxxxx" --sdk-auth
```

Andiamo ora a fornirgli i permessi per gestire key vault e storage accounts, inserendo il l'object id del service principal appena creato (visionabile dall'output o da portale)

```bash
az role assignment create --assignee <objectId> --role "Key Vault Contributor" --scope /subscriptions/xxxxx/resourceGroups/rg-pegaso-dev/providers/Microsoft.KeyVault/vaults/kv-pegaso-dev-westeu-001

az role assignment create --assignee <objectId> --role "Key Vault Secrets User" --scope /subscriptions/xxxxx/resourceGroups/rg-pegaso-dev/providers/Microsoft.KeyVault/vaults/kv-pegaso-dev-westeu-001

az role assignment create --assignee <objectId> --role "Storage Account Contributor" --scope /subscriptions/xxxxx/resourceGroups/rg-pegaso-dev/providers/Microsoft.Storage/storageAccounts/sapegasodev

az role assignment create --assignee <objectId> --role "Storage Blob Data Contributor" --scope /subscriptions/xxxxx/resourceGroups/rg-pegaso-dev/providers/Microsoft.Storage/storageAccounts/sapegasodev
```


e ci salviamo l'output contente i dati di connettività del service principal.

Andiamo ora a fornirgli i permessi per gestire key vault e storage accounts e rbac, inserendo il l'application id del service principal appena creato (visionabile dall'output o da portale)

```bash
az role assignment create --assignee <id> --role "Key Vault Contributor" --scope /subscriptions/xxxxx

az role assignment create --assignee <id> --role "Key Vault Secrets User" --scope /subscriptions/xxxxx

az role assignment create --assignee <id> --role "Storage Account Contributor" --scope /subscriptions/xxxxx

az role assignment create --assignee <id> --role "Storage Blob Data Contributor" --scope /subscriptions/xxxxx

az role assignment create --assignee <id> --role "User Access Administrator" --scope /subscriptions/xxxxx

az role assignment create --assignee <id> --role "Key Vault Secrets Officer" --scope /subscriptions/xxxxx

```

Successivamente andiamo ad inserire il json appena salvato sul portale dove risiede il nostro terraform.
Andiamo a creare i valori che verranno utilizzati all'interno della pipeline:

![alt text](docs/img/github_secrets.png)

Adesso abbiamo modo di far effettuare il deploy del nostro terraform, grazie alla connessione garantita dal nostro service principal

Andiamo ora a creare la cartella ./github/workflows, al cui interno inseriremo i nostri workflow per le github actions.

```yaml
name: 'Terraform Plan and Apply'

on:
  push:
    paths:
      - 'terraform/**'
    branches:
      - main
  pull_request:
    paths:
      - 'terraform/**'
    branches:
      - main
  workflow_dispatch:

jobs:
  terraform:
    runs-on: ubuntu-latest

    steps:
    - name: Checkout repository
      uses: actions/checkout@v3

    - name: Setup Terraform
      uses: hashicorp/setup-terraform@v2
      with:
        terraform_version: 1.4.5

    - name: Azure Login via Service Principal
      uses: azure/login@v1
      with:
        creds: ${{ secrets.AZURE_CREDENTIALS }}

    - name: Set up Azure environment variables
      run: |
          echo "ARM_CLIENT_ID=${{ secrets.ARM_CLIENT_ID }}" >> $GITHUB_ENV
          echo "ARM_CLIENT_SECRET=${{ secrets.ARM_CLIENT_SECRET }}" >> $GITHUB_ENV
          echo "ARM_SUBSCRIPTION_ID=${{ secrets.ARM_SUBSCRIPTION_ID }}" >> $GITHUB_ENV
          echo "ARM_TENANT_ID=${{ secrets.ARM_TENANT_ID }}" >> $GITHUB_ENV

    - name: Terraform Init
      working-directory: ./terraform/development
      run: terraform init

    - name: Terraform Plan
      working-directory: ./terraform/development
      run: terraform plan -out=tfplan.binary

    - name: Upload Plan for Review
      uses: actions/upload-artifact@v3
      with:
        name: tfplan
        path: |
              ./terraform/development/tfplan.binary
              ./terraform/development/.terraform.lock.hcl

  apply:
    runs-on: ubuntu-latest
    needs: terraform  
    environment: development  
    steps:
    - name: Checkout repository
      uses: actions/checkout@v3

    - name: Setup Terraform
      uses: hashicorp/setup-terraform@v2
      with:
        terraform_version: 1.4.5

    - name: Azure Login via Service Principal
      uses: azure/login@v1
      with:
        creds: ${{ secrets.AZURE_CREDENTIALS }}

    - name: Set up Azure environment variables
      run: |
          echo "ARM_CLIENT_ID=${{ secrets.ARM_CLIENT_ID }}" >> $GITHUB_ENV
          echo "ARM_CLIENT_SECRET=${{ secrets.ARM_CLIENT_SECRET }}" >> $GITHUB_ENV
          echo "ARM_SUBSCRIPTION_ID=${{ secrets.ARM_SUBSCRIPTION_ID }}" >> $GITHUB_ENV
          echo "ARM_TENANT_ID=${{ secrets.ARM_TENANT_ID }}" >> $GITHUB_ENV
          
    - name: Download Plan
      uses: actions/download-artifact@v3
      with:
        name: tfplan
        path: |
              ./terraform/development
    - name: Terraform Init with Lock File
      working-directory: ./terraform/development
      run: terraform init
      
    - name: Terraform Apply
      working-directory: ./terraform/development
      run: terraform apply "tfplan.binary"
```


I punti salienti qui sono:

```yaml
on:
  push:
    paths:
      - 'terraform/development/**'
    branches:
      - main
  workflow_dispatch:
```
Definiamo i trigger della pipeline.
In questo caso sono la push sulla cartella terraform di ambiente, per il branch main, e il lancio manuale

```yaml
- name: Azure Login via Service Principal
      uses: azure/login@v1
      with:
        creds: ${{ secrets.AZURE_CREDENTIALS }}

    - name: Set up Azure environment variables
      run: |
          echo "ARM_CLIENT_ID=${{ secrets.ARM_CLIENT_ID }}" >> $GITHUB_ENV
          echo "ARM_CLIENT_SECRET=${{ secrets.ARM_CLIENT_SECRET }}" >> $GITHUB_ENV
          echo "ARM_SUBSCRIPTION_ID=${{ secrets.ARM_SUBSCRIPTION_ID }}" >> $GITHUB_ENV
          echo "ARM_TENANT_ID=${{ secrets.ARM_TENANT_ID }}" >> $GITHUB_ENV
```

Qui andiamo ad effettuare la login grazie al json salvato in precedenza.
Successivamente andiamo a settare come variabili di ambiente del nostro workflow i parametri di connessione che verranno utilizzati dal terraform per effettuare le operazioni


```yaml
- name: Terraform Init
      working-directory: ./terraform/development
      run: terraform init

    - name: Terraform Plan
      working-directory: ./terraform/development
      run: terraform plan -out=tfplan.binary

    - name: Upload Plan for Review
      uses: actions/upload-artifact@v3
      with:
        name: tfplan
        path: |
              ./terraform/development/tfplan.binary
              ./terraform/development/.terraform.lock.hcl
```

Qui andiamo ad effettuare init ed il plan, e successivamente andiamo a salvare il nostro plan in modo da poterlo utilizzare negli step successivi

```yaml

- name: Azure Login via Service Principal
      uses: azure/login@v1
      with:
        creds: ${{ secrets.AZURE_CREDENTIALS }}

    - name: Set up Azure environment variables
      run: |
          echo "ARM_CLIENT_ID=${{ secrets.ARM_CLIENT_ID }}" >> $GITHUB_ENV
          echo "ARM_CLIENT_SECRET=${{ secrets.ARM_CLIENT_SECRET }}" >> $GITHUB_ENV
          echo "ARM_SUBSCRIPTION_ID=${{ secrets.ARM_SUBSCRIPTION_ID }}" >> $GITHUB_ENV
          echo "ARM_TENANT_ID=${{ secrets.ARM_TENANT_ID }}" >> $GITHUB_ENV
```

Essendo i vari step gestiti in modo separato, dobbiamo effettuare nuovamente la login e il setting delle variabili di ambiente

```yaml

- name: Download Plan
      uses: actions/download-artifact@v3
      with:
        name: tfplan
        path: |
              ./terraform/development
    - name: Terraform Init with Lock File
      working-directory: ./terraform/development
      run: terraform init
      
    - name: Terraform Apply
      working-directory: ./terraform/development
      run: terraform apply "tfplan.binary"
```

Infine concludiamo andando a scaricare i file di lock e di plan precedentemente generati, in modo da poter effettuare l'apply


Importante per il processo di corretta gestione della pipeline la seguente parte:

```yaml
apply:
    runs-on: ubuntu-latest
    needs: terraform  
    environment: development
```

Il parametro environment, ci permette di associare il lancio ad un github environment specifico.
Andiamo a creare un environment, e a settare la protection rule che ci permette di richiedere l'approval

![alt text](docs/img/github_environments.png)


Questo viene effettuato in quanto in questo modo, possiamo richiedere un'approval dello step prima di procedere, in modo da poter prima verificare il risultato del plan, e solo successivamente andarlo ad eseguire.

![alt text](docs/img/github_actions_approval.png)

![alt text](docs/img/github_env_protection_rule.png)


Andando adesso a creare i corrispondenti file per la gestione del workflow negli altri ambienti, abbiamo un metodo per aggiornare la nostra infrastruttura, completamente in remoto, e gestita da github.

### Pipeline Deploy WebApp

Andiamo a creare la pipeline che ci permetterà di effettuare il deploy della webapp sull'App Service creato.
Il contenuto sarà:

```yaml
name: Deploy Django App to Azure

on:
  push:
    paths:
      - 'hotel_pegaso/**'
    branches:
      - main
  workflow_dispatch:

jobs:
  build-and-deploy:
    runs-on: ubuntu-latest

    steps:
    - name: Checkout code
      uses: actions/checkout@v2

    - name: Set up Python
      uses: actions/setup-python@v2
      with:
        python-version: '3.9'

    - name: Deploy to Azure Web App
      uses: azure/webapps-deploy@v2
      with:
        app-name: 'as-pegaso-dev-westeu-001'
        publish-profile: ${{ secrets.AZURE_WEBAPP_PUBLISH_PROFILE }}
        package: ./hotel_pegaso
```

Come si vede da codice, servirà salvare come secret su github il publish profile della webapp.
Andiamo quindi ad eseguire

```bash
az webapp deployment list-publishing-profiles --name as-pegaso-dev-westeu-001 --resource-group rg-pegaso-dev-westeu-001 --xml
```
e a salvare il contenuto in un secret chiamato AZURE_WEBAPP_PUBLISH_PROFILE


Importante è che l'app service abbia come app settings i seguenti parametri

```terraform
"SCM_DO_BUILD_DURING_DEPLOYMENT"  = "true"
"PRE_BUILD_COMMAND"               = "echo Pre-build command executed"
"POST_BUILD_COMMAND"              = "python3 manage.py makemigrations && python3 manage.py migrate && python3 manage.py collectstatic --noinput"
"PYTHON_VERSION"                  = "3.9"
"SCM_BUILD_ARGS"                  = "--platform python --platform-version 3.9"
"PYTHON_ENABLE_WORKER_EXTENSIONS" = "true"
```

Queste servono per attivare e gestiro in modo corretto il lancio automatico del sistema di Build Oryx di App Service

Dopo aver lanciato la pipeline, se tutto è andato correttamente avremo 

![alt text](docs/img/django_on_app_service.png)

Oppure la nostra homepage se tutto viene configurato correttamente.

L'ultimo step da eseguire per concludere la configurazione è quello di creare un superuser per l'app django.Questo può essere fatto sempre tramite la pipeline usando il comando createsuperuser --noinput e andando a settare i parametri di ambiente per prelevare i valori necessari, quindi questi valori saranno settati su app_settings

- DJANGO_SUPERUSER_USERNAME

- DJANGO_SUPERUSER_EMAIL

- DJANGO_SUPERUSER_PASSWORD

e avendo lo step 

```bash
python3 manage.py createsuperuser --noinput
```
### Elementi infratrutturali

#### PostgreSQL
Useremo un Postgresql server come appoggio per l'applicazione.
Utilizzando lo SKU minore per motivi di costi, non avremo un livello di sicurezza adeguato ad un eventuale ambiente di produzione, in quanto non supporta la disabilitazione della navigazione pubblica, o la creazione di un private endpoint.
E' importante creare le firewall rules in azure per permettere la comunicazione tra la webapp ed il db

```terraform
resource "azurerm_postgresql_firewall_rule" "allow_azure_services" {
  name                = "AllowAzureServices"
  resource_group_name = azurerm_resource_group.dev_rg.name
  server_name         = azurerm_postgresql_server.postgres_server.name

  start_ip_address = "0.0.0.0"
  end_ip_address   = "0.0.0.0"
}

resource "azurerm_postgresql_firewall_rule" "allow_app_service_outbound2" {
  name                = "AllowAppServiceOutboundAccess2"
  resource_group_name = azurerm_resource_group.dev_rg.name
  server_name         = azurerm_postgresql_server.postgres_server.name

  start_ip_address = "10.0.1.0"
  end_ip_address   = "10.0.1.255"
}

```




## Improvements

- Utilizzare SKU Maggiori su DB per implementare navigazione privata
- Utilizzare self hosted agents per github actions
- Nascondere secret del db tramite keyvault reference su app settings


## BiblioGraphy

https://docs.github.com/en/actions

https://learn.microsoft.com/en-us/azure/developer/github/connect-from-azure

https://learn.microsoft.com/en-us/azure/app-service/quickstart-python?tabs=flask%2Cwindows%2Cazure-cli%2Cazure-cli-deploy%2Cdeploy-instructions-azportal%2Cterminal-bash%2Cdeploy-instructions-zip-azcli

https://developer.hashicorp.com/terraform/tutorials/automation/github-actions

https://learn.microsoft.com/en-us/training/modules/django-deployment/1-introduction

https://www.bing.com/search?q=azure+app+service+django+db+setup+terraform&qs=n&form=QBRE&sp=-1&ghc=1&lq=0&pq=azure+app+service+django+db+setup+terraform&sc=11-43&sk=&cvid=6653358178E841329B35E7202D451868&ghsh=0&ghacc=0&ghpl=

https://learn.microsoft.com/en-us/azure/app-service/configure-language-python

https://github.com/microsoft/Oryx/blob/main/doc/configuration.md

https://docs.djangoproject.com/en/3.0/ref/django-admin/#django-admin-createsuperuser