# 
# Capacidad es la maxima cantidad de vehículos simultáneos por intersección.

# REGLA: capacidad_total del grafo debe ser > N_VEHICULOS para evitar deadlock.
# Con N_VEHICULOS=10: capacidad_total=16 deja 6 plazas libres → congestión sin deadlock.
# Nodos con capacidad baja seran los cuellos de botella del Circuito Comercial.
nodes = [
    ("Av. Costanera",                  {"tiene_semaforo": True,  "zona": "comercial", "vehi_presentes": 0, "capacidad": 3}),
    ("Plaza Artigas",                  {"tiene_semaforo": False, "zona": "costanera", "vehi_presentes": 0, "capacidad": 4}),
    ("Mercado Municipal",              {"tiene_semaforo": True,  "zona": "mercado",   "vehi_presentes": 0, "capacidad": 2}),
    ("Mcal. Estigarribia y Pereira",   {"tiene_semaforo": False, "zona": "costanera", "vehi_presentes": 0, "capacidad": 3}),
    ("Mcal. Estigarribia y Caballero", {"tiene_semaforo": True,  "zona": "comercial", "vehi_presentes": 0, "capacidad": 4}),
]
# Total = 16. N_VEHICULOS = 10. Plazas libres = 6
# Mercado Municipal (cap=2) y Av. Costanera (cap=3) serán los nodos congestionados.

node_position = {
    'Av. Costanera'                     : ([-0.85263999,  0.5282904 ]),
    'Plaza Artigas'                     : ([ 0.37905282, -0.92551331]),
    'Mercado Municipal'                 : ([-0.7665546 , -0.92551331]),
    'Mcal. Estigarribia y Pereira'      : ([ 0.24014177,  0.97087115]),
    'Mcal. Estigarribia y Caballero'    : ([ 1.         , 0.07324743]),
}

connections = [
    ["Mcal. Estigarribia y Caballero", "Mcal. Estigarribia y Pereira",   {"vel_max": 20, "carriles": 2, "vehi_calle": 0, "weight": 30}],
    ["Plaza Artigas",                  "Mcal. Estigarribia y Caballero", {"vel_max": 20, "carriles": 2, "vehi_calle": 0, "weight": 20}],
    ["Av. Costanera",                  "Mercado Municipal",              {"vel_max": 50, "carriles": 2, "vehi_calle": 0, "weight": 30}],
    ["Mcal. Estigarribia y Pereira",   "Av. Costanera",                  {"vel_max": 20, "carriles": 2, "vehi_calle": 0, "weight": 40}],
    ["Mercado Municipal",              "Plaza Artigas",                  {"vel_max": 20, "carriles": 2, "vehi_calle": 0, "weight": 50}],
]