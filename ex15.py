from sys import argv

#arguments do script usando argv (2)
script, filename = argv

#abre filename (o segundo argument especificado na command line) para uso
txt = open(filename)

#lê o nome da variável criada pelo segundo argument na command line
print(f"Here's your file {filename}:\n")
#lê o conteúdo da variável txt, que abriu a filename, através da função read
print(txt.read())
print(txt)

#fecha txt
txt.close()

#print simples
print("\nType the filename again:")

#pega novo valor através da variável de input, again uma file
file_again = input("> ")

#abre (open) para uso o valor conferido e especificado através do input
#(open cria um file object)
txt_again = open(file_again)

#lê o conteúdo do arquivo especificado
print(txt_again.read())

#fecha txt_again
print(txt_again.close())
