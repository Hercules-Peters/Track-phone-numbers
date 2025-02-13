import phonenumbers
from phonenumbers import geocoder, carrier

# Enter the phone number in E.164 format
phone_number = phonenumbers.parse("+254712345678")

# Get the location information
location = geocoder.description_for_number(phone_number, "en")

# Get the carrier information
service_provider = carrier.name_for_number(phone_number, "en")

print(f"Location: {location}")
print(f"Service Provider: {service_provider}")

