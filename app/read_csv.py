import csv
#Para poder leer, hay que importar la libreria de csv
#Normalmente, cada dato en un csv estan separados por -> , <- pero puede ser ;
def read_csv(path):
    with open(path, 'r') as csvfile:
        #El reader es un iterable!
        reader = csv.reader(csvfile, delimiter=',')
        header = next(reader)
        data = []
        print(header)
        for row in reader:
            iterable = zip(header, row)
            #creando un dictonary comprehension
            country_dict = {key : value for key, value in iterable}
            data.append(country_dict)
        return data
#Cada columna viene como un array/lista -> []

if __name__ == '__main__':
    data = read_csv('./data.csv')
    print(data)