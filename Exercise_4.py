import random


def encode(message):
    if len(message) >= 3:
        first_letter = message[0]
        modified_message = message[1:] + first_letter
        random_chars = ''.join(random.choices(
            'abcdefghijklmnopqrstuvwxyz', k=3))
        encoded_message = random_chars + modified_message + random_chars
        return encoded_message
    else:
        return message[::-1]


def decode(message):
    if len(message) < 3:
        return message[::-1]
    else:
        random_chars = message[:3]
        modified_message = message[3:-1] + message[0]
        return modified_message


print("Welcome to the Secret Code Machine\n")
choice = int(input("Press 1 for coding and 2 for decoding: "))

if choice == 1:
    original_message = input("Enter a message: ")
    encrypted_message = encode(original_message)
    print('Encrypting...')
    print('Encoded message:', encrypted_message)
elif choice == 2:
    encrypted_message = input("Enter an encrypted message: ")
    decrypted_message = decode(encrypted_message)
    print('Decrypting...')
    print('Decoded message:', decrypted_message)
else:
    print("Invalid choice. Please select 1 for coding or 2 for decoding.")
