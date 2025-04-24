# etapa 1
print("Etapa 1")
objetos = ["livro", "relógio", "anel", "fone de ouvido", "cartão"]
print("lista de objetos criada!")
print(objetos)

# etapa 2
print("Etapa 2")
objetos.append("chave")
print("objeto adicionado!")
print(objetos)

# etapa 3
print("Etapa 3")
print(f'{objetos[1]}')
print("objeto acessado!")

# etapa 4
print("Etapa 4")
objetos = ["livro", "relógio", "anel", "fone de ouvido", "cartão", "chave"]
objetos.remove("chave")
print("objeto removido!")
print(objetos)

# etapa 5
print("Etapa 5")
len(objetos)
print('A lista tem:', len(objetos), 'itens')


# etapa 6
for objeto in objetos:
    print(objeto)

# etapa 7
print("Etapa 7")
if "cadeira" in objetos:
    objetos.remove("cadeira")
    print("objeto removido!")
    print(len(objetos))
else:
    objetos.append("cadeira")
    print("objeto adicionado!")
    print(objetos)

# etapa 8
print("Etapa 8")
objetos.sort()
print('lista em ordem alfabética:', objetos)

#etapa 9
print("Etapa 9")
ordemprimeiro = objetos[0]
print('primeiro valor:', ordemprimeiro)

ordemultimo = objetos[len(objetos)-1]
print('ultimo valor:', ordemultimo)


#etapa 10
print("Etapa 10")
objetos.clear()
print('lista limpa:')
print(objetos)

