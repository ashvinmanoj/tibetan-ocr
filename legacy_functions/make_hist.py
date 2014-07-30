import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

box_widths = [12, 17, 27, 12, 14, 17, 13, 18, 11, 12, 21, 15, 11, 18, 14, 12, 12, 53, 14, 14, 12, 14, 12, 15, 19, 12, 11, 12, 25, 19, 17, 20, 27, 12, 30, 11, 11, 44, 23, 11, 24, 22, 17, 14, 13, 11, 18, 14, 14, 12, 11, 28, 11, 32, 38, 36, 12, 29, 33, 32, 31, 32, 37, 37, 66, 37, 33, 28, 42, 37, 29, 87, 30, 34, 35, 30, 31, 36, 35, 27, 36, 29, 28, 28, 14, 28, 29, 38, 36, 43, 79, 17, 41, 36, 66, 29, 30, 48, 39, 57, 22, 21, 36, 36, 45, 28, 73, 29, 26, 12, 31, 92, 40, 39, 32, 27, 43, 69, 88, 20, 33, 37, 36, 36, 29, 33, 31, 35, 66, 39, 39, 11, 30, 34, 11, 28, 35, 27, 35, 43, 14, 57, 35, 64, 65, 72, 36, 34, 19, 36, 28, 43, 25, 33, 77, 31, 45, 53, 34, 11, 39, 30, 36, 32, 34, 70, 35, 41, 57, 72, 29, 29, 13, 30, 46, 29, 48, 51, 36, 41, 59, 13, 32, 27, 32, 12, 43, 35, 57, 53, 19, 31, 30, 83, 29, 50, 65, 88, 52, 38, 94, 39, 13, 83, 30, 46, 39, 36, 38, 37, 30, 11, 34, 67, 37, 12, 13, 38, 29, 85, 97, 44, 44, 31, 32, 35, 26, 34, 47, 45, 32, 34, 42, 89, 50, 63, 37, 52, 42, 79, 60, 28, 20, 23, 26, 31, 26, 39, 34, 37, 36, 65, 34, 41, 34, 36, 39, 40, 31, 11, 34, 30, 35, 32, 35, 36, 33, 28, 30, 35, 33, 41, 60, 28, 30, 38, 33, 62, 29, 27, 30, 39, 59, 82, 98, 37, 92, 67, 59, 39, 49, 42, 34, 58, 65, 37, 30, 71, 28, 38, 49, 34, 14, 46, 34, 37, 35, 45, 52, 44, 49, 31, 40, 32, 38, 35, 68, 40, 30, 30, 68, 33, 28, 31, 34, 29, 78, 42, 28, 31, 76, 61, 30, 31, 26, 30, 44, 62, 31, 36, 37, 26, 34, 43, 30, 31, 44, 59, 66, 90, 56, 40, 96, 36, 36, 51, 70, 35, 35, 34, 36, 39, 37, 33, 73, 40, 51, 35, 31, 56, 38, 33, 63, 40, 70, 39, 36, 35, 11, 34, 29, 36, 33, 81, 72, 44, 41, 30, 38, 30, 11, 33, 81, 51, 25, 38, 33, 30, 11, 15, 60, 59, 58, 87, 50, 55, 54, 65, 77, 67, 25, 15, 75, 30, 13, 77, 36, 32, 76, 30, 40, 30, 35, 49, 35, 30, 32, 38, 31, 26, 41, 33, 92, 37, 37, 73, 40, 43, 16, 32, 64, 69, 90, 36, 33, 95, 65, 53, 67, 18, 72, 39, 22, 11, 35, 39, 26, 33, 31, 39, 89, 59, 11, 11, 23, 12, 11, 14, 41, 11, 12, 11, 12, 12, 16, 13, 12, 14, 11, 14, 23, 11, 15, 35, 13, 20, 54, 19, 38, 18, 13, 39, 14, 15, 13, 12, 35, 12, 11, 51, 15, 38, 37, 22, 58, 47, 40, 35, 31, 34, 32, 35, 39, 31, 31, 32, 28, 30, 30, 36, 36, 68, 37, 38, 40, 45, 30, 81, 76, 17, 35, 45, 30, 48, 33, 37, 35, 35, 35, 31, 57, 30, 84, 35, 37, 37, 57, 55, 28, 27, 24, 62, 60, 88, 36, 59, 59, 80, 59, 17, 87, 75, 27, 38, 11, 35, 24, 50, 67, 38, 74, 35, 74, 36, 31, 37, 54, 43, 41, 33, 52, 39, 28, 30, 52, 36, 37, 56, 34, 32, 39, 31, 29, 11, 29, 30, 85, 33, 79, 33, 45, 32, 37, 19, 38, 84, 62, 41, 71, 68, 39, 26, 27, 16, 33, 14, 53, 79, 52, 33, 34, 42, 26, 38, 11, 12, 26, 32, 35, 64, 36, 37, 36, 71, 34, 27, 31, 15, 42, 31, 31, 58, 40, 59, 43, 64, 85, 38, 36, 61, 34, 26, 44, 35, 33, 59, 39, 31, 11, 33, 35, 53, 65, 31, 37, 96, 38, 79, 36, 30, 26, 58, 24, 19, 55, 57, 58, 34, 60, 84, 30, 32, 53, 53, 33, 31, 42, 48, 34, 65, 62, 48, 15, 32, 31, 35, 26, 37, 32, 32, 33, 33, 41, 29, 37, 88, 42, 44, 71, 42, 39, 36, 28, 64, 39, 43, 34, 36, 31, 38, 67, 37, 52, 30, 38, 37, 42, 30, 38, 85, 34, 51, 30, 25, 67, 29, 14, 79, 59, 64, 33, 16, 65, 63, 56, 16, 46, 11, 32, 34, 76, 71, 27, 36, 33, 30, 33, 38, 33, 44, 42, 31, 83, 29, 29, 33, 38, 40, 37, 29, 30, 41, 34, 55, 11, 34, 31, 34, 85, 56, 36, 42, 39, 73, 32, 37, 95, 77, 44, 38, 95, 37, 41, 26, 62, 34, 36, 32, 62, 63, 77, 75, 41, 67, 37, 40, 30, 70, 46, 35, 34, 62, 95, 61, 30, 34, 31, 34, 34, 44, 26, 39, 29, 36, 95, 43, 44, 40, 28, 37, 36, 38, 64, 44, 40, 31, 77, 37, 31, 41, 79, 35, 30, 15, 39, 68, 35, 32, 35, 32, 34, 66, 11, 36, 65, 36, 36, 96, 11, 86, 35, 36, 30, 29, 82, 34, 34, 31, 47, 46, 39, 40, 47, 34, 69, 36, 77, 71, 47, 41, 76, 84, 64, 54, 57, 32, 69, 61, 66, 11, 68, 39, 39, 38, 89, 40, 35, 32, 14, 37, 11, 35, 29, 33, 99, 74, 45, 46, 40, 11, 36, 70, 31, 37, 37, 95, 30, 77, 70, 94, 64, 70, 32, 37, 32, 39, 15, 18, 18, 11, 57, 11, 13, 13, 39, 29, 17, 14, 12, 16, 27, 30, 19, 18, 18, 43, 11, 12, 19, 17, 20, 90, 27, 23, 44, 25, 11, 26, 19, 11, 19, 16, 12, 12, 58, 20, 11, 18, 11, 13, 12, 26, 19, 15, 17, 21, 11, 11, 17, 18, 13, 13, 13, 13]
x1s = [2511, 2493, 2487, 2486, 2485, 2477, 2461, 2452, 2449, 2419, 2399, 2397, 2394, 2374, 2357, 2338, 2337, 2323, 2305, 2258, 2226, 2225, 2224, 2224, 2224, 2224, 2224, 2224, 2223, 2222, 2222, 2221, 2220, 2220, 2220, 2220, 2216, 2215, 2214, 2214, 2213, 2213, 2212, 2212, 2211, 2211, 2211, 2210, 2209, 2208, 2208, 2208, 2207, 2206, 2206, 2206, 2205, 2201, 2200, 2197, 2194, 2194, 2193, 2192, 2188, 2184, 2156, 2142, 2140, 2140, 2140, 2140, 2139, 2139, 2139, 2138, 2138, 2138, 2138, 2137, 2136, 2136, 2134, 2133, 2133, 2132, 2132, 2132, 2131, 2131, 2131, 2130, 2130, 2128, 2126, 2125, 2123, 2123, 2121, 2121, 2119, 2119, 2118, 2117, 2114, 2112, 2111, 2111, 2108, 2108, 2106, 2104, 2100, 2097, 2091, 2065, 2057, 2057, 2057, 2056, 2056, 2056, 2056, 2056, 2055, 2055, 2055, 2055, 2054, 2054, 2054, 2054, 2054, 2054, 2054, 2054, 2053, 2052, 2051, 2050, 2048, 2048, 2047, 2045, 2044, 2044, 2044, 2044, 2043, 2042, 2042, 2042, 2033, 2032, 2032, 2030, 2027, 2026, 2022, 2018, 2015, 2007, 1994, 1976, 1976, 1976, 1974, 1974, 1974, 1971, 1970, 1970, 1970, 1968, 1968, 1967, 1965, 1964, 1964, 1963, 1963, 1963, 1962, 1961, 1961, 1960, 1955, 1947, 1945, 1944, 1943, 1942, 1940, 1940, 1940, 1940, 1923, 1904, 1899, 1892, 1892, 1892, 1891, 1891, 1891, 1890, 1890, 1890, 1889, 1889, 1888, 1887, 1886, 1886, 1886, 1886, 1885, 1885, 1884, 1882, 1882, 1882, 1880, 1880, 1880, 1880, 1879, 1879, 1878, 1878, 1877, 1876, 1875, 1870, 1868, 1868, 1868, 1866, 1865, 1864, 1864, 1862, 1861, 1861, 1860, 1859, 1857, 1856, 1856, 1854, 1847, 1825, 1812, 1804, 1804, 1804, 1803, 1803, 1803, 1803, 1803, 1803, 1803, 1803, 1802, 1802, 1802, 1802, 1802, 1802, 1802, 1801, 1801, 1801, 1801, 1801, 1801, 1800, 1797, 1797, 1797, 1797, 1797, 1797, 1796, 1795, 1795, 1794, 1794, 1794, 1793, 1793, 1793, 1792, 1792, 1781, 1781, 1780, 1780, 1777, 1777, 1776, 1775, 1774, 1770, 1767, 1766, 1764, 1718, 1718, 1718, 1718, 1718, 1718, 1718, 1717, 1717, 1717, 1716, 1716, 1716, 1716, 1716, 1716, 1716, 1715, 1715, 1715, 1714, 1713, 1713, 1713, 1712, 1712, 1712, 1712, 1712, 1712, 1711, 1710, 1710, 1709, 1707, 1701, 1698, 1696, 1696, 1696, 1696, 1693, 1691, 1690, 1690, 1688, 1686, 1667, 1649, 1635, 1635, 1635, 1635, 1635, 1634, 1634, 1634, 1634, 1634, 1634, 1634, 1633, 1633, 1633, 1632, 1632, 1632, 1632, 1631, 1629, 1629, 1629, 1628, 1626, 1622, 1620, 1614, 1614, 1612, 1612, 1610, 1609, 1608, 1608, 1605, 1604, 1604, 1604, 1603, 1603, 1558, 1534, 1484, 1464, 1380, 1359, 1333, 1309, 1294, 1236, 1216, 1201, 1196, 1152, 1124, 1103, 1040, 1027, 1017, 1010, 1003, 1002, 1001, 999, 998, 998, 997, 997, 996, 996, 996, 995, 994, 992, 991, 990, 990, 989, 989, 989, 988, 986, 985, 985, 985, 984, 984, 984, 984, 984, 984, 984, 984, 984, 984, 984, 984, 983, 983, 982, 974, 973, 973, 972, 964, 964, 964, 960, 960, 960, 960, 958, 958, 956, 955, 955, 919, 917, 916, 915, 912, 911, 908, 907, 907, 906, 905, 904, 903, 903, 903, 903, 903, 902, 901, 901, 901, 900, 900, 900, 900, 900, 900, 899, 899, 899, 899, 899, 899, 899, 899, 899, 898, 898, 898, 898, 897, 894, 892, 881, 880, 880, 879, 879, 878, 874, 872, 867, 831, 830, 828, 827, 827, 827, 826, 825, 824, 824, 823, 822, 822, 819, 818, 817, 817, 817, 817, 817, 816, 816, 816, 816, 815, 815, 815, 814, 814, 814, 814, 814, 813, 813, 813, 813, 813, 812, 812, 808, 805, 805, 802, 797, 796, 796, 792, 792, 792, 792, 792, 791, 791, 789, 788, 787, 786, 786, 754, 747, 747, 747, 746, 745, 743, 743, 742, 741, 741, 739, 739, 735, 730, 730, 729, 729, 729, 728, 728, 728, 728, 728, 728, 727, 727, 727, 726, 726, 726, 725, 725, 725, 722, 721, 719, 717, 712, 706, 706, 705, 705, 700, 700, 697, 670, 660, 656, 655, 655, 655, 654, 653, 652, 651, 650, 650, 648, 647, 646, 646, 646, 645, 645, 644, 644, 644, 644, 644, 643, 642, 642, 642, 641, 641, 641, 641, 640, 640, 640, 640, 640, 640, 640, 639, 639, 638, 638, 638, 637, 636, 632, 631, 631, 616, 613, 610, 607, 581, 578, 577, 576, 575, 573, 572, 569, 569, 568, 564, 563, 562, 562, 561, 561, 561, 560, 560, 560, 559, 558, 558, 558, 557, 557, 556, 556, 555, 555, 555, 555, 555, 554, 554, 554, 554, 554, 554, 554, 553, 549, 545, 545, 540, 536, 492, 491, 490, 486, 484, 480, 478, 477, 475, 474, 474, 472, 472, 471, 471, 470, 470, 470, 469, 468, 468, 467, 465, 460, 458, 449, 448, 445, 407, 402, 399, 398, 395, 391, 391, 389, 389, 389, 388, 388, 387, 387, 387, 386, 384, 384, 384, 384, 384, 383, 382, 379, 378, 368, 362, 359, 359, 355, 350, 153, 143, 140, 120, 120]
cum_summed = [(31, 1804), (29, 1803), (28, 903), (26, 1825), (26, 1812), (25, 904), (24, 1718), (24, 902), (24, 901), (24, 817), (23, 1802), (23, 1717), (23, 1635), (23, 818), (22, 2091), (22, 2065), (22, 2057), (22, 1766), (22, 1764), (22, 990), (22, 989), (22, 900), (22, 645), (22, 644), (21, 1847), (21, 1716), (21, 1667), (21, 1649), (21, 985), (20, 2056), (20, 1767), (20, 988), (20, 986), (20, 816), (20, 730), (20, 643), (20, 642), (20, 559), (20, 558), (19, 1801), (19, 1634), (19, 984), (19, 819), (19, 729), (18, 1686), (18, 815), (18, 735), (18, 646), (18, 641), (18, 557), (18, 556), (17, 1797), (17, 905), (17, 899), (17, 739), (17, 728), (17, 555), (16, 2055), (16, 1886), (16, 1800), (16, 1715), (16, 1688), (16, 822), (16, 814), (16, 741), (16, 560), (16, 391), (15, 2225), (15, 2224), (15, 2142), (15, 2140), (15, 2097), (15, 1887), (15, 1854), (15, 647), (15, 640), (15, 389), (14, 2184), (14, 2156), (14, 2054), (14, 1891), (14, 1885), (14, 1795), (14, 1794), (14, 1770), (14, 1714), (14, 1713), (14, 823), (14, 650), (14, 562), (14, 561), (13, 2139), (13, 2138), (13, 2136), (13, 1994), (13, 1976), (13, 1940), (13, 1904), (13, 1899), (13, 1892), (13, 1890), (13, 1884), (13, 1882), (13, 1796), (13, 1633), (13, 974), (13, 973), (13, 972), (13, 964), (13, 805), (13, 648), (13, 563), (13, 554), (13, 388), (12, 2258), (12, 2226), (12, 2220), (12, 2213), (12, 2211), (12, 2137), (12, 2134), (12, 2133), (12, 2100), (12, 2048), (12, 2045), (12, 2044), (12, 2007), (12, 1970), (12, 1923), (12, 1888), (12, 1793), (12, 1774), (12, 1712), (12, 982), (12, 906), (12, 824), (12, 813), (12, 808), (12, 802), (12, 797), (12, 796), (12, 792), (12, 727), (12, 474), (12, 398), (12, 395), (12, 387), (11, 2323), (11, 2305), (11, 2222), (11, 2221), (11, 2216), (11, 2215), (11, 2214), (11, 2212), (11, 2188), (11, 2132), (11, 2047), (11, 1974), (11, 1942), (11, 1889), (11, 1880), (11, 1690), (11, 1632), (11, 991), (11, 960), (11, 908), (11, 907), (11, 742), (11, 568), (11, 564), (11, 477), (11, 475), (11, 472), (10, 2223), (10, 2210), (10, 2209), (10, 2208), (10, 2131), (10, 2051), (10, 2050), (10, 2018), (10, 2015), (10, 1971), (10, 1968), (10, 1967), (10, 1965), (10, 1964), (10, 1868), (10, 1792), (10, 1710), (10, 1701), (10, 1698), (10, 1696), (10, 1612), (10, 1610), (10, 1609), (10, 1608), (10, 1002), (10, 1001), (10, 999), (10, 998), (10, 983), (10, 898), (10, 827), (10, 786), (10, 747), (10, 743), (10, 726), (10, 651), (10, 639), (10, 569), (10, 471), (10, 399), (10, 386), (10, 384), (9, 2206), (9, 2192), (9, 2130), (9, 2128), (9, 2126), (9, 2125), (9, 2123), (9, 2043), (9, 2042), (9, 1963), (9, 1947), (9, 1945), (9, 1944), (9, 1943), (9, 1878), (9, 1875), (9, 1870), (9, 1856), (9, 1781), (9, 1709), (9, 1707), (9, 1629), (9, 1620), (9, 1614), (9, 1605), (9, 1604), (9, 997), (9, 996), (9, 995), (9, 994), (9, 992), (9, 830), (9, 828), (9, 812), (9, 789), (9, 788), (9, 787), (9, 754), (9, 746), (9, 745), (9, 719), (9, 717), (9, 712), (9, 706), (9, 700), (9, 655), (9, 652), (9, 638), (9, 478), (9, 470), (9, 402), (8, 2207), (8, 2121), (8, 2119), (8, 2118), (8, 2117), (8, 2114), (8, 2112), (8, 2111), (8, 2104), (8, 2022), (8, 1879), (8, 1877), (8, 1876), (8, 1866), (8, 1865), (8, 1864), (8, 1862), (8, 1861), (8, 1780), (8, 1631), (8, 1628), (8, 1626), (8, 1622), (8, 1003), (8, 958), (8, 897), (8, 894), (8, 892), (8, 881), (8, 880), (8, 872), (8, 867), (8, 831), (8, 826), (8, 825), (8, 791), (8, 725), (8, 721), (8, 705), (8, 697), (8, 670), (8, 660), (8, 656), (8, 572), (8, 480), (7, 2205), (7, 2201), (7, 2200), (7, 2197), (7, 2194), (7, 2108), (7, 2053), (7, 2052), (7, 2033), (7, 2032), (7, 1962), (7, 1961), (7, 1860), (7, 1859), (7, 1857), (7, 1777), (7, 1711), (7, 1693), (7, 1691), (7, 1603), (7, 1010), (7, 956), (7, 955), (7, 916), (7, 915), (7, 912), (7, 911), (7, 879), (7, 722), (7, 654), (7, 653), (7, 637), (7, 636), (7, 632), (7, 631), (7, 577), (7, 576), (7, 575), (7, 573), (7, 553), (7, 549), (7, 545), (7, 484), (7, 469), (7, 468), (7, 407), (7, 382), (7, 379), (7, 378), (7, 368), (7, 362), (7, 359), (7, 355), (6, 2511), (6, 2493), (6, 2487), (6, 2486), (6, 2485), (6, 2477), (6, 2461), (6, 2452), (6, 2449), (6, 2419), (6, 2399), (6, 2397), (6, 2394), (6, 2374), (6, 2357), (6, 2338), (6, 2337), (6, 2193), (6, 2106), (6, 2030), (6, 2027), (6, 2026), (6, 1960), (6, 1955), (6, 1776), (6, 1775), (6, 1558), (6, 1534), (6, 1484), (6, 1464), (6, 1380), (6, 1359), (6, 1333), (6, 1309), (6, 1294), (6, 1236), (6, 1216), (6, 1201), (6, 1196), (6, 1152), (6, 1124), (6, 1103), (6, 1040), (6, 1027), (6, 1017), (6, 919), (6, 917), (6, 878), (6, 874), (6, 616), (6, 613), (6, 610), (6, 607), (6, 581), (6, 578), (6, 540), (6, 536), (6, 492), (6, 491), (6, 490), (6, 486), (6, 467), (6, 465), (6, 460), (6, 458), (6, 449), (6, 448), (6, 445), (6, 383), (6, 350), (5, 153), (4, 143), (3, 140), (2, 120)]

fig = plt.figure()
ax = fig.add_subplot(111)

# the histogram of the data
n, bins, patches = ax.hist(cum_summed, len(cum_summed), normed=1, facecolor='blue')

# hist uses np.histogram under the hood to create 'n' and 'bins'.
# np.histogram returns the bin edges, so there will be 50 probability
# density values in n, 51 bin edges in bins and 50 patches.  To get
# everything lined up, we'll compute the bin centers
#bincenters = 0.5*(bins[1:]+bins[:-1])
# add a 'best fit' line for the normal PDF
#y = mlab.normpdf( bincenters, mu, sigma)
#l = ax.plot(bincenters, y, 'r--', linewidth=1)

ax.set_xlabel('y value')
ax.set_ylabel('Occurence')
#ax.set_title(r'$\mathrm{Histogram\ of\ IQ:}\ \mu=100,\ \sigma=15$')
ax.grid(True)

fig.savefig('image/y_value_hist.png')
