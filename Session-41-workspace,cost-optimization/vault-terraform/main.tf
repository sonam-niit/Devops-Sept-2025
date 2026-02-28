provider "vault" {
  
}
data "vault_kv_secret" "db"{
    path = "secret/db-pass"
}