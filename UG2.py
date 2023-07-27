import math

def hitung_volume_tabung(diameter, tinggi):
    jari_jari = diameter / 2
    volume = math.pi * jari_jari ** 2 * tinggi
    return volume

def hitung_volume_kubus(sisi):
    volume = sisi ** 3
    return volume

def hitung_volume_balok(panjang, lebar, tinggi):
    volume = panjang * lebar * tinggi
    return volume

def main():
    print("==================== KALKULATOR CERDAS ====================")
    print("Pilihlah bangun yang ingin anda hitung (input angka saja):")
    print("1. Tabung")
    print("2. Kubus")
    print("3. Balok")

    pilihan = int(input(">> "))

    if pilihan == 1:
        diameter = int(input("Masukkan diameter (cm) : "))
        tinggi = int(input("Masukkan tinggi (cm) : "))
        volume = hitung_volume_tabung(diameter, tinggi)
        print(f"Volume tabung adalah {volume:.2f} cm")
    elif pilihan == 2:
        sisi = int(input("Masukkan panjang sisi (cm) : "))
        volume = hitung_volume_kubus(sisi)
        print(f"Volume kubus adalah {volume:.2f} cm")
    elif pilihan == 3:
        panjang = int(input("Masukkan panjang (cm) : "))
        lebar = int(input("Masukkan lebar (cm) : "))
        tinggi = int(input("Masukkan tinggi (cm) : "))
        volume = hitung_volume_balok(panjang, lebar, tinggi)
        print(f"Volume balok adalah {volume:.2f} cm")
    else:
        print("Inputan yang anda masukkan salah !!")

if __name__ == "__main__":
    main()
