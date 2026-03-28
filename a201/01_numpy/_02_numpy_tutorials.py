import numpy as np


print("Numpy  Sürümü : ", np.__version__)

# Not: Liste benzerdir ancak iç yapı farklıdır
# NOTTTTT: Numpy array, sayısal işelmler için daha uygundur

# Liste
normal_liste= [20,10,30,40,50]
print(normal_liste)

# Numpy Liste
numpy_liste =np.array([20,10,30,40,50])
print(numpy_liste)

dizi = np.array([20,10,30,40,50])
print(dizi[0])  # ilk eleman
print(dizi[1])  # ikinci eleman
print(dizi[-1])  # son eleman
print(dizi[-2])  # son eleman bir önceki

# Toplu işlemler
print(dizi+15)
print(dizi*15)
print(dizi/15)


# Temel İstatistik (Math)
print("Toplam: ", np.sum(dizi))
print("Ortalama: ", np.mean(dizi))
print("En küçük: ", np.min(dizi))
print("En büyük: ", np.max(dizi))
print("Standart Sapma: ", np.std(dizi))

