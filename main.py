meme_dict = {
        "STALKEAR" : "investigar a vida de alguém online",
        "CRINGE" : "algo vergonhoso ou constrangedor",
        "VDD" : "abreviação da palavra verdade",
        "BISCOITAR" : "postar algo apenas para chamar a atenção",
        "HATER" : "pessoa que está constantemente criticando os outros",
        "VLW" : "abreviação da palavra valeu"
            }

word = input("Digite uma palavra moderna que você não entende (escreva todo a palavra em letras maiúsculas): ")

if word in meme_dict.keys():
    print(meme_dict[word])
else:
    print("Pergunte outra palavra pois nem eu sei essa.")
