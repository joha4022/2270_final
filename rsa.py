## my main() function will take 3 parameter public key information (n and e) and message and print 
## the decrypted message to the user and it will prompt the user for a response to the message 
## and return the same public key information with encrypted response

import xml.etree.ElementTree as ET
import random

class Mini_E:
    # select 2 random primes 
    def select_primes(p1, p2):
        p1 = p1
        p2 = p2
        
        for i in range(1, p1):
            if(p1 % i) == 0:
                p1 += 1
        print(p1)


    # extended_euclidean_algo
    # function RETURNS M, S1 AND T1
    def extended_euclidean_algo(a, b):
        # variables for m, n, s1, t1, s2, t2. Use a list for bezout's coefficients
        m = a
        n = b
        s1_t1 = [1,0]
        s2_t2 = [0,1]
        # while loop: condition n>0
        while(n > 0):
            # k = m mod n, q = m // n (finding the quotient)
            # if the loop executes it means there is a remainder, k
            k = m % n
            q = m // n
            # new value m will become n and new value of n = k
            m = n
            n = k
            # variabl with _hat is a temporary value holder for new s1_t1 and s2_t2 value
            s1_t1_hat = s2_t2
            # s1_hat = s1-q*s2, s2_hat = t1-q*t2
            s2_t2_hat = [s1_t1[0]-q*s2_t2[0], s1_t1[1]-q*s2_t2[1]]
            # now assign them to s1_t1 and s2_t2
            s1_t1 = s1_t1_hat
            s2_t2 = s2_t2_hat
            
        # return m, s1_t1
        return m, s1_t1

    # find private key function RETURNS D "PRIVATE KEY"
    def Find_Private_Key_d(e, p, q):
        # use extended_euclidean_algo
        # and insert e and p-1*q-1 as the parameters
        # if the result is negative, add p-1*q-1 until positive number returns
        p1 = p-1
        q1 = q-1
        d = Mini_E.extended_euclidean_algo(e, p1*q1)[1][0]
        while(d < 0):
            d += (p1*q1)
        return d

    # factorize function RETURNS P & Q OR FALSE
    def factorize(n):
        for i in range(2, n-1):
            if n % i == 0:
                # return both p and q
                return i, n//i
        return False

    # convert num to string function RETURNS A STRING
    def Convert_Num(_list):
        _string = ''
        for i in _list:
            _string += chr(i)
        return _string

    # convert string to num function RETURNS LIST OF INT
    def Convert_Text(_string):
        integer_list = []
        for ltr in _string:
            integer_list.append(ord(ltr))
        return integer_list

    def Convert_Binary_String(_int):
        result = ""
        while (_int > 0):
            # num mod 2, insert the result into the list and use floor division
            result= result + str(_int % 2)
            _int = _int // 2
        return result

    # fme function RETURNS VALUE OF b**n mod m
    def FME(b, n, m):
        # variables
        # b^n mod m
        # result is value determined based on each digits of the binary and this algorithm, starting value 1
        # b_x, binary expansion of value n, in a string format, need to go in reverse order
        result = 1
        power = b % m
        b_x = Mini_E.Convert_Binary_String(n)
        
        # for loop to go through the binary expansion digits and modify result and power
        for i in b_x:
            
            # if i is 1, update the value of result
            if i == '1':
                result = (result * power) % m
            power = (power * power) % m
            
        # return final value of result
        return result

    # decode function RETURNS MESSAGE
    def Decode(n, d, cipher_text):
        message = ''
        decrpyted_int_list = []
        # use FME to get decrypted list of int
        for int in cipher_text:
            decrpyted_int_list.append(Mini_E.FME(int, d, n))
        # convert decrypted message to text
        message = Mini_E.Convert_Num(decrpyted_int_list)
        
        return message

    # encode function RETURNS A LIST OF CIPHER TEXT
    def Encode(n, e, message):
        cipher_text = []
        message_in_num = Mini_E.Convert_Text(message)
        for num in message_in_num:
            # use fme here to encrypt the message
            cipher_text.append(Mini_E.FME(num, e, n))
        
        return cipher_text

    # euclidean_alg RETURNS INT
    def Euclidean_Alg(a, b):
        r = a % b
        while r > 0:
            # r = a mod b
            # b mod r would be the next step and this would replace r
            a = b
            b = r
            r = a%b
        return b

    ## main function RETURNS N, E, CIPHER RESPONSE
    def search_encrypt(id, n, e, message):
        
        tree = ET.parse('example.xml')
        root = tree.getroot()

        # Change 'book' depending on the format of the xml
        for book in root:

            # a = cat.find(cat_a).text
            # b = cat.find(cat_b).text
            print(book.attrib['id'])
            # factorize and find the p and q value
            p = Mini_E.factorize(n)[0]
            q = Mini_E.factorize(n)[1]
        
        # if gcd(p,q) does not equal 1 notify the user, else decode
        if(Mini_E.Euclidean_Alg(p, q) != 1):
            print("Error: Double check the value of n.")
        else: 
            # find the private key
            d = Mini_E.Find_Private_Key_d(e, p, q)
            # decrypt the message
            decrypted_message = Mini_E.Decode(n, d, message)
            print(decrypted_message)
            response_message = input("Response: ")
            response_cipher = Mini_E.Encode(n, e, response_message)
            print ("\nn, e = {}, {}\ncipher = {}".format(n, e, response_cipher))


Mini_E.select_primes(random.randint(1,10000), random.randint(1,10000))