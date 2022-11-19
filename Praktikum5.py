data = []
while True:
    nama = input("Masukan nama = ")
    nim = input("Masukan NIM = ")
    tugas = int(input("Masukan nilai tugas = "))
    uts = int(input("Masukan nilai UTS = "))
    uas = int(input("Masukan nilai UAS = "))


    hasil_1 = tugas *30/100
    hasil_2 = uts *35/100
    hasil_3 = uas *35/100
    akhir = hasil_1 + hasil_2 + hasil_3

    dataBaru = [nama, nim, tugas, uts, uas,akhir]
    data.append(dataBaru)
    

    
    print("="*105)
    print("NO.\t| Nama\t\t\t| NIM\t\t| Tugas\t\t| UTS\t\t| UAS\t\t| Akhir|")
    print("="*105)
    for index, info  in enumerate (data):
        print(f"{index+1}\t| {info[0]}\t| {info[1]}\t| {info[2]}\t\t| {info[3]}\t\t| {info[4]}\t\t| {info[5]}|")
    print("="*105)

    user = input("Apakah ingin menambahkan data lagi? (yes/no) = ")
    if user == "no":
        break
print("Terimakasih telah menggunakan program ini")