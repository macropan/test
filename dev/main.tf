terraform {
  required_providers {
    azurerm = {
      source = "hashicorp/azurerm"
      version = "-> 2.65"
    }
  }
  required_version = ">= 1.1.0"
}

resource "azurerm_resource_group" "rg" {
  name = "cicd-test"
  location = "chinaeast2"
  
  tags = {
    Enviroment = "Test"
    Owner = "Pan Hong"
  }
}
