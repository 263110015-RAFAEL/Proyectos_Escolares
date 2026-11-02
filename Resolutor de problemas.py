import matplotlib.pyplot as plt
import numpy as np

print("Resolutor de problemas")

print("Ingresa los datos de la primera ecuacion")
print("Escribe el primer valor de x")
a1 = float(input())
print("Escribe el primer valor de y")
b1 = float(input())
print("Escribe el primer resultado")
c1 = float(input())

print("Ingresa los datos de la segunda ecuacion")
print("Escribe el segundo valor de x")
a2 = float(input())
print("Escribe el segundo valor de y")
b2 = float(input())
print("Escribe el segundo resultado")
c2 = float(input())

if (a1 == 0 and b1 == 0) or (a2 == 0 and b2 == 0):
    print("Error: cada ecuacion debe tener al menos un número diferente de cero")

else:
    delta = a1*b2 - a2*b1
    delta_x = c1*b2 - c2*b1
    delta_y = a1*c2 - a2*c1

    if delta != 0:
        x = delta_x/delta
        y = delta_y/delta

        print("El valor de x es:", x)
        print("El valor de y es:", y)
        plt.scatter(x, y, color="black")
        plt.annotate(f"({x:.2f}, {y:.2f})", xy=(x, y), xytext=(x+1, y+1))

    elif delta_x != 0 or delta_y != 0:
        print("La ecuacion no tiene solucion")

    else:
        print("La ecuacion tiene infinitas soluciones")

valores_x = np.linspace(-10, 10, 100)

if b1 != 0:
    valores_y1 = (c1 - a1*valores_x)/b1
    plt.plot(valores_x, valores_y1, 'red', label=f"{a1}x + {b1}y = {c1}" if b1 > 0 else f"{a1}x - {abs(b1)}y = {c1}")
else:
    plt.axvline(x=c1/a1, color='red', label=f"{a1}x = {c1}")

if b2 != 0:
    valores_y2 = (c2 - a2*valores_x)/b2
    plt.plot(valores_x, valores_y2, 'blue', label=f"{a2}x + {b2}y = {c2}" if b2 > 0 else f"{a2}x - {abs(b2)}y = {c2}")
else:
    plt.axvline(x=c2/a2, color='blue', label=f"{a2}x = {c2}")

plt.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc=3, ncol=2, mode="expand", borderaxespad=0)

plt.title("Resolutor de problemas", pad=25)
plt.xlabel("Eje x")
plt.ylabel("Eje y")

plt.axhline(0, color="black")
plt.axvline(0, color="black")

plt.grid()
plt.show()

