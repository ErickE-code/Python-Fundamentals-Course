
emojis =  {"feliz": "😃"
           , "amo": "😍"
           , "risa": "🤣"
           , "sonrisa": "😊"
           , "llorar": "😭"
           , "beso": "😘"
           , "aplauso": "👏"
           , "reir": "😁"
           , "fuego": "🔥"
           , "roto": "💔"
           , "pensando": "🤔"
           , "maravillado": "🤩"
           , "aburrido": "🙄"
           , "güiño": "😉"
           , "ok": "👌"
           , "abrazo": "🤗"
           , "cool": "😎"
           , "enojado": "😠"
           , "python": "🐍"}

frase = input('Ingresa una frase por favor. ')

palabras = frase.split(" ")

respuesta = ""
for i in palabras:
    if i in emojis:
        respuesta = respuesta+" "+emojis[i]
    else:
        respuesta = respuesta+" "+i

print(respuesta)