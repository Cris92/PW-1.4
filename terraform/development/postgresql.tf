resource "azurerm_postgresql_server" "postgres_server" {
  name                = "psql-pegaso-dev-westeu-001"
  location            = azurerm_resource_group.dev_rg.location
  resource_group_name = azurerm_resource_group.dev_rg.name

  administrator_login          = "adminuser123"
  administrator_login_password = azurerm_key_vault_secret.db_password.value
  ssl_enforcement_enabled      = false
  sku_name                     = "B_Gen5_1"
  version                      = "11"
  storage_mb                   = 5120
  backup_retention_days        = 7

  geo_redundant_backup_enabled  = false
  public_network_access_enabled = false

  depends_on = [
    azurerm_virtual_network.vnet,
    azurerm_subnet.subnet
  ]
}

resource "azurerm_postgresql_database" "postgres_db" {
  name                = "psqldb-pegaso-dev-westeu-001"
  resource_group_name = azurerm_resource_group.dev_rg.name
  server_name         = azurerm_postgresql_server.postgres_server.name
  charset             = "UTF8"
  collation           = "English_United States.1252"
}

resource "azurerm_private_endpoint" "postgres_private_endpoint" {
  name                = "pe-pegaso-dev-westeu-psql-001"
  location            = azurerm_resource_group.dev_rg.location
  resource_group_name = azurerm_resource_group.dev_rg.name
  subnet_id           = azurerm_subnet.subnet.id

  private_service_connection {
    name                           = "postgresConnection"
    private_connection_resource_id = azurerm_postgresql_server.postgres_server.id
    subresource_names              = ["postgresqlServer"]
    is_manual_connection           = false
  }
}
