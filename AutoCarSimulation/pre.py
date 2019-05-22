#!/usr/bin/env python

###
### This file is generated automatically by SALOME v9.2.1 with dump python functionality
###
import os
import sys
import salome

salome.salome_init()
import salome_notebook
notebook = salome_notebook.NoteBook()
sys.path.insert(0,os.environ['path'])

###
### GEOM component
###

import GEOM
from salome.geom import geomBuilder
import math
import SALOMEDS

print("STO FACENDO LE GEOMETRIE")
geompy = geomBuilder.New()

O = geompy.MakeVertex(0, 0, 0)
OX = geompy.MakeVectorDXDYDZ(1, 0, 0)
OY = geompy.MakeVectorDXDYDZ(0, 1, 0)
OZ = geompy.MakeVectorDXDYDZ(0, 0, 1)
Test_Car_3 = geompy.ImportSTEP(os.environ['path']+r'/CAD/car.stp', False, True)
tetto = geompy.CreateGroup(Test_Car_3, geompy.ShapeType["FACE"])
geompy.UnionIDs(tetto, [244, 623, 442, 1723, 1481, 2057, 613, 1501, 1506, 1687, 1871, 478, 202, 1682, 237, 1657, 1476, 1861, 2050, 1652, 809, 407, 251, 802, 412, 1677, 618, 608, 432, 209, 1866, 437, 1511, 2040, 1856, 2045, 427, 1486, 1662, 1720, 417, 216, 475, 230, 1672, 1496, 1667, 422, 1491, 223, 1132, 2260, 797, 1014, 2249, 2242, 994, 1008, 2380, 792, 2256, 1001, 2262, 1011, 1466, 402, 1471, 1647, 195, 188, 397, 984, 1123, 598, 603, 989, 787, 1128, 1118, 782, 979, 1851, 2232, 1846, 2227, 2376, 2035, 2237, 2366, 2030, 2371, 1637, 1461, 392, 974, 1642, 593, 777, 181, 1113, 1841, 2222, 2361, 2025, 1456, 1627, 588, 387, 1831, 583, 382, 1451, 969, 1632, 772, 1110, 2013, 2020, 2217, 174, 1836, 167, 963, 2214, 765, 2204, 956, 967, 2211, 760, 949, 160, 2008, 1826, 1622, 377, 2197, 578, 1446, 2358])
[geomObj_1,geomObj_2,geomObj_3,geomObj_4,geomObj_5,geomObj_6,geomObj_7,geomObj_8,geomObj_9,geomObj_10,geomObj_11,geomObj_12,geomObj_13,geomObj_14,geomObj_15,geomObj_16,geomObj_17,geomObj_18,geomObj_19,geomObj_20,geomObj_21,geomObj_22,geomObj_23,geomObj_24,geomObj_25,geomObj_26,geomObj_27,geomObj_28,geomObj_29,geomObj_30,geomObj_31,geomObj_32,geomObj_33,geomObj_34,geomObj_35,geomObj_36,geomObj_37,geomObj_38,geomObj_39,geomObj_40,geomObj_41,geomObj_42,geomObj_43,geomObj_44,geomObj_45,geomObj_46,geomObj_47,geomObj_48,geomObj_49,geomObj_50,geomObj_51,geomObj_52,geomObj_53,geomObj_54,geomObj_55,geomObj_56,geomObj_57,geomObj_58,geomObj_59,geomObj_60,geomObj_61,geomObj_62,geomObj_63,geomObj_64,geomObj_65,geomObj_66,geomObj_67,geomObj_68,geomObj_69,geomObj_70,geomObj_71,geomObj_72,geomObj_73,geomObj_74,geomObj_75,geomObj_76,geomObj_77,geomObj_78,geomObj_79,geomObj_80,geomObj_81,geomObj_82,geomObj_83,geomObj_84,geomObj_85,geomObj_86,geomObj_87,geomObj_88,geomObj_89,geomObj_90,geomObj_91,geomObj_92,geomObj_93,geomObj_94,geomObj_95,geomObj_96,geomObj_97,geomObj_98,geomObj_99,geomObj_100,geomObj_101,geomObj_102,geomObj_103,geomObj_104,geomObj_105,geomObj_106,geomObj_107,geomObj_108,geomObj_109,geomObj_110,geomObj_111,geomObj_112,geomObj_113,geomObj_114,geomObj_115,geomObj_116,geomObj_117,geomObj_118,geomObj_119,geomObj_120,geomObj_121,geomObj_122,geomObj_123,geomObj_124,geomObj_125,geomObj_126,geomObj_127,geomObj_128,geomObj_129,geomObj_130,geomObj_131,geomObj_132,geomObj_133,geomObj_134,geomObj_135,geomObj_136,geomObj_137,geomObj_138,geomObj_139,geomObj_140] = geompy.SubShapeAll(tetto, geompy.ShapeType["FACE"])
lato = geompy.CreateGroup(Test_Car_3, geompy.ShapeType["FACE"])
geompy.UnionIDs(lato, [1324, 1287, 1167, 1241, 1330, 1244, 1327, 1203, 1213, 1230, 1218, 1284, 1274, 1238, 1235, 1225, 1304, 1247, 1299, 1294, 1314, 1254, 1208, 1259, 1309, 1279, 1264, 1269, 1319, 1333, 1198, 1162, 2562, 2547, 2557, 2581, 2572, 2575, 2535, 2542, 2552, 2527, 2489, 2532, 2451, 2492, 2578, 2461, 2456, 2567, 2522, 2495, 2507, 2512, 2502, 2478, 2473, 2486, 2483, 2466, 2446, 2415, 2410])
resto = geompy.CreateGroup(Test_Car_3, geompy.ShapeType["FACE"])
geompy.UnionIDs(resto, [2, 12, 19, 26, 31, 38, 43, 50, 55, 62, 69, 76, 83, 90, 97, 104, 111, 118, 125, 132, 139, 146, 153, 258, 265, 272, 279, 286, 293, 300, 304, 309, 314, 319, 324, 329, 334, 339, 342, 347, 352, 357, 362, 367, 372, 447, 452, 457, 462, 467, 472, 481, 488, 493, 498, 503, 508, 513, 518, 523, 528, 533, 538, 543, 548, 553, 558, 563, 568, 573, 628, 633, 638, 643, 648, 651, 654, 661, 666, 671, 678, 683, 688, 693, 698, 703, 708, 713, 718, 725, 730, 735, 740, 745, 750, 755, 814, 819, 822, 829, 834, 839, 846, 851, 856, 859, 864, 869, 874, 879, 884, 889, 894, 901, 908, 912, 914, 919, 924, 929, 934, 939, 944, 1019, 1022, 1027, 1032, 1037, 1042, 1047, 1052, 1057, 1062, 1067, 1072, 1075, 1080, 1085, 1090, 1095, 1100, 1105, 1134, 1139, 1144, 1149, 1154, 1157, 1172, 1177, 1182, 1187, 1190, 1195, 1335, 1342, 1347, 1352, 1359, 1364, 1371, 1376, 1381, 1386, 1391, 1396, 1401, 1406, 1411, 1416, 1421, 1426, 1431, 1436, 1441, 1516, 1521, 1526, 1531, 1536, 1541, 1546, 1549, 1554, 1559, 1564, 1569, 1574, 1579, 1584, 1587, 1592, 1597, 1602, 1607, 1612, 1617, 1692, 1697, 1702, 1707, 1712, 1717, 1726, 1733, 1740, 1746, 1751, 1756, 1761, 1766, 1771, 1776, 1781, 1786, 1791, 1796, 1801, 1806, 1811, 1816, 1821, 1876, 1881, 1886, 1891, 1896, 1899, 1902, 1909, 1914, 1919, 1926, 1931, 1936, 1941, 1946, 1951, 1956, 1961, 1966, 1973, 1978, 1983, 1988, 1993, 1998, 2003, 2062, 2067, 2070, 2077, 2082, 2087, 2094, 2099, 2104, 2107, 2112, 2117, 2122, 2127, 2132, 2137, 2142, 2149, 2156, 2159, 2162, 2167, 2172, 2177, 2182, 2187, 2192, 2267, 2270, 2275, 2280, 2285, 2290, 2295, 2300, 2305, 2310, 2315, 2320, 2323, 2328, 2333, 2338, 2343, 2348, 2353, 2382, 2387, 2392, 2397, 2402, 2405, 2420, 2425, 2430, 2435, 2438, 2443, 2517, 2583, 2586])
Solid_1 = geompy.MakeSolid([Test_Car_3])
tetto_1 = geompy.CreateGroup(Solid_1, geompy.ShapeType["FACE"])
geompy.UnionIDs(tetto_1, [245, 624, 443, 1724, 1482, 2058, 614, 1502, 1507, 1688, 1872, 479, 203, 1683, 238, 1658, 1477, 1862, 2051, 1653, 810, 408, 252, 803, 413, 1678, 619, 609, 433, 210, 1867, 438, 1512, 2041, 1857, 2046, 428, 1487, 1663, 1721, 418, 217, 476, 231, 1673, 1497, 1668, 423, 1492, 224, 1133, 2261, 798, 1015, 2250, 2243, 995, 1009, 2381, 793, 2257, 1002, 2263, 1012, 1467, 403, 1472, 1648, 196, 189, 398, 985, 1124, 599, 604, 990, 788, 1129, 1119, 783, 980, 1852, 2233, 1847, 2228, 2377, 2036, 2238, 2367, 2031, 2372, 1638, 1462, 393, 975, 1643, 594, 778, 182, 1114, 1842, 2223, 2362, 2026, 1457, 1628, 589, 388, 1832, 584, 383, 1452, 970, 1633, 773, 1111, 2014, 2021, 2218, 175, 1837, 168, 964, 2215, 766, 2205, 957, 968, 2212, 761, 950, 161, 2009, 1827, 1623, 378, 2198, 579, 1447, 2359])
lato_1 = geompy.CreateGroup(Solid_1, geompy.ShapeType["FACE"])
geompy.UnionIDs(lato_1, [1325, 1288, 1168, 1242, 1331, 1245, 1328, 1204, 1214, 1231, 1219, 1285, 1275, 1239, 1236, 1226, 1305, 1248, 1300, 1295, 1315, 1255, 1209, 1260, 1310, 1280, 1265, 1270, 1320, 1334, 1199, 1163, 2563, 2548, 2558, 2582, 2573, 2576, 2536, 2543, 2553, 2528, 2490, 2533, 2452, 2493, 2579, 2462, 2457, 2568, 2523, 2496, 2508, 2513, 2503, 2479, 2474, 2487, 2484, 2467, 2447, 2416, 2411])
Group_3 = geompy.CreateGroup(Solid_1, geompy.ShapeType["FACE"])
geompy.UnionIDs(Group_3, [3, 13, 20, 27, 32, 39, 44, 51, 56, 63, 70, 77, 84, 91, 98, 105, 112, 119, 126, 133, 140, 147, 154, 259, 266, 273, 280, 287, 294, 301, 305, 310, 315, 320, 325, 330, 335, 340, 343, 348, 353, 358, 363, 368, 373, 448, 453, 458, 463, 468, 473, 482, 489, 494, 499, 504, 509, 514, 519, 524, 529, 534, 539, 544, 549, 554, 559, 564, 569, 574, 629, 634, 639, 644, 649, 652, 655, 662, 667, 672, 679, 684, 689, 694, 699, 704, 709, 714, 719, 726, 731, 736, 741, 746, 751, 756, 815, 820, 823, 830, 835, 840, 847, 852, 857, 860, 865, 870, 875, 880, 885, 890, 895, 902, 909, 913, 915, 920, 925, 930, 935, 940, 945, 1020, 1023, 1028, 1033, 1038, 1043, 1048, 1053, 1058, 1063, 1068, 1073, 1076, 1081, 1086, 1091, 1096, 1101, 1106, 1135, 1140, 1145, 1150, 1155, 1158, 1173, 1178, 1183, 1188, 1191, 1196, 1336, 1343, 1348, 1353, 1360, 1365, 1372, 1377, 1382, 1387, 1392, 1397, 1402, 1407, 1412, 1417, 1422, 1427, 1432, 1437, 1442, 1517, 1522, 1527, 1532, 1537, 1542, 1547, 1550, 1555, 1560, 1565, 1570, 1575, 1580, 1585, 1588, 1593, 1598, 1603, 1608, 1613, 1618, 1693, 1698, 1703, 1708, 1713, 1718, 1727, 1734, 1741, 1747, 1752, 1757, 1762, 1767, 1772, 1777, 1782, 1787, 1792, 1797, 1802, 1807, 1812, 1817, 1822, 1877, 1882, 1887, 1892, 1897, 1900, 1903, 1910, 1915, 1920, 1927, 1932, 1937, 1942, 1947, 1952, 1957, 1962, 1967, 1974, 1979, 1984, 1989, 1994, 1999, 2004, 2063, 2068, 2071, 2078, 2083, 2088, 2095, 2100, 2105, 2108, 2113, 2118, 2123, 2128, 2133, 2138, 2143, 2150, 2157, 2160, 2163, 2168, 2173, 2178, 2183, 2188, 2193, 2268, 2271, 2276, 2281, 2286, 2291, 2296, 2301, 2306, 2311, 2316, 2321, 2324, 2329, 2334, 2339, 2344, 2349, 2354, 2383, 2388, 2393, 2398, 2403, 2406, 2421, 2426, 2431, 2436, 2439, 2444, 2518, 2584, 2587])
resto.SetColor(SALOMEDS.Color(0.333333,0,1))
tetto.SetColor(SALOMEDS.Color(0.666667,0.333333,0))
lato.SetColor(SALOMEDS.Color(0.333333,1,0.498039))
geompy.addToStudy( O, 'O' )
geompy.addToStudy( OX, 'OX' )
geompy.addToStudy( OY, 'OY' )
geompy.addToStudy( OZ, 'OZ' )
geompy.addToStudy( Test_Car_3, 'Test Car 3' )
geompy.addToStudyInFather( Test_Car_3, tetto, 'tetto' )
geompy.addToStudyInFather( Test_Car_3, lato, 'lato' )
geompy.addToStudyInFather( Test_Car_3, resto, 'resto' )
geompy.addToStudy( Solid_1, 'Solid_1' )
geompy.addToStudyInFather( Solid_1, tetto_1, 'tetto' )
geompy.addToStudyInFather( Solid_1, lato_1, 'lato' )
geompy.addToStudyInFather( Solid_1, Group_3, 'Group_3' )

print("HO FINITO DI FARE I SOLIDI ORA VADO IN MESH")
###
### SMESH component
###

import  SMESH, SALOMEDS
from salome.smesh import smeshBuilder

smesh = smeshBuilder.New()
Mesh_1 = smesh.Mesh(Solid_1)
NETGEN_1D_2D = Mesh_1.Triangle(algo=smeshBuilder.NETGEN_1D2D)
NETGEN_2D_Parameters_1 = NETGEN_1D_2D.Parameters()
NETGEN_2D_Parameters_1.SetSecondOrder( 0 )
NETGEN_2D_Parameters_1.SetOptimize( 1 )
NETGEN_2D_Parameters_1.SetFineness( 2 )
NETGEN_2D_Parameters_1.SetChordalError( 0.1 )
NETGEN_2D_Parameters_1.SetChordalErrorEnabled( 0 )
NETGEN_2D_Parameters_1.SetUseSurfaceCurvature( 1 )
NETGEN_2D_Parameters_1.SetFuseEdges( 1 )
NETGEN_2D_Parameters_1.SetQuadAllowed( 0 )
tetto_2 = Mesh_1.GroupOnGeom(tetto_1,'Group_1',SMESH.FACE)
lato_2 = Mesh_1.GroupOnGeom(lato_1,'Group_2',SMESH.FACE)
altro = Mesh_1.GroupOnGeom(Group_3,'Group_3',SMESH.FACE)
NETGEN_2D_Parameters_1.SetMaxSize( 0.001 )
NETGEN_2D_Parameters_1.SetMinSize( 0.0001 )
NETGEN_2D_Parameters_1.SetLocalSizeOnShape(tetto_1, 0.001)
NETGEN_2D_Parameters_1.SetLocalSizeOnShape(lato_1, 0.0005)
NETGEN_2D_Parameters_1.SetLocalSizeOnShape(Group_3, 0.001)
isDone = Mesh_1.Compute()
[ tetto_2, lato_2, altro ] = Mesh_1.GetGroups()
tetto_2.SetName( 'tetto' )
altro.SetName( 'altro' )
'''
try:
  Mesh_1.ExportSTL( r'/home/daniel/PROVA/STL/tetto.stl', 1, tetto_2)
  pass
except:
  print('ExportPartToSTL() failed. Invalid file name?')
try:
  Mesh_1.ExportSTL( r'/home/daniel/altro.stl', 1, altro)
  pass
except:
  print('ExportPartToSTL() failed. Invalid file name?')
try:
  Mesh_1.ExportSTL( r'/home/daniel/PROVA/STL/lato.stl', 1, lato_2)
  pass
except:
  print('ExportPartToSTL() failed. Invalid file name?')
lato_2.SetName( 'lato' )
try:
  Mesh_1.ExportSTL( r'/home/daniel/PROVA/STL/lato.stl', 1, lato_2)
  pass
except:
  print('ExportPartToSTL() failed. Invalid file name?')
'''

## Set names of Mesh objects
smesh.SetName(NETGEN_1D_2D.GetAlgorithm(), 'NETGEN 1D-2D')
smesh.SetName(NETGEN_2D_Parameters_1, 'NETGEN 2D Parameters_1')
smesh.SetName(tetto_2, 'tetto')
smesh.SetName(lato_2, 'lato')
smesh.SetName(altro, 'altro')
smesh.SetName(Mesh_1.GetMesh(), 'Mesh_1')
print("STO ESPORTANDO GLI STL")
try:
  Mesh_1.ExportSTL(os.environ['path']+r'/STL/tetto.stl', 1, tetto_2)
  pass
except:
  print('ExportPartToSTL() failed. Invalid file name?')
try:
  Mesh_1.ExportSTL(os.environ['path']+r'/STL/altro.stl', 1, altro)
  pass
except:
  print('ExportPartToSTL() failed. Invalid file name?')
try:
  Mesh_1.ExportSTL(os.environ['path']+r'/STL/lato.stl', 1, lato_2)
  pass
except:
  print('ExportPartToSTL() failed. Invalid file name?')
lato_2.SetName( 'lato' )
try:
  Mesh_1.ExportSTL(os.environ['path']+r'/STL/lato.stl', 1, lato_2)
  pass
except:
  print('ExportPartToSTL() failed. Invalid file name?')

if salome.sg.hasDesktop():
  salome.sg.updateObjBrowser()

print("Ho finito bye")
