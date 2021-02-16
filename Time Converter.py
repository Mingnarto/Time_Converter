# Soal 1 - Time Converter (30 Poin)
# Buatlah sebuah return function dengan 1 argumen yang akan menerima inputan bilangan integer(Seconds). Dan akan menghasilkan output string dengan format waktu ("HH:MM:SS").
# HH : Hours, 2 digits, range: 00 - 99
# MM : Minutes, 2 digits, range: 00 - 59
# SS : Seconds, 2 digits, range: 00 - 59
# Case Flow: Saat dieksekusi, program akan mencetak nilai return function.

# def timeConverter(seconds):
#       .....
 
# Masukkan detik : 3600
# Konversi : 01:00:00

# Masukkan detik : 3665
# Konversi : 01:01:05

# Condition: Program hanya menerima angka bulat, dengan nilai maksimal 359999,
# jika user memasukkan nilai lebih dari 359999, bilangan desimal,
# bilangan negatif, maupun memasukkan string akan keluar notifikasi. Invalid Input

# Masukkan detik : ujian
# Invalid Input!

# Masukkan detik : 20.5
# Invalid Input!

# Masukkan detik : -20
# Invalid Input!

print('-'*100)
ask = input('Masukkan detik: ',)

try:
    time = int(ask)
except:
    print('Invalid Input')
    quit()

if time > 359999 or time <= 0:
    print('Invalid Input')
    quit()

else:
    def timeConverter(time):
        hour = time // 3600
        hours = str(hour)

        hourRemain = time % 3600
        minu = hourRemain // 60
        minute = str(minu)

        sec = hourRemain % 60
        second = str(sec)

        return 'Konversi: ' + hours + ':' + minute + ':' + second

print(timeConverter(time))