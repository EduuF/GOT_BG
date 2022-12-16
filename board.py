import igraph as ig

# 12 seas, 38 lands
n_vertices = 50

edges = [
    (1,2), (1,3), (1,39), (1,50),
    (2,1), (2,3), (2,50),
    (3,1), (3,2), (3,4), (3,5), (3,9), (3,39), (3,50),
    (4,3), (4,39),
    (5,3), (5,6), (5,9), (5,49), (5,50),
    (6,5), (6,49), (6,50),
    (7,8), (7,39), (7,40), (7,41),
    (8,7), (8,9), (8,11), (8,39), (8,41),
    (9,3), (9,5), (9,8), (9,11), (9,12), (9,49),
    (10,41),
    (11,8), (11,9), (11,12), (11,16), (11,41),
    (12,9), (12,11), (12,13), (12,14), (12,49),
    (13,12), (13, 14), (13,49),
    (14,12), (14,13), (14,15), (14,20), (14,49),
    (15,14), (15,49),
    (16,11), (16,17), (16,18), (16,19), (16,19), (16,41), (16,42),
    (17,16), (17,18), (17,21), (17,42),
    (18,16), (18, 17), (18,19), (18,21), (18,22),
    (19,16), (19,18), (19,20), (19,22),
    (20,14), (20,19), (20,22), (20,23), (20,47), (20,48), (20,49),
    (21,17), (21,18), (21,22), (21,26), (21,27), (21,40), (21,42), (21,43),
    (22,18), (22,19), (22,20), (22,21), (22,23), (22,26),
    (23,20), (23,22), (23,25), (23,26), (23,48),
    (24,47),
    (25,23), (25,26), (25,32), (25,33), (25,47), (25,48),
    (26,21), (26,22), (26,23), (26,25), (26,27), (26,28), (26,32),
    (27,21), (27,26), (27,28), (27,29), (27,43), (27,44),
    (28,26), (28,27), (28,29), (28,30), (28,31), (28,32),
    (29,27), (29,28), (29,30), (29,44),
    (30,28), (30,29), (30,31), (30,43), (30,44),
    (31,28), (31,30), (31,32), (31,34), (31,35),
    (32,25), (32,26), (32,28), (32,31), (32,33), (32,35), (32,46),
    (33,25), (33,32), (33,45), (33,46), (33,47),
    (34,31), (34,35), (34,37), (34,43), (34,45),
    (35,31), (35,32), (35,34), (35,36), (35,37), (35,46),
    (36,35), (36,37), (36,45), (36,46),
    (37,34), (37,35), (37,36), (37,45),
    (38,43), (38,44),
    (39,1), (39,3), (39,4), (39,7), (39,8), (39,40),
    (40,7), (40,21), (40,39), (40,41), (40,42), (40,43),
    (41,7), (41,8), (41,10), (41,11), (41,16), (41,40), (41,42),
    (42,16), (42,17), (42,21), (42,40), (42,41),
    (43,21), (43,27), (43,30), (43,34), (43,38), (43,40), (43,44), (43,45),
    (44,27), (44,29), (44,30), (44,38), (44,43),
    (45,33), (45,34), (45,36), (45,37), (45,43), (45,46), (45,47),
    (46,32), (46,33), (46,35), (46,36), (46,45),
    (47,20), (47,24), (47,25), (47,33), (47,45), (47,48), (47,49),
    (48,20), (48,23), (48,25), (48,47),
    (49,5), (49,6), (49,9), (49,12), (49,13), (49,14), (49,15), (49,20), (49,47), (49,50),
    (50,1), (50,2), (50,3), (50,5), (50,6), (50,49)

         ]

g = ig.Graph(n_vertices, edges)

# Set attributes for the graph, nodes, and edges
g["title"] = "GOT Map"
g.vs["name"] = ["Castle Black", "Karhold", "Winterfell", "The Stony Shore", "White Harbor", "Widow's Watch",
                "Flint's Finger", "Greywater Watch", "Moat Cailin", "Pyke", "Seagard", "The Twins", "The Fingers",
                "The Mountaisn of the Moon", "The Eyrie", "Riverrun", "Lannisport", "Stoney Sept", "Harrenhal",
                "Crackclaw Point", "Searoad Marches", "Blackwater", "King's Landing", "Dragonstone",
                "Kingswood", "The Reach", "Highgarden", "Dornish Marches", "Oldtown", "Three Towers", "Prince's Pass",
                "The Boneway", "Storm's End", "Starfall", "Yronwood", "Sunspear", "Salt Shore", "The Arbor",
                "Bay of Ice", "Sunset Sea", "Ironman's Bay", "The Golden Sound", "West Summer Sea", "Redwine Straits" , "East Summer Sea",
                "Sea of Dorne", "Shipbreaker Bay", "Blackwater Bay", "The Narrow Sea", "The Shivering Sea"]

g.vs['land'] = [True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True,
                True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True,
                True, True, True, True, True, True, False, False, False, False, False, False, False, False, False,
                False, False, False]

g.vs['port'] = [(False,0), (False,0), (True,39), (False,0), (True,49), (False,0), (False,0), (False,0), (False,0),
                (True,41), (False,0), (False,0), (False,0), (False,0), (False,0), (False,0), (True,42), (False,0),
                (False,0), (False,0), (False,0), (False,0), (False,0), (True,47), (False,0), (False,0), (False,0),
                (False,0), (True,44), (False,0), (False,0), (False,0), (True,47), (False,0), (False,0), (True,45),
                (False,0), (False,0), (False,0), (False,0), (False,0), (False,0), (False,0), (False,0), (False,0),
                (False,0), (False,0), (False,0), (False,0), (False,0)]

g.vs['supply'] = [0,0,1,1,0,1,0,1,0,1,1,0,1,1,1,1,2,0,0,0,1,2,0,1,1,0,2,0,0,1,1,0,0,1,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0]

g.vs['crown'] = [1,1,1,0,0,0,0,0,0,1,1,1,0,0,1,1,0,1,1,0,0,0,2,1,1,0,0,1,0,0,1,1,0,0,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0]

g.vs['castle'] = [(False,0), (False,0), (True,5), (False,0), (False,0), (False,0), (False,0), (False,0), (False,0), (True,5), (True,0), (False,0), (False,0), (False,0),
                  (False,0), (True,0), (True,5), (False,0), (False,0), (False,0), (False,0), (False,0), (True,5), (True,5), (False,0), (False,0), (True,5), (False,0),
                  (True,0), (False,0), (False,0), (False,0), (False,0), (False,0), (False,0), (True,5), (False,0), (False,0), (False,0), (False,0), (False,0), (False,0),
                  (False,0), (False,0), (False,0), (False,0), (False,0), (False,0), (False,0), (False,0)]

g.vs['stronghold'] = [False, False, False, False, True, False, True, False, True, False, False, False, False,
                      False, True, False, False, False, True, True, False, False, False, False, False, True,
                      False, False, False, False, False, False, True, True, True, False, False, False, False,
                      False, False, False, False, False, False, False, False, False, False, False]

