#!/usr/bin/env python
from random import uniform
import math
from random import random
import random

    # GLOBAL VARIABLES
alphabet="abcdefghijklmnopqrstuvwxyz 1234567890-!@$%^&*(()_<>?QWERTYUIOPASDFGHJKLZXCVBNM"

    # SHIFT CIPHER 
def encode_shift(message):
    key=(random.randint(1000000000000000000000000000, 10000000000000000000000000000000000000000000000000000))
    print("Key: "+str(key))
    return shift_aux(message, key)

def decode_shift(message):
    key=-1*(int(input("Pick a Key: ")))
    return shift_aux(message, key)

def shift_aux(message, key):

    alphabet="abcdefghijklmnopqrstuvwxyz 1234567890-!@$%^&*(()_<>?QWERTYUIOPASDFGHJKLZXCVBNM"
    first_half=""
    second_half=""
    new_alphabet=""
    new_message=""
    if key==0:
        new_alphabet=alphabet
    elif key > 0:
        first_half=alphabet[:key]
        second_half=alphabet[key:]
        new_alphabet=second_half+first_half
    else:
        first_half=alphabet[:(len(alphabet)+key)]
        second_half=alphabet[(len(alphabet)+key):]
        new_alphabet=second_half+first_half
    for i in range(0,len(message)):

        index=alphabet.find(message[i])
        new_message+=new_alphabet[index]
    return new_message

#CIRCUMFERENCE CIPHER
def encode_circ(message):
    new_message=""
    for i in range(len(message)):
        new_message+=message[i]
        for j in range(4):
            index = int(uniform(0,len(alphabet)))
            new_message+=alphabet[index]
    return new_message

def decode_circ(message):
    new_message=""
    for i in range(len(message)):
        if (i%5==0):
            new_message+=message[i]
    return new_message

#MODULUS CIPHER
def encode_mod(message):
    new_message=""
    for i in range(len(message)):
        x=int(uniform(0,10))
        index=alphabet.find(message[i])
        new_message+=str(len(alphabet)*x+index)+" "
    return new_message

def decode_mod(message):
    new_message=""
    num_list = message.split()
    for i in range(len(num_list)):
        new_message+=alphabet[int(num_list[i])%len(alphabet)]
    return new_message

#RAIL FENCE CIPHER
def encode_rail(message):
    new_message=""
    str_1=""
    str_2=""
    for i in range(len(message)):
        if i%2==0:
            str_1+=message[i]
        else:
            str_2+=message[i]
    new_message=str_1+str_2
    return new_message

def decode_rail(message):
    new_message=""
    mid_index = math.ceil(len(message)/2)
    str_1=message[:mid_index]
    str_2=message[mid_index:]
    for i in range(len(str_1 and str_2)):
        new_message+=str_1[i]+str_2[i]
    if len(message)%2==1:
        new_message+=message[mid_index-1]
    return new_message
    
#MAIN CODE
    #VARIABLES

message=input("Type Your Message: ")
e_d=int(input("Do You Want to Encode(1) or Decode(2): "))
cipher_order=input("What Order of ciphers do You Want to Encode With\n1=Shift cipher\n2=Circumference cipher\n3=Modulus cipher\n4=Rail Fence cipher\nRemember That If You are Decoding You Must Put the Order Backwards\n(Place all the Numbers in a Order ex. 1234): ")
print("Cipher Order Backwards: "+cipher_order[::-1])

  #LOOPS AND IF STATEMENTS
for i in range(len(cipher_order)):
    if e_d==1:
        if (cipher_order[i]=="1"):
            message=encode_shift(message)
        if (cipher_order[i]=="2"):
            message=encode_circ(message)
        if (cipher_order[i]=="3"):
            message=encode_mod(message)
        if (cipher_order[i]=="4"):
            message=encode_rail(message)
    if e_d==2:
        if (cipher_order[i]=="1"):
            message=decode_shift(message)
        if (cipher_order[i]=="2"):
            message=decode_circ(message)
        if (cipher_order[i]=="3"):
            message=decode_mod(message)
        if (cipher_order[i]=="4"):
            message=decode_rail(message)
print(message)
