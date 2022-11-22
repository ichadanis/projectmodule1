# Akademik Scores - Data Nilai Siswa

#Menu Utama
print('\n\tData Nilai Geografi Siswa Kelas 10B 2016/2017')
menuUtama= '''    
        Pilihan Menu Utama:
        A. Melihat Nilai
        B. Menambahkan Nilai
        C. Update Nilai Siswa
        D. Delete Nilai Siswa
        E. Keluar
'''

dataNilaiSiswa = [[2017001, 'Ali', 85],[2017002, 'Budi', 90],[2017003, 'Dian', 95],
[2017004, 'Dini', 95],[2017005, 'Fina', 63],[2017006, 'Mira', 70],
[2017007, 'Nia', 98],[2017008, 'Meli', 78],[2017009, 'Laso', 67],
[2017010, 'Ziki', 78]]  


def lihatdata (): 
    print('\n\t\tTabel Data Nilai Geografi Siswa Kelas 10B 2016/2017 \n')
    print('No.\t|ID Siswa\t| Nama \t| Nilai\t|')
    for i in range(len(dataNilaiSiswa)) :
     print('{}\t|{}\t| {} \t|{} \t|'.format(i,dataNilaiSiswa[i][0],dataNilaiSiswa[i][1],dataNilaiSiswa[i][2]))


#fiturRead
def melihatdata (): 
    print('\n\t\tTabel Data Nilai Geografi Siswa Kelas 10B 2016/2017 \n')
    print('No.\t|ID Siswa\t| Nama \t| Nilai\t|')
    for i in range(len(dataNilaiSiswa)) :
     print('{}\t|{}\t| {} \t|{} \t|'.format(i,dataNilaiSiswa[i][0],dataNilaiSiswa[i][1],dataNilaiSiswa[i][2]))
    kembalikemenu()


#fiturCreate
def tambahnilai() :
    IDsiswa= int(input('Masukkan ID Siswa (7 karakter): '))
    namaSiswa= (input('Masukkan Nama Siswa (maks 4 karakter) : '))
    nilaiSiswa= int(input('Masukkan Nilai Siswa: '))
    dataNilaiSiswa.append([IDsiswa,namaSiswa,nilaiSiswa])
    lihatdata()
    print('\nSiswa yang bernama {} dengan nilai {} berhasil ditambahkan pada tabel data \n'.format(namaSiswa,nilaiSiswa))
    kembalikemenu()


#fiturUpdate
def updatenilai(): 
    print('\n\t\t\tAnda akan meng-update nilai Siswa')
    lihatdata()
    no_update_nilai= int(input('Masukkan No. Tabel yang ingin nilainya diupdate : '))
    update_nilai= int(input('Silahkan masukkan nilai terupdate: '))
    dataNilaiSiswa[no_update_nilai][2]=update_nilai
    lihatdata()
    print('\nNilai dari siswa yang bernama {}, telah berhasil diupdate menjadi {}\n'.format(dataNilaiSiswa[no_update_nilai][1],dataNilaiSiswa[no_update_nilai][2]))
    kembalikemenu()


#fiturDelete
def hapusdata() : 
    lihatdata()
    nomorSiswa = int(input('Masukkan No. Tabel yang ingin nilainya dihapus : '))
    print('\nNilai dari siswa yang bernama {} telah dihapus\n'.format(dataNilaiSiswa[nomorSiswa][1]))
    del dataNilaiSiswa[nomorSiswa]
    lihatdata()
    kembalikemenu()


#untukkembalikeMenuUtama  
def kembalikemenu():
    kembali_ke_menu=(input('Apakah Anda ingin kembali ke Menu Utama? (ya/tidak): '))
    if (kembali_ke_menu=='ya'):
        print(menuUtama)
        pilihanmenu=input('Apa yang ingin Anda lakukan? (Silahkan pilih A-D): ')
        if (pilihanmenu=='A'):
            melihatdata()
        elif (pilihanmenu== 'B'):
            print('Anda akan menambah nilai siswa')
            tambahnilai()
        elif (pilihanmenu== 'C'):
            updatenilai()
        elif (pilihanmenu== 'D'):
            hapusdata()
        elif (pilihanmenu== 'E'):
            print ('Selamat Tinggal')
        else:
            print('Pilihan menu yang dimasukkan salah,\nSilahkan masukkan A,B,C,D atau E')
    elif (kembali_ke_menu=='tidak'):
        print('Selamat tinggal')
    else:
        print ('Pilihan menu yang dimasukkan salah,\nSilahkan ya atau tidak')


print(menuUtama)
a=0
while a<1:
    pilihanmenu=input('Apa yang ingin Anda lakukan? (Silahkan pilih A-E): ')
    if (pilihanmenu=='A'):
        a=+1
        melihatdata()
    elif (pilihanmenu== 'B'):
        a=+1
        print('Anda akan menambah nilai siswa')
        tambahnilai()  
    elif (pilihanmenu== 'C'):
        a=+1
        updatenilai()
    elif (pilihanmenu== 'D'):
        a=+1
        hapusdata()
    elif (pilihanmenu== 'E'):
        a=+1
        print ('Selamat Tinggal')
    else:
        print('Pilihan menu yang dimasukkan salah,\nSilahkan masukkan A,B,C,D atau E')



