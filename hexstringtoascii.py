#program to convert hex string to ascii string
#ishan hambir 

hexa_string="0x48657920436F6465722E"

slicing=hexa_string[2:]

converting_hexa=bytes.fromhex(slicing)

ascii_string=converting_hexa.decode()

print(ascii_string)