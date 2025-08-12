import pandas as pd
import os

# Carpeta donde está este script
script_dir = os.path.dirname(os.path.abspath(__file__))

# Ruta al archivo CSV en la misma carpeta
file_name = os.path.join(script_dir, "grocery_list.csv")

# Si existe el archivo, lo carga; si no, crea lista vacía
if os.path.exists(file_name):
    grocery_list_df = pd.read_csv(file_name)
    grocery_list = grocery_list_df['item'].tolist()
    print("Lista inicial:", grocery_list)
else:
    print(f"Archivo '{file_name}' no encontrado. Creando lista vacía...")
    grocery_list = []

# Agregar "Kiwis" y "Raspberries"
grocery_list.extend(["Kiwis", "Raspberries"])
print("Lista después de agregar Kiwis y Raspberries:", grocery_list)

# Pedir un nuevo ítem al usuario
new_item = input("Ingrese un artículo para agregar: ")
grocery_list.append(new_item)
print("Lista actualizada:", grocery_list)

# Agregar "Cinnamon" y "Paprika"
grocery_list.extend(["Cinnamon", "Paprika"])
print("\nLista después de agregar Cinnamon y Paprika:")
print(grocery_list)

# Eliminar "Eggs" y "Apples" si están en la lista
for item in ["Eggs", "Apples"]:
    if item in grocery_list:
        grocery_list.remove(item)

print("\nLista después de eliminar Eggs y Apples:")
print(grocery_list)

# Guardar cambios en el CSV
pd.DataFrame({'item': grocery_list}).to_csv(file_name, index=False)

print(f"\nLista guardada en {file_name}")
