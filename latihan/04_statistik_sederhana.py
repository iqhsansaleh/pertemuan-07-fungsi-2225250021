def statistik(data):
    total = 0
    minimum = data[0]
    maksimum = data[0]
    
    for x in data:
        total += x
        if x < minimum:
            minimum = x
        if x > maksimum:
            maksimum = x
            
    rata = total / len(data)
    return minimum, maksimum, rata

# Memanggil fungsi dengan data list
mn, mx, rt = statistik([70, 80, 65, 90, 75])

# Menampilkan hasil
print(f"Nilai Minimum : {mn}")
print(f"Nilai Maksimum: {mx}")
print(f"Nilai Rata-rata: {rt}")