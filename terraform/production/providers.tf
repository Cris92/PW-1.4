terraform {
  backend "azurerm" {
    resource_group_name   = "rg-terraform-states-001"
    storage_account_name  = "satfcrosswesteu001"
    container_name        = "tfstate"
    key                   = "production.tfstate"  # Puoi personalizzare il nome del file di stato
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