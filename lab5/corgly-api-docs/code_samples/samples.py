import requests

# ==============================================================================
# Endpoint 1: POST /v1/pets/upload-photo
# Context: Uploads a local JPEG image file to update a specific pet's profile picture.
# Assumes an active API JWT token and a valid local file path.
# ==============================================================================
auth_token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."
headers = {"Authorization": f"Bearer {auth_token}"}

with open("einstein.jpg", "rb") as image_file:
    payload_files = {"photo": image_file}
    payload_data = {"pet_id": "corgi_98231"}
    
    upload_response = requests.post(
        "https://api.corg.ly/v1/pets/upload-photo",
        headers=headers,
        data=payload_data,
        files=payload_files
    )

print(upload_response.json())
# Expected Output: {"status": "success", "photo_url": "https://media.corg.ly/photos/einstein.jpg"}


# ==============================================================================
# Endpoint 2: POST /v1/audio/translate-bark
# Context: Sends a pet audio recording to the translation engine to obtain a human-language meaning.
# Assumes a valid audio file named 'sample_bark.wav' in the execution path.
# ==============================================================================
with open("sample_bark.wav", "rb") as audio_file:
    payload_files = {"audio_file": audio_file}
    
    translation_response = requests.post(
        "https://api.corg.ly/v1/audio/translate-bark",
        headers=headers,
        files=payload_files
    )

print(translation_response.json())
# Expected Output: {"translation": "I demand treats immediately!", "confidence": 0.98}


# ==============================================================================
# Endpoint 3: POST /v1/webhooks/subscribe
# Context: Registers a customer webhook endpoint to receive notifications when a bark is processed.
# Assumes a publicly accessible HTTPS endpoint ready to accept HTTP POST calls.
# ==============================================================================
subscription_payload = {
    "target_url": "https://myapp.com/webhooks/corgly",
    "event_type": "pet.bark_detected"
}

webhook_response = requests.post(
    "https://api.corg.ly/v1/webhooks/subscribe",
    headers=headers,
    json=subscription_payload
)

print(webhook_response.json())
# Expected Output: {"subscription_id": "sub_88321", "status": "active"}