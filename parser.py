import base64
def encode(key, clear):
    enc = []
    for i in range(len(clear)):
        key_c = key[i % len(key)]
        enc_c = chr((ord(clear[i]) + ord(key_c)) % 256)
        enc.append(enc_c)
    return base64.urlsafe_b64encode("".join(enc).encode()).decode()

def decode(key, enc):
    dec = []
    enc = base64.urlsafe_b64decode(enc).decode()
    for i in range(len(enc)):
        key_c = key[i % len(key)]
        dec_c = chr((256 + ord(enc[i]) - ord(key_c)) % 256)
        dec.append(dec_c)
    return "".join(dec)

def log_untaxed(self,data):
    path = 'resources/config_integrity.config'
    self.__key = 'zebrafamilyshridhar'
    # Data is of format: time_stamp as t_id , c_id , time , amount , products
    with open(path, 'a' if os.path.isfile(path) else 'w' ) as file_pointer:
        data = '&sep'.join(map(str,data))
        data = self.__encode(self.__key , data)
        file_pointer.write(data+'\n')
        file_pointer.flush()
        file_pointer.close()



f = open('resources/config_integrity.config' , 'r')
z = f.read()
f.close()

z = z.split('\n')

for i in z:
    key = 'emscustom'
    print( decode(key,i).split('&sep') )
