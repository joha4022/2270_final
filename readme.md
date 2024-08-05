# Mini RSA Encrypter
This is mini python tool that extracts information from the xml file based on the user's requset and encrypt the message and outputs an encrypted version of the xml file. It can also decrypt the encrypted xml by entering in the `n` and `e` values provided from the initial encryption.

## Fundamentals
RSA is an asymmetric crytophgraphy that requires public key and a private key. It is based on the idea that it's extremely time consuming and difficult to factor a composite number. This tool uses basic mathematical fundamentals and algorithms such as Euclidean algorithm and extended Euclidean algorithm to derive a public key generated from 2 randomly generated prime numbers that are between 1 to 10,000. This is only to show a simple concept of how the RSA works in its most basic form.

## Functionalities
1. Run the rsa_ui.py file using python
2. To encrypt the message, browse and select the example.xml and press `Encrypt`
  - This will open up a pop-up window that will provide the user with `n` and `e` value
  - Without these values, the user will not be able to decrypt the message
  - There will be a new xml file in the same directory named, `encrypted_` + `original_file_name.xml`
3. To decrypt the message, brwose and selected the encrypted xml file and press `Decrypt`
  - This will prompt a pop-up window that requires the user to enter `n` and `e` value
  - There will be a new xml file in the same directory named, `decrypted_` + `original_file_name.xml`
