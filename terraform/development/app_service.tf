# Crea un Service Plan su Linux
resource "azurerm_service_plan" "asp" {
  name                = "asp-pegaso-dev-westeu-001"
  location            = azurerm_resource_group.dev_rg.location
  resource_group_name = azurerm_resource_group.dev_rg.name
  sku_name            = "B1"
  os_type             = "Linux"

}

# Crea un Linux App Service
resource "azurerm_linux_web_app" "app" {
  name                = "as-pegaso-dev-westeu-001"
  location            = azurerm_resource_group.dev_rg.location
  resource_group_name = azurerm_resource_group.dev_rg.name
  service_plan_id     = azurerm_service_plan.asp.id

  site_config {
  }
  app_settings = {
    "SCM_DO_BUILD_DURING_DEPLOYMENT"  = "true"
    "PRE_BUILD_COMMAND"               = "echo Pre-build command executed"
    "POST_BUILD_COMMAND"              = "python3 manage.py makemigrations && python3 manage.py migrate && python3 manage.py collectstatic --noinput && python3 manage.py createsuperuser --noinput"
    "PYTHON_VERSION"                  = "3.9"
    "SCM_BUILD_ARGS"                  = "--platform python --platform-version 3.9"
    "PYTHON_ENABLE_WORKER_EXTENSIONS" = "true"
    "DJANGO_SUPERUSER_USERNAME"       = "admin"
    "DJANGO_SUPERUSER_EMAIL"          = "admin@example.com"
    "DJANGO_SUPERUSER_PASSWORD"       = "SuperSecretPassword"
    "DB_HOST"                         = azurerm_postgresql_server.postgres_server.fqdn
    "DB_NAME"                         = azurerm_postgresql_database.postgres_db.name
    "DB_USER"                         = "${azurerm_postgresql_server.postgres_server.administrator_login}@${azurerm_postgresql_server.postgres_server.name}"
    "DB_PASSWORD"                     = azurerm_key_vault_secret.db_password.value
    "SECRET_KEY"                      = "django-insecure-de^(3m@7^j+4vix#p&1vj)(3h_tr(h+5d%uofit*g8zb9ecc6a"
  }
}
