from datetime import datetime

hora_actual = datetime.now().hour

nombre = input("Cuál es tu nombre:")

if hora_actual >= 6 and hora_actual < 13:
    print(f"¡Buenos días {nombre}!")
elif hora_actual >= 13 and hora_actual < 21:
    print(f"¡Buenas tardes {nombre}")
elif hora_actual >= 21 and hora_actual <6:
    print(f"¡Buenas noches {nombre}!")