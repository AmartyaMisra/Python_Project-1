import hashlib

# Get the string to be hashed from the user
message = input("Enter a message to hash: ")

# Encode the message as bytes using UTF-8 encoding
message_bytes = message.encode('utf-8')

# Use the SHA-1 hash function to compute the hash of the message
hash_object = hashlib.sha1(message_bytes)
hash_hex = hash_object.hexdigest()

# Print the hash to the console
print("SHA-1 hash:", hash_hex)



