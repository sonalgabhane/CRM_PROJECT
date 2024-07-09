import uuid
def generate_lead_no():
    code = str(uuid.uuid4()).replace("-", "")[:5]
    return code