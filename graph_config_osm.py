# graph_config.py — Circuito Comercial de Encarnación
# Fuente: resultados_final.json (Overpass GeoJSON)
# Criterio de nodos: equivalente a osmnx simplify=True
#   - Intersecciones (deg >= 3)
#   - Extremos de way (dead-ends y cambios de atributo)
#   - 2 rotondas como nodo único en su centroide real
# Posiciones: lon/lat normalizadas a [-1, 1]
# weight: distancia Haversine en metros
#
# REGLA: capacidad_total > N_VEHICULOS para evitar deadlock.

nodes = [
    (
        "Ab. Mercedes Sandoval y Av. Moisés Bertoni",
        {
            "pos": (  0.11638295,   0.39406618),
            "semaforo": True , 
            "zona": "comercial",   
            "vp": 0, 
            "capacidad": 4
        },
    ),
    (
        "Ab. Nelson González Maya y Av. San Roque",
        {
            "pos": ( -0.36329346,   0.40141725),
            "semaforo": True ,
            "zona": "comercial",
            "vp": 0, 
            "capacidad": 4
        },
    ),
    (
        "Av. Moisés Bertoni",
        {
            "pos": (  0.42970867,   0.76057114), 
            "semaforo": True , 
            "zona": "comercial",
            "vp": 0,
            "capacidad": 4
        },
    ),
    (
        "Av. Moisés Bertoni (2)",
        {
            "pos": (  0.34954588,   0.63786967), 
            "semaforo": True ,
            "zona": "comercial",
            "vp": 0,
            "capacidad": 4
        },
    ),
    (
        "Av. Moisés Bertoni (3)",
        {
            "pos": (  0.27208298,   0.54397932), 
            "semaforo": True , 
            "zona": "comercial",   
            "vp": 0, 
            "capacidad": 4
        },
    ),
    (
        "Av. Moisés Bertoni (4)",
        {
            "pos": (  0.23172366,   0.51598381), 
            "semaforo": True , 
            "zona": "comercial",   
            "vp": 0, 
            "capacidad": 4
        },
    ),
    (
        "Av. Moisés Bertoni (5)",
        {
            "pos": (  0.32425431,   0.59797898), 
            "semaforo": True , 
            "zona": "comercial",   
            "vp": 0, 
            "capacidad": 4
        },
    ),
    (
        "Av. Moisés Bertoni (6)",
        {
            "pos": (  0.48172118,   0.72671807), 
            "semaforo": True , 
            "zona": "comercial",   
            "vp": 0, 
            "capacidad": 4
        },
    ),
    (
        "Av. Moisés Bertoni (7)",
        {
            "pos": (  0.38603405,   0.66610880), 
            "semaforo": True , 
            "zona": "comercial",   
            "vp": 0, 
            "capacidad": 4
        },
    ),
    (
        "Av. Moisés Bertoni y Peat. La Revendedora",
        {
            "pos": (  0.15547174,   0.42335395), 
            "semaforo": True , 
            "zona": "comercial",   
            "vp": 0, 
            "capacidad": 4
        },
    ),
    (
        "Av. Moisés Bertoni y Prof. Alberto Delvalle",
        {
            "pos": (  0.01063080,   0.26993475), 
            "semaforo": True , 
            "zona": "comercial",   
            "vp": 0, 
            "capacidad": 4
        },
    ),
    (
        "Av. Moisés Bertoni y Sor Graciela Estigarribia",
        {
            "pos": (  0.20712690,   0.47786205), 
            "semaforo": True , 
            "zona": "comercial",   
            "vp": 0, 
            "capacidad": 4
        },
    ),
    (
        "Av. Perimetral",
        {
            "pos": (  0.19827287,   1.00000000), 
            "semaforo": True , 
            "zona": "comercial",   
            "vp": 0, 
            "capacidad": 4
        },
    ),
    (
        "Av. Perimetral (2)",
        {
            "pos": (  0.42899399,   0.77556987), 
            "semaforo": True , 
            "zona": "comercial",   
            "vp": 0, 
            "capacidad": 4
        },
    ),
    (
        "Av. Perimetral y Don Carlos González Arias",
        {
            "pos": (  0.33363442,   0.89357893), 
            "semaforo": True , 
            "zona": "comercial",   
            "vp": 0, 
            "capacidad": 4
        },
    ),
    (
        "Av. San Roque (2)",
        {
            "pos": ( -0.18640131,   0.21589272), 
            "semaforo": True , 
            "zona": "comercial",   
            "vp": 0, 
            "capacidad": 4
        },
    ),
    (
        "Av. San Roque (3)",
        {
            "pos": ( -0.45777954,  -0.54749597), 
            "semaforo": True , 
            "zona": "comercial",   
            "vp": 0, 
            "capacidad": 4
        },
    ),
    (
        "Av. San Roque (4)",
        {
            "pos": ( -0.30273463,  -0.29777138), 
            "semaforo": True , 
            "zona": "comercial",   
            "vp": 0, 
            "capacidad": 4
        },
    ),
    (
        "Av. San Roque (5)",
        {
            "pos": ( -0.59299221,  -0.78222185), 
            "semaforo": True , 
            "zona": "comercial",   
            "vp": 0, 
            "capacidad": 4
        },
    ),
    (
        "Av. San Roque (6)",
        {
            "pos": ( -0.52982282,  -0.67231591), 
            "semaforo": True , 
            "zona": "comercial",   
            "vp": 0, 
            "capacidad": 4
        },
    ),
    (
        "Av. San Roque y C.M. Pérez Lizzandro",
        {
            "pos": ( -0.42443794,  -0.49664223), 
            "semaforo": True , 
            "zona": "comercial",   
            "vp": 0, 
            "capacidad": 4
        },
    ),
    (
        "Av. San Roque y D. Moreno Ocampo",
        {
            "pos": ( -0.37767631,  -0.41617236), 
            "semaforo": True , 
            "zona": "comercial",   
            "vp": 0, 
            "capacidad": 4
        },
    ),
    (
        "Av. San Roque y Don Carlos González Arias",
        {
            "pos": ( -0.23856271,   0.28761334), 
            "semaforo": True , 
            "zona": "comercial",   
            "vp": 0, 
            "capacidad": 4
        },
    ),
    (
        "Av. San Roque y Próceres de Mayo",
        {
            "pos": ( -0.21413470,  -0.13295483), 
            "semaforo": True , 
            "zona": "comercial",   
            "vp": 0, 
            "capacidad": 4
        },
    ),
    (
        "Av. San Roque y San José",
        {
            "pos": ( -0.57321951,   0.56844759), 
            "semaforo": True , 
            "zona": "comercial",   
            "vp": 0, 
            "capacidad": 4
        },
    ),
    (
        "Av. San Roque y Vía 1",
        {
            "pos": ( -0.57625689,  -0.75161003), 
            "semaforo": True , 
            "zona": "comercial",   
            "vp": 0, 
            "capacidad": 4
        },
    ),
    (
        "Rot. Av. Moisés Bertoni",
        {
            "pos": (  0.47471033,   0.76828561), 
            "semaforo": True , 
            "zona": "comercial",   
            "vp": 0, 
            "capacidad": 4
        },
    ),
    (
        "Rot. San Roque González",
        {
            "pos": ( -0.10615614,   0.16302326), 
            "semaforo": True , 
            "zona": "comercial",   
            "vp": 0, 
            "capacidad": 4
        },
    ),
    (
        "Ab. Serafina Dávalos y Av. Padre Juan Von Winckel",
        {
            "pos": (  0.19716115,  -0.07907169), 
            "semaforo": True , 
            "zona": "secundaria",  
            "vp": 0, 
            "capacidad": 3
        },
    ),
    (
        "Av. Padre Juan Von Winckel",
        {
            "pos": (  0.80740483,  -0.68528091), 
            "semaforo": True , 
            "zona": "secundaria",  
            "vp": 0, 
            "capacidad": 3
        },
    ),
    (
        "Av. Padre Juan Von Winckel (2)",
        {
            "pos": (  0.61385677,  -0.48197187), 
            "semaforo": True , 
            "zona": "secundaria",  
            "vp": 0, 
            "capacidad": 3
        },
    ),
    (
        "Av. Padre Juan Von Winckel (3)",
        {
            "pos": (  0.65302496,  -0.93449708), 
            "semaforo": True , 
            "zona": "secundaria",  
            "vp": 0, 
            "capacidad": 3
        },
    ),
    (
        "Av. Padre Juan Von Winckel (4)",
        {
            "pos": (  0.73392228,  -0.80520719), 
            "semaforo": True , 
            "zona": "secundaria",  
            "vp": 0, 
            "capacidad": 3
        },
    ),
    (
        "Av. Padre Juan Von Winckel (5)",
        {
            "pos": (  0.37924463,  -0.21042708), 
            "semaforo": True , 
            "zona": "secundaria",  
            "vp": 0, 
            "capacidad": 3
        },
    ),
    (
        "Av. Padre Juan Von Winckel (6)",
        {
            "pos": (  0.32147501,  -0.18627659), 
            "semaforo": True , 
            "zona": "secundaria",  
            "vp": 0, 
            "capacidad": 3
        },
    ),
    (
        "Av. Padre Juan Von Winckel (7)",
        {
            "pos": (  0.71083428,  -1.00000000), 
            "semaforo": True , 
            "zona": "secundaria",  
            "vp": 0, 
            "capacidad": 3
        },
    ),
    (
        "Av. Padre Juan Von Winckel y Juana de Lara",
        {
            "pos": (  0.30631793,  -0.16195661), 
            "semaforo": True , 
            "zona": "secundaria",  
            "vp": 0, 
            "capacidad": 3
        },
    ),
    (
        "Av. Padre Juan Von Winckel y Prof. Clementina Irrazabal Barboza",
        {
            "pos": (  0.08702169,   0.01238243), 
            "semaforo": True , 
            "zona": "secundaria",  
            "vp": 0, 
            "capacidad": 3
        },
    ),
    (
        "Ab. Serafina Dávalos (5)",
        {
            "pos": (  0.08672391,  -0.20608423), 
            "semaforo": False, 
            "zona": "peatonal",    
            "vp": 0, 
            "capacidad": 1
        },
    ),
    (
        "Ab. Serafina Dávalos y Juan Brítez",
        {
            "pos": ( -0.14618095,  -0.47394289), 
            "semaforo": False, 
            "zona": "peatonal",    
            "vp": 0, 
            "capacidad": 1
        },
    ),
    (
        "Juan Brítez y Prof. Clementina Irrazabal Barboza",
        {
            "pos": ( -0.26231575,  -0.38776375), 
            "semaforo": False, 
            "zona": "peatonal",    
            "vp": 0, 
            "capacidad": 1
        },
    ),
    (
        "Juana de Lara (7)",
        {
            "pos": (  0.19666485,  -0.28368359), 
            "semaforo": False, 
            "zona": "peatonal",    
            "vp": 0, 
            "capacidad": 1
        },
    ),
    (
        "Juana de Lara y Juan Brítez",
        {
            "pos": ( -0.03437391,  -0.55711380), 
            "semaforo": False, 
            "zona": "peatonal",    
            "vp": 0, 
            "capacidad": 1
        },
    ),
    (
        "Prof. Clementina Irrazabal Barboza",
        {
            "pos": ( -0.02810065,  -0.11899415), 
            "semaforo": False, 
            "zona": "peatonal",    
            "vp": 0, 
            "capacidad": 1
        },
    ),
    (
        "Ab. Mercedes Sandoval",
        {
            "pos": ( -0.37120453,   0.72652741), 
            "semaforo": False, 
            "zona": "residencial", 
            "vp": 0, 
            "capacidad": 2
        },
    ),
    (
        "Ab. Mercedes Sandoval (2)",
        {
            "pos": (  0.20502258,   0.32054487), 
            "semaforo": False, 
            "zona": "residencial", 
            "vp": 0, 
            "capacidad": 2
        },
    ),
    (
        "Ab. Mercedes Sandoval (3)",
        {
            "pos": ( -1.00000000,   0.84980086), 
            "semaforo": False, 
            "zona": "residencial", 
            "vp": 0, 
            "capacidad": 2
        },
    ),
    (
        "Ab. Mercedes Sandoval y Ab. Nelson González Maya",
        {
            "pos": ( -0.15070723,   0.62670536), 
            "semaforo": False, 
            "zona": "residencial", 
            "vp": 0, 
            "capacidad": 2
        },
    ),
    (
        "Ab. Mercedes Sandoval y Ab. Serafina Dávalos",
        {
            "pos": (  0.39697255,   0.15108889), 
            "semaforo": False, 
            "zona": "residencial", 
            "vp": 0, 
            "capacidad": 2
        },
    ),
    (
        "Ab. Mercedes Sandoval y Don Carlos González Arias",
        {
            "pos": ( -0.02343541,   0.51319803), 
            "semaforo": False, 
            "zona": "residencial", 
            "vp": 0, 
            "capacidad": 2
        },
    ),
    (
        "Ab. Mercedes Sandoval y Juana de Lara",
        {
            "pos": (  0.50103727,   0.05747394), 
            "semaforo": False, 
            "zona": "residencial", 
            "vp": 0, 
            "capacidad": 2
        },
    ),
    (
        "Ab. Mercedes Sandoval y Prof. Clementina Irrazabal Barboza",
        {
            "pos": (  0.29068440,   0.24720363), 
            "semaforo": False, 
            "zona": "residencial", 
            "vp": 0, 
            "capacidad": 2
        },
    ),
    (
        "Ab. Mercedes Sandoval y San José",
        {
            "pos": ( -0.53301901,   0.75644013), 
            "semaforo": False, 
            "zona": "residencial", 
            "vp": 0, 
            "capacidad": 2
        },
    ),
    (
        "Ab. Nelson González Maya",
        {
            "pos": ( -0.25471239,   0.51639692), 
            "semaforo": False, 
            "zona": "residencial", 
            "vp": 0, 
            "capacidad": 2
        },
    ),
    (
        "Ab. Serafina Dávalos",
        {
            "pos": ( -0.45601271,  -0.81683756), 
            "semaforo": False, 
            "zona": "residencial", 
            "vp": 0, 
            "capacidad": 2
        },
    ),
    (
        "Ab. Serafina Dávalos (2)",
        {
            "pos": (  0.74865254,   0.53993306), 
            "semaforo": False, 
            "zona": "residencial", 
            "vp": 0, 
            "capacidad": 2
        },
    ),
    (
        "Ab. Serafina Dávalos (3)",
        {
            "pos": (  0.62342548,   0.40358868), 
            "semaforo": False, 
            "zona": "residencial", 
            "vp": 0, 
            "capacidad": 2
        },
    ),
    (
        "Ab. Serafina Dávalos (4)",
        {
            "pos": (  0.79550350,   0.58889077), 
            "semaforo": False, 
            "zona": "residencial", 
            "vp": 0, 
            "capacidad": 2
        },
    ),
    (
        "Ab. Serafina Dávalos (6)",
        {
            "pos": (  0.50973249,   0.27754004), 
            "semaforo": False, 
            "zona": "residencial", 
            "vp": 0, 
            "capacidad": 2
        },
    ),
    (
        "Ab. Serafina Dávalos (7)",
        {
            "pos": (  0.36824656,   0.11710872), 
            "semaforo": False, 
            "zona": "residencial", 
            "vp": 0, 
            "capacidad": 2
        },
    ),
    (
        "Ab. Serafina Dávalos (8)",
        {
            "pos": (  0.69814879,   0.48747987), 
            "semaforo": False, 
            "zona": "residencial", 
            "vp": 0, 
            "capacidad": 2
        },
    ),
    (
        "Ab. Serafina Dávalos (9)",
        {
            "pos": (  0.65161546,   0.43521735), 
            "semaforo": False, 
            "zona": "residencial", 
            "vp": 0, 
            "capacidad": 2
        },
    ),
    (
        "Ab. Serafina Dávalos y C.M. Pérez Lizzandro",
        {
            "pos": ( -0.27144771,  -0.61804084), 
            "semaforo": False, 
            "zona": "residencial", 
            "vp": 0, 
            "capacidad": 2
        },
    ),
    (
        "Ab. Serafina Dávalos y C.N. Pérez Lizzardo",
        {
            "pos": ( -0.32052211,  -0.67695534), 
            "semaforo": False, 
            "zona": "residencial", 
            "vp": 0, 
            "capacidad": 2
        },
    ),
    (
        "Ab. Serafina Dávalos y Juana de Lara",
        {
            "pos": (  0.84662266,   0.64390730), 
            "semaforo": False, 
            "zona": "residencial", 
            "vp": 0, 
            "capacidad": 2
        },
    ),
    (
        "Ab. Serafina Dávalos y L. Scosceria",
        {
            "pos": ( -0.02210532,  -0.33259893), 
            "semaforo": False, 
            "zona": "residencial", 
            "vp": 0, 
            "capacidad": 2
        },
    ),
    (
        "Ab. Serafina Dávalos y Peat. La Revendedora",
        {
            "pos": (  0.43123728,   0.18782307), 
            "semaforo": False, 
            "zona": "residencial", 
            "vp": 0, 
            "capacidad": 2
        },
    ),
    (
        "Ab. Serafina Dávalos y Sor Graciela Estigarribia",
        {
            "pos": (  0.47923966,   0.24173799), 
            "semaforo": False, 
            "zona": "residencial", 
            "vp": 0, 
            "capacidad": 2
        },
    ),
    (
        "C.M. Pérez Lizzandro y C.N. Pérez Lizzardo",
        {
            "pos": ( -0.39298228,  -0.53296331), 
            "semaforo": False, 
            "zona": "residencial", 
            "vp": 0, 
            "capacidad": 2
        },
    ),
    (
        "C.M. Pérez Lizzandro y Juana de Lara",
        {
            "pos": ( -0.16325376,  -0.70608423), 
            "semaforo": False, 
            "zona": "residencial", 
            "vp": 0, 
            "capacidad": 2
        },
    ),
    (
        "C.N. Pérez Lizzardo",
        {
            "pos": ( -0.28431188,  -0.75167359), 
            "semaforo": False, 
            "zona": "residencial", 
            "vp": 0, 
            "capacidad": 2
        },
    ),
    (
        "C.N. Pérez Lizzardo y Juana de Lara",
        {
            "pos": ( -0.23936672,  -0.79688162), 
            "semaforo": False, 
            "zona": "residencial", 
            "vp": 0, 
            "capacidad": 2
        },
    ),
    (
        "D. Moreno Ocampo",
        {
            "pos": ( -0.40491340,  -0.40121600), 
            "semaforo": False, 
            "zona": "residencial", 
            "vp": 0, 
            "capacidad": 2
        },
    ),
    (
        "D. Moreno Ocampo y Tte. Arzamendia Samaniego",
        {
            "pos": ( -0.69392029,  -0.24548767), 
            "semaforo": False, 
            "zona": "residencial", 
            "vp": 0, 
            "capacidad": 2
        },
    ),
    (
        "Don Carlos González Arias",
        {
            "pos": ( -0.20243188,   0.30903101), 
            "semaforo": False, 
            "zona": "residencial", 
            "vp": 0, 
            "capacidad": 2
        },
    ),
    (
        "Juana de Lara",
        {
            "pos": (  0.95263289,   0.58675112), 
            "semaforo": False, 
            "zona": "residencial", 
            "vp": 0, 
            "capacidad": 2
        },
    ),
    (
        "Juana de Lara (10)",
        {
            "pos": (  0.84130230,   0.45557580), 
            "semaforo": False, 
            "zona": "residencial", 
            "vp": 0, 
            "capacidad": 2
        },
    ),
    (
        "Juana de Lara (11)",
        {
            "pos": (  0.57492680,   0.73012880), 
            "semaforo": False, 
            "zona": "residencial", 
            "vp": 0, 
            "capacidad": 2
        },
    ),
    (
        "Juana de Lara (2)",
        {
            "pos": (  0.52015485,   0.77823913), 
            "semaforo": False, 
            "zona": "residencial", 
            "vp": 0, 
            "capacidad": 2
        },
    ),
    (
        "Juana de Lara (3)",
        {
            "pos": (  0.88704154,   0.50955428), 
            "semaforo": False, 
            "zona": "residencial", 
            "vp": 0, 
            "capacidad": 2
        },
    ),
    (
        "Juana de Lara (4)",
        {
            "pos": (  0.61167304,   0.18782307), 
            "semaforo": False, 
            "zona": "residencial", 
            "vp": 0, 
            "capacidad": 2
        },
    ),
    (
        "Juana de Lara (5)",
        {
            "pos": (  0.79731004,   0.40363105), 
            "semaforo": False, 
            "zona": "residencial", 
            "vp": 0, 
            "capacidad": 2
        },
    ),
    (
        "Juana de Lara (6)",
        {
            "pos": (  0.47495161,   0.02669265), 
            "semaforo": False, 
            "zona": "residencial", 
            "vp": 0, 
            "capacidad": 2
        },
    ),
    (
        "Juana de Lara (8)",
        {
            "pos": (  0.75115390,   0.34916532), 
            "semaforo": False, 
            "zona": "residencial", 
            "vp": 0, 
            "capacidad": 2
        },
    ),
    (
        "Juana de Lara (9)",
        {
            "pos": (  0.72336096,   0.31668926), 
            "semaforo": False, 
            "zona": "residencial", 
            "vp": 0, 
            "capacidad": 2
        },
    ),
    (
        "Juana de Lara y L. Scosceria",
        {
            "pos": (  0.08827237,  -0.41532497), 
            "semaforo": False, 
            "zona": "residencial", 
            "vp": 0, 
            "capacidad": 2
        },
    ),
    (
        "Juana de Lara y Peat. La Revendedora",
        {
            "pos": (  0.53276093,   0.09547920), 
            "semaforo": False, 
            "zona": "residencial", 
            "vp": 0, 
            "capacidad": 2
        },
    ),
    (
        "Juana de Lara y Prof. Clementina Irrazabal Barboza",
        {
            "pos": (  0.70944464,   0.68900941), 
            "semaforo": False, 
            "zona": "residencial", 
            "vp": 0, 
            "capacidad": 2
        },
    ),
    (
        "Juana de Lara y Sor Graciela Estigarribia",
        {
            "pos": (  0.58131917,   0.15227523), 
            "semaforo": False, 
            "zona": "residencial", 
            "vp": 0, 
            "capacidad": 2
        },
    ),
    (
        "L. Scosceria y Prof. Clementina Irrazabal Barboza",
        {
            "pos": ( -0.13359472,  -0.24474621), 
            "semaforo": False, 
            "zona": "residencial", 
            "vp": 0, 
            "capacidad": 2
        },
    ),
    (
        "Peat. La Revendedora",
        {
            "pos": (  0.23692491,   0.35395305), 
            "semaforo": False, 
            "zona": "residencial", 
            "vp": 0, 
            "capacidad": 2
        },
    ),
    (
        "Peat. La Revendedora y Prof. Clementina Irrazabal Barboza",
        {
            "pos": (  0.32375800,   0.28362003), 
            "semaforo": False, 
            "zona": "residencial", 
            "vp": 0, 
            "capacidad": 2
        },
    ),
    (
        "Prof. Alberto Delvalle",
        {
            "pos": (  0.05897067,   0.23438692), 
            "semaforo": False, 
            "zona": "residencial", 
            "vp": 0, 
            "capacidad": 2
        },
    ),
    (
        "Prof. Alberto Delvalle (2)",
        {
            "pos": (  0.09377140,   0.20881705), 
            "semaforo": False, 
            "zona": "residencial", 
            "vp": 0, 
            "capacidad": 2
        },
    ),
    (
        "Prof. Alberto Delvalle (3)",
        {
            "pos": (  0.03546578,   0.25167359), 
            "semaforo": False, 
            "zona": "residencial", 
            "vp": 0, 
            "capacidad": 2
        },
    ),
    (
        "Prof. Alberto Delvalle y Prof. Clementina Irrazabal Barboza",
        {
            "pos": (  0.19053055,   0.13270062), 
            "semaforo": False, 
            "zona": "residencial", 
            "vp": 0, 
            "capacidad": 2
        },
    ),
    (
        "Prof. Clementina Irrazabal Barboza (2)",
        {
            "pos": (  0.55662316,   0.52218032), 
            "semaforo": False, 
            "zona": "residencial", 
            "vp": 0, 
            "capacidad": 2
        },
    ),
    (
        "Prof. Clementina Irrazabal Barboza (3)",
        {
            "pos": (  0.44088540,   0.40295314), 
            "semaforo": False, 
            "zona": "residencial", 
            "vp": 0, 
            "capacidad": 2
        },
    ),
    (
        "Prof. Clementina Irrazabal Barboza (4)",
        {
            "pos": (  0.40630304,   0.36910008), 
            "semaforo": False, 
            "zona": "residencial", 
            "vp": 0, 
            "capacidad": 2
        },
    ),
    (
        "Prof. Clementina Irrazabal Barboza (5)",
        {
            "pos": (  0.64957070,   0.62073129), 
            "semaforo": False, 
            "zona": "residencial", 
            "vp": 0, 
            "capacidad": 2
        },
    ),
    (
        "Prof. Clementina Irrazabal Barboza (6)",
        {
            "pos": (  0.52388704,   0.48826371), 
            "semaforo": False, 
            "zona": "residencial", 
            "vp": 0, 
            "capacidad": 2
        },
    ),
    (
        "Prof. Clementina Irrazabal Barboza (7)",
        {
            "pos": (  0.49543898,   0.45926193), 
            "semaforo": False, 
            "zona": "residencial", 
            "vp": 0, 
            "capacidad": 2
        },
    ),
    (
        "Prof. Clementina Irrazabal Barboza (8)",
        {
            "pos": (  0.59996030,   0.57033302), 
            "semaforo": False, 
            "zona": "residencial", 
            "vp": 0, 
            "capacidad": 2
        },
    ),
    (
        "Prof. Clementina Irrazabal Barboza (9)",
        {
            "pos": (  0.26114447,   0.21309635), 
            "semaforo": False, 
            "zona": "residencial", 
            "vp": 0, 
            "capacidad": 2
        },
    ),
    (
        "Prof. Clementina Irrazabal Barboza y Sor Graciela Estigarribia",
        {
            "pos": (  0.37326914,   0.33567071), 
            "semaforo": False, 
            "zona": "residencial", 
            "vp": 0, 
            "capacidad": 2
        },
    ),
    (
        "Próceres de Mayo",
        {
            "pos": ( -0.32058167,  -0.07776883), 
            "semaforo": False, 
            "zona": "residencial", 
            "vp": 0, 
            "capacidad": 2
        },
    ),
    (
        "Próceres de Mayo y Tte. Arzamendia Samaniego",
        {
            "pos": ( -0.50752229,   0.01355111), 
            "semaforo": False, 
            "zona": "residencial", 
            "vp": 0, 
            "capacidad": 2
        },
    ),
    (
        "Sor Graciela Estigarribia",
        {
            "pos": (  0.28818304,   0.40744428), 
            "semaforo": False, 
            "zona": "residencial", 
            "vp": 0, 
            "capacidad": 2
        },
    ),
    (
        "Tte. Arzamendia Samaniego",
        {
            "pos": ( -0.91650206,  -0.37001102), 
            "semaforo": False, 
            "zona": "residencial", 
            "vp": 0, 
            "capacidad": 2
        },
    ),
    (
        "Tte. Arzamendia Samaniego (2)",
        {
            "pos": ( -0.59529505,  -0.12992543), 
            "semaforo": False, 
            "zona": "residencial", 
            "vp": 0, 
            "capacidad": 2
        },
    ),
    (
        "Vía 1",
        {
            "pos": ( -0.69922081,  -0.79965681), 
            "semaforo": False, 
            "zona": "residencial", 
            "vp": 0, 
            "capacidad": 2
        },
    ),
    (
        "nodo_(-55.84467, ",
        {
            "pos": (  1.00000000,   0.45269469), 
            "semaforo": False, 
            "zona": "residencial", 
            "vp": 0, 
            "capacidad": 2
        },
    ),
    (
        "nodo_(-55.84506, ",
        {
            "pos": (  0.92168346,  -0.77948903), 
            "semaforo": False, 
            "zona": "residencial", 
            "vp": 0, 
            "capacidad": 2
        },
    ),
    (
        "nodo_(-55.84541, ",
        {
            "pos": (  0.85263785,  -0.88742479), 
            "semaforo": False, 
            "zona": "residencial", 
            "vp": 0, 
            "capacidad": 2
        },
    ),
    (
        "nodo_(-55.84673, ",
        {
            "pos": (  0.59092759,  -0.86075333), 
            "semaforo": False, 
            "zona": "residencial", 
            "vp": 0, 
            "capacidad": 2
        },
    ),
    (
        "nodo_(-55.84688, ",
        {
            "pos": (  0.56128840,   0.69794933), 
            "semaforo": False, 
            "zona": "residencial", 
            "vp": 0, 
            "capacidad": 2
        },
    ),
    (
        "nodo_(-55.84716, ",
        {
            "pos": (  0.50566281,   0.73743751), 
            "semaforo": False, 
            "zona": "residencial", 
            "vp": 0, 
            "capacidad": 2
        },
    ),
    (
        "nodo_(-55.84717, ",
        {
            "pos": (  0.50310189,   0.65331328), 
            "semaforo": False, 
            "zona": "residencial", 
            "vp": 0, 
            "capacidad": 2
        },
    ),
    (
        "nodo_(-55.84725, ",
        {
            "pos": (  0.48785548,   0.61643081), 
            "semaforo": False, 
            "zona": "residencial", 
            "vp": 0, 
            "capacidad": 2
        },
    ),
    (
        "nodo_(-55.84735, ",
        {
            "pos": (  0.46826145,   0.59535209), 
            "semaforo": False, 
            "zona": "residencial", 
            "vp": 0, 
            "capacidad": 2
        },
    ),
    (
        "nodo_(-55.84738, ",
        {
            "pos": (  0.46226612,  -0.71379544), 
            "semaforo": False, 
            "zona": "residencial", 
            "vp": 0, 
            "capacidad": 2
        },
    ),
    (
        "nodo_(-55.8475, -",
        {
            "pos": (  0.43766936,   0.56342683), 
            "semaforo": False, 
            "zona": "residencial", 
            "vp": 0, 
            "capacidad": 2
        },
    ),
    (
        "nodo_(-55.84807, ",
        {
            "pos": (  0.32558440,   0.75618592), 
            "semaforo": False, 
            "zona": "residencial", 
            "vp": 0, 
            "capacidad": 2
        },
    ),
    (
        "nodo_(-55.8481, -",
        {
            "pos": (  0.31988684,   0.44174223), 
            "semaforo": False, 
            "zona": "residencial", 
            "vp": 0, 
            "capacidad": 2
        },
    ),
    (
        "nodo_(-55.8481, - (2)",
        {
            "pos": (  0.31970817,  -0.54847047), 
            "semaforo": False, 
            "zona": "residencial", 
            "vp": 0, 
            "capacidad": 2
        },
    ),
    (
        "nodo_(-55.84862, ",
        {
            "pos": (  0.21679488,   0.74608084), 
            "semaforo": False, 
            "zona": "residencial", 
            "vp": 0, 
            "capacidad": 2
        },
    ),
    (
        "nodo_(-55.84887, ",
        {
            "pos": (  0.16585438,   0.58056521), 
            "semaforo": False, 
            "zona": "residencial", 
            "vp": 0, 
            "capacidad": 2
        },
    ),
    (
        "nodo_(-55.84925, ",
        {
            "pos": (  0.08984069,   0.82041776), 
            "semaforo": False, 
            "zona": "residencial", 
            "vp": 0, 
            "capacidad": 2
        },
    ),
    (
        "nodo_(-55.84961, ",
        {
            "pos": (  0.01970321,   0.80539785), 
            "semaforo": False, 
            "zona": "residencial", 
            "vp": 0, 
            "capacidad": 2
        },
    ),
    (
        "nodo_(-55.8503, -",
        {
            "pos": ( -0.11735570,  -0.06128718), 
            "semaforo": False, 
            "zona": "residencial", 
            "vp": 0, 
            "capacidad": 2
        },
    ),
    (
        "nodo_(-55.85042, ",
        {
            "pos": ( -0.14131719,   0.25800780), 
            "semaforo": False, 
            "zona": "residencial", 
            "vp": 0, 
            "capacidad": 2
        },
    ),
    (
        "nodo_(-55.85138, ",
        {
            "pos": ( -0.33265174,  -0.28294212), 
            "semaforo": False, 
            "zona": "residencial", 
            "vp": 0, 
            "capacidad": 2
        },
    ),
    (
        "nodo_(-55.85173, ",
        {
            "pos": ( -0.40185617,  -0.91784595), 
            "semaforo": False, 
            "zona": "residencial", 
            "vp": 0, 
            "capacidad": 2
        },
    ),
    (
        "nodo_(-55.85182, ",
        {
            "pos": ( -0.41946499,  -0.88500974), 
            "semaforo": False, 
            "zona": "residencial", 
            "vp": 0, 
            "capacidad": 2
        },
    ),
    (
        "nodo_(-55.85215, ",
        {
            "pos": ( -0.48469899,  -0.53156512), 
            "semaforo": False, 
            "zona": "residencial", 
            "vp": 0, 
            "capacidad": 2
        },
    ),
    (
        "nodo_(-55.85282, ",
        {
            "pos": ( -0.61768822,  -0.71714262), 
            "semaforo": False, 
            "zona": "residencial", 
            "vp": 0, 
            "capacidad": 2
        },
    ),
    (
        "nodo_(-55.85334, ",
        {
            "pos": ( -0.72155442,  -0.34645369), 
            "semaforo": False, 
            "zona": "residencial", 
            "vp": 0, 
            "capacidad": 2
        },
    ),
]
# capacidad_total = 344

connections = [
    [
        "Ab. Mercedes Sandoval", "Ab. Mercedes Sandoval y Ab. Nelson González Maya", 
        {"vel_max": 30, "carriles": 1, "vehi_calle": 0, "weight": 122}
    ],
    [
        "Ab. Mercedes Sandoval (2)", "Ab. Mercedes Sandoval y Prof. Clementina Irrazabal Barboza", 
        {"vel_max": 30, "carriles": 1, "vehi_calle": 0, "weight": 57}
    ],
    [
        "Ab. Mercedes Sandoval (2)", "Peat. La Revendedora", 
        {"vel_max": 20, "carriles": 1, "vehi_calle": 0, "weight": 24}
    ],
    [
        "Ab. Mercedes Sandoval (3)", "Ab. Mercedes Sandoval y San José", 
        {"vel_max": 30, "carriles": 1, "vehi_calle": 0, "weight": 237}
    ],
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
        "Ab. Mercedes Sandoval y Av. Moisés Bertoni", "Ab. Mercedes Sandoval (2)", 
        {"vel_max": 30, "carriles": 1, "vehi_calle": 0, "weight": 59}
    ],
    [
        "Ab. Mercedes Sandoval y Av. Moisés Bertoni", "Av. Moisés Bertoni y Peat. La Revendedora", 
        {"vel_max": 60, "carriles": 2, "vehi_calle": 0, "weight": 25}
    ],
    [
        "Ab. Mercedes Sandoval y Don Carlos González Arias", "Ab. Mercedes Sandoval y Av. Moisés Bertoni", 
        {"vel_max": 30, "carriles": 1, "vehi_calle": 0, "weight": 94}
    ],
    [
        "Ab. Mercedes Sandoval y Don Carlos González Arias", "Av. Perimetral y Don Carlos González Arias", 
        {"vel_max": 30, "carriles": 1, "vehi_calle": 0, "weight": 267}
    ],
    [
        "Ab. Mercedes Sandoval y Juana de Lara", "Juana de Lara y Peat. La Revendedora", 
        {"vel_max": 30, "carriles": 1, "vehi_calle": 0, "weight": 25}
    ],
    [
        "Ab. Mercedes Sandoval y Prof. Clementina Irrazabal Barboza", "Ab. Mercedes Sandoval y Ab. Serafina Dávalos", 
        {"vel_max": 30, "carriles": 1, "vehi_calle": 0, "weight": 73}
    ],
    [
        "Ab. Mercedes Sandoval y Prof. Clementina Irrazabal Barboza", "Prof. Clementina Irrazabal Barboza (9)", 
        {"vel_max": 30, "carriles": 1, "vehi_calle": 0, "weight": 23}
    ],
    [
        "Ab. Mercedes Sandoval y San José", "Ab. Mercedes Sandoval", 
        {"vel_max": 30, "carriles": 1, "vehi_calle": 0, "weight": 82}
    ],
    [
        "Ab. Mercedes Sandoval y San José", "Av. San Roque y San José", 
        {"vel_max": 30, "carriles": 1, "vehi_calle": 0, "weight": 101}
    ],
    [
        "Ab. Nelson González Maya", "Ab. Mercedes Sandoval", 
        {"vel_max": 30, "carriles": 1, "vehi_calle": 0, "weight": 125}
    ],
    [
        "Ab. Nelson González Maya", "Ab. Mercedes Sandoval y Ab. Nelson González Maya", 
        {"vel_max": 30, "carriles": 1, "vehi_calle": 0, "weight": 78}
    ],
    [
        "Ab. Nelson González Maya y Av. San Roque", "Ab. Nelson González Maya", 
        {"vel_max": 30, "carriles": 1, "vehi_calle": 0, "weight": 81}
    ],
    [
        "Ab. Nelson González Maya y Av. San Roque", "Av. San Roque y Don Carlos González Arias", 
        {"vel_max": 80, "carriles": 2, "vehi_calle": 0, "weight": 86}
    ],
    [
        "Ab. Nelson González Maya y Av. San Roque", "Av. San Roque y San José", 
        {"vel_max": 80, "carriles": 2, "vehi_calle": 0, "weight": 136}
    ],
    [
        "Ab. Serafina Dávalos", "Ab. Serafina Dávalos y C.N. Pérez Lizzardo", 
        {"vel_max": 30, "carriles": 1, "vehi_calle": 0, "weight": 100}
    ],
    [
        "Ab. Serafina Dávalos", "nodo_(-55.85182, ", 
        {"vel_max": 30, "carriles": 1, "vehi_calle": 0, "weight": 40}
    ],
    [
        "Ab. Serafina Dávalos (2)", "Ab. Serafina Dávalos (4)", 
        {"vel_max": 30, "carriles": 1, "vehi_calle": 0, "weight": 35}
    ],
    [
        "Ab. Serafina Dávalos (2)", "Juana de Lara (10)", 
        {"vel_max": 20, "carriles": 1, "vehi_calle": 0, "weight": 64}
    ],
    [
        "Ab. Serafina Dávalos (3)", "Ab. Serafina Dávalos (9)", 
        {"vel_max": 30, "carriles": 1, "vehi_calle": 0, "weight": 22}
    ],
    [
        "Ab. Serafina Dávalos (3)", "Juana de Lara (9)", 
        {"vel_max": 30, "carriles": 1, "vehi_calle": 0, "weight": 67}
    ],
    [
        "Ab. Serafina Dávalos (4)", "Ab. Serafina Dávalos y Juana de Lara", 
        {"vel_max": 30, "carriles": 1, "vehi_calle": 0, "weight": 38}
    ],
    [
        "Ab. Serafina Dávalos (4)", "Juana de Lara (3)", 
        {"vel_max": 30, "carriles": 1, "vehi_calle": 0, "weight": 62}
    ],
    [
        "Ab. Serafina Dávalos (5)", "Ab. Serafina Dávalos y Av. Padre Juan Von Winckel", 
        {"vel_max": 30, "carriles": 1, "vehi_calle": 0, "weight": 86}
    ],
    [
        "Ab. Serafina Dávalos (5)", "Juana de Lara (7)", 
        {"vel_max": 10, "carriles": 1, "vehi_calle": 0, "weight": 68}
    ],
    [
        "Ab. Serafina Dávalos (6)", "Ab. Serafina Dávalos (3)", 
        {"vel_max": 30, "carriles": 1, "vehi_calle": 0, "weight": 87}
    ],
    [
        "Ab. Serafina Dávalos (6)", "Juana de Lara (4)", 
        {"vel_max": 30, "carriles": 1, "vehi_calle": 0, "weight": 69}
    ],
    [
        "Ab. Serafina Dávalos (7)", "Ab. Mercedes Sandoval y Ab. Serafina Dávalos", 
        {"vel_max": 30, "carriles": 1, "vehi_calle": 0, "weight": 23}
    ],
    [
        "Ab. Serafina Dávalos (7)", "Juana de Lara (6)", 
        {"vel_max": 20, "carriles": 1, "vehi_calle": 0, "weight": 71}
    ],
    [
        "Ab. Serafina Dávalos (8)", "Ab. Serafina Dávalos (2)", 
        {"vel_max": 30, "carriles": 1, "vehi_calle": 0, "weight": 37}
    ],
    [
        "Ab. Serafina Dávalos (8)", "Juana de Lara (5)", 
        {"vel_max": 20, "carriles": 1, "vehi_calle": 0, "weight": 66}
    ],
    [
        "Ab. Serafina Dávalos (9)", "Ab. Serafina Dávalos (8)", 
        {"vel_max": 30, "carriles": 1, "vehi_calle": 0, "weight": 36}
    ],
    [
        "Ab. Serafina Dávalos (9)", "Juana de Lara (8)", 
        {"vel_max": 20, "carriles": 1, "vehi_calle": 0, "weight": 67}
    ],
    [
        "Ab. Serafina Dávalos y Av. Padre Juan Von Winckel", "Ab. Serafina Dávalos (7)", 
        {"vel_max": 30, "carriles": 1, "vehi_calle": 0, "weight": 134}
    ],
    [
        "Ab. Serafina Dávalos y Av. Padre Juan Von Winckel", "Av. Padre Juan Von Winckel y Juana de Lara", 
        {"vel_max": 50, "carriles": 1, "vehi_calle": 0, "weight": 70}
    ],
    [
        "Ab. Serafina Dávalos y Av. Padre Juan Von Winckel", "Av. Padre Juan Von Winckel y Prof. Clementina Irrazabal Barboza", 
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
        "Ab. Serafina Dávalos y Juana de Lara", "Juana de Lara", 
        {"vel_max": 30, "carriles": 1, "vehi_calle": 0, "weight": 61}
    ],
    [
        "Ab. Serafina Dávalos y L. Scosceria", "Ab. Serafina Dávalos (5)", 
        {"vel_max": 30, "carriles": 1, "vehi_calle": 0, "weight": 86}
    ],
    [
        "Ab. Serafina Dávalos y L. Scosceria", "Juana de Lara y L. Scosceria", 
        {"vel_max": 30, "carriles": 1, "vehi_calle": 0, "weight": 70}
    ],
    [
        "Ab. Serafina Dávalos y Peat. La Revendedora", "Ab. Serafina Dávalos y Sor Graciela Estigarribia", 
        {"vel_max": 30, "carriles": 1, "vehi_calle": 0, "weight": 37}
    ],
    [
        "Ab. Serafina Dávalos y Peat. La Revendedora", "Juana de Lara y Peat. La Revendedora", 
        {"vel_max": 20, "carriles": 1, "vehi_calle": 0, "weight": 70}
    ],
    [
        "Ab. Serafina Dávalos y Sor Graciela Estigarribia", "Ab. Serafina Dávalos (6)", 
        {"vel_max": 30, "carriles": 1, "vehi_calle": 0, "weight": 24}
    ],
    [
        "Ab. Serafina Dávalos y Sor Graciela Estigarribia", "Juana de Lara y Sor Graciela Estigarribia", 
        {"vel_max": 20, "carriles": 1, "vehi_calle": 0, "weight": 69}
    ],
    [
        "Av. Moisés Bertoni", "Av. Moisés Bertoni (2)", 
        {"vel_max": 60, "carriles": 2, "vehi_calle": 0, "weight": 76}
    ],
    [
        "Av. Moisés Bertoni (2)", "Av. Moisés Bertoni (7)", 
        {"vel_max": 60, "carriles": 2, "vehi_calle": 0, "weight": 23}
    ],
    [
        "Av. Moisés Bertoni (2)", "nodo_(-55.8475, -", 
        {"vel_max": 30, "carriles": 1, "vehi_calle": 0, "weight": 59}
    ],
    [
        "Av. Moisés Bertoni (3)", "Av. Moisés Bertoni (5)", 
        {"vel_max": 60, "carriles": 2, "vehi_calle": 0, "weight": 38}
    ],
    [
        "Av. Moisés Bertoni (3)", "Prof. Clementina Irrazabal Barboza (3)", 
        {"vel_max": 20, "carriles": 1, "vehi_calle": 0, "weight": 112}
    ],
    [
        "Av. Moisés Bertoni (4)", "Av. Moisés Bertoni (3)", 
        {"vel_max": 60, "carriles": 2, "vehi_calle": 0, "weight": 25}
    ],
    [
        "Av. Moisés Bertoni (4)", "nodo_(-55.8481, -", 
        {"vel_max": 30, "carriles": 1, "vehi_calle": 0, "weight": 59}
    ],
    [
        "Av. Moisés Bertoni (5)", "Av. Moisés Bertoni (2)", 
        {"vel_max": 60, "carriles": 2, "vehi_calle": 0, "weight": 24}
    ],
    [
        "Av. Moisés Bertoni (5)", "Prof. Clementina Irrazabal Barboza (7)", 
        {"vel_max": 20, "carriles": 1, "vehi_calle": 0, "weight": 112}
    ],
    [
        "Av. Moisés Bertoni (6)", "Rot. Av. Moisés Bertoni", 
        {"vel_max": 60, "carriles": 2, "vehi_calle": 0, "weight": 22}
    ],
    [
        "Av. Moisés Bertoni (7)", "Av. Moisés Bertoni (6)", 
        {"vel_max": 60, "carriles": 2, "vehi_calle": 0, "weight": 57}
    ],
    [
        "Av. Moisés Bertoni (7)", "nodo_(-55.84735, ", 
        {"vel_max": 20, "carriles": 1, "vehi_calle": 0, "weight": 55}
    ],
    [
        "Av. Moisés Bertoni y Peat. La Revendedora", "Av. Moisés Bertoni y Sor Graciela Estigarribia", 
        {"vel_max": 60, "carriles": 2, "vehi_calle": 0, "weight": 38}
    ],
    [
        "Av. Moisés Bertoni y Peat. La Revendedora", "Peat. La Revendedora", 
        {"vel_max": 20, "carriles": 1, "vehi_calle": 0, "weight": 54}
    ],
    [
        "Av. Moisés Bertoni y Prof. Alberto Delvalle", "Ab. Mercedes Sandoval y Av. Moisés Bertoni", 
        {"vel_max": 60, "carriles": 2, "vehi_calle": 0, "weight": 84}
    ],
    [
        "Av. Moisés Bertoni y Prof. Alberto Delvalle", "Prof. Alberto Delvalle (3)", 
        {"vel_max": 30, "carriles": 1, "vehi_calle": 0, "weight": 16}
    ],
    [
        "Av. Moisés Bertoni y Prof. Alberto Delvalle", "Rot. San Roque González", 
        {"vel_max": 60, "carriles": 2, "vehi_calle": 0, "weight": 81}
    ],
    [
        "Av. Moisés Bertoni y Sor Graciela Estigarribia", "Av. Moisés Bertoni (4)", 
        {"vel_max": 60, "carriles": 2, "vehi_calle": 0, "weight": 23}
    ],
    [
        "Av. Moisés Bertoni y Sor Graciela Estigarribia", "Sor Graciela Estigarribia", 
        {"vel_max": 20, "carriles": 1, "vehi_calle": 0, "weight": 55}
    ],
    [
        "Av. Padre Juan Von Winckel", "Av. Padre Juan Von Winckel (5)", 
        {"vel_max": 50, "carriles": 1, "vehi_calle": 0, "weight": 328}
    ],
    [
        "Av. Padre Juan Von Winckel (2)", "Av. Padre Juan Von Winckel", 
        {"vel_max": 50, "carriles": 1, "vehi_calle": 0, "weight": 144}
    ],
    [
        "Av. Padre Juan Von Winckel (3)", "Av. Padre Juan Von Winckel (4)", 
        {"vel_max": 50, "carriles": 1, "vehi_calle": 0, "weight": 79}
    ],
    [
        "Av. Padre Juan Von Winckel (3)", "nodo_(-55.84673, ", 
        {"vel_max": 30, "carriles": 2, "vehi_calle": 0, "weight": 50}
    ],
    [
        "Av. Padre Juan Von Winckel (4)", "Av. Padre Juan Von Winckel", 
        {"vel_max": 50, "carriles": 1, "vehi_calle": 0, "weight": 73}
    ],
    [
        "Av. Padre Juan Von Winckel (4)", "nodo_(-55.84541, ", 
        {"vel_max": 30, "carriles": 2, "vehi_calle": 0, "weight": 73}
    ],
    [
        "Av. Padre Juan Von Winckel (5)", "Av. Padre Juan Von Winckel y Juana de Lara", 
        {"vel_max": 50, "carriles": 1, "vehi_calle": 0, "weight": 44}
    ],
    [
        "Av. Padre Juan Von Winckel (6)", "Av. Padre Juan Von Winckel (2)", 
        {"vel_max": 50, "carriles": 1, "vehi_calle": 0, "weight": 213}
    ],
    [
        "Av. Padre Juan Von Winckel (7)", "Av. Padre Juan Von Winckel (3)", 
        {"vel_max": 50, "carriles": 2, "vehi_calle": 0, "weight": 45}
    ],
    [
        "Av. Padre Juan Von Winckel y Juana de Lara", "Ab. Serafina Dávalos y Av. Padre Juan Von Winckel", 
        {"vel_max": 50, "carriles": 1, "vehi_calle": 0, "weight": 70}
    ],
    [
        "Av. Padre Juan Von Winckel y Juana de Lara", "Av. Padre Juan Von Winckel (6)", 
        {"vel_max": 50, "carriles": 1, "vehi_calle": 0, "weight": 15}
    ],
    [
        "Av. Padre Juan Von Winckel y Juana de Lara", "Juana de Lara (6)", 
        {"vel_max": 30, "carriles": 1, "vehi_calle": 0, "weight": 130}
    ],
    [
        "Av. Padre Juan Von Winckel y Prof. Clementina Irrazabal Barboza", "Ab. Serafina Dávalos y Av. Padre Juan Von Winckel", 
        {"vel_max": 50, "carriles": 1, "vehi_calle": 0, "weight": 73}
    ],
    [
        "Av. Padre Juan Von Winckel y Prof. Clementina Irrazabal Barboza", "Prof. Clementina Irrazabal Barboza", 
        {"vel_max": 30, "carriles": 1, "vehi_calle": 0, "weight": 90}
    ],
    [
        "Av. Perimetral", "Av. Perimetral y Don Carlos González Arias", 
        {"vel_max": 60, "carriles": 2, "vehi_calle": 0, "weight": 87}
    ],
    [
        "Av. Perimetral", "nodo_(-55.84961, ", 
        {"vel_max": 30, "carriles": 1, "vehi_calle": 0, "weight": 135}
    ],
    [
        "Av. Perimetral (2)", "Rot. Av. Moisés Bertoni", 
        {"vel_max": 60, "carriles": 2, "vehi_calle": 0, "weight": 23}
    ],
    [
        "Av. Perimetral y Don Carlos González Arias", "Av. Perimetral (2)", 
        {"vel_max": 60, "carriles": 2, "vehi_calle": 0, "weight": 78}
    ],
    [
        "Rot. San Roque González", "Av. San Roque y Próceres de Mayo", 
        {"vel_max": 80, "carriles": 2, "vehi_calle": 0, "weight": 92}
    ],
    [
        "Av. San Roque (2)", "Rot. San Roque González", 
        {"vel_max": 60, "carriles": 2, "vehi_calle": 0, "weight": 49}
    ],
    [
        "Av. San Roque (3)", "Av. San Roque (6)", 
        {"vel_max": 80, "carriles": 2, "vehi_calle": 0, "weight": 75}
    ],
    [
        "Av. San Roque (4)", "Av. San Roque y D. Moreno Ocampo", 
        {"vel_max": 80, "carriles": 2, "vehi_calle": 0, "weight": 72}
    ],
    [
        "Av. San Roque (5)", "Av. San Roque y Vía 1", 
        {"vel_max": 80, "carriles": 2, "vehi_calle": 0, "weight": 18}
    ],
    [
        "Av. San Roque (6)", "Ab. Serafina Dávalos", 
        {"vel_max": 30, "carriles": 1, "vehi_calle": 0, "weight": 84}
    ],
    [
        "Av. San Roque (6)", "Av. San Roque y Vía 1", 
        {"vel_max": 80, "carriles": 2, "vehi_calle": 0, "weight": 48}
    ],
    [
        "Av. San Roque y C.M. Pérez Lizzandro", "Av. San Roque (3)", 
        {"vel_max": 80, "carriles": 2, "vehi_calle": 0, "weight": 31}
    ],
    [
        "Av. San Roque y C.M. Pérez Lizzandro", "C.M. Pérez Lizzandro y C.N. Pérez Lizzardo", 
        {"vel_max": 30, "carriles": 1, "vehi_calle": 0, "weight": 25}
    ],
    [
        "Av. San Roque y D. Moreno Ocampo", "Av. San Roque y C.M. Pérez Lizzandro", 
        {"vel_max": 80, "carriles": 2, "vehi_calle": 0, "weight": 48}
    ],
    [
        "Av. San Roque y D. Moreno Ocampo", "D. Moreno Ocampo", 
        {"vel_max": 30, "carriles": 1, "vehi_calle": 0, "weight": 16}
    ],
    [
        "Av. San Roque y Don Carlos González Arias", "Ab. Nelson González Maya y Av. San Roque", 
        {"vel_max": 80, "carriles": 2, "vehi_calle": 0, "weight": 86}
    ],
    [
        "Av. San Roque y Don Carlos González Arias", "Av. San Roque (2)", 
        {"vel_max": 80, "carriles": 2, "vehi_calle": 0, "weight": 46}
    ],
    [
        "Av. San Roque y Don Carlos González Arias", "Don Carlos González Arias", 
        {"vel_max": 30, "carriles": 1, "vehi_calle": 0, "weight": 21}
    ],
    [
        "Av. San Roque y Próceres de Mayo", "Av. San Roque (4)", 
        {"vel_max": 80, "carriles": 2, "vehi_calle": 0, "weight": 97}
    ],
    [
        "Av. San Roque y San José", "Ab. Nelson González Maya y Av. San Roque", 
        {"vel_max": 80, "carriles": 2, "vehi_calle": 0, "weight": 136}
    ],
    [
        "Av. San Roque y Vía 1", "Vía 1", 
        {"vel_max": 20, "carriles": 1, "vehi_calle": 0, "weight": 66}
    ],
    [
        "C.M. Pérez Lizzandro y C.N. Pérez Lizzardo", "Ab. Serafina Dávalos y C.M. Pérez Lizzandro", 
        {"vel_max": 30, "carriles": 1, "vehi_calle": 0, "weight": 75}
    ],
    [
        "C.M. Pérez Lizzandro y C.N. Pérez Lizzardo", "Av. San Roque y C.M. Pérez Lizzandro", 
        {"vel_max": 30, "carriles": 1, "vehi_calle": 0, "weight": 25}
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
        "C.N. Pérez Lizzardo", "Ab. Serafina Dávalos y C.N. Pérez Lizzardo", 
        {"vel_max": 30, "carriles": 1, "vehi_calle": 0, "weight": 43}
    ],
    [
        "C.N. Pérez Lizzardo y Juana de Lara", "C.N. Pérez Lizzardo", 
        {"vel_max": 30, "carriles": 1, "vehi_calle": 0, "weight": 33}
    ],
    [
        "D. Moreno Ocampo", "D. Moreno Ocampo y Tte. Arzamendia Samaniego", 
        {"vel_max": 30, "carriles": 1, "vehi_calle": 0, "weight": 165}
    ],
    [
        "D. Moreno Ocampo", "nodo_(-55.85138, ", 
        {"vel_max": 30, "carriles": 1, "vehi_calle": 0, "weight": 72}
    ],
    [
        "D. Moreno Ocampo y Tte. Arzamendia Samaniego", "Tte. Arzamendia Samaniego (2)", 
        {"vel_max": 30, "carriles": 2, "vehi_calle": 0, "weight": 78}
    ],
    [
        "Don Carlos González Arias", "Ab. Mercedes Sandoval y Don Carlos González Arias", 
        {"vel_max": 30, "carriles": 1, "vehi_calle": 0, "weight": 139}
    ],
    [
        "Don Carlos González Arias", "nodo_(-55.85042, ", 
        {"vel_max": 20, "carriles": 1, "vehi_calle": 0, "weight": 41}
    ],
    [
        "Juan Brítez y Prof. Clementina Irrazabal Barboza", "Ab. Serafina Dávalos y Juan Brítez", 
        {"vel_max": 10, "carriles": 1, "vehi_calle": 0, "weight": 73}
    ],
    [
        "Juan Brítez y Prof. Clementina Irrazabal Barboza", "C.M. Pérez Lizzandro y C.N. Pérez Lizzardo", 
        {"vel_max": 30, "carriles": 1, "vehi_calle": 0, "weight": 100}
    ],
    [
        "Juana de Lara (10)", "Juana de Lara (3)", 
        {"vel_max": 30, "carriles": 1, "vehi_calle": 0, "weight": 36}
    ],
    [
        "Juana de Lara (11)", "Juana de Lara (2)", 
        {"vel_max": 30, "carriles": 1, "vehi_calle": 0, "weight": 37}
    ],
    [
        "Juana de Lara (11)", "Juana de Lara y Prof. Clementina Irrazabal Barboza", 
        {"vel_max": 30, "carriles": 1, "vehi_calle": 0, "weight": 70}
    ],
    [
        "Juana de Lara (3)", "Juana de Lara", 
        {"vel_max": 30, "carriles": 1, "vehi_calle": 0, "weight": 52}
    ],
    [
        "Juana de Lara (4)", "Juana de Lara (9)", 
        {"vel_max": 30, "carriles": 1, "vehi_calle": 0, "weight": 88}
    ],
    [
        "Juana de Lara (5)", "Juana de Lara (10)", 
        {"vel_max": 30, "carriles": 1, "vehi_calle": 0, "weight": 35}
    ],
    [
        "Juana de Lara (6)", "Ab. Mercedes Sandoval y Juana de Lara", 
        {"vel_max": 30, "carriles": 1, "vehi_calle": 0, "weight": 21}
    ],
    [
        "Juana de Lara (7)", "Av. Padre Juan Von Winckel y Juana de Lara", 
        {"vel_max": 30, "carriles": 1, "vehi_calle": 0, "weight": 84}
    ],
    [
        "Juana de Lara (8)", "Juana de Lara (5)", 
        {"vel_max": 30, "carriles": 1, "vehi_calle": 0, "weight": 37}
    ],
    [
        "Juana de Lara (9)", "Juana de Lara (8)", 
        {"vel_max": 30, "carriles": 1, "vehi_calle": 0, "weight": 22}
    ],
    [
        "Juana de Lara y Juan Brítez", "Juana de Lara y L. Scosceria", 
        {"vel_max": 30, "carriles": 1, "vehi_calle": 0, "weight": 96}
    ],
    [
        "Juana de Lara y L. Scosceria", "Juana de Lara (7)", 
        {"vel_max": 30, "carriles": 1, "vehi_calle": 0, "weight": 88}
    ],
    [
        "Juana de Lara y Peat. La Revendedora", "Juana de Lara y Sor Graciela Estigarribia", 
        {"vel_max": 30, "carriles": 1, "vehi_calle": 0, "weight": 38}
    ],
    [
        "Juana de Lara y Prof. Clementina Irrazabal Barboza", "Ab. Serafina Dávalos y Juana de Lara", 
        {"vel_max": 30, "carriles": 1, "vehi_calle": 0, "weight": 72}
    ],
    [
        "Juana de Lara y Prof. Clementina Irrazabal Barboza", "Prof. Clementina Irrazabal Barboza (5)", 
        {"vel_max": 30, "carriles": 1, "vehi_calle": 0, "weight": 47}
    ],
    [
        "Juana de Lara y Sor Graciela Estigarribia", "Juana de Lara (4)", 
        {"vel_max": 30, "carriles": 1, "vehi_calle": 0, "weight": 24}
    ],
    [
        "L. Scosceria y Prof. Clementina Irrazabal Barboza", "Ab. Serafina Dávalos y L. Scosceria", 
        {"vel_max": 30, "carriles": 1, "vehi_calle": 0, "weight": 72}
    ],
    [
        "L. Scosceria y Prof. Clementina Irrazabal Barboza", "Juan Brítez y Prof. Clementina Irrazabal Barboza", 
        {"vel_max": 30, "carriles": 1, "vehi_calle": 0, "weight": 99}
    ],
    [
        "Peat. La Revendedora", "Peat. La Revendedora y Prof. Clementina Irrazabal Barboza", 
        {"vel_max": 20, "carriles": 1, "vehi_calle": 0, "weight": 57}
    ],
    [
        "Peat. La Revendedora", "Sor Graciela Estigarribia", 
        {"vel_max": 20, "carriles": 1, "vehi_calle": 0, "weight": 38}
    ],
    [
        "Peat. La Revendedora y Prof. Clementina Irrazabal Barboza", "Ab. Mercedes Sandoval y Prof. Clementina Irrazabal Barboza", 
        {"vel_max": 30, "carriles": 1, "vehi_calle": 0, "weight": 25}
    ],
    [
        "Peat. La Revendedora y Prof. Clementina Irrazabal Barboza", "Ab. Serafina Dávalos y Peat. La Revendedora", 
        {"vel_max": 20, "carriles": 1, "vehi_calle": 0, "weight": 73}
    ],
    [
        "Prof. Alberto Delvalle", "Prof. Alberto Delvalle (2)", 
        {"vel_max": 30, "carriles": 1, "vehi_calle": 0, "weight": 22}
    ],
    [
        "Prof. Alberto Delvalle (2)", "Ab. Mercedes Sandoval (2)", 
        {"vel_max": 20, "carriles": 1, "vehi_calle": 0, "weight": 81}
    ],
    [
        "Prof. Alberto Delvalle (2)", "Prof. Alberto Delvalle y Prof. Clementina Irrazabal Barboza", 
        {"vel_max": 30, "carriles": 1, "vehi_calle": 0, "weight": 63}
    ],
    [
        "Prof. Alberto Delvalle (3)", "Prof. Alberto Delvalle", 
        {"vel_max": 30, "carriles": 1, "vehi_calle": 0, "weight": 15}
    ],
    [
        "Prof. Alberto Delvalle y Prof. Clementina Irrazabal Barboza", "Av. Padre Juan Von Winckel y Prof. Clementina Irrazabal Barboza", 
        {"vel_max": 30, "carriles": 1, "vehi_calle": 0, "weight": 81}
    ],
    [
        "Prof. Clementina Irrazabal Barboza", "Ab. Serafina Dávalos (5)", 
        {"vel_max": 10, "carriles": 1, "vehi_calle": 0, "weight": 73}
    ],
    [
        "Prof. Clementina Irrazabal Barboza", "L. Scosceria y Prof. Clementina Irrazabal Barboza", 
        {"vel_max": 30, "carriles": 1, "vehi_calle": 0, "weight": 84}
    ],
    [
        "Prof. Clementina Irrazabal Barboza (2)", "Ab. Serafina Dávalos (9)", 
        {"vel_max": 20, "carriles": 1, "vehi_calle": 0, "weight": 66}
    ],
    [
        "Prof. Clementina Irrazabal Barboza (2)", "Prof. Clementina Irrazabal Barboza (6)", 
        {"vel_max": 30, "carriles": 1, "vehi_calle": 0, "weight": 24}
    ],
    [
        "Prof. Clementina Irrazabal Barboza (3)", "Prof. Clementina Irrazabal Barboza (4)", 
        {"vel_max": 30, "carriles": 1, "vehi_calle": 0, "weight": 25}
    ],
    [
        "Prof. Clementina Irrazabal Barboza (4)", "Ab. Serafina Dávalos (6)", 
        {"vel_max": 30, "carriles": 1, "vehi_calle": 0, "weight": 70}
    ],
    [
        "Prof. Clementina Irrazabal Barboza (4)", "Prof. Clementina Irrazabal Barboza y Sor Graciela Estigarribia", 
        {"vel_max": 30, "carriles": 1, "vehi_calle": 0, "weight": 24}
    ],
    [
        "Prof. Clementina Irrazabal Barboza (5)", "Ab. Serafina Dávalos (2)", 
        {"vel_max": 20, "carriles": 1, "vehi_calle": 0, "weight": 65}
    ],
    [
        "Prof. Clementina Irrazabal Barboza (5)", "Prof. Clementina Irrazabal Barboza (8)", 
        {"vel_max": 30, "carriles": 1, "vehi_calle": 0, "weight": 36}
    ],
    [
        "Prof. Clementina Irrazabal Barboza (6)", "Ab. Serafina Dávalos (3)", 
        {"vel_max": 30, "carriles": 1, "vehi_calle": 0, "weight": 67}
    ],
    [
        "Prof. Clementina Irrazabal Barboza (6)", "Prof. Clementina Irrazabal Barboza (7)", 
        {"vel_max": 30, "carriles": 1, "vehi_calle": 0, "weight": 21}
    ],
    [
        "Prof. Clementina Irrazabal Barboza (7)", "Prof. Clementina Irrazabal Barboza (3)", 
        {"vel_max": 30, "carriles": 1, "vehi_calle": 0, "weight": 40}
    ],
    [
        "Prof. Clementina Irrazabal Barboza (8)", "Ab. Serafina Dávalos (8)", 
        {"vel_max": 20, "carriles": 1, "vehi_calle": 0, "weight": 65}
    ],
    [
        "Prof. Clementina Irrazabal Barboza (8)", "Prof. Clementina Irrazabal Barboza (2)", 
        {"vel_max": 30, "carriles": 1, "vehi_calle": 0, "weight": 33}
    ],
    [
        "Prof. Clementina Irrazabal Barboza (9)", "Ab. Serafina Dávalos (7)", 
        {"vel_max": 20, "carriles": 1, "vehi_calle": 0, "weight": 73}
    ],
    [
        "Prof. Clementina Irrazabal Barboza (9)", "Prof. Alberto Delvalle y Prof. Clementina Irrazabal Barboza", 
        {"vel_max": 30, "carriles": 1, "vehi_calle": 0, "weight": 55}
    ],
    [
        "Prof. Clementina Irrazabal Barboza y Sor Graciela Estigarribia", "Ab. Serafina Dávalos y Sor Graciela Estigarribia", 
        {"vel_max": 20, "carriles": 1, "vehi_calle": 0, "weight": 72}
    ],
    [
        "Prof. Clementina Irrazabal Barboza y Sor Graciela Estigarribia", "Peat. La Revendedora y Prof. Clementina Irrazabal Barboza", 
        {"vel_max": 30, "carriles": 1, "vehi_calle": 0, "weight": 37}
    ],
    [
        "Próceres de Mayo", "Av. San Roque y Próceres de Mayo", 
        {"vel_max": 30, "carriles": 1, "vehi_calle": 0, "weight": 60}
    ],
    [
        "Próceres de Mayo y Tte. Arzamendia Samaniego", "Próceres de Mayo", 
        {"vel_max": 30, "carriles": 1, "vehi_calle": 0, "weight": 105}
    ],
    [
        "Rot. Av. Moisés Bertoni", "Av. Moisés Bertoni (6)", 
        {"vel_max": 60, "carriles": 2, "vehi_calle": 0, "weight": 22}
    ],
    [
        "Rot. Av. Moisés Bertoni", "Av. Perimetral (2)", 
        {"vel_max": 60, "carriles": 2, "vehi_calle": 0, "weight": 23}
    ],
    [
        "Rot. San Roque González", "Av. Moisés Bertoni y Prof. Alberto Delvalle", 
        {"vel_max": 60, "carriles": 2, "vehi_calle": 0, "weight": 81}
    ],
    [
        "Rot. San Roque González", "Av. San Roque (2)", 
        {"vel_max": 60, "carriles": 2, "vehi_calle": 0, "weight": 49}
    ],
    [
        "Sor Graciela Estigarribia", "Prof. Clementina Irrazabal Barboza y Sor Graciela Estigarribia", 
        {"vel_max": 20, "carriles": 1, "vehi_calle": 0, "weight": 57}
    ],
    [
        "Sor Graciela Estigarribia", "nodo_(-55.8481, -", 
        {"vel_max": 20, "carriles": 1, "vehi_calle": 0, "weight": 24}
    ],
    [
        "Tte. Arzamendia Samaniego", "D. Moreno Ocampo y Tte. Arzamendia Samaniego", 
        {"vel_max": 30, "carriles": 2, "vehi_calle": 0, "weight": 129}
    ],
    [
        "Tte. Arzamendia Samaniego (2)", "Próceres de Mayo y Tte. Arzamendia Samaniego", 
        {"vel_max": 30, "carriles": 2, "vehi_calle": 0, "weight": 87}
    ],
    [
        "Tte. Arzamendia Samaniego (2)", "nodo_(-55.85138, ", 
        {"vel_max": 20, "carriles": 1, "vehi_calle": 0, "weight": 153}
    ],
    [
        "nodo_(-55.84467, ", "Juana de Lara", 
        {"vel_max": 30, "carriles": 1, "vehi_calle": 0, "weight": 74}
    ],
    [
        "nodo_(-55.84541, ", "nodo_(-55.84506, ", 
        {"vel_max": 30, "carriles": 1, "vehi_calle": 0, "weight": 66}
    ],
    [
        "nodo_(-55.84673, ", "nodo_(-55.84738, ", 
        {"vel_max": 30, "carriles": 2, "vehi_calle": 0, "weight": 100}
    ],
    [
        "nodo_(-55.84688, ", "Prof. Clementina Irrazabal Barboza (5)", 
        {"vel_max": 20, "carriles": 1, "vehi_calle": 0, "weight": 60}
    ],
    [
        "nodo_(-55.84716, ", "Juana de Lara (11)", 
        {"vel_max": 30, "carriles": 1, "vehi_calle": 0, "weight": 35}
    ],
    [
        "nodo_(-55.84717, ", "Prof. Clementina Irrazabal Barboza (8)", 
        {"vel_max": 20, "carriles": 1, "vehi_calle": 0, "weight": 65}
    ],
    [
        "nodo_(-55.84735, ", "Prof. Clementina Irrazabal Barboza (2)", 
        {"vel_max": 20, "carriles": 1, "vehi_calle": 0, "weight": 58}
    ],
    [
        "nodo_(-55.84735, ", "nodo_(-55.84725, ", 
        {"vel_max": 20, "carriles": 1, "vehi_calle": 0, "weight": 15}
    ],
    [
        "nodo_(-55.84738, ", "Av. Padre Juan Von Winckel (2)", 
        {"vel_max": 30, "carriles": 1, "vehi_calle": 0, "weight": 143}
    ],
    [
        "nodo_(-55.84738, ", "nodo_(-55.8481, - (2)", 
        {"vel_max": 30, "carriles": 2, "vehi_calle": 0, "weight": 112}
    ],
    [
        "nodo_(-55.8475, -", "Prof. Clementina Irrazabal Barboza (6)", 
        {"vel_max": 30, "carriles": 1, "vehi_calle": 0, "weight": 58}
    ],
    [
        "nodo_(-55.8475, -", "nodo_(-55.84735, ", 
        {"vel_max": 20, "carriles": 1, "vehi_calle": 0, "weight": 23}
    ],
    [
        "nodo_(-55.8481, -", "Prof. Clementina Irrazabal Barboza (4)", 
        {"vel_max": 30, "carriles": 1, "vehi_calle": 0, "weight": 57}
    ],
    [
        "nodo_(-55.8481, -", "nodo_(-55.8475, -", 
        {"vel_max": 20, "carriles": 1, "vehi_calle": 0, "weight": 87}
    ],
    [
        "nodo_(-55.8481, - (2)", "Av. Padre Juan Von Winckel (6)", 
        {"vel_max": 30, "carriles": 2, "vehi_calle": 0, "weight": 190}
    ],
    [
        "nodo_(-55.84862, ", "Av. Moisés Bertoni (2)", 
        {"vel_max": 20, "carriles": 1, "vehi_calle": 0, "weight": 87}
    ],
    [
        "nodo_(-55.84887, ", "nodo_(-55.84807, ", 
        {"vel_max": 20, "carriles": 1, "vehi_calle": 0, "weight": 122}
    ],
    [
        "nodo_(-55.84961, ", "Ab. Mercedes Sandoval y Ab. Nelson González Maya", 
        {"vel_max": 30, "carriles": 1, "vehi_calle": 0, "weight": 126}
    ],
    [
        "nodo_(-55.84961, ", "nodo_(-55.84925, ", 
        {"vel_max": 20, "carriles": 1, "vehi_calle": 0, "weight": 36}
    ],
    [
        "nodo_(-55.8503, -", "Prof. Clementina Irrazabal Barboza", 
        {"vel_max": 20, "carriles": 1, "vehi_calle": 0, "weight": 54}
    ],
    [
        "nodo_(-55.85138, ", "Av. San Roque (4)", 
        {"vel_max": 20, "carriles": 1, "vehi_calle": 0, "weight": 17}
    ],
    [
        "nodo_(-55.85182, ", "C.N. Pérez Lizzardo", 
        {"vel_max": 30, "carriles": 1, "vehi_calle": 0, "weight": 97}
    ],
    [
        "nodo_(-55.85182, ", "nodo_(-55.85173, ", 
        {"vel_max": 30, "carriles": 1, "vehi_calle": 0, "weight": 19}
    ],
    [
        "nodo_(-55.85215, ", "Av. San Roque (3)", 
        {"vel_max": 20, "carriles": 1, "vehi_calle": 0, "weight": 16}
    ],
    [
        "nodo_(-55.85215, ", "D. Moreno Ocampo", 
        {"vel_max": 30, "carriles": 1, "vehi_calle": 0, "weight": 79}
    ],
    [
        "nodo_(-55.85282, ", "nodo_(-55.85215, ", 
        {"vel_max": 30, "carriles": 1, "vehi_calle": 0, "weight": 118}
    ],
    [
        "nodo_(-55.85334, ", "nodo_(-55.85215, ", 
        {"vel_max": 20, "carriles": 1, "vehi_calle": 0, "weight": 153}
    ],
]