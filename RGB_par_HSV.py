import colorsys

def cor_complementar(r, g, b):
    """
    Recebe uma cor RGB (0-255) e retorna
    sua cor complementar, girando o matiz
    (H) em 180 graus no circulo cromatico.
    """
    
    r_norm = r / 255.0
    g_norm = g / 255.0
    b_norm = b / 255.0

    h, s, v = colorsys.rgb_to_hsv(
        r_norm, g_norm, b_norm)


    h_complementar = (h + 0.5) % 1.0    


    r2, g2, b2 = colorsys.hsv_to_rgb(
        h_complementar, s, v)

    return (round(r2 * 255),
            round(g2 * 255),
            round(b2 * 255))


def cor_analoga(r, g, b):
    """
    Recebe uma cor RGB (0-255) e retorna
    sua cor complementar, girando o matiz
    (H) em 180 graus no circulo cromatico.
    """

    r_norm = r / 255.0
    g_norm = g / 255.0
    b_norm = b / 255.0

    h, s, v = colorsys.rgb_to_hsv(
        r_norm, g_norm, b_norm)

    # 3) soma 180 graus ao matiz
    # (equivale a somar 0.5)
    angulo = 3/36
    h_analog1 = (h + angulo) % 1.0    
    h_analog2 = (h - angulo) % 1.0    


    r1, g1, b1 = colorsys.hsv_to_rgb(
        h_analog1, s, v)

    r2, g2, b2 = colorsys.hsv_to_rgb(
        h_analog2, s, v)     



    rr1 = round(r1 * 255)
    gr1 = round(g1 * 255)
    br1 = round(b1 * 255)

    rr2 = round(r2 * 255)
    gr2 = round(g2 * 255)
    br2 = round(b2 * 255)


    return rr1, gr1, br1, rr2, gr2, br2


def cor_triadices(r, g, b):
    """
    Recebe uma cor RGB (0-255) e retorna
    sua cor complementar, girando o matiz
    (H) em 180 graus no circulo cromatico.
    """

    r_norm = r / 255.0
    g_norm = g / 255.0
    b_norm = b / 255.0


    h, s, v = colorsys.rgb_to_hsv(
        r_norm, g_norm, b_norm)

    
    angulo1 = 12/36
    angulo2 = 24/36
   
    h_analog2 = (h + angulo1) % 1.0    
    h_analog3 = (h + angulo2) % 1.0    


   
    r2, g2, b2 = colorsys.hsv_to_rgb(
        h_analog2, s, v)

    r3, g3, b3 = colorsys.hsv_to_rgb(
        h_analog3, s, v)          


    rr2 = round(r2 * 255)
    gr2 = round(g2 * 255)
    br2 = round(b2 * 255)

    rr3 = round(r3 * 255)
    gr3 = round(g3 * 255)
    br3 = round(b3 * 255)

    return rr2, gr2, br2, rr3, gr3, br3


def cor_split_complementar(r, g, b):
    """
    Recebe uma cor RGB (0-255) e retorna
    sua cor complementar, girando o matiz
    (H) em 180 graus no circulo cromatico.
    """

    r_norm = r / 255.0
    g_norm = g / 255.0
    b_norm = b / 255.0

    h, s, v = colorsys.rgb_to_hsv(
        r_norm, g_norm, b_norm)

    angulo1 = 15/36
    angulo2 = 21/36
    h_analog1 = (h + angulo1) % 1.0    
    h_analog2 = (h + angulo2) % 1.0    

    r1, g1, b1 = colorsys.hsv_to_rgb(
        h_analog1, s, v)

    r2, g2, b2 = colorsys.hsv_to_rgb(
        h_analog2, s, v)     


    rr1 = round(r1 * 255)
    gr1 = round(g1 * 255)
    br1 = round(b1 * 255)

    rr2 = round(r2 * 255)
    gr2 = round(g2 * 255)
    br2 = round(b2 * 255)


    return rr1, gr1, br1, rr2, gr2, br2


def cor_tetradica(r, g, b):
    """
    Recebe uma cor RGB (0-255) e retorna
    sua cor complementar, girando o matiz
    (H) em 180 graus no circulo cromatico.
    """

    r_norm = r / 255.0
    g_norm = g / 255.0
    b_norm = b / 255.0

    h, s, v = colorsys.rgb_to_hsv(
        r_norm, g_norm, b_norm)

    angulo1 = 6/36
    angulo2 = 18/36
    angulo3 = 24/36
    h_analog1 = (h + angulo1) % 1.0    
    h_analog2 = (h + angulo2) % 1.0  
    h_analog3 = (h + angulo3) % 1.0  


    r1, g1, b1 = colorsys.hsv_to_rgb(
        h_analog1, s, v)

    r2, g2, b2 = colorsys.hsv_to_rgb(
        h_analog2, s, v)
       
    r3, g3, b3 = colorsys.hsv_to_rgb(
        h_analog3, s, v)      


    rr1 = round(r1 * 255)
    gr1 = round(g1 * 255)
    br1 = round(b1 * 255)

    rr2 = round(r2 * 255)
    gr2 = round(g2 * 255)
    br2 = round(b2 * 255)

    rr3 = round(r2 * 255)
    gr3 = round(g2 * 255)
    br3 = round(b2 * 255)



    return rr1, gr1, br1, rr2, gr2, br2, rr3, gr3, br3


def cor_quadrada(r, g, b):
    """
    Recebe uma cor RGB (0-255) e retorna
    sua cor complementar, girando o matiz
    (H) em 180 graus no circulo cromatico.
    """

    r_norm = r / 255.0
    g_norm = g / 255.0
    b_norm = b / 255.0

    h, s, v = colorsys.rgb_to_hsv(
        r_norm, g_norm, b_norm)

    angulo1 = 9/36
    angulo2 = 18/36
    angulo3 = 27/36
    h_analog1 = (h + angulo1) % 1.0    
    h_analog2 = (h + angulo2) % 1.0  
    h_analog3 = (h + angulo3) % 1.0  


    r1, g1, b1 = colorsys.hsv_to_rgb(
        h_analog1, s, v)

    r2, g2, b2 = colorsys.hsv_to_rgb(
        h_analog2, s, v)
       
    r3, g3, b3 = colorsys.hsv_to_rgb(
        h_analog3, s, v)      


    rr1 = round(r1 * 255)
    gr1 = round(g1 * 255)
    br1 = round(b1 * 255)

    rr2 = round(r2 * 255)
    gr2 = round(g2 * 255)
    br2 = round(b2 * 255)

    rr3 = round(r2 * 255)
    gr3 = round(g2 * 255)
    br3 = round(b2 * 255)



    return rr1, gr1, br1, rr2, gr2, br2, rr3, gr3, br3

cor_original = (230, 57, 70)  # um vermelho
cor_comp = cor_complementar(*cor_original)
cor_analo = cor_analoga(*cor_origial)
cor_tri = cor_analoga(*cor_origial)
cor_split = cor_analoga(*cor_origial)
cor_tetra = cor_analoga(*cor_origial)
cor_quadra = cor_analoga(*cor_origial)


print(f"Original:     RGB{cor_original}")
print(f"Complementar: RGB{cor_comp}")
print(f"análoga: RGB{cor_analo}")
print(f"triádicas: RGB{cor_tri}")
print(f"split_complementar: RGB{cor_split}")
print(f"tetrádica: RGB{cor_tetra}")
print(f"quadrada: RGB{cor_quadra}")

qual a funcionalide deste codigo?
