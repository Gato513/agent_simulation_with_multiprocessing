# Circuito Comercial de Encarnación | bbox: (-27.36414, -55.85261, -27.35517, -55.84462)

#* Capacidad: es la maxima cantidad de vehículos simultáneos por intersección.

# REGLA: capacidad_total del grafo debe ser > N_VEHICULOS para evitar deadlock.
# Con N_VEHICULOS=10: capacidad_total=16 deja 6 plazas libres → congestión sin deadlock.
# Nodos con capacidad baja seran los cuellos de botella del Circuito Comercial.

# Posiciones → coordenadas geográficas normalizadas a [-1, 1].
# weight     → distancia real en metros (Haversine).
#
# REGLA: capacidad_total > N_VEHICULOS para evitar deadlock.
# capacidad_total = 55

nodes = [
    ("Ab. Mercedes Sandoval y Av. Moisés Bertoni",               {"semaforo": True , "zona": "comercial",   "vh_pr": 0, "capacidad": 3},),
    ("Av. Moisés Bertoni y Av. Perimetral",                      {"semaforo": True , "zona": "comercial",   "vh_pr": 0, "capacidad": 3},),
    ("Av. Moisés Bertoni y Juana de Lara",                       {"semaforo": True , "zona": "comercial",   "vh_pr": 0, "capacidad": 3},),
    ("Av. Moisés Bertoni y Peat. La Revendedora",                {"semaforo": True , "zona": "comercial",   "vh_pr": 0, "capacidad": 3},),
    ("Av. Moisés Bertoni y Prof. Alberto Delvalle",              {"semaforo": True , "zona": "comercial",   "vh_pr": 0, "capacidad": 3},),
    ("Av. Moisés Bertoni y Sr. Graciela Estigarribia",           {"semaforo": True , "zona": "comercial",   "vh_pr": 0, "capacidad": 3},),
    ("Av. Perimetral y Don Carlos González Arias",               {"semaforo": True , "zona": "comercial",   "vh_pr": 0, "capacidad": 3},),
    ("Ab. Serafina Dávalos y Av. Padre Juan Von Winckel",        {"semaforo": True , "zona": "secundaria",  "vh_pr": 0, "capacidad": 2},),
    ("Av. Padre Juan Von Winckel y Juana de Lara",               {"semaforo": True , "zona": "secundaria",  "vh_pr": 0, "capacidad": 2},),
    ("Av. Padre Juan Von Winckel y Prof. Clementina I. Barboza", {"semaforo": True , "zona": "secundaria",  "vh_pr": 0, "capacidad": 2},),
    ("Ab. Serafina Dávalos y Juan Brítez",                       {"semaforo": False, "zona": "peatonal",    "vh_pr": 0, "capacidad": 1},),
    ("Juan Brítez y Prof. Clementina I. Barboza",                {"semaforo": False, "zona": "peatonal",    "vh_pr": 0, "capacidad": 1},),
    ("Juana de Lara y Juan Brítez",                              {"semaforo": False, "zona": "peatonal",    "vh_pr": 0, "capacidad": 1},),
    ("Ab. Mercedes Sandoval y Ab. Nelson González Maya",         {"semaforo": False, "zona": "residencial", "vh_pr": 0, "capacidad": 1},),
    ("Ab. Mercedes Sandoval y Ab. Serafina Dávalos",             {"semaforo": False, "zona": "residencial", "vh_pr": 0, "capacidad": 1},),
    ("Ab. Mercedes Sandoval y Don Carlos González Arias",        {"semaforo": False, "zona": "residencial", "vh_pr": 0, "capacidad": 1},),
    ("Ab. Mercedes Sandoval y Juana de Lara",                    {"semaforo": False, "zona": "residencial", "vh_pr": 0, "capacidad": 1},),
    ("Ab. Mercedes Sandoval y Prof. Clementina I. Barboza",      {"semaforo": False, "zona": "residencial", "vh_pr": 0, "capacidad": 1},),
    ("Ab. Mercedes Sandoval y San José",                         {"semaforo": False, "zona": "residencial", "vh_pr": 0, "capacidad": 1},),
    ("Ab. Serafina Dávalos y C.M. Pérez Lizzandro",              {"semaforo": False, "zona": "residencial", "vh_pr": 0, "capacidad": 1},),
    ("Ab. Serafina Dávalos y C.N. Pérez Lizzardo",               {"semaforo": False, "zona": "residencial", "vh_pr": 0, "capacidad": 1},),
    ("Ab. Serafina Dávalos y Juana de Lara",                     {"semaforo": False, "zona": "residencial", "vh_pr": 0, "capacidad": 1},),
    ("Ab. Serafina Dávalos y L. Scosceria",                      {"semaforo": False, "zona": "residencial", "vh_pr": 0, "capacidad": 1},),
    ("Ab. Serafina Dávalos y Peat. La Revendedora",              {"semaforo": False, "zona": "residencial", "vh_pr": 0, "capacidad": 1},),
    ("Ab. Serafina Dávalos y Sr. Graciela Estigarribia",         {"semaforo": False, "zona": "residencial", "vh_pr": 0, "capacidad": 1},),
    ("C.M. Pérez Lizzandro y C.N. Pérez Lizzardo",               {"semaforo": False, "zona": "residencial", "vh_pr": 0, "capacidad": 1},),
    ("C.M. Pérez Lizzandro y Juana de Lara",                     {"semaforo": False, "zona": "residencial", "vh_pr": 0, "capacidad": 1},),
    ("C.N. Pérez Lizzardo y Juana de Lara",                      {"semaforo": False, "zona": "residencial", "vh_pr": 0, "capacidad": 1},),
    ("D. Moreno Ocampo y Tte. Arzamendia Samaniego",             {"semaforo": False, "zona": "residencial", "vh_pr": 0, "capacidad": 1},),
    ("Juana de Lara y L. Scosceria",                             {"semaforo": False, "zona": "residencial", "vh_pr": 0, "capacidad": 1},),
    ("Juana de Lara y Peat. La Revendedora",                     {"semaforo": False, "zona": "residencial", "vh_pr": 0, "capacidad": 1},),
    ("Juana de Lara y Prof. Clementina I. Barboza",              {"semaforo": False, "zona": "residencial", "vh_pr": 0, "capacidad": 1},),
    ("Juana de Lara y Sr. Graciela Estigarribia",                {"semaforo": False, "zona": "residencial", "vh_pr": 0, "capacidad": 1},),
    ("L. Scosceria y Prof. Clementina I. Barboza",               {"semaforo": False, "zona": "residencial", "vh_pr": 0, "capacidad": 1},),
    ("Peat. La Revendedora y Prof. Clementina I. Barboza",       {"semaforo": False, "zona": "residencial", "vh_pr": 0, "capacidad": 1},),
    ("Prof. Alberto Delvalle y Prof. Clementina I. Barboza",     {"semaforo": False, "zona": "residencial", "vh_pr": 0, "capacidad": 1},),
    ("Prof. Clementina I. Barboza y Sr. Graciela Estigarribia",  {"semaforo": False, "zona": "residencial", "vh_pr": 0, "capacidad": 1},),
    ("Próceres de Mayo y Tte. Arzamendia Samaniego",             {"semaforo": False, "zona": "residencial", "vh_pr": 0, "capacidad": 1},),
]

node_position = {
    'Ab. Mercedes Sandoval y Av. Moisés Bertoni'               : (  0.04271852,   0.42329095),
    'Av. Moisés Bertoni y Av. Perimetral'                      : (  0.45781627,   0.86896639),
    'Av. Moisés Bertoni y Juana de Lara'                       : (  0.57616526,   0.87213899),
    'Av. Moisés Bertoni y Peat. La Revendedora'                : (  0.10271775,   0.45033363),
    'Av. Moisés Bertoni y Prof. Alberto Delvalle'              : ( -0.08532107,   0.26798439),
    'Av. Moisés Bertoni y Sr. Graciela Estigarribia'           : (  0.16977874,   0.51512023),
    'Av. Perimetral y Don Carlos González Arias'               : (  0.32395201,   1.00000000),
    'Ab. Serafina Dávalos y Av. Padre Juan Von Winckel'        : (  0.16629940,  -0.13687524),
    'Av. Padre Juan Von Winckel y Juana de Lara'               : (  0.30508627,  -0.23786982),
    'Av. Padre Juan Von Winckel y Prof. Clementina I. Barboza' : (  0.00503859,  -0.04776533),
    'Ab. Serafina Dávalos y Juan Brítez'                       : ( -0.28890092,  -0.61616518),
    'Juan Brítez y Prof. Clementina I. Barboza'                : ( -0.43967217,  -0.51373536),
    'Juana de Lara y Juan Brítez'                              : ( -0.14374815,  -0.71501951),
    'Ab. Mercedes Sandoval y Ab. Nelson González Maya'         : ( -0.29477713,   0.69203072),
    'Ab. Mercedes Sandoval y Ab. Serafina Dávalos'             : (  0.41624464,   0.12672794),
    'Ab. Mercedes Sandoval y Don Carlos González Arias'        : ( -0.12954730,   0.55711948),
    'Ab. Mercedes Sandoval y Juana de Lara'                    : (  0.55134599,   0.01546015),
    'Ab. Mercedes Sandoval y Prof. Clementina I. Barboza'      : (  0.27825672,   0.24096689),
    'Ab. Mercedes Sandoval y San José'                         : ( -0.79111094,   0.84622938),
    'Ab. Serafina Dávalos y C.M. Pérez Lizzandro'              : ( -0.45152769,  -0.78743548),
    'Ab. Serafina Dávalos y C.N. Pérez Lizzardo'               : ( -0.51523821,  -0.85745940),
    'Ab. Serafina Dávalos y Juana de Lara'                     : (  1.00000000,   0.71247639),
    'Ab. Serafina Dávalos y L. Scosceria'                      : ( -0.12782052,  -0.44816820),
    'Ab. Serafina Dávalos y Peat. La Revendedora'              : (  0.46072860,   0.17038902),
    'Ab. Serafina Dávalos y Sr. Graciela Estigarribia'         : (  0.52304738,   0.23447060),
    'C.M. Pérez Lizzandro y C.N. Pérez Lizzardo'               : ( -0.60930916,  -0.68631499),
    'C.M. Pérez Lizzandro y Juana de Lara'                     : ( -0.31106558,  -0.89208108),
    'C.N. Pérez Lizzardo y Juana de Lara'                      : ( -0.40987874,  -1.00000000),
    'D. Moreno Ocampo y Tte. Arzamendia Samaniego'             : ( -1.00000000,  -0.34463049),
    'Juana de Lara y L. Scosceria'                             : (  0.01547660,  -0.54649377),
    'Juana de Lara y Peat. La Revendedora'                     : (  0.59253102,   0.06063200),
    'Juana de Lara y Prof. Clementina I. Barboza'              : (  0.82190951,   0.76608334),
    'Juana de Lara y Sr. Graciela Estigarribia'                : (  0.65557145,   0.12813798),
    'L. Scosceria y Prof. Clementina I. Barboza'               : ( -0.27256092,  -0.34374921),
    'Peat. La Revendedora y Prof. Clementina I. Barboza'       : (  0.32119431,   0.28425028),
    'Prof. Alberto Delvalle y Prof. Clementina I. Barboza'     : (  0.14823263,   0.10487221),
    'Prof. Clementina I. Barboza y Sr. Graciela Estigarribia'  : (  0.38547184,   0.34611608),
    'Próceres de Mayo y Tte. Arzamendia Samaniego'             : ( -0.74827644,  -0.04557472),
}

connections = [
    [
        "Ab. Mercedes Sandoval y Ab. Nelson González Maya", "Ab. Mercedes Sandoval y Don Carlos González Arias", 
        {"vel_max": 30, "carriles": 1, "vehi_calle": 0, "weight": 87}
    ],

    [
        "Ab. Mercedes Sandoval y Ab. Serafina Dávalos", "Ab. Mercedes Sandoval y Juana de Lara", 
        {"vel_max": 30, "carriles": 1, "vehi_calle": 0, "weight": 71}
    ],

    [
        "Ab. Mercedes Sandoval y Ab. Serafina Dávalos", "Ab. Serafina Dávalos y Peat. La Revendedora", 
        {"vel_max": 30, "carriles": 1, "vehi_calle": 0, "weight": 26}
    ],

    [
        "Ab. Mercedes Sandoval y Av. Moisés Bertoni", "Ab. Mercedes Sandoval y Prof. Clementina I. Barboza", 
        {"vel_max": 30, "carriles": 1, "vehi_calle": 0, "weight": 121}
    ],

    [
        "Ab. Mercedes Sandoval y Av. Moisés Bertoni", "Av. Moisés Bertoni y Peat. La Revendedora", 
        {"vel_max": 60, "carriles": 2, "vehi_calle": 0, "weight": 26}
    ],

    [
        "Ab. Mercedes Sandoval y Don Carlos González Arias", "Ab. Mercedes Sandoval y Av. Moisés Bertoni", 
        {"vel_max": 30, "carriles": 1, "vehi_calle": 0, "weight": 89}
    ],

    [
        "Ab. Mercedes Sandoval y Don Carlos González Arias", "Av. Perimetral y Don Carlos González Arias", 
        {"vel_max": 30, "carriles": 1, "vehi_calle": 0, "weight": 262}
    ],

    [
        "Ab. Mercedes Sandoval y Juana de Lara", "Juana de Lara y Peat. La Revendedora", 
        {"vel_max": 30, "carriles": 1, "vehi_calle": 0, "weight": 25}
    ],

    [
        "Ab. Mercedes Sandoval y Prof. Clementina I. Barboza", "Ab. Mercedes Sandoval y Ab. Serafina Dávalos", 
        {"vel_max": 30, "carriles": 1, "vehi_calle": 0, "weight": 73}
    ],

    [
        "Ab. Mercedes Sandoval y Prof. Clementina I. Barboza", "Prof. Alberto Delvalle y Prof. Clementina I. Barboza", 
        {"vel_max": 30, "carriles": 1, "vehi_calle": 0, "weight": 78}
    ],

    [
        "Ab. Mercedes Sandoval y San José", "Ab. Mercedes Sandoval y Ab. Nelson González Maya", 
        {"vel_max": 30, "carriles": 1, "vehi_calle": 0, "weight": 202}
    ],

    [
        "Ab. Serafina Dávalos y Av. Padre Juan Von Winckel", "Ab. Mercedes Sandoval y Ab. Serafina Dávalos", 
        {"vel_max": 30, "carriles": 1, "vehi_calle": 0, "weight": 151}
    ],

    [
        "Ab. Serafina Dávalos y Av. Padre Juan Von Winckel", "Av. Padre Juan Von Winckel y Juana de Lara", 
        {"vel_max": 50, "carriles": 1, "vehi_calle": 0, "weight": 69}
    ],

    [
        "Ab. Serafina Dávalos y Av. Padre Juan Von Winckel", "Av. Padre Juan Von Winckel y Prof. Clementina I. Barboza", 
        {"vel_max": 50, "carriles": 1, "vehi_calle": 0, "weight": 73}
    ],

    [
        "Ab. Serafina Dávalos y C.M. Pérez Lizzandro", "Ab. Serafina Dávalos y Juan Brítez", 
        {"vel_max": 30, "carriles": 1, "vehi_calle": 0, "weight": 98}
    ],

    [
        "Ab. Serafina Dávalos y C.M. Pérez Lizzandro", "C.M. Pérez Lizzandro y Juana de Lara", 
        {"vel_max": 30, "carriles": 1, "vehi_calle": 0, "weight": 71}
    ],

    [
        "Ab. Serafina Dávalos y C.N. Pérez Lizzardo", "Ab. Serafina Dávalos y C.M. Pérez Lizzandro", 
        {"vel_max": 30, "carriles": 1, "vehi_calle": 0, "weight": 39}
    ],

    [
        "Ab. Serafina Dávalos y C.N. Pérez Lizzardo", "C.M. Pérez Lizzandro y C.N. Pérez Lizzardo", 
        {"vel_max": 30, "carriles": 1, "vehi_calle": 0, "weight": 84}
    ],

    [
        "Ab. Serafina Dávalos y Juan Brítez", "Ab. Serafina Dávalos y L. Scosceria", 
        {"vel_max": 30, "carriles": 1, "vehi_calle": 0, "weight": 97}
    ],

    [
        "Ab. Serafina Dávalos y Juan Brítez", "Juana de Lara y Juan Brítez", 
        {"vel_max": 10, "carriles": 1, "vehi_calle": 0, "weight": 71}
    ],

    [
        "Ab. Serafina Dávalos y L. Scosceria", "Ab. Serafina Dávalos y Av. Padre Juan Von Winckel", 
        {"vel_max": 30, "carriles": 1, "vehi_calle": 0, "weight": 178}
    ],

    [
        "Ab. Serafina Dávalos y L. Scosceria", "Juana de Lara y L. Scosceria", 
        {"vel_max": 30, "carriles": 1, "vehi_calle": 0, "weight": 70}
    ],

    [
        "Ab. Serafina Dávalos y Peat. La Revendedora", "Ab. Serafina Dávalos y Sr. Graciela Estigarribia", 
        {"vel_max": 30, "carriles": 1, "vehi_calle": 0, "weight": 37}
    ],

    [
        "Ab. Serafina Dávalos y Peat. La Revendedora", "Juana de Lara y Peat. La Revendedora", 
        {"vel_max": 20, "carriles": 1, "vehi_calle": 0, "weight": 70}
    ],

    [
        "Ab. Serafina Dávalos y Sr. Graciela Estigarribia", "Ab. Serafina Dávalos y Juana de Lara", 
        {"vel_max": 30, "carriles": 1, "vehi_calle": 0, "weight": 279}
    ],

    [
        "Ab. Serafina Dávalos y Sr. Graciela Estigarribia", "Juana de Lara y Sr. Graciela Estigarribia", 
        {"vel_max": 20, "carriles": 1, "vehi_calle": 0, "weight": 69}
    ],

    [
        "Av. Moisés Bertoni y Juana de Lara", "Av. Moisés Bertoni y Av. Perimetral", 
        {"vel_max": 60, "carriles": 1, "vehi_calle": 0, "weight": 45}
    ],

    [
        "Av. Moisés Bertoni y Peat. La Revendedora", "Av. Moisés Bertoni y Sr. Graciela Estigarribia", 
        {"vel_max": 60, "carriles": 2, "vehi_calle": 0, "weight": 38}
    ],

    [
        "Av. Moisés Bertoni y Peat. La Revendedora", "Peat. La Revendedora y Prof. Clementina I. Barboza", 
        {"vel_max": 20, "carriles": 1, "vehi_calle": 0, "weight": 111}
    ],

    [
        "Av. Moisés Bertoni y Prof. Alberto Delvalle", "Ab. Mercedes Sandoval y Av. Moisés Bertoni", 
        {"vel_max": 60, "carriles": 2, "vehi_calle": 0, "weight": 84}
    ],

    [
        "Av. Moisés Bertoni y Prof. Alberto Delvalle", "Prof. Alberto Delvalle y Prof. Clementina I. Barboza", 
        {"vel_max": 30, "carriles": 1, "vehi_calle": 0, "weight": 115}
    ],

    [
        "Av. Moisés Bertoni y Sr. Graciela Estigarribia", "Prof. Clementina I. Barboza y Sr. Graciela Estigarribia", 
        {"vel_max": 20, "carriles": 1, "vehi_calle": 0, "weight": 111}
    ],

    [
        "Av. Padre Juan Von Winckel y Juana de Lara", "Ab. Mercedes Sandoval y Juana de Lara", 
        {"vel_max": 30, "carriles": 1, "vehi_calle": 0, "weight": 146}
    ],

    [
        "Av. Padre Juan Von Winckel y Juana de Lara", "Ab. Serafina Dávalos y Av. Padre Juan Von Winckel", 
        {"vel_max": 50, "carriles": 1, "vehi_calle": 0, "weight": 69}
    ],

    [
        "Av. Padre Juan Von Winckel y Prof. Clementina I. Barboza", "Ab. Serafina Dávalos y Av. Padre Juan Von Winckel", 
        {"vel_max": 50, "carriles": 1, "vehi_calle": 0, "weight": 73}
    ],

    [
        "Av. Padre Juan Von Winckel y Prof. Clementina I. Barboza", "L. Scosceria y Prof. Clementina I. Barboza", 
        {"vel_max": 30, "carriles": 1, "vehi_calle": 0, "weight": 169}
    ],

    [
        "Av. Perimetral y Don Carlos González Arias", "Av. Moisés Bertoni y Av. Perimetral", 
        {"vel_max": 60, "carriles": 2, "vehi_calle": 0, "weight": 77}
    ],

    [
        "C.M. Pérez Lizzandro y C.N. Pérez Lizzardo", "Ab. Serafina Dávalos y C.M. Pérez Lizzandro", 
        {"vel_max": 30, "carriles": 1, "vehi_calle": 0, "weight": 75}
    ],

    [
        "C.M. Pérez Lizzandro y Juana de Lara", "C.N. Pérez Lizzardo y Juana de Lara", 
        {"vel_max": 30, "carriles": 1, "vehi_calle": 0, "weight": 61}
    ],

    [
        "C.M. Pérez Lizzandro y Juana de Lara", "Juana de Lara y Juan Brítez", 
        {"vel_max": 30, "carriles": 1, "vehi_calle": 0, "weight": 101}
    ],

    [
        "C.N. Pérez Lizzardo y Juana de Lara", "Ab. Serafina Dávalos y C.N. Pérez Lizzardo", 
        {"vel_max": 30, "carriles": 1, "vehi_calle": 0, "weight": 75}
    ],

    [
        "D. Moreno Ocampo y Tte. Arzamendia Samaniego", "Próceres de Mayo y Tte. Arzamendia Samaniego", 
        {"vel_max": 30, "carriles": 2, "vehi_calle": 0, "weight": 164}
    ],

    [
        "Juan Brítez y Prof. Clementina I. Barboza", "Ab. Serafina Dávalos y Juan Brítez", 
        {"vel_max": 10, "carriles": 1, "vehi_calle": 0, "weight": 73}
    ],

    [
        "Juan Brítez y Prof. Clementina I. Barboza", "C.M. Pérez Lizzandro y C.N. Pérez Lizzardo", 
        {"vel_max": 30, "carriles": 1, "vehi_calle": 0, "weight": 100}
    ],

    [
        "Juana de Lara y Juan Brítez", "Juana de Lara y L. Scosceria", 
        {"vel_max": 30, "carriles": 1, "vehi_calle": 0, "weight": 96}
    ],

    [
        "Juana de Lara y L. Scosceria", "Av. Padre Juan Von Winckel y Juana de Lara", 
        {"vel_max": 30, "carriles": 1, "vehi_calle": 0, "weight": 176}
    ],

    [
        "Juana de Lara y Peat. La Revendedora", "Juana de Lara y Sr. Graciela Estigarribia", 
        {"vel_max": 30, "carriles": 1, "vehi_calle": 0, "weight": 38}
    ],

    [
        "Juana de Lara y Prof. Clementina I. Barboza", "Ab. Serafina Dávalos y Juana de Lara", 
        {"vel_max": 30, "carriles": 1, "vehi_calle": 0, "weight": 72}
    ],

    [
        "Juana de Lara y Prof. Clementina I. Barboza", "Prof. Clementina I. Barboza y Sr. Graciela Estigarribia", 
        {"vel_max": 30, "carriles": 1, "vehi_calle": 0, "weight": 250}
    ],

    [
        "L. Scosceria y Prof. Clementina I. Barboza", "Ab. Serafina Dávalos y L. Scosceria", 
        {"vel_max": 30, "carriles": 1, "vehi_calle": 0, "weight": 72}
    ],

    [
        "L. Scosceria y Prof. Clementina I. Barboza", "Juan Brítez y Prof. Clementina I. Barboza", 
        {"vel_max": 30, "carriles": 1, "vehi_calle": 0, "weight": 99}
    ],

    [
        "Peat. La Revendedora y Prof. Clementina I. Barboza", "Ab. Mercedes Sandoval y Prof. Clementina I. Barboza", 
        {"vel_max": 30, "carriles": 1, "vehi_calle": 0, "weight": 25}
    ],

    [
        "Peat. La Revendedora y Prof. Clementina I. Barboza", "Ab. Serafina Dávalos y Peat. La Revendedora", 
        {"vel_max": 20, "carriles": 1, "vehi_calle": 0, "weight": 73}
    ],

    [
        "Prof. Alberto Delvalle y Prof. Clementina I. Barboza", "Av. Padre Juan Von Winckel y Prof. Clementina I. Barboza", 
        {"vel_max": 30, "carriles": 1, "vehi_calle": 0, "weight": 87}
    ],

    [
        "Prof. Clementina I. Barboza y Sr. Graciela Estigarribia", "Ab. Serafina Dávalos y Sr. Graciela Estigarribia", 
        {"vel_max": 20, "carriles": 1, "vehi_calle": 0, "weight": 72}
    ],

    [
        "Prof. Clementina I. Barboza y Sr. Graciela Estigarribia", "Peat. La Revendedora y Prof. Clementina I. Barboza", 
        {"vel_max": 30, "carriles": 1, "vehi_calle": 0, "weight": 37}
    ],

]