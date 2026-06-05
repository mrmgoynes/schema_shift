import yaml

def load_openapi_required_fields(openapi_path, endpoint, method, status_code="200"):
    """Reads the OpenAPI YAML file and extracts fields marked as required."""
    with open(openapi_path, 'r') as file:
        spec = yaml.safe_load(file)
        
    try:
        # Navigate through the standard OpenAPI dictionary path structure
        content = spec['paths'][endpoint][method]['responses'][status_code]['content']
        schema = content['application/json']['schema']
        return schema.get('required', [])
    except KeyError:
        print(f"Error: Path structure not found for {method.upper()} {endpoint}")
        return []

def validate_schema(db_columns, required_fields):
    """Compares live database columns against contract expectations."""
    missing_fields = []
    
    for field in required_fields:
        if field not in db_columns:
            missing_fields.append(field)
            
    return missing_fields
