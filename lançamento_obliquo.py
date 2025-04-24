import numpy as np
import matplotlib.pyplot as plt

g = 9.81  


def calcular_trajetoria(velocidade, angulo):
    angulo_rad = np.radians(angulo)
    
    v_x = velocidade * np.cos(angulo_rad)
    v_y = velocidade * np.sin(angulo_rad)
    t_total = 2 * v_y / g
    alcance_max = v_x * t_total
    h_max = (v_y**2) / (2 * g)
    
    t = np.linspace(0, t_total, num=500)  
    x = v_x * t  
    y = v_y * t - 0.5 * g * t**2  

    plt.figure(figsize=(15, 5))
    plt.plot(x, y, label="Trajetória", color='b')
    x_vert = alcance_max / 2  
    ymin = 0  
    ymax = h_max  
    plt.plot([x_vert, x_vert], [ymin, ymax], color='r', linestyle='--', linewidth=2, alpha=0.5)
    plt.title("Trajetória de um projétil")
    plt.xlabel("Distância horizontal (m)")
    plt.ylabel("Altura (m)")
    plt.grid(True)
    plt.axhline(0, color='black',linewidth=0.5)
    plt.axvline(0, color='black',linewidth=0.5)
    plt.legend()
    plt.show()
    
    return h_max, alcance_max


def main():
    teste = 0
    while teste == 0:
        velocidade = float(input("Digite a velocidade inicial do projétil (m/s): "))
        angulo = float(input("Digite o ângulo de lançamento (em graus): "))
        if velocidade <= 0 or angulo<=0 or angulo==90 or angulo>=180:
            print("Valores inválidos, digite novamente: \n")
            teste = 0
        else:
            teste = 1
    
    h_max, alcance_max = calcular_trajetoria(velocidade, angulo)
    print(f"\nAltura máxima: {h_max:.2f} metros")
    print(f"Alcance máximo: {alcance_max:.2f} metros")
    print(f"Alcance na altura máxima {alcance_max/2:.2f} metros")

if __name__ == "__main__":
    main()
