productos = {'8475HD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i5', 'Nvidia GTX1050'],
 '2175HD': ['Acer', 14, '4GB', 'SSD', '512GB', 'Intel Core i5', 'Nvidia GTX1050'],
 'JjfFHD': ['Asus', 14, '16GB', 'SSD', '256GB', 'Intel Core i7', 'Nvidia RTX2080Ti'],
 'fgdxFHD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i3', 'integrada'],
 'GF75HD': ['Asus', 15.6, '8GB', 'DD', '1T', 'Intel Core i7', 'Nvidia GTX1050'],
 '123FHD': ['Acer', 14, '6GB', 'DD', '1T', 'AMD Ryzen 5', 'integrada'],
 '342FHD': ['Acer', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 7', 'Nvidia GTX1050'],
 'UWU131HD': ['Dell', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 3', 'Nvidia GTX1050'],
 }
stock = {'8475HD': [387990,10], '2175HD': [327990,4], 'JjfFHD': [424990,1],
 'fgdxFHD': [664990,21], '123FHD': [290890,32], '342FHD': [444990,7],
 'GF75HD': [749990,2], 'UWU131HD': [349990,1], 'FS1230HD': [249990,0],
 }
marcas_validas=["HP, Acer, Asus, Dell"]
rams=["4GB, 8GB, 16GB"]
ram_max=["16GB"]
ram_min=["4GB"]

def stock_marcas(marca):
 marca = input("ingrese la marca del producto: ").capitalize()
 if marca in marcas_validas:
  encontrados = False
  print(f/" Productos de la marca{marca}: /n")
  for codigo, datos in productos.items():
   if datos[0] == marca:
     precio,cantidad = stock.get(codigo,[0,0])
     print(F"{codigo}: {datos} - precio: {precio} - stock: {cantidad}")
     encontrados = True
     if not encontrados:
      print("Producto no encontrado o no existe: ")
     else:
      print("Marca invalida / intente otra vez: ")
      
def busqueda_ram_precio():
    while True:
        try:
            ram_min_str= input("Ingrese la RAM mínima (ej. 4GB, 8GB, 16GB) o 'cancelar' para salir: ").strip().upper()
            if ram_min_str.lower() == 'cancelar':
                return
            if ram_min_str not in rams_validas:
                print("--> RAM mínima no válida. Por favor, use 4GB, 6GB, 8GB, o 16GB. <--")
                continue
            ram_max_str = input("Ingrese la RAM máxima (ej. 4GB, 8GB, 16GB) o 'cancelar' para salir: ").strip().upper()
            if ram_max_str.lower() == 'cancelar':
                return
            if ram_max_str not in rams_validas:
                print("--> RAM máxima no válida. Por favor, use 4GB, 6GB, 8GB, o 16GB. <--")
                continue
            ram_min_val = int(ram_min_str.replace('GB', ''))
            ram_max_val = int(ram_max_str.replace('GB', ''))
            if ram_min_val > ram_max_val:
                print("--> La RAM mínima no puede ser mayor que la RAM máxima. <--")
                continue
            precio_max = int(input("Ingrese el precio máximo (solo números) o 'cancelar' para salir: ").strip())
            if str(precio_max).lower() == 'cancelar':
                return
            break
        except ValueError:
            print("--> Entrada inválida. Asegúrese de ingresar solo números para el precio y valores válidos para la RAM. <--")

    print(f"\n--- Productos con RAM entre {ram_min_str} y {ram_max_str} y precio hasta ${precio_max:,} ---")
    productos_encontrados = False
    for modelo, detalles in productos.items():
        ram_producto_str = detalles[2]
        ram_producto_val = int(ram_producto_str.replace('GB', ''))
        
        if ram_min_val <= ram_producto_val <= ram_max_val:
            if modelo in stock:
                precio_producto = stock[modelo][0]
                cantidad_producto = stock[modelo][1]
                if precio_producto <= precio_max:
                    productos_encontrados = True
                    print(f"  Modelo: {modelo}, Marca: {detalles[0]}, RAM: {detalles[2]}, Precio: ${precio_producto:,}, Stock: {cantidad_producto}")
            else:
                if precio_max >= 0:
                    print(f"  Modelo: {modelo}, Marca: {detalles[0]}, RAM: {detalles[2]}, Precio: No disponible en stock, Stock: 0")

    if not productos_encontrados:
        print(">>> No se encontraron productos con los criterios especificados <<<")



def eliminar_producto(modelo):
  while True:
        modelo_eliminar = input("Ingrese el modelo del producto a eliminar (ej. 8475HD) o 'cancelar' para salir: ").strip()
        if modelo_eliminar.lower() == 'cancelar':
            break
        
        if modelo_eliminar in productos:
            confirmacion = input(f"¿Está seguro de que desea eliminar el producto '{modelo_eliminar}'? (S/N): ").strip().upper()
            if confirmacion == 'S':
                del productos[modelo_eliminar]
                if modelo_eliminar in stock:
                    del stock[modelo_eliminar]
                print(f"--> Producto '{modelo_eliminar}' eliminado exitosamente. <--")
            else:
                print("Operación de eliminación fue cancelada.")
            break
        else:
            print("--> Producto no encontrado. Por favor, ingrese un modelo válido. <--")
            continue
def menu():
 while True:
  print("--> MENU PRINCIPAL <---")
  print("")
  print("1° STOCK MARCA: ")
  print("2° BUSQUEDA POR RAM Y PRECIOS: ")
  print("3° ELIMINAR PRODUCTO: ")
  print("4° SALIR")
  
  opc=input("INGRESE OPCION (1-4): ")
  
  if opc=="1":
   stock_marcas("")
  elif opc=="2":
    busqueda_ram_precio("")
  elif opc=="3":
   eliminar_producto("")
  elif opc=="4":
   print("PROGRAMA FINALIZADO")
  break
menu()