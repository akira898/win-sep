from pynput import keyboard
from sonidosSeleccion import sound
hystorial = []
times = 0
forbiddenWords = ["PORN", "MILK-CHAN", "FEMBOY","BOOPS","DICKS","COCKS"]
game=["dont","touch","keep","strong"]
def al_presionar(key):
    global times, hystorial,game
    
    try:
        # Extrae el caracter presionado (si es una letra/número normal)
        tecla = key.char
        
        if tecla:
            hystorial.append(tecla)
            hystorialVeredict = "".join(hystorial)
            # Diálogo por defecto
            # esto es para al final saltar  a una intraccion especial
            if hystorialVeredict.upper() in forbiddenWords and times < 4:
                print("don't!\n")
                print(game)
                hystorial.clear()
                times += 1
                sound(game)
            elif hystorialVeredict.upper() in forbiddenWords and times == 4:
                print("Dont give up soldier!")
                print("sir, I think we might have lost him")
                print("Dammit")
                hystorial.clear()
                times = 0
                
            print(hystorial)
            print(hystorialVeredict)

    except AttributeError:
        # pynput maneja las teclas especiales (como Backspace) a través de excepciones
        if key == keyboard.Key.backspace:
            if len(hystorial) >= 1:
                del hystorial[-1]
                print(hystorial)
                print("no word (character deleted)")

# Listener global de pynput en segundo plano
with keyboard.Listener(on_press=al_presionar) as listener:
    listener.join()