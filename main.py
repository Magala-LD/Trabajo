meme_dict = {
            "CRINGE": "Algo excepcionalmente raro o embarazoso",
            "LOL": "Una respuesta común a algo gracioso",
            "ROFL": "una respuesta a una broma",
            "SHEESH": "ligera desaprobacion", 
            "CREEPY": "atterador, siniestro o perturbador",
            "AGGRO": "ponerse enojado o agresivo",
            }

word = input("Escribe una palabra que no entiendas (¡con mayúsculas!): ")

if word in meme_dict.keys():
    print(meme_dict[word])
else:
    # ¿Qué hacer si no se encuentra la palabra?
    print("no se encuentra la palabra que busca, intenta de nuevo")
    print("Tip: intente escribir la palabra en mayuscula")
