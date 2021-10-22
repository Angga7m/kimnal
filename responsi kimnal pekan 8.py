#N = [10, 25, 50, 100, 110, 125, 150, 200]
#fin = []
#for each in N:
#    I = each * 0.01
#    U = I * 25
#    fin.append(U)
#print(fin)
# penentuan volume nilai berdasarkan persentase


import math
L = [2.5, 6.25, 12.5, 25.0, 27.5, 31.25, 37.5, 50]
B = L
#B menunjukkan list untuk perhitungan sebelum titik ekuivlen yaitu 25

t = 50 * 0.05
# t adalah mol dari asam dan konstan dan harus dibagi dengan v total yaitu v asam + v titran basa yang ada persennya

lis_basa = list()
for each in B:
    new = (each * 0.1) / (50 + each)
    lis_basa.append(new)
#perhitungan basa


i = 1
list_asam = list()
for each in B:
    konsentrasi_asam = (t) / (50 + each)
    list_asam.append(konsentrasi_asam)
#perhitungan asam

i = 0
ls_asam_pakai = list()
for each in list_asam:
    new = list_asam[i] - lis_basa[i]
    ls_asam_pakai.append(new)
    i += 1
lis_asam_pakai = ls_asam_pakai[0:3]
#perhitungan asam pakai, yang digunakan kurang dari 25ml atau sebelum titik ekuivalen

i = 0
for each in lis_asam_pakai:
    konsentrasi_ion = (1.8*10e-4 * each) / lis_basa[i]
    i += 1
    pH = -math.log(konsentrasi_ion, 10) + 1
    #nilai juga ditambah dengan nilai 1 karena ada error pada kode
    print(pH)

#perhitungan kosentrasi asam untuk pH beserta nilai pH dengan pH
# 2.790484985457369
# 3.2676062401770314
# 3.7447274948966935

#--------------------------------------------------------------------------------
print(8.11)
#titik ekuivalen menggunakan hidrolisis
#--------------------------------------------------------------------------------

i = 4
list_basa_setelah_ekuivalen = [0.035483870967741936, 0.038461538461538464, 0.04285714285714286, 0.05]
for each in list_basa_setelah_ekuivalen:
    OH = each - list_asam[i]
    i += 1
    pOH = -math.log(OH, 10)
    pH = 14 - pOH
    print(pH)
#adalah perhitungan untuk basa setelah titik ekuivalen di mana pada line 59 rumus dibalik untuk menghindari nilai negatif
#nilai pH
#11.508638306165729
#11.886056647693163
#12.154901959985743
#12.397940008672037
