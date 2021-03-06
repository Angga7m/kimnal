def statistik(list_siap):
    print(f'nilai rata-rata: {statistics.mean(list_siap)}')
    print(f'nilai standar deviasi: {statistics.stdev(list_siap)}')

    u = (1 - (statistics.stdev(list_siap) / statistics.mean(list_siap))) * 100
    print(f'akurasi : {u}%')
    print('-' * 50)
#perhitungan statistik
#data volume titrasi
import statistics

awal = [3.5,4.6,5.9]
akhir = [4.5,5.9,6.9]
#pake data tabel 4, modip dulu
i = 0
for each in awal:
    a = akhir[i]
    #print(a-each)
    #dimatikan biar datanya gak semraut
    i += 1
#hitung konsentrasi tabel 1
print('tabel 1'.upper())
V_EDTA = [9.4, 9.3, 9.7]
#modip dulu. tabel 1 olahan
kons_caco3 = 0.01
V_caco3 = 10
list_kons_EDTA = list()
i = 0
print('nilai konsentrasi EDTA adalah:')
for each in V_EDTA:
    Kons_EDTA = (kons_caco3 * V_caco3) / each
    print(Kons_EDTA)
    list_kons_EDTA.append(Kons_EDTA)
print(''
      '')
statistik(list_kons_EDTA)#cek atas

#-------------------------------------------------------------
print('tabel 2'.upper())
V_EDTA = [9.5, 10.0, 9.9]
kons_EDTA_f = 0.0105
BM_Mg = 24
V_Mg = 10

list_kadar_Mg = list()
for Vedta in V_EDTA:
    kadar_Mg = (Vedta * kons_EDTA_f * BM_Mg) / V_Mg
    print(kadar_Mg)
    list_kadar_Mg.append(kadar_Mg)
print(''
      '')
print('nilai kadar Mg adalah:')
statistik(list_kadar_Mg)#cek atas
#-------------------------------------------------------------
print('tabel 3'.upper())
V_EDTA = [9.2, 9.3, 9.4]
V_Ca = 10
BM_Ca = 40
kons_EDTA_f = 0.0105

list_kadar_Ca = list()
for Vedta in V_EDTA:
    kadar_Ca = (Vedta * kons_EDTA_f * BM_Ca) / V_Ca
    print(kadar_Ca)
    list_kadar_Ca.append(kadar_Ca)
print(''
      '')
print('nilai kadar Ca adalah:')
statistik(list_kadar_Ca)
#------------------------------------------------------------
print('tabel 4 dan 5'.upper())

V_EDTA = [8.4, 8.7, 8.6]
V_Mg = [1.0, 1.3, 1.0]
kons_EDTA_f = 0.0105
kons_Mg_f = 0.01

list_kadar_Ca = []
i = 0
for each in V_EDTA:
    kadar_Ca_F = (((each * kons_EDTA_f) - (V_Mg[i] * kons_Mg_f)) * 40) / 10
    kadar_Ca = abs(kadar_Ca_F)
    i =+ 1
    print(kadar_Ca)
    list_kadar_Ca.append(kadar_Ca)
print(''
      '')
print('nilai kadar Ca adalah:')
statistik(list_kadar_Ca)
