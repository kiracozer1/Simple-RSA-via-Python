
# cipher_list → şifreli sayılar, d → özel anahtar, n → modül
def decrypt(cipher_list, d, n):
    decrypted_list = []
    for c in cipher_list:
        m = pow(c, d, n)        # modüler üs alma: m = c^d % n
        decrypted_list.append(chr(m))  # sayıyı karaktere çevir
    return "".join(decrypted_list)    # tüm karakterleri birleştir ve string yap

# Kullanımı:
# decrypted_msg = decrypt(cipher_list, d, n)
# print(decrypted_msg)




def gcd(n1, n2):  #greatest common diviser
    r = n1 % n2
    while r != 0:
        n1 = n2
        n2 = r
        r = n1 % n2
        print("Döngü devam ediyor")
    
    print("Sona ulaşıldı, ebob:", n2)
    return n2
                

def rsaEncrypt(msg):
    p = 59
    q = 23
    n = p * q  # şifreleme ve çözmede kullanılacak modül
    nn = (p-1)*(q-1)  # euler fonksiyonu
    e = 17
    value=gcd(e,nn)
    if (value==1):
        print("Sorun yok devam edebilirsin.")
        d = pow(e, -1, nn)
        cipher_list=[]
        for i in msg:
            i=ord(i)
            c=(i**e)%n
            cipher_list.append(c)
        cipher_text="".join(str(c) for c in cipher_list)
        print(cipher_text)
        return cipher_list,d,n
         
    else:
         print("e değerini yeniden seç.")

message=input("Lütfen şifrelemek istediğiniz kelimeyi giriniz:")
cipherList,prvtKey,modul=rsaEncrypt(message)

if cipherList:
  print("2. Şifreli Liste (Sayılar):", cipherList)
    
    # Deşifreleme fonksiyonuna şifreli listeyi ve anahtarları gönder
decyrptedText = decrypt(cipherList, prvtKey, modul)
print("3. Deşifre Edilen Mesaj:", decyrptedText)    

