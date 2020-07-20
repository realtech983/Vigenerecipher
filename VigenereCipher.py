alphabets = "abcdefghijklmnopqrstuvwxyz"

letter_to_index = dict(zip(alphabets,range(len(alphabets))))
index_to_letter = dict(zip(range(len(alphabets)),alphabets))

def encrypt(msg,key):
    encrypted = ""
    #split msg acording to key
    split_msg = [msg[i:i+len(key)] for i in range(0,len(msg),len(key))]

    for each_split in split_msg:
        i=0
        for letter in each_split:
             number = (letter_to_index[letter] + letter_to_index[key[i]]) % len(alphabets)
             encrypted += index_to_letter[number]
             i+=1
    return encrypted

def decryption(cipher,key):
    decrypted = ""
    split_cipher = [cipher[i:i + len(key)] for i in range(0, len(cipher), len(key))]
    for each_split in split_cipher:
        i=0
        for letter in each_split:
             number = (letter_to_index[letter] - letter_to_index[key[i]]) % len(alphabets)
             decrypted += index_to_letter[number]
             i+=1
    return decrypted

def main():
    print("vigenerecipher:")
    print("\n1.Encryption\n2.Decryption")
    case = int(input("\nEnter Number : "))
    if case == 1:
        msg  = input("Enter Plain Text :")
        key = input("Enter Key :")
        print("Cipher Text is : ",encrypt(msg,key))
    elif case == 2:
        cipher = input("Enter Cipher Text :")
        key = input("Enter Key :")
        print("Original Text is : ",decryption(cipher,key))
    else:
        print("wrong input")


main()