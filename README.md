# breadthFirstSearch-2.7
('Breadth-first search graph_1:', ['A', 'B', 'C', 'D', 'E'])
('Breadth-first search graph_2:', ['A', 'B', 'C', 'D', 'E', 'F', 'H', 'G', 'I'])
('Breadth-first search graph_3:', ['A', 'B', 'D', 'F', 'C', 'E', 'G', 'I', 'H'])
('Breadth-first search graph_4:', ​​['D', 'C', 'I', 'B', 'F', 'H', 'K', 'A', 'E', ' G ',' J ',' L '])



1. Antrian:

Daftar -> dipesan
 list.append (elemen) -> masukkan elemen di akhir:
 list.pop () -> hapus dan kembalikan elemen yang terakhir dimasukkan
 list.pop (0) -> hapus elemen yang dimasukkan terlebih dahulu dan kembalikan

-> inisialisasi kosong
-> tambahkan tiga angka berbeda
-> ambil yang sudah disisipkan terlebih dahulu di awal

2. Menampilkan tetangga node dalam grafik

Pengulangan: grafik direpresentasikan sebagai daftar lingkungan:
Di Python, ini adalah "kamus" yang berisi tetangganya untuk setiap node:

grafik = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'D'],
    'D': ['B', 'C', 'E'],
    'E': ['B', 'D']
}

Untuk mengembalikan tetangga dari B, itu cukup untuk mendapatkan elemen yang sesuai dari kamus:
neighbour_von_B = grafik ['B']
Hasilnya adalah daftar yang berisi tetangga B, jadi ['A', 'D', 'E']

Menerapkan metode dengan dua parameter "node" dan "grafik", yang mengembalikan tetangga dari node yang sesuai (daftar). Uji fungsi dengan grafik yang diberikan ...

def neighbour_of (node, grafik):
    grafik kembali [node]

3. Menerapkan metode "pencarian luas-pertama" dengan dua parameter "grafik", "start_knoten", yang mengembalikan daftar urutan node yang mencari seluruh grafik dengan pencarian luas-pertama yang dimulai dari start_knoten.

Saya sudah menyiapkan bagian pertama dari tugas => File 1


a) Tentukan metode "pencarian lebar" dengan dua parameter "grafik", "start_knoten", yang mengembalikan daftar kosong.
   Kemudian kita memanggil metode dengan grafik yang diberikan "graph_1" dan mulai node 'A'.

grafik_1 = {...}
grafik_2 = {...}

def latensearch (grafik, start_knoten):
    Visit_nodes = [start_nodes] # Daftar semua node yang akan dicari
    # dari sini pencarian diimplementasikan pada langkah berikutnya ...
    return visiting_node

cetak "Breadth-search in graph_1:", luas-penelusuran (graph_1, 'A')
cetak "Breadth-search in graph_2:", luas-search (graph_2, 'D')

=> bangun dan jalankan ...

b) Implementasikan algoritma sebagai berikut:

def latensearch (grafik, start_knoten):
    Visit_node = [start_node]
    # tentukan antrian dan masukkan start_node
    # selama antrian tidak kosong:
        # ambil node pertama dari antrian dan simpan di variabel "current_node"
        # temukan semua node tetangga dari "current_node"
        # untuk setiap node yang berdekatan ini:
            # jika tetangga belum ada dalam daftar "visiting_nodes":
                # tambahkan tetangga ke antrean
                # tambahkan tetangga ke daftar "visiting_nodes"
    return visiting_node

4. Kami menerapkan metode baru "shortest_path", yang menemukan jalur terpendek antara dua node dalam grafik.

a) mengimplementasikan "ist_weg_vorhanden" dan menggunakan bagian kode dari metode pencarian lebar.
   Nilai yang dikembalikan: True atau False, bergantung pada apakah jalur ditemukan atau tidak.

b) menerapkan "kuerzester_weg"

Petunjuk:
Selain daftar "visiting_nodes", gunakan kamus tambahan yang juga menyimpan node induknya untuk setiap node yang dikunjungi. Node awal tidak memiliki node induk: kamus dapat diinisialisasi sebagai berikut:
eltern_dict = {start_node: Tidak Ada}
Untuk mengembalikan jalur yang dicakup dari simpul awal ke simpul tujuan di akhir, kamus induk harus digunakan ...
