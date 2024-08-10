# Mini RSA Encrypter
This is mini python tool that extracts information from the xml file based on the user's requset and encrypt the message and outputs an encrypted version of the xml file. It can also decrypt the encrypted xml by entering in the `n` and `e` values provided from the initial encryption.

## Fundamentals
RSA is an asymmetric cryptography method that requires a public key and a private key. It is based on the idea that it is extremely time-consuming and difficult to factor a composite number. This tool uses basic mathematical fundamentals and algorithms, such as the Euclidean algorithm and the extended Euclidean algorithm, to derive a public key generated from two randomly selected prime numbers that are between 1 and 10,000. This is meant to demonstrate a simple concept of how RSA works in its most basic form.<br>
<br>
The purpose behind this project is to extract a specific message or text in an XML that would usually be transmitted via a SOAP message, encrypt and compress the message, and send it via another method, such as radio frequency or over a secure network, and then decrypt the message once received by another device. This requirement is a simplified version of one of the small projects I am working on in the military. There are encryption tools such as TACLANES already available as resources, but they are typically used to encrypt an entire network, and using them for a project this small would only create technical debt. In addition, it would require the user to maintain the proper keys and such. I wanted to develop something that can simply extract, encrypt, and compress data so it can be sent via any method possible and be extremely easy for the user to utilize.
<br>
<br>
RSA encryption can be implemented using libraries such as cryptography, but I wanted to reuse my other project that delves into the mathematical concepts of how RSA cryptography works, involving different algorithms that manipulate prime numbers, composite numbers, factoring, and modulo operations.<br>
<br>
For data structure, only an array is used when the message is being converted into numerical values using Python's ord() function. As the letters in the XML message are converted, their numerical values are pushed into the array, which is returned once all the letters have been converted. Then, using those numerically converted values, the array is iterated through to encrypt each value.<br>
<br>
For this project, example.xml is used, and no compression is applied yet. The reason why certain sections of the XML are encrypted is hardcoded in the rsa.py file is that the XML file will always be in a specific format according to the user. For the sake of simplicity, this will not encrypt the tag but change it so the user has no idea what the tag represents.

## Functionalities
1. Run the rsa_ui.py file using python
2. To encrypt the message, browse and select the example.xml and press `Encrypt`
  - This will open up a pop-up window that will provide the user with `n` and `e` value
  - Without these values, the user will not be able to decrypt the message
  - There will be a new xml file in the same directory named, `encrypted_` + `original_file_name.xml`
3. To decrypt the message, brwose and selected the encrypted xml file and press `Decrypt`
  - This will prompt a pop-up window that requires the user to enter `n` and `e` value
  - There will be a new xml file in the same directory named, `decrypted_` + `original_file_name.xml`
