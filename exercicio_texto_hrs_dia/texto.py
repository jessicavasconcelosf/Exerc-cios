texto = "Contrary to popular belief, Lorme Ipsum is not simply random text. It has roots in a piece of classical latin literature from 45 BC, making it over 2000 years old. Richard McClintock, a Latin professor at Hampden-Sydney College in Virginia, looked up one of the more obscure Latin words, consectetur"

num_palavras = texto.split()

qnt_palavra = len(num_palavras)

print ("O numero de palavras é: ", qnt_palavra)

print ("Palavras com mais de 4 letras: ")
for letra in num_palavras:
    if len(letra) > 4:
        print (letra)

print ("\nPalavras com mais de 2 vogais: ")

for palavra in num_palavras:
    vogal = sum(1 for letra in palavra if letra.lower() in 'aeiou')
    if vogal > 2:
        print(palavra)  

print ("A 14° palavra do texto é: ",num_palavras[13])
print ("A 22° palavra do texto é: ", num_palavras[21])
print ("A 29° palavra do texto é: ",num_palavras[28])
print ("A penultima palavra do texto é: ", num_palavras[-2])