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
    app_command_line = "/home/site/wwwroot/hotel_pegaso/app_service_config.sh"
    linux_fx_version = "PYTHON|3.9"
  }
  app_settings = {
    "WEBSITE_RUN_FROM_PACKAGE"        = "1"
    "PYTHON_ENABLE_WORKER_EXTENSIONS" = "true"
    "DB_HOST"                         = azurerm_postgresql_server.postgres_server.fqdn
    "DB_NAME"                         = azurerm_postgresql_database.postgres_db.name
    "DB_USER"                         = "${azurerm_postgresql_server.postgres_server.administrator_login}@${azurerm_postgresql_server.postgres_server.name}"
    "DB_PASSWORD"                     = azurerm_key_vault_secret.db_password.value
    "SECRET_KEY"                      = "django-insecure-de^(3m@7^j+4vix#p&1vj)(3h_tr(h+5d%uofit*g8zb9ecc6a"
  }
}
