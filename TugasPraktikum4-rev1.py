x = int(0)
data = []
while (True) :
    x += 1
    nama =  str(input('Masukkan Nama        : '))
    nim =   int(input('Masukkan NIM         : '))
    tugas = int(input('Masukkan Nilai Tugas : '))
    uts =   int(input('Masukkan Nilai UTS   : '))
    uas =   int(input('Masukkan NIlai UAS   : '))
    akhir = float((tugas*0.3)+(uts*0.35)+(uas*0.35))
    data.append ([x,nama,nim,tugas,uts,uas,akhir])
    lagi =  input('Tambah data (y/t) ?  : ')
    if lagi.lower() == 't':
        break
garis = 79
print ('='*garis)
print ( '| No |          Nama          |    NIM    |  Tugas  |  UTS  |  UAS  |  Akhir  |')
print ('='*garis)
for i in data:
    print ('| {0:2d} |  {1:20s}  |  {2:7d}  |  {3:5d}  |  {4:3d}  |  {5:3d}  |  {6:5.2f}  |'.format(i[0], i[1], i[2], i[3], i[4], i[5], i[6]))
print ('='*garis)