from django.shortcuts import render
from . import rsaProject

# Create your views here.
def index(request):
    return render(request, 'index.html')

def enc_dec_view(request):

    m = []
    c = []
    plaintext = []

    #Plaintext sequence
    m1 = request.GET.get('message1')
    m2 = request.GET.get('message2')
    m3 = request.GET.get('message2')
    original_m = list()
    original_m.append(m1)
    original_m.append(m2)
    original_m.append(m3)

    # Encryption
    c,n,e = rsaProject.encryptionAlg(original_m)

    # Decryption
    plaintext = rsaProject.decryptionAlg(c, n, e)

    encrypted_m = c
    decrypted_m = plaintext

    context = {
        'original_m1': original_m[0],
        'original_m2': original_m[1],
        'original_m3': original_m[2],
        'encrypted_m1': encrypted_m[0],
        'encrypted_m2': encrypted_m[1],
        'encrypted_m3': encrypted_m[2],
        'decrypted_m1': decrypted_m[0],
        'decrypted_m2': decrypted_m[1],
        'decrypted_m3': decrypted_m[2]
    }
    return render(request, 'enc_dec.html', context)

def back_view(request):
    return render(request, 'index.html')