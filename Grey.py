from PIL import Image 
import numpy as np 
 
imagem = Image.open("images.jpeg") 
cinza = imagem.convert("L") 
cinza.save("image_cinza.jpeg") 
 
img = Image.open("image_cinza.jpeg") 
largura, altura = img.size 
pixels = img.load() 
imagem = [[pixels[x, y] for x in range(largura)] for y in range(altura)]  # matriz 2D de intensidades 
 
def salvarImagem(imagem, nome): 
    aplicada = np.array(imagem, dtype=np.uint8) 
    imagemAp = Image.fromarray(aplicada, mode="L") 
    imagemAp.save("./" + nome) 
 
def histograma(imagem): 
    altura = len(imagem) 
    largura = len(imagem[0]) 
    h = [0 for _ in range(256)] 
 
    for x in range(altura): 
        for y in range(largura): 
            i = imagem[x][y] 
            h[i] = h[i] + 1 
    return h 
 
def limiar(imagem, T): 
    altura = len(imagem) 
    largura = len(imagem[0]) 
    saida = [[0 for _ in range(largura)] for _ in range(altura)] 
 
    for x in range(altura): 
        for y in range(largura):  # corrigido 
            if imagem[x][y] > T: 
                saida[x][y] = 255 
            else: 
                saida[x][y] = 0 
    return saida 
 
def equalizar(imagem): 
    h = histograma(imagem) 
    altura = len(imagem) 
    largura = len(imagem[0]) 
    N = altura * largura 
    soma = 0 
 
    cdf = [0 for _ in range(256)] 
    for i in range(256):  # corrigido 
        soma = soma + h[i] 
        cdf[i] = soma 
 
    saida = [[0 for _ in range(largura)] for _ in range(altura)] 
    nova = [0 for _ in range(256)]  # corrigido 
 
    for i in range(256):  # corrigido 
        nova[i] = round(cdf[i] * 255 / N) 
 
    for x in range(altura): 
        for y in range(largura): 
            saida[x][y] = nova[imagem[x][y]] 
    return saida 
 
def aplicar_kernel(imagem, kernel): 
    altura, largura = len(imagem), len(imagem[0]) 
 
    k = len(kernel) 
    borda = k // 2 
    saida = [[0] * largura for _ in range(altura)] 
 
    for y in range(borda, altura - borda): 
        for x in range(borda, largura - borda): 
            soma = 0.0 
            for i in range(k): 
                iy = y + i - borda 
                row = imagem[iy] 
                for j in range(k): 
                    ix = x + j - borda 
                    soma += row[ix] * kernel[i][j] 
            saida[y][x] = max(0, min(255, round(soma))) 
 
    return saida 
 
kernel_media = [[1 / 9] * 3 for _ in range(3)] 
imagem_media = aplicar_kernel(imagem, kernel_media) 
salvarImagem(imagem_media, "media.png") 
 
