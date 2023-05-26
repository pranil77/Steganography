import pywhatkit

# set the phone number and message
phone_number = '+919022195405'  # replace with the phone number you want to send the message to
message = 'Hello, this is a test message!'

# set the path to the image file
image_path = "E:\\Steganography-Tools-master\\Steganography-Tools-master\\hidden.png"

# send the image with the message
pywhatkit.sendwhats_image(phone_number, image_path, caption=message)