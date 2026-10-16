def jumlah_n(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    return total

nilai_n = [1, 5, 10, 100]

print("n  |  Hasil Fungsi  |  Hasil Rumus n(n+1)/2  |  Status")
print("-" * 50)

for n in nilai_n:
    hasil_fungsi = jumlah_n(n)
    hasil_rumus = n * (n + 1) // 2
    status = "Sama" if hasil_fungsi == hasil_rumus else "Beda"
    
    print(f"{n:<3} | {hasil_fungsi:<14} | {hasil_rumus:<22} | {status}")