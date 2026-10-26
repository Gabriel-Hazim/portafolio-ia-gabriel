# dia0_prueba_entorno.py
# Autor: Gabriel Hazim
# Reto Dia 0: Calculo de precios multimoneda y margen comercial

producto = "Filtro de Aceite 20W50"
costo_usd = 6.50
margen_ganancia = 0.30  # 30% de margen
tasa_bcv = 881.07       # Tasa oficial de referencia

# 1. Calculamos el precio de venta en USD sumando el margen
precio_venta_usd = round(costo_usd * (1 + margen_ganancia), 2)

# 2. Convertimos el precio de venta a Bolivares
precio_venta_bs = round(precio_venta_usd * tasa_bcv, 2)

# 3. Imprimimos el reporte formal para el negocio
print("==========================================")
print("REPORTE DE PRECIO - ALMACEN / TIENDA")
print("==========================================")
print(f"Producto:         {producto}")
print(f"Costo Base:       ${costo_usd:.2f} USD")
print(f"Margen Aplicado:  {margen_ganancia * 100:.0f}%")
print(f"Precio Venta USD: ${precio_venta_usd:.2f} USD")
print(f"Precio Venta Bs:  {precio_venta_bs:,.2f} Bs (Tasa: {tasa_bcv:,.2f})")
print("==========================================")