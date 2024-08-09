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