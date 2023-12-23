ma_liste = ["Allef lej jool", "daera oào poma ssimss osuonumr cnek ddsea", "e svlinen fcnh emzp lmrald abnmi"]
mes_indices = []
res = ''

for i in range(4):
    res += ma_liste[0][i]
for i in range(3,40, 2):
    res += ma_liste[1][i]
for i in range(1,32,2):
    res += ma_liste[2][i]
print(res)