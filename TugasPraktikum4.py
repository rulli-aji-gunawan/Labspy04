
nama = []
nim = []
tugas = []
uts = []
uas = []
akhir = []

x = []
y = 0
tambah = 'y'

while tambah == 'y' :
    y += 1
    x.append (y)
    a = str(input ("Nama : "))
    nama.append (a)
    b = int(input ("NIM : "))
    nim.append (b)
    c = int(input ("Nilai Tugas : "))
    tugas.append (c)
    d = int(input ("Nilai UTS : "))
    uts.append (d)
    e = int(input ("Nilai UAS : "))
    uas.append (e)
    f = float ((c*0.3)+(d*0.35)+(e*0.35))
    akhir.append (f)

    tambah = str(input("Tambah data (y/t) ? : "))

garis = 71
print ('='*garis)
print ('| No |       Nama       |   NIM   |  Tugas  |  UTS  |  UAS  |  Akhir  |')
print ('='*garis)

for i in x :
    print('| ',i,'| ',nama[i-1],' '*(14-len(nama[i-1])),'| ',nim[i-1],' ','|  ',tugas[i-1],'  ','|  ',uts[i-1],'','|  ',uas[i-1],'','|  ','{:02.2f}'.format(akhir[i-1]),'|')
print ('='*garis)

# clnol = '|  '
# clnor = '  |'
# clnamal = '                  '
# clnim = '|         |'
# cltugas = '         '
# cluts = '|       |'
# cluas = '       '
# clakhir = '|         |'


