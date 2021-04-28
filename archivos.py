"""
Modos de Apertura

	•     r -> Solo lectura
	•     r+ -> Lectura y escritura
	•     w -> Solo escritura. Sobre escribe el archivo si existe. Crea el archivo si no existe
	•     w+ -> Escritura y lectura. Sobre escribe el archivo si existe. Crea el archivo si no existe
	•     a -> Añadido (agregar contenido). Crea el archivo si éste no existe
    a+ -> Añadido (agregar contenido) y lectura. Crea el archivo si éste no existe.
"""


def read():
    numbers =[]
    #Con encoding="utf-8", nos vamos asegurar que todo lo que vamos a leer o a escribir, 
    #en posteriores archivos no tengan caracteres extraños, no tenga errores por ejemplo cuando vamos a leer letras
    #con tíldes o la ñ etc 
    with open("./archivos/numbers.txt", "r", encoding="utf-8") as f:
        for line in f: 
            numbers.append(int(line))
    print(numbers)

def write():
    names = ["Sara", "Víctor", "Adrian", "Alejandra"]
    with open("./archivos/names.txt", "a", encoding="utf-8") as f:
        for name in names:
            f.write(name)
            f.write("\n")
    
def run():
    read()

if __name__=='__main__':
    run()