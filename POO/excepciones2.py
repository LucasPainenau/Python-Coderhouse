# def dividir(a,b):
#     return a/b


# try:
#     a = int(input("Ingrese A: "))
#     b = int(input("Ingrese B: "))

#     resultado = dividir(a,b)
#     print(resultado)
# except Exception as error:
#     print("[!] TIPO DE ERROR: ", type(error).__name__)
#     print(f"Se ha disparado un error: {error}")


def dividir(a,b):
    return a/b


try:
    a = int(input("Ingrese A: "))
    b = int(input("Ingrese B: "))

    resultado = dividir(a,b)
    print(resultado)








# except Exception as error:
#     tipo_error = type(error).__name__
#     print("[!] TIPO DE ERROR: ", tipo_error)

#     if tipo_error == "ZeroDivisionError":
#         print("No podes dividir por CERO!!!")
#     elif tipo_error == "ValueError":
#         print("No sabias que las operaciones matematicas requieren numeros?")
#     else:
#         print(f"Se ha disparado un error: {error}")



