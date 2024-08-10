resource "azurerm_app_service_plan" "asp" {
  name                = "asp-pegaso-dev-westeu-001"
  location            = azurerm_resource_group.dev_rg.location
  resource_group_name = azurerm_resource_group.dev_rg.name
  kind                = "Linux"

  sku {
    tier = "Basic"
    size = "B1"
  }
}

resource "azurerm_app_service" "app" {
  name                = "as-pegaso-dev-westeu-001"
  location            = azurerm_resource_group.dev_rg.location
  resource_group_name = azurerm_resource_group.dev_rg.name
  app_service_plan_id = azurerm_app_service_plan.asp.id

  app_settings = {
    "WEBSITE_RUN_FROM_PACKAGE" = "1"
    "DB_HOST"                  = azurerm_postgresql_server.postgres_server.fqdn
    "DB_NAME"                  = azurerm_postgresql_database.postgres_db.name
    "DB_USER"                  = "${azurerm_postgresql_server.postgres_server.administrator_login}@${azurerm_postgresql_server.postgres_server.name}"
    "DB_PASSWORD"              = azurerm_key_vault_secret.db_password.value
  }
}
