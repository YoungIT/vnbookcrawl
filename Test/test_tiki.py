def test_get_book(tiki_fixture):

    result = tiki.getBooks()

    assert result == [(52789367, 52789368), (52805060, 52805061), (205033951, 205033955), 
    (56226544, 56226545), (92096344, 92096345), (182972780, 182972781), (531103, 17992969), (166033459, 166033461), (198644080, 198644082), (626886, 626888), (884432, 885778), (111290700, 111290701), (219148748, 246770499), (192333857, 192333860), (2496281, 2496329), (52785564, 52785565), (571210, 17505305), (73434639, 73434640), (104935828, 104935829), (174038857, 174038858), (207830866, 207830868), (520358, 238716), (52207306, 52207307), (91471511, 91471512), (175146839, 175146840), (193099631, 193099632), (656342, 17512475), (11357193, 11357194), (210143419, 210143420), (175176401, 175176402), (10392851, 242174732), (568762, 17509940), (40750124, 40750125), (520330, 238688), (174038853, 174038855), (214617629, 214617632), (510195, 17990925), (207777935, 207777937), (46332534, 46332536), (56226546, 56226547), (194959694, 194959699), (1021663, 1021665), (49549972, 49549973), (870619, 872753), (129765498, 129765499), (195306005, 195306006), (46849710, 46837049), (467896, 177227), (56908132, 56908133), (198342225, 198342228), (205694860, 205694861), (165956567, 165956568), (49549966, 49549967), (1891219, 19559599), (172175803, 172175804), (184226852, 184226853), (529695, 88965773), (77988131, 80619067), (26222265, 26222266), (110447670, 110447673), (510482, 17990964), (10568888, 10568889), (51574033, 51574034), (248989445, 248989446), (197599718, 197599720), (46332538, 46332539), (215186535, 215186536), (188535523, 188535524), (213861834, 213861835), (114275076, 114275079), (248755012, 248755019), (214611399, 214611400), (77330632, 77330634), (457248, 165155), (77326136, 78005822), (219148742, 219148743), (201004696, 201004699), (17371066, 17371067), (57380875, 72006356), (195545504, 195545505), (3282119, 3283219), (510486, 17994046), (196932364, 196932365), (205034090, 205034125), (9729890, 9729891), (571448, 
    19340314), (162832796, 162832799), (741765, 750953), (32916374, 32916375), (214496614, 246970909), (174626750, 174626751), (520318, 238676), (52207304, 52207305), (1725947, 19340998), (215186533, 215186534), (206308041, 206308044), (219148752, 219148753), (168234720, 184122440), (382544, 130730681), (1392941, 21485963)]
