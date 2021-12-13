articulo=int(input("Digite el codigo de un articulo : "))
cantidadVendida = int(input("Digite cantidad vendida :"))
precioUnitario = int(input("Digite el precio unitario del articulo : "))
totalVenta =precioUnitario * cantidadVendida
impuesto=0.16
iva = float(totalVenta *0.16)
totalApagar = totalVenta + iva
print("total venta",totalVenta , "iva",iva , "total a pagar",totalApagar)