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
    ("Ab. Mercedes Sandoval y Av. Moisés Bertoni",                      {"semaforo": True , "zona": "comercial",   "vp": 0, "capacidad": 4},),
    ("Ab. Nelson González Maya y Av. San Roque",                        {"semaforo": True , "zona": "comercial",   "vp": 0, "capacidad": 4},),
    ("Av. Moisés Bertoni",                                              {"semaforo": True , "zona": "comercial",   "vp": 0, "capacidad": 4},),
    ("Av. Moisés Bertoni (2)",                                          {"semaforo": True , "zona": "comercial",   "vp": 0, "capacidad": 4},),
    ("Av. Moisés Bertoni (3)",                                          {"semaforo": True , "zona": "comercial",   "vp": 0, "capacidad": 4},),
    ("Av. Moisés Bertoni (4)",                                          {"semaforo": True , "zona": "comercial",   "vp": 0, "capacidad": 4},),
    ("Av. Moisés Bertoni (5)",                                          {"semaforo": True , "zona": "comercial",   "vp": 0, "capacidad": 4},),
    ("Av. Moisés Bertoni (6)",                                          {"semaforo": True , "zona": "comercial",   "vp": 0, "capacidad": 4},),
    ("Av. Moisés Bertoni (7)",                                          {"semaforo": True , "zona": "comercial",   "vp": 0, "capacidad": 4},),
    ("Av. Moisés Bertoni y Peat. La Revendedora",                       {"semaforo": True , "zona": "comercial",   "vp": 0, "capacidad": 4},),
    ("Av. Moisés Bertoni y Prof. Alberto Delvalle",                     {"semaforo": True , "zona": "comercial",   "vp": 0, "capacidad": 4},),
    ("Av. Moisés Bertoni y Sor Graciela Estigarribia",                  {"semaforo": True , "zona": "comercial",   "vp": 0, "capacidad": 4},),
    ("Av. Perimetral",                                                  {"semaforo": True , "zona": "comercial",   "vp": 0, "capacidad": 4},),
    ("Av. Perimetral (2)",                                              {"semaforo": True , "zona": "comercial",   "vp": 0, "capacidad": 4},),
    ("Av. Perimetral y Don Carlos González Arias",                      {"semaforo": True , "zona": "comercial",   "vp": 0, "capacidad": 4},),
    ("Av. San Roque",                                                   {"semaforo": True , "zona": "comercial",   "vp": 0, "capacidad": 4},),
    ("Av. San Roque (2)",                                               {"semaforo": True , "zona": "comercial",   "vp": 0, "capacidad": 4},),
    ("Av. San Roque (3)",                                               {"semaforo": True , "zona": "comercial",   "vp": 0, "capacidad": 4},),
    ("Av. San Roque (4)",                                               {"semaforo": True , "zona": "comercial",   "vp": 0, "capacidad": 4},),
    ("Av. San Roque (5)",                                               {"semaforo": True , "zona": "comercial",   "vp": 0, "capacidad": 4},),
    ("Av. San Roque (6)",                                               {"semaforo": True , "zona": "comercial",   "vp": 0, "capacidad": 4},),
    ("Av. San Roque y C.M. Pérez Lizzandro",                            {"semaforo": True , "zona": "comercial",   "vp": 0, "capacidad": 4},),
    ("Av. San Roque y D. Moreno Ocampo",                                {"semaforo": True , "zona": "comercial",   "vp": 0, "capacidad": 4},),
    ("Av. San Roque y Don Carlos González Arias",                       {"semaforo": True , "zona": "comercial",   "vp": 0, "capacidad": 4},),
    ("Av. San Roque y Próceres de Mayo",                                {"semaforo": True , "zona": "comercial",   "vp": 0, "capacidad": 4},),
    ("Av. San Roque y San José",                                        {"semaforo": True , "zona": "comercial",   "vp": 0, "capacidad": 4},),
    ("Av. San Roque y Vía 1",                                           {"semaforo": True , "zona": "comercial",   "vp": 0, "capacidad": 4},),
    ("Rot. Av. Moisés Bertoni",                                         {"semaforo": True , "zona": "comercial",   "vp": 0, "capacidad": 4},),
    ("Rot. San Roque González",                                         {"semaforo": True , "zona": "comercial",   "vp": 0, "capacidad": 4},),
    ("Ab. Serafina Dávalos y Av. Padre Juan Von Winckel",               {"semaforo": True , "zona": "secundaria",  "vp": 0, "capacidad": 3},),
    ("Av. Padre Juan Von Winckel",                                      {"semaforo": True , "zona": "secundaria",  "vp": 0, "capacidad": 3},),
    ("Av. Padre Juan Von Winckel (2)",                                  {"semaforo": True , "zona": "secundaria",  "vp": 0, "capacidad": 3},),
    ("Av. Padre Juan Von Winckel (3)",                                  {"semaforo": True , "zona": "secundaria",  "vp": 0, "capacidad": 3},),
    ("Av. Padre Juan Von Winckel (4)",                                  {"semaforo": True , "zona": "secundaria",  "vp": 0, "capacidad": 3},),
    ("Av. Padre Juan Von Winckel (5)",                                  {"semaforo": True , "zona": "secundaria",  "vp": 0, "capacidad": 3},),
    ("Av. Padre Juan Von Winckel (6)",                                  {"semaforo": True , "zona": "secundaria",  "vp": 0, "capacidad": 3},),
    ("Av. Padre Juan Von Winckel (7)",                                  {"semaforo": True , "zona": "secundaria",  "vp": 0, "capacidad": 3},),
    ("Av. Padre Juan Von Winckel y Juana de Lara",                      {"semaforo": True , "zona": "secundaria",  "vp": 0, "capacidad": 3},),
    ("Av. Padre Juan Von Winckel y Prof. Clementina Irrazabal Barboza", {"semaforo": True , "zona": "secundaria",  "vp": 0, "capacidad": 3},),
    ("Ab. Serafina Dávalos (5)",                                        {"semaforo": False, "zona": "peatonal",    "vp": 0, "capacidad": 1},),
    ("Ab. Serafina Dávalos y Juan Brítez",                              {"semaforo": False, "zona": "peatonal",    "vp": 0, "capacidad": 1},),
    ("Juan Brítez y Prof. Clementina Irrazabal Barboza",                {"semaforo": False, "zona": "peatonal",    "vp": 0, "capacidad": 1},),
    ("Juana de Lara (7)",                                               {"semaforo": False, "zona": "peatonal",    "vp": 0, "capacidad": 1},),
    ("Juana de Lara y Juan Brítez",                                     {"semaforo": False, "zona": "peatonal",    "vp": 0, "capacidad": 1},),
    ("Prof. Clementina Irrazabal Barboza",                              {"semaforo": False, "zona": "peatonal",    "vp": 0, "capacidad": 1},),
    ("Ab. Mercedes Sandoval",                                           {"semaforo": False, "zona": "residencial", "vp": 0, "capacidad": 2},),
    ("Ab. Mercedes Sandoval (2)",                                       {"semaforo": False, "zona": "residencial", "vp": 0, "capacidad": 2},),
    ("Ab. Mercedes Sandoval (3)",                                       {"semaforo": False, "zona": "residencial", "vp": 0, "capacidad": 2},),
    ("Ab. Mercedes Sandoval y Ab. Nelson González Maya",                {"semaforo": False, "zona": "residencial", "vp": 0, "capacidad": 2},),
    ("Ab. Mercedes Sandoval y Ab. Serafina Dávalos",                    {"semaforo": False, "zona": "residencial", "vp": 0, "capacidad": 2},),
    ("Ab. Mercedes Sandoval y Don Carlos González Arias",               {"semaforo": False, "zona": "residencial", "vp": 0, "capacidad": 2},),
    ("Ab. Mercedes Sandoval y Juana de Lara",                           {"semaforo": False, "zona": "residencial", "vp": 0, "capacidad": 2},),
    ("Ab. Mercedes Sandoval y Prof. Clementina Irrazabal Barboza",      {"semaforo": False, "zona": "residencial", "vp": 0, "capacidad": 2},),
    ("Ab. Mercedes Sandoval y San José",                                {"semaforo": False, "zona": "residencial", "vp": 0, "capacidad": 2},),
    ("Ab. Nelson González Maya",                                        {"semaforo": False, "zona": "residencial", "vp": 0, "capacidad": 2},),
    ("Ab. Serafina Dávalos",                                            {"semaforo": False, "zona": "residencial", "vp": 0, "capacidad": 2},),
    ("Ab. Serafina Dávalos (2)",                                        {"semaforo": False, "zona": "residencial", "vp": 0, "capacidad": 2},),
    ("Ab. Serafina Dávalos (3)",                                        {"semaforo": False, "zona": "residencial", "vp": 0, "capacidad": 2},),
    ("Ab. Serafina Dávalos (4)",                                        {"semaforo": False, "zona": "residencial", "vp": 0, "capacidad": 2},),
    ("Ab. Serafina Dávalos (6)",                                        {"semaforo": False, "zona": "residencial", "vp": 0, "capacidad": 2},),
    ("Ab. Serafina Dávalos (7)",                                        {"semaforo": False, "zona": "residencial", "vp": 0, "capacidad": 2},),
    ("Ab. Serafina Dávalos (8)",                                        {"semaforo": False, "zona": "residencial", "vp": 0, "capacidad": 2},),
    ("Ab. Serafina Dávalos (9)",                                        {"semaforo": False, "zona": "residencial", "vp": 0, "capacidad": 2},),
    ("Ab. Serafina Dávalos y C.M. Pérez Lizzandro",                     {"semaforo": False, "zona": "residencial", "vp": 0, "capacidad": 2},),
    ("Ab. Serafina Dávalos y C.N. Pérez Lizzardo",                      {"semaforo": False, "zona": "residencial", "vp": 0, "capacidad": 2},),
    ("Ab. Serafina Dávalos y Juana de Lara",                            {"semaforo": False, "zona": "residencial", "vp": 0, "capacidad": 2},),
    ("Ab. Serafina Dávalos y L. Scosceria",                             {"semaforo": False, "zona": "residencial", "vp": 0, "capacidad": 2},),
    ("Ab. Serafina Dávalos y Peat. La Revendedora",                     {"semaforo": False, "zona": "residencial", "vp": 0, "capacidad": 2},),
    ("Ab. Serafina Dávalos y Sor Graciela Estigarribia",                {"semaforo": False, "zona": "residencial", "vp": 0, "capacidad": 2},),
    ("C.M. Pérez Lizzandro y C.N. Pérez Lizzardo",                      {"semaforo": False, "zona": "residencial", "vp": 0, "capacidad": 2},),
    ("C.M. Pérez Lizzandro y Juana de Lara",                            {"semaforo": False, "zona": "residencial", "vp": 0, "capacidad": 2},),
    ("C.N. Pérez Lizzardo",                                             {"semaforo": False, "zona": "residencial", "vp": 0, "capacidad": 2},),
    ("C.N. Pérez Lizzardo y Juana de Lara",                             {"semaforo": False, "zona": "residencial", "vp": 0, "capacidad": 2},),
    ("D. Moreno Ocampo",                                                {"semaforo": False, "zona": "residencial", "vp": 0, "capacidad": 2},),
    ("D. Moreno Ocampo y Tte. Arzamendia Samaniego",                    {"semaforo": False, "zona": "residencial", "vp": 0, "capacidad": 2},),
    ("Don Carlos González Arias",                                       {"semaforo": False, "zona": "residencial", "vp": 0, "capacidad": 2},),
    ("Juana de Lara",                                                   {"semaforo": False, "zona": "residencial", "vp": 0, "capacidad": 2},),
    ("Juana de Lara (10)",                                              {"semaforo": False, "zona": "residencial", "vp": 0, "capacidad": 2},),
    ("Juana de Lara (11)",                                              {"semaforo": False, "zona": "residencial", "vp": 0, "capacidad": 2},),
    ("Juana de Lara (2)",                                               {"semaforo": False, "zona": "residencial", "vp": 0, "capacidad": 2},),
    ("Juana de Lara (3)",                                               {"semaforo": False, "zona": "residencial", "vp": 0, "capacidad": 2},),
    ("Juana de Lara (4)",                                               {"semaforo": False, "zona": "residencial", "vp": 0, "capacidad": 2},),
    ("Juana de Lara (5)",                                               {"semaforo": False, "zona": "residencial", "vp": 0, "capacidad": 2},),
    ("Juana de Lara (6)",                                               {"semaforo": False, "zona": "residencial", "vp": 0, "capacidad": 2},),
    ("Juana de Lara (8)",                                               {"semaforo": False, "zona": "residencial", "vp": 0, "capacidad": 2},),
    ("Juana de Lara (9)",                                               {"semaforo": False, "zona": "residencial", "vp": 0, "capacidad": 2},),
    ("Juana de Lara y L. Scosceria",                                    {"semaforo": False, "zona": "residencial", "vp": 0, "capacidad": 2},),
    ("Juana de Lara y Peat. La Revendedora",                            {"semaforo": False, "zona": "residencial", "vp": 0, "capacidad": 2},),
    ("Juana de Lara y Prof. Clementina Irrazabal Barboza",              {"semaforo": False, "zona": "residencial", "vp": 0, "capacidad": 2},),
    ("Juana de Lara y Sor Graciela Estigarribia",                       {"semaforo": False, "zona": "residencial", "vp": 0, "capacidad": 2},),
    ("L. Scosceria y Prof. Clementina Irrazabal Barboza",               {"semaforo": False, "zona": "residencial", "vp": 0, "capacidad": 2},),
    ("Peat. La Revendedora",                                            {"semaforo": False, "zona": "residencial", "vp": 0, "capacidad": 2},),
    ("Peat. La Revendedora y Prof. Clementina Irrazabal Barboza",       {"semaforo": False, "zona": "residencial", "vp": 0, "capacidad": 2},),
    ("Prof. Alberto Delvalle",                                          {"semaforo": False, "zona": "residencial", "vp": 0, "capacidad": 2},),
    ("Prof. Alberto Delvalle (2)",                                      {"semaforo": False, "zona": "residencial", "vp": 0, "capacidad": 2},),
    ("Prof. Alberto Delvalle (3)",                                      {"semaforo": False, "zona": "residencial", "vp": 0, "capacidad": 2},),
    ("Prof. Alberto Delvalle y Prof. Clementina Irrazabal Barboza",     {"semaforo": False, "zona": "residencial", "vp": 0, "capacidad": 2},),
    ("Prof. Clementina Irrazabal Barboza (2)",                          {"semaforo": False, "zona": "residencial", "vp": 0, "capacidad": 2},),
    ("Prof. Clementina Irrazabal Barboza (3)",                          {"semaforo": False, "zona": "residencial", "vp": 0, "capacidad": 2},),
    ("Prof. Clementina Irrazabal Barboza (4)",                          {"semaforo": False, "zona": "residencial", "vp": 0, "capacidad": 2},),
    ("Prof. Clementina Irrazabal Barboza (5)",                          {"semaforo": False, "zona": "residencial", "vp": 0, "capacidad": 2},),
    ("Prof. Clementina Irrazabal Barboza (6)",                          {"semaforo": False, "zona": "residencial", "vp": 0, "capacidad": 2},),
    ("Prof. Clementina Irrazabal Barboza (7)",                          {"semaforo": False, "zona": "residencial", "vp": 0, "capacidad": 2},),
    ("Prof. Clementina Irrazabal Barboza (8)",                          {"semaforo": False, "zona": "residencial", "vp": 0, "capacidad": 2},),
    ("Prof. Clementina Irrazabal Barboza (9)",                          {"semaforo": False, "zona": "residencial", "vp": 0, "capacidad": 2},),
    ("Prof. Clementina Irrazabal Barboza y Sor Graciela Estigarribia",  {"semaforo": False, "zona": "residencial", "vp": 0, "capacidad": 2},),
    ("Próceres de Mayo",                                                {"semaforo": False, "zona": "residencial", "vp": 0, "capacidad": 2},),
    ("Próceres de Mayo y Tte. Arzamendia Samaniego",                    {"semaforo": False, "zona": "residencial", "vp": 0, "capacidad": 2},),
    ("Sor Graciela Estigarribia",                                       {"semaforo": False, "zona": "residencial", "vp": 0, "capacidad": 2},),
    ("Tte. Arzamendia Samaniego",                                       {"semaforo": False, "zona": "residencial", "vp": 0, "capacidad": 2},),
    ("Tte. Arzamendia Samaniego (2)",                                   {"semaforo": False, "zona": "residencial", "vp": 0, "capacidad": 2},),
    ("Vía 1",                                                           {"semaforo": False, "zona": "residencial", "vp": 0, "capacidad": 2},),
    ("nodo_(-55.84467, ",                                               {"semaforo": False, "zona": "residencial", "vp": 0, "capacidad": 2},),
    ("nodo_(-55.84488, ",                                               {"semaforo": False, "zona": "residencial", "vp": 0, "capacidad": 2},),
    ("nodo_(-55.84506, ",                                               {"semaforo": False, "zona": "residencial", "vp": 0, "capacidad": 2},),
    ("nodo_(-55.84541, ",                                               {"semaforo": False, "zona": "residencial", "vp": 0, "capacidad": 2},),
    ("nodo_(-55.84673, ",                                               {"semaforo": False, "zona": "residencial", "vp": 0, "capacidad": 2},),
    ("nodo_(-55.84688, ",                                               {"semaforo": False, "zona": "residencial", "vp": 0, "capacidad": 2},),
    ("nodo_(-55.84716, ",                                               {"semaforo": False, "zona": "residencial", "vp": 0, "capacidad": 2},),
    ("nodo_(-55.84717, ",                                               {"semaforo": False, "zona": "residencial", "vp": 0, "capacidad": 2},),
    ("nodo_(-55.84725, ",                                               {"semaforo": False, "zona": "residencial", "vp": 0, "capacidad": 2},),
    ("nodo_(-55.84735, ",                                               {"semaforo": False, "zona": "residencial", "vp": 0, "capacidad": 2},),
    ("nodo_(-55.84738, ",                                               {"semaforo": False, "zona": "residencial", "vp": 0, "capacidad": 2},),
    ("nodo_(-55.8475, -",                                               {"semaforo": False, "zona": "residencial", "vp": 0, "capacidad": 2},),
    ("nodo_(-55.84807, ",                                               {"semaforo": False, "zona": "residencial", "vp": 0, "capacidad": 2},),
    ("nodo_(-55.8481, -",                                               {"semaforo": False, "zona": "residencial", "vp": 0, "capacidad": 2},),
    ("nodo_(-55.8481, - (2)",                                           {"semaforo": False, "zona": "residencial", "vp": 0, "capacidad": 2},),
    ("nodo_(-55.84862, ",                                               {"semaforo": False, "zona": "residencial", "vp": 0, "capacidad": 2},),
    ("nodo_(-55.84887, ",                                               {"semaforo": False, "zona": "residencial", "vp": 0, "capacidad": 2},),
    ("nodo_(-55.84925, ",                                               {"semaforo": False, "zona": "residencial", "vp": 0, "capacidad": 2},),
    ("nodo_(-55.84946, ",                                               {"semaforo": False, "zona": "residencial", "vp": 0, "capacidad": 2},),
    ("nodo_(-55.84961, ",                                               {"semaforo": False, "zona": "residencial", "vp": 0, "capacidad": 2},),
    ("nodo_(-55.8503, -",                                               {"semaforo": False, "zona": "residencial", "vp": 0, "capacidad": 2},),
    ("nodo_(-55.85042, ",                                               {"semaforo": False, "zona": "residencial", "vp": 0, "capacidad": 2},),
    ("nodo_(-55.85045, ",                                               {"semaforo": False, "zona": "residencial", "vp": 0, "capacidad": 2},),
    ("nodo_(-55.85138, ",                                               {"semaforo": False, "zona": "residencial", "vp": 0, "capacidad": 2},),
    ("nodo_(-55.85173, ",                                               {"semaforo": False, "zona": "residencial", "vp": 0, "capacidad": 2},),
    ("nodo_(-55.85182, ",                                               {"semaforo": False, "zona": "residencial", "vp": 0, "capacidad": 2},),
    ("nodo_(-55.85215, ",                                               {"semaforo": False, "zona": "residencial", "vp": 0, "capacidad": 2},),
    ("nodo_(-55.85282, ",                                               {"semaforo": False, "zona": "residencial", "vp": 0, "capacidad": 2},),
    ("nodo_(-55.85334, ",                                               {"semaforo": False, "zona": "residencial", "vp": 0, "capacidad": 2},),
]
# capacidad_total = 344

node_position = {
    'Ab. Mercedes Sandoval y Av. Moisés Bertoni'                       : (  0.11638295,   0.39406618),
    'Ab. Nelson González Maya y Av. San Roque'                         : ( -0.36329346,   0.40141725),
    'Av. Moisés Bertoni'                                               : (  0.42970867,   0.76057114),
    'Av. Moisés Bertoni (2)'                                           : (  0.34954588,   0.63786967),
    'Av. Moisés Bertoni (3)'                                           : (  0.27208298,   0.54397932),
    'Av. Moisés Bertoni (4)'                                           : (  0.23172366,   0.51598381),
    'Av. Moisés Bertoni (5)'                                           : (  0.32425431,   0.59797898),
    'Av. Moisés Bertoni (6)'                                           : (  0.48172118,   0.72671807),
    'Av. Moisés Bertoni (7)'                                           : (  0.38603405,   0.66610880),
    'Av. Moisés Bertoni y Peat. La Revendedora'                        : (  0.15547174,   0.42335395),
    'Av. Moisés Bertoni y Prof. Alberto Delvalle'                      : (  0.01063080,   0.26993475),
    'Av. Moisés Bertoni y Sor Graciela Estigarribia'                   : (  0.20712690,   0.47786205),
    'Av. Perimetral'                                                   : (  0.19827287,   1.00000000),
    'Av. Perimetral (2)'                                               : (  0.42899399,   0.77556987),
    'Av. Perimetral y Don Carlos González Arias'                       : (  0.33363442,   0.89357893),
    'Av. San Roque'                                                    : ( -0.15467765,   0.03230658),
    'Av. San Roque (2)'                                                : ( -0.18640131,   0.21589272), 
    'Av. San Roque (3)'                                                : ( -0.45777954,  -0.54749597),
    'Av. San Roque (4)'                                                : ( -0.30273463,  -0.29777138),
    'Av. San Roque (5)'                                                : ( -0.59299221,  -0.78222185),
    'Av. San Roque (6)'                                                : ( -0.52982282,  -0.67231591),
    'Av. San Roque y C.M. Pérez Lizzandro'                             : ( -0.42443794,  -0.49664223),
    'Av. San Roque y D. Moreno Ocampo'                                 : ( -0.37767631,  -0.41617236),
    'Av. San Roque y Don Carlos González Arias'                        : ( -0.23856271,   0.28761334),
    'Av. San Roque y Próceres de Mayo'                                 : ( -0.21413470,  -0.13295483),
    'Av. San Roque y San José'                                         : ( -0.57321951,   0.56844759),
    'Av. San Roque y Vía 1'                                            : ( -0.57625689,  -0.75161003),
    'Rot. Av. Moisés Bertoni'                                          : (  0.47471033,   0.76828561),
    'Rot. San Roque González'                                          : ( -0.10615614,   0.16302326),
    'Ab. Serafina Dávalos y Av. Padre Juan Von Winckel'                : (  0.19716115,  -0.07907169),
    'Av. Padre Juan Von Winckel'                                       : (  0.80740483,  -0.68528091),
    'Av. Padre Juan Von Winckel (2)'                                   : (  0.61385677,  -0.48197187),
    'Av. Padre Juan Von Winckel (3)'                                   : (  0.65302496,  -0.93449708),
    'Av. Padre Juan Von Winckel (4)'                                   : (  0.73392228,  -0.80520719),
    'Av. Padre Juan Von Winckel (5)'                                   : (  0.37924463,  -0.21042708),
    'Av. Padre Juan Von Winckel (6)'                                   : (  0.32147501,  -0.18627659),
    'Av. Padre Juan Von Winckel (7)'                                   : (  0.71083428,  -1.00000000),
    'Av. Padre Juan Von Winckel y Juana de Lara'                       : (  0.30631793,  -0.16195661),
    'Av. Padre Juan Von Winckel y Prof. Clementina Irrazabal Barboza'  : (  0.08702169,   0.01238243),
    'Ab. Serafina Dávalos (5)'                                         : (  0.08672391,  -0.20608423),
    'Ab. Serafina Dávalos y Juan Brítez'                               : ( -0.14618095,  -0.47394289),
    'Juan Brítez y Prof. Clementina Irrazabal Barboza'                 : ( -0.26231575,  -0.38776375),
    'Juana de Lara (7)'                                                : (  0.19666485,  -0.28368359),
    'Juana de Lara y Juan Brítez'                                      : ( -0.03437391,  -0.55711380),
    'Prof. Clementina Irrazabal Barboza'                               : ( -0.02810065,  -0.11899415),
    'Ab. Mercedes Sandoval'                                            : ( -0.37120453,   0.72652741),
    'Ab. Mercedes Sandoval (2)'                                        : (  0.20502258,   0.32054487),
    'Ab. Mercedes Sandoval (3)'                                        : ( -1.00000000,   0.84980086),
    'Ab. Mercedes Sandoval y Ab. Nelson González Maya'                 : ( -0.15070723,   0.62670536),
    'Ab. Mercedes Sandoval y Ab. Serafina Dávalos'                     : (  0.39697255,   0.15108889),
    'Ab. Mercedes Sandoval y Don Carlos González Arias'                : ( -0.02343541,   0.51319803),
    'Ab. Mercedes Sandoval y Juana de Lara'                            : (  0.50103727,   0.05747394),
    'Ab. Mercedes Sandoval y Prof. Clementina Irrazabal Barboza'       : (  0.29068440,   0.24720363),
    'Ab. Mercedes Sandoval y San José'                                 : ( -0.53301901,   0.75644013),
    'Ab. Nelson González Maya'                                         : ( -0.25471239,   0.51639692),
    'Ab. Serafina Dávalos'                                             : ( -0.45601271,  -0.81683756),
    'Ab. Serafina Dávalos (2)'                                         : (  0.74865254,   0.53993306),
    'Ab. Serafina Dávalos (3)'                                         : (  0.62342548,   0.40358868),
    'Ab. Serafina Dávalos (4)'                                         : (  0.79550350,   0.58889077),
    'Ab. Serafina Dávalos (6)'                                         : (  0.50973249,   0.27754004),
    'Ab. Serafina Dávalos (7)'                                         : (  0.36824656,   0.11710872),
    'Ab. Serafina Dávalos (8)'                                         : (  0.69814879,   0.48747987),
    'Ab. Serafina Dávalos (9)'                                         : (  0.65161546,   0.43521735),
    'Ab. Serafina Dávalos y C.M. Pérez Lizzandro'                      : ( -0.27144771,  -0.61804084),
    'Ab. Serafina Dávalos y C.N. Pérez Lizzardo'                       : ( -0.32052211,  -0.67695534),
    'Ab. Serafina Dávalos y Juana de Lara'                             : (  0.84662266,   0.64390730),
    'Ab. Serafina Dávalos y L. Scosceria'                              : ( -0.02210532,  -0.33259893),
    'Ab. Serafina Dávalos y Peat. La Revendedora'                      : (  0.43123728,   0.18782307),
    'Ab. Serafina Dávalos y Sor Graciela Estigarribia'                 : (  0.47923966,   0.24173799),
    'C.M. Pérez Lizzandro y C.N. Pérez Lizzardo'                       : ( -0.39298228,  -0.53296331),
    'C.M. Pérez Lizzandro y Juana de Lara'                             : ( -0.16325376,  -0.70608423),
    'C.N. Pérez Lizzardo'                                              : ( -0.28431188,  -0.75167359),
    'C.N. Pérez Lizzardo y Juana de Lara'                              : ( -0.23936672,  -0.79688162),
    'D. Moreno Ocampo'                                                 : ( -0.40491340,  -0.40121600),
    'D. Moreno Ocampo y Tte. Arzamendia Samaniego'                     : ( -0.69392029,  -0.24548767),
    'Don Carlos González Arias'                                        : ( -0.20243188,   0.30903101),
    'Juana de Lara'                                                    : (  0.95263289,   0.58675112),
    'Juana de Lara (10)'                                               : (  0.84130230,   0.45557580),
    'Juana de Lara (11)'                                               : (  0.57492680,   0.73012880),
    'Juana de Lara (2)'                                                : (  0.52015485,   0.77823913),
    'Juana de Lara (3)'                                                : (  0.88704154,   0.50955428),
    'Juana de Lara (4)'                                                : (  0.61167304,   0.18782307),
    'Juana de Lara (5)'                                                : (  0.79731004,   0.40363105),
    'Juana de Lara (6)'                                                : (  0.47495161,   0.02669265),
    'Juana de Lara (8)'                                                : (  0.75115390,   0.34916532),
    'Juana de Lara (9)'                                                : (  0.72336096,   0.31668926),
    'Juana de Lara y L. Scosceria'                                     : (  0.08827237,  -0.41532497),
    'Juana de Lara y Peat. La Revendedora'                             : (  0.53276093,   0.09547920),
    'Juana de Lara y Prof. Clementina Irrazabal Barboza'               : (  0.70944464,   0.68900941),
    'Juana de Lara y Sor Graciela Estigarribia'                        : (  0.58131917,   0.15227523),
    'L. Scosceria y Prof. Clementina Irrazabal Barboza'                : ( -0.13359472,  -0.24474621),
    'Peat. La Revendedora'                                             : (  0.23692491,   0.35395305),
    'Peat. La Revendedora y Prof. Clementina Irrazabal Barboza'        : (  0.32375800,   0.28362003),
    'Prof. Alberto Delvalle'                                           : (  0.05897067,   0.23438692),
    'Prof. Alberto Delvalle (2)'                                       : (  0.09377140,   0.20881705),
    'Prof. Alberto Delvalle (3)'                                       : (  0.03546578,   0.25167359),
    'Prof. Alberto Delvalle y Prof. Clementina Irrazabal Barboza'      : (  0.19053055,   0.13270062),
    'Prof. Clementina Irrazabal Barboza (2)'                           : (  0.55662316,   0.52218032),
    'Prof. Clementina Irrazabal Barboza (3)'                           : (  0.44088540,   0.40295314),
    'Prof. Clementina Irrazabal Barboza (4)'                           : (  0.40630304,   0.36910008),
    'Prof. Clementina Irrazabal Barboza (5)'                           : (  0.64957070,   0.62073129),
    'Prof. Clementina Irrazabal Barboza (6)'                           : (  0.52388704,   0.48826371),
    'Prof. Clementina Irrazabal Barboza (7)'                           : (  0.49543898,   0.45926193),
    'Prof. Clementina Irrazabal Barboza (8)'                           : (  0.59996030,   0.57033302),
    'Prof. Clementina Irrazabal Barboza (9)'                           : (  0.26114447,   0.21309635),
    'Prof. Clementina Irrazabal Barboza y Sor Graciela Estigarribia'   : (  0.37326914,   0.33567071),
    'Próceres de Mayo'                                                 : ( -0.32058167,  -0.07776883),
    'Próceres de Mayo y Tte. Arzamendia Samaniego'                     : ( -0.50752229,   0.01355111),
    'Sor Graciela Estigarribia'                                        : (  0.28818304,   0.40744428),
    'Tte. Arzamendia Samaniego'                                        : ( -0.91650206,  -0.37001102),
    'Tte. Arzamendia Samaniego (2)'                                    : ( -0.59529505,  -0.12992543),
    'Vía 1'                                                            : ( -0.69922081,  -0.79965681),
    'nodo_(-55.84467, '                                                : (  1.00000000,   0.45269469),
    'nodo_(-55.84488, '                                                : (  0.95884659,  -0.44610626),
    'nodo_(-55.84506, '                                                : (  0.92168346,  -0.77948903),
    'nodo_(-55.84541, '                                                : (  0.85263785,  -0.88742479),
    'nodo_(-55.84673, '                                                : (  0.59092759,  -0.86075333),
    'nodo_(-55.84688, '                                                : (  0.56128840,   0.69794933),
    'nodo_(-55.84716, '                                                : (  0.50566281,   0.73743751),
    'nodo_(-55.84717, '                                                : (  0.50310189,   0.65331328),
    'nodo_(-55.84725, '                                                : (  0.48785548,   0.61643081),
    'nodo_(-55.84735, '                                                : (  0.46826145,   0.59535209),
    'nodo_(-55.84738, '                                                : (  0.46226612,  -0.71379544),
    'nodo_(-55.8475, -'                                                : (  0.43766936,   0.56342683),
    'nodo_(-55.84807, '                                                : (  0.32558440,   0.75618592),
    'nodo_(-55.8481, -'                                                : (  0.31988684,   0.44174223),
    'nodo_(-55.8481, - (2)'                                            : (  0.31970817,  -0.54847047),
    'nodo_(-55.84862, '                                                : (  0.21679488,   0.74608084),
    'nodo_(-55.84887, '                                                : (  0.16585438,   0.58056521),
    'nodo_(-55.84925, '                                                : (  0.08984069,   0.82041776),
    'nodo_(-55.84946, '                                                : (  0.04989826,  -0.74586899),
    'nodo_(-55.84961, '                                                : (  0.01970321,   0.80539785),
    'nodo_(-55.8503, -'                                                : ( -0.11735570,  -0.06128718),
    'nodo_(-55.85042, '                                                : ( -0.14131719,   0.25800780),
    'nodo_(-55.85045, '                                                : ( -0.14723311,  -0.92769681),
    'nodo_(-55.85138, '                                                : ( -0.33265174,  -0.28294212),
    'nodo_(-55.85173, '                                                : ( -0.40185617,  -0.91784595),
    'nodo_(-55.85182, '                                                : ( -0.41946499,  -0.88500974),
    'nodo_(-55.85215, '                                                : ( -0.48469899,  -0.53156512),
    'nodo_(-55.85282, '                                                : ( -0.61768822,  -0.71714262),
    'nodo_(-55.85334, '                                                : ( -0.72155442,  -0.34645369),
}

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
        "Av. Moisés Bertoni (2)", "Av. Moisés Bertoni (4)", 
        {"vel_max": 60, "carriles": 2, "vehi_calle": 0, "weight": 87}
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
        "Av. Moisés Bertoni (4)", "Ab. Mercedes Sandoval y Av. Moisés Bertoni", 
        {"vel_max": 60, "carriles": 2, "vehi_calle": 0, "weight": 86}
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
        "Av. Padre Juan Von Winckel", "nodo_(-55.84488, ", 
        {"vel_max": 30, "carriles": 1, "vehi_calle": 0, "weight": 146}
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
        "Av. San Roque", "Av. San Roque y Próceres de Mayo", 
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