def encriptacao(texto, chave):
    alfabeto=" !\"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~"
    encoded= ""
    for cont in texto:
        encodedLetterIndex=((ord(cont)- ord (' '))+chave)%96
        encoded+=alfabeto[encodedLetterIndex]
    return encoded
def descriptacao(cri, chave):
    alfabeto=" !\"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~"
    textodescriptado=""
    for cont in cri:
        decodedLetterIndex=((ord(cont)-ord(' '))+96-chave)%96
        textodescriptado+=alfabeto[decodedLetterIndex]
    return textodescriptado
print("Algoritmo de Criptografia e Descriptografia") 
chave=int(input("Digite a chave que vai ser usada para criptografar e descriptografar: "))
texto=input("Digite o texto que vai ser criptografado ou descriptografado: ")
ask=input("Digite C para criptografar ou digite D para descriptografar o texto: ")
if (ask=="C"):
    textocriptado=encriptacao(texto, chave)
    print("texto encriptado:",textocriptado)
elif (ask=="D"):
    textodescriptado=descriptacao(texto,chave)
    print("texto descriptado:",textodescriptado)
else:
    print("Não existe essa opção")
    
 


   
    
