DATA = [
    {
        'name': 'Facundo',
        'age': 72,
        'organization': 'Platzi',
        'position': 'Technical Coach',
        'language': 'python',
    },
    {
        'name': 'Luisana',
        'age': 33,
        'organization': 'Globant',
        'position': 'UX Designer',
        'language': 'javascript',
    }, 
    {
        'name': 'Héctor',
        'age': 19,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'ruby',
    },
    {
        'name': 'Gabriel',
        'age': 20,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'javascript',
    },
    {
        'name': 'Isabella',
        'age': 30,
        'organization': 'Platzi',
        'position': 'QA Manager',
        'language': 'java',
    },
    {
        'name': 'Karo',
        'age': 23,
        'organization': 'Everis',
        'position': 'Backend Developer',
        'language': 'python',
    },
    {
        'name': 'Ariel',
        'age': 32,
        'organization': 'Rappi',
        'position': 'Support',
        'language': '',
    },
    {
        'name': 'Juan',
        'age': 17,
        'organization': '',
        'position': 'Student',
        'language': 'go',
    },
    {
        'name': 'Pablo',
        'age': 32,
        'organization': 'Master',
        'position': 'Human Resources Manager',
        'language': 'python',
    },
    {
        'name': 'Lorena',
        'age': 56,
        'organization': 'Python Organization',
        'position': 'Language Maker',
        'language': 'python',
    },
]

def run():

    # Comprehensions solutions
    all_python_devs = [worker["name"] for worker in DATA if worker["language"] == "python"]
    all_Platzi_workers = [worker["name"] for worker in DATA if worker["organization"] == "Platzi"]
    #adults =  [worker["name"] for worker in DATA if worker["age"] > 18]

    #Lo que estamos haciendo, es transformar cada uno de los diccionarios que nosotros tenemo en "DATA"
    # en un diccionario nuevo que es la conbinacción de nuestro diccionario original con un nuevo diccionario
    #Que simplemente es una llaver "old" y un valor que es resultado de la expresión worker["age"] > 70
    # | solo funciona en python 3.9 es unir a un diccionario con otro nuevo 
    #old_people = list(map(lambda worker: worker | {"old": worker["age"] > 70}, DATA))

    #adults = list(filter(lambda worker:worker["age"] > 18, DATA))
    #dults= list(map(lambda worker: worker["name"], adults))

    #Obtiene información de las personas que manejan el lenguage "Python"
    all_python_devs = list(filter(lambda worker: worker["language"]=="python", DATA))
    #Obtiene solo los nombres de las personas que manejan este tipo de lenguaje, reuitliza lo anterior
    all_python_devs = list(map(lambda worker: worker['name'], all_python_devs))

    #Obtiene el nombre de las personas que trabajan en Platzi
    all_Platzi_workers = list(filter(lambda worker: worker["organization"]=="Platzi", DATA))
    #Obtiene el nombre de esas personas
    all_Platzi_workers = list(map(lambda worker: worker['name'], all_Platzi_workers))

    old_people = [worker["old"] for worker in DATA if worker["age"]>70]
    #Código para versiones mayores a 3.8 
    #old_people = [{**worker, **{"old": worker["age"] > 70}} for worker in DATA]
    #Codigo para versiones mayores a 3.9
    #old_people = [worker | {"old": worker["age"] > 70} for worker in DATA]

    for worker in old_people:
        print(worker)


if __name__ == '__main__':
    run()