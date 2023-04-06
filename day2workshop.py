vize = int(input("Vize notunuzu giriniz: "))
final = int(input("Final notunuzu giriniz: "))
ortalama = (vize * 0.4) + (final * 0.6) 

if final<40:
    print("Kaldınız")
if ortalama<50:
    print("Ortalamadan kaldınız")
elif vize>final*2:
    print("Malasef kaldınız")

else:
    print("Tebrikler")
