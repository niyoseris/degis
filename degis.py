import sys
import os

dosyalar = os.listdir(".")

for dosya in dosyalar:
    if str(dosya).endswith('.srt'):
        acilacak = dosya
        kaydedilecek = str(dosya) + "jubiju"

ac = open(acilacak, 'r')
bak = ac.read()
degis = bak.replace('ý','ı').replace('ð', 'ğ').replace('þ', 'ş').replace('Ý','İ').replace('Þ', 'Ş').replace('Ð', 'Ğ')
ac.close()

kaydet = open(kaydedilecek, 'w')
kaydet.write(degis)
kaydet.close()

os.system('mv ' + kaydedilecek + " " +  acilacak)

print('ne uçan ne gaçan.')

#altyazı dosyasının bulunduğu klasörde çalıştırın yeter.
#örnek kullanım
#python3 degis.py
#sevgiyle.
