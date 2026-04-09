import numpy as np
from PIL import Image
import cmath

def safe_exp(x):
    try:
        return cmath.exp(x)
    except OverflowError:
        return cmath.exp(700) if x.real > 0 else 0

def safe_cos(x):
    return cmath.cos(min(max(x.real, -100), 100) + 1j * min(max(x.imag, -100), 100))

def F(x):
    return abs(255 * safe_exp(-x/1000*x) * int(x.real) * safe_exp(x/1000*(x-1)))

def U_k(x, y):
    return safe_cos(17*x) * x + cmath.sin(17*x) * y + 2 * cmath.sin(8*x)

def V_k(x, y):
    return safe_cos(17*x) * y - cmath.sin(17*x) * x + 2 * cmath.sin(9*x)

def W_func(x, y):
    return sum(safe_exp(-safe_exp(-0.5*(safe_cos((11/10)**s*(safe_cos(2*x)+cmath.sin(2*x))+x*2*cmath.sin(2*x))**2 + 
                                   safe_cos((11/10)**s*(cmath.sin(2*x)-safe_cos(2*x))+x*2*safe_cos(2*x))**2) - 0.5)) 
               for s in range(1, 41))

def Q_k(x, y, k):
    U = U_k(x, y)
    V = V_k(x, y)
    return (2*U + 0.1*safe_cos(3*V + 2*U + safe_cos(3*U) + 2)**2 + 
            0.5*safe_exp(-safe_exp(100*safe_cos(U+cmath.pi/4))))

def P_k(x, y, k):
    U = U_k(x, y)
    V = V_k(x, y)
    return (4*V + 0.1*safe_cos(3*U + 2*V + safe_cos(4*V) + 2)**2 + 
            0.1*safe_cos(9*U - 2*V + safe_cos(6*V))**2 + 1)

def L_k(x, y, k):
    Q = Q_k(x, y, k)
    P = P_k(x, y, k)
    return safe_exp(-safe_exp(-k*(safe_cos(P-cmath.sin(Q/2+cmath.pi/4)**4))+10+9*cmath.sin(Q)/safe_cos(Q)**3+0.2))

def K_k(x, y, k):
    Q = Q_k(x, y, k)
    W = W_func(x, y)
    return safe_exp(-safe_exp(-0.5*(safe_cos(W+0.1*safe_cos(Q/2+cmath.pi/4)**30)**12-0.01-0.8*safe_cos(Q/2+cmath.pi/4)**14)-2/3))

def I_k(x, y, k):
    L = L_k(x, y, k)
    K = K_k(x, y, k)
    return 1 - (1 - L) * (1 - K)

def N_k(x, y, k):
    Q = Q_k(x, y, k)
    P = P_k(x, y, k)
    return safe_exp(-safe_exp(-k*(safe_cos(P-cmath.sin(Q/2+cmath.pi/4)**4))+10+9*cmath.sin(Q)/safe_cos(Q)**4+0.4))

def A_k(x, y, k):
    L = L_k(x, y, k)
    W = W_func(x, y)
    v = 0.5
    return (0.1*(4*v**2 - 16*v + 16 + (-1)**k*(11*v - 5*v**2 - 2) + (5*v - 3*v**2 + 2) * safe_cos((7 + v)*x) + 
                           0.05*(40 - x) * (6*L)) +
            0.1*(-9*v**2 + 13*v + 10 + safe_cos((4 + v)*x)) + 0.05*W)

def S_i(x, y, i):
    return sum(I_k(x,y,k) * A_k(x,y,k) * (3/5 + 2/5*I_k(x,y,k)) * 
               np.prod([1 - safe_exp(-1000*(1-j/k))*I_k(x,y,j) for j in range(k)]) *
               (1 - 0.7*safe_exp(-1000*(1-k/50))*N_k(x,y,k))
               for k in range(1, 51))

def generate_starry_sky(width, height):
    image = np.zeros((height, width, 3), dtype=np.uint8)
    for n in range(height):
        for m in range(width):
            x = (m - width/2) / (width/4)
            y = (height/2 - n) / (height/4)
            pixel = [int(abs(F(S_i(x, y, i)))) for i in range(3)]
            image[n, m] = np.clip(pixel, 0, 255)
    return image

# Generate and save the image
width, height = 200, 120  # Reduced size for faster computation
starry_sky = generate_starry_sky(width, height)
img = Image.fromarray(starry_sky)
img.save('starry_sky.png')
print("Image saved as starry_sky.png")