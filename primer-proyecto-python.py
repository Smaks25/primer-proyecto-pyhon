# archivo: conversor_divisas.py

def convertir_dolares_a_euros(dolares):
    tasa_cambio = 0.92  # ejemplo, puede variar
    euros = dolares * tasa_cambio
    return euros

if __name__ == "__main__":
    dolares = float(input("Ingresa cantidad en dólares: "))
    euros = convertir_dolares_a_euros(dolares)
    print(f"{dolares} USD son aproximadamente {euros:.2f} EUR")
