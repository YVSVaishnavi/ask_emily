def validate_data(data):
    required_fields = ['location', 'preferences', 'start', 'destination', 'rig_size']  
    for field in required_fields:
        if field not in data:
            return False, f"Missing required field: {field}"
    if not isinstance(data['rig_size'], (int, float)) or data['rig_size'] <= 0:
        return False, "Invalid rig_size: it must be a positive number."
    if not isinstance(data['preferences'], str) or not data['preferences']:
        return False, "Invalid preferences: it must be a non-empty string."
    return True, "Validation successful."
