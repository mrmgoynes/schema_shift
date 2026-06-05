from db_inspector import get_table_schema
from contract_validator import load_openapi_required_fields, validate_schema

DB_CONFIG = {
    "host": "localhost",
    "port": "5432",
    "user": "sdet_admin",
    "password": "SecretPassword123",
    "database": "user_directory"
}

print("Executing SchemaShift Contract Validation Suite...")

# 1. Fetch live database structural columns
db_columns = get_table_schema(DB_CONFIG, "users")

# 2. Extract required keys from our text blueprint contract
contract_fields = load_openapi_required_fields("openapi.yaml", "/users/{id}", "get")

print(f"\n[Contract Requirements]: {contract_fields}")
print(f"[Live Database State]  : {list(db_columns.keys())}")

# 3. Compare the layers to check for system drift
drift = validate_schema(db_columns, contract_fields)

if not drift:
    print("\n✅ SUCCESS: Database structure matches the API Contract perfectly!")
else:
    print(f"\n❌ CRITICAL FAILURE: API contract broken! Missing columns: {drift}")
