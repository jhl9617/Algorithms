import base64

encoded_string = "TFdGUFJreDBTV0ZwVDB4aVpraENlbEUxVFdOT1pXTklRMk15U1ZSZk5IazFSMWhTTUdGWWQyMUlWUQ=="
decoded_bytes = base64.b64decode(encoded_string)

print(decoded_bytes)