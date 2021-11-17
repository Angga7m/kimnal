
import statistics
def statistik(list_siap):
    print(f'nilai rata-rata: {statistics.mean(list_siap)}')
    print(f'nilai standar deviasi: {statistics.stdev(list_siap)}')

    u = (1 - (statistics.stdev(list_siap) / statistics.mean(list_siap))) * 100
    print(f'akurasi : {u}%')
    print('-' * 50)
def penentuan_konsentrasi_asam_oksalat(awal, akhir):
    i = 0
    terpakai = []
    for awalan in awal:
        L = akhir[i] - awalan
        i += 1
        terpakai.append(L)

    for c in terpakai:
        print(c)

    print(
        '\n'
    )
    jadi = list()
    for masing in terpakai:
        K = (10 * 0.05 * 2) / masing
        jadi.append(K)
        print(K)

    statistik(jadi)
def penentuan_koef_partisi(konsentrasi_naoh,
                           awal_naoh_titrasi,
                           akhir_naoh_titrasi,
                           awal_naoh_tertitrasi,
                           akhir_naoh_tertitrasi):
    print('pernyataan dari bawah ke atas \n penentuan koef partisi'.upper())
    #vnaoh titrasi
    i = 0
    volume_naoh_titrasi = []
    for tiap in awal_naoh_titrasi:
        u = akhir_naoh_titrasi[i] - tiap
        i += 1
        volume_naoh_titrasi.append(u)
        print(u)
    print('vnaoh titrasi'
          '\n')

    #vnaoh tertitrasi
    i = 0
    volume_naoh_tertitrasi = []
    for tiap in awal_naoh_tertitrasi:
        u = akhir_naoh_tertitrasi[i] - tiap
        i += 1
        volume_naoh_tertitrasi.append(u)
        print(u)
    print('vnaoh tertitrasi'
          '\n')

    #konsentrasi ch3cooh awal
    i = 0
    konsentrasi_ch3cooh_awal = []
    for tiap in volume_naoh_titrasi:
        u = (konsentrasi_naoh * tiap) / 10
        i += 1
        konsentrasi_ch3cooh_awal.append(u)
        print(u)
    print('konsentrasi ch3cooh awal'
          '\n')

    #kosentrasi ch3cooh akhir
    konsentrasi_ch3cooh_akhir = []
    i = 0
    for tiap in volume_naoh_tertitrasi:
        u = (konsentrasi_naoh * tiap) / 15
        i += 1
        konsentrasi_ch3cooh_akhir.append(u)
        print(u)
    print('kosentrasi ch3cooh akhir dan saq (valuenya sama)'
          '\n')

    #sorganik
    sorganik = []
    i = 0
    for tiap in konsentrasi_ch3cooh_awal:
        u = (tiap - konsentrasi_ch3cooh_akhir[i])
        i += 1
        sorganik.append(u)
        print(u)
    print('sorganik'
          '\n')

    #koef partisi
    kd = list()
    i = 0
    for tiap in sorganik:
        u = tiap / konsentrasi_ch3cooh_akhir[i]
        print(u)
        kd.append(u)
    print('koeffisien partisi kD'
            '\n')

    statistik(kd)

def penentuan_nisbah_distribusi(konsentrasi_naoh,
                                awal_naoh_titrasi,
                                akhir_naoh_titrasi,
                                awal_naoh_tertitrasi,
                                akhir_naoh_tertitrasi,
                                nilai_pH_awal,
                                nilai_pH_akhir):
    #V NaOH titrasi (mL)
    vol_terpakai_naoh_titrasi = []
    i = 0
    for tiap in awal_naoh_titrasi:
        u = akhir_naoh_titrasi[i] - tiap
        print(u)
        vol_terpakai_naoh_titrasi.append(u)
        i += 1
    print('vol_terpakai_naoh_titrasi')
    print('\n')

    # V NaOH tertitrasi (mL)
    vol_terpakai_naoh_tertitrasi = []
    i = 0
    for tiap in awal_naoh_tertitrasi:
        u = akhir_naoh_tertitrasi[i] - tiap
        print(u)
        vol_terpakai_naoh_tertitrasi.append(u)
        i += 1
    print('vol_terpakai_naoh_tertitrasi')
    print('\n')

    #pH awal akhir cari H+
    for tiap in nilai_pH_awal:
        u = pow(10, -tiap)
        print(u)
    print('pH awal')
    print('\n')

    pH_value_akhir = []
    for tiap in nilai_pH_akhir:
        u = pow(10, -tiap)
        print(u)
        pH_value_akhir.append(u)
    print('pH akhir')
    print('\n')

    #konsentrasi asam asetat awal
    asetat_awal = []
    for tiap in vol_terpakai_naoh_titrasi:
        u = (konsentrasi_naoh * tiap)/10
        print(u)
        asetat_awal.append(u)
    print('konsentrasi asetat awal')
    print('\n')

    # konsentrasi asam asetat akhir
    asetat_akhir = []
    for tiap in vol_terpakai_naoh_tertitrasi:
        u = (konsentrasi_naoh * tiap) / 15
        print(u)
        asetat_akhir.append(u)
    print('konsentrasi asetat akhir')
    print('\n')

    #D1
    i = 0
    d1_lis = []
    for tiap in asetat_akhir:
        u = (asetat_awal[i] - tiap) / (pH_value_akhir[i] + asetat_awal[i])
        print(u)
        i += 1
        d1_lis.append(u)
    print('nilai D1')
    statistik(d1_lis)
    print('\n')

    # D2
    i = 0
    d2_lis = []
    kd = [
        0.697,
        0.650,
        0.696
    ]
    for tiap in asetat_awal:
        u = ( kd[i] * tiap / tiap + 1.8*10e-5)
        print(u)
        i += 1
        d2_lis.append(u)
    print('nilai D2')
    statistik(d2_lis)




awal = [0.00,
        7.10,
        14.35]
akhir = [7.10,
         14.35,
         21.70]
#penentuan_konsentrasi_asam_oksalat(awal, akhir)

konsentrasi_naoh = 0.14
awal_naoh_titrasi = [0,
                     9,
                     18
                     ]
akhir_naoh_titrasi = [8.85,
                      17.9,
                      26.9
                      ]
awal_naoh_tertitrasi = [27.00,
                        34.86,
                        25.00
                        ]
akhir_naoh_tertitrasi = [34.82,
                         43.12,
                         32.90
                         ]
#penentuan_koef_partisi(konsentrasi_naoh, awal_naoh_titrasi, akhir_naoh_titrasi, awal_naoh_tertitrasi, akhir_naoh_tertitrasi)


M_naoh = 0.14

awal_Naoh_titrasi = [34.0,
                    29.2,
                    19.5]

akhir_Naoh_titrasi = [49.1,
                      42.5,
                      34.0]

awal_Naoh_tertitrasi = [1.00,
                        3.70,
                        6.60]

akhir_Naoh_tertitrasi = [3.70,
                        6.60,
                        9.40]

pH_awal = [5.02,
            5.03,
            5.00]

pH_akhir = [5.01,
            5.02,
            5.01]


penentuan_nisbah_distribusi(M_naoh,
                            awal_Naoh_titrasi,
                            akhir_Naoh_titrasi,
                            awal_Naoh_tertitrasi,
                            akhir_Naoh_tertitrasi,
                            pH_awal,
                            pH_akhir,
                            )

