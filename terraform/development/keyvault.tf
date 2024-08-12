resource "azurerm_key_vault" "keyvault" {
  name                      = "kv-pegaso-dev-westeu-001"
  location                  = azurerm_resource_group.dev_rg.location
  resource_group_name       = azurerm_resource_group.dev_rg.name
  enable_rbac_authorization = true

  sku_name  = "standard"
  tenant_id = data.azurerm_client_config.current.tenant_id
}
resource "random_password" "postgres_password" {
  length  = 16
  special = true
}


resource "azurerm_key_vault_secret" "db_password" {
  name         = "DBPASSWORD"
  value        = random_password.postgres_password.result
  key_vault_id = azurerm_key_vault.keyvault.id
}
