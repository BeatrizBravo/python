import csv  # Importa el módulo CSV para leer los datos del archivo

#read_data = función que lee los datos del archivo
def read_data():
    data = []
    with open('sales.csv', 'r') as sales_csv: # Abre el archivo 'sales.csv' en modo lectura
        spreadsheet = csv.DictReader(sales_csv) #permite leer un archivo CSV como un diccionario.
                                                # El archivo CSV se debe pasar como argumento a la función y,
                                                #al hacerlo, se creará un **objeto DictReader** que se puede usar
                                                # para iterar sobre cada fila del archivo como un diccionario.
        for row in spreadsheet:  # Itera sobre los datos del objeto DictReader
            data.append(row)  # Itera sobre los datos del objeto DictReader
    return data


# run =  lee datos de algún lugar, lo procesa y luego imprime la suma de las ventas totales
def run():
    data = read_data()
    sales = []
    for row in data:
        sale = int(row['sales'])  # Obtiene el valor de ventas de la fila actual y lo convierte en un entero
        sales.append(sale)   # Agrega el valor de ventas a la lista sales
    total = sum(sales)
    print('Total sales: {}'.format(total))
run()
