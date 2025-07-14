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
 stock={}
 if marca in productos:
  if stock["marcas"] == marca:
   return None
def busqueda_ram_precio(ram_max, ram_min, precio):
 stock={}
 while True:
  try:
   if precio <= stock:
    print("INGRESE SU PEDIDO: ", ram_max, ram_min)
  except:
   print("--> Debe ingresar valores enteros <--")

def eliminar_producto(modelo):
 modelo
 productos = int(input("Ingrese el producto que desea eliminar: "))
 if any(modelo["marca"] == stock for modelo in productos):
  print("--> Producto no encontrado <--")
  return False
 else:
   print("DESEA ELIMINAR OTRO PRODUCTO (S/N)")

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
....