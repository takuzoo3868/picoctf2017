#!/usr/bin/env python3

# Decrypt with AES in ECB mode
# Author: takuzoo3868
# Last Modified: 15 Api 2017.

import base64
from Crypto.Cipher import AES

key = base64.b64decode("6v3TyEgjUcQRnWuIhjdTBA==")
ciphertext = base64.b64decode("rW4q3swEuIOEy8RTIp/DCMdNPtdYopSRXKSLYnX9NQe8z+LMsZ6Mx/x8pwGwofdZ")
crypter = AES.new(key, AES.MODE_ECB)
plaintext = crypter.decrypt(ciphertext).decode("utf-8")

print(plaintext)
