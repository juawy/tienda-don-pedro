from pathlib import Path

archivo = Path("datos/productos.txt")
lineas = archivo.read_text(encoding="utf-8").splitlines()

print("=== Inventario Tienda Don Pedro ===")
for linea in lineas[2:]:
    print("-", linea)

productos = [linea for linea in lineas[2:] if linea.strip()]
total = sum(int(linea.split("$")[-1].replace(".", "")) for linea in productos)
print(f"Total de productos: {len(productos)}")
print(f"Valor del inventario: ${total}")
