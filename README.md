# Pertemuan 07 Fungsi Python

Nama: Iqhsan Saleh  
NIM: 2225250021  
Kelas: 3A

## Tujuan

Menggunakan fungsi, parameter, return value, dan scope untuk membuat program modular.

## Cara Menjalankan

Jalankan program dari direktori utama proyek:

```bash
python3 praktik/utilitas_matematika.py
```

## Struktur Fungsi

Fungsi-fungsi dalam `praktik/utilitas_matematika.py` adalah:

| Nama fungsi | Parameter | Nilai return / tugas |
|---|---|---|
| `luas_persegi_panjang(p, l)` | `p`: panjang, `l`: lebar | Mengembalikan hasil perkalian panjang dan lebar. |
| `luas_segitiga(a, t)` | `a`: alas, `t`: tinggi | Mengembalikan setengah dari hasil perkalian alas dan tinggi. |
| `jumlah_n(n)` | `n`: batas bilangan bulat | Mengembalikan jumlah bilangan dari 1 sampai `n`. |
| `faktorial(n)` | `n`: bilangan bulat | Mengembalikan hasil perkalian bilangan 1 sampai `n`. |
| `tampilkan_menu()` | Tidak ada | Menampilkan pilihan menu; tidak mengembalikan nilai. |
| `main()` | Tidak ada | Mengatur alur program, membaca input, memanggil fungsi yang sesuai, dan menampilkan hasil; tidak mengembalikan nilai. |

## Hasil Pengujian

| Operasi | Input | Hasil yang diharapkan | Hasil aktual | Status |
|---|---|---|---|---|
| Luas persegi panjang | `p=8, l=5` | `40` | `40.0` | Lulus |
| Luas segitiga | `a=10, t=6` | `30.0` | `30.0` | Lulus |
| Jumlah `1..n` | `n=10` | `55` | `55` | Lulus |
| Faktorial | `n=5` | `120` | `120` | Lulus |
| Faktorial | `n=0` | `1` | `1` | Lulus |
| Luas persegi panjang | `p=0, l=5` | `0` | `0.0` | Lulus |
| Luas segitiga | `a=4, t=3` | `6.0` | `6.0` | Lulus |
| Jumlah `1..n` | `n=0` | `0` | `0` | Lulus |
| Jumlah `1..n` dengan nilai negatif | `n=-1` | Pesan bahwa `n` harus berupa bilangan bulat non-negatif | `Error: n harus berupa bilangan bulat non-negatif.` | Lulus |
| Pilihan menu tidak valid | `pilihan=9` | `Pilihan menu tidak valid.` | `Pilihan menu tidak valid.` | Lulus |

## Refleksi

Perhitungan luas persegi panjang menjadi lebih sederhana di dalam `main()` karena rumus perkalian panjang dan lebar dipisahkan ke fungsi `luas_persegi_panjang()`. `main()` cukup mengumpulkan input, memanggil fungsi, lalu menampilkan hasil. Fungsi perhitungan juga dapat digunakan kembali tanpa menulis ulang rumus.
