import pandas as pd


print("Pandas  Sürümü : ", pd.__version__)

# Series: Pandas
numbers= pd.Series([10,30,20,50,40])
print(numbers)

# DataFrame: Küçük bir tablo
data = {
    "Ad":["Ali","Fatma","Mehmet","Ayşe","Mustafa","Nezihat"],
    "Soyad":["soyad1","soyad2","soyad3","soyad4","soyad5","soyad6"],
    "Yas":[10,20,30,40,50,60],
}

print("\n##### DATAFRAME ##########")
person= pd.DataFrame(data)
print(person)

print("\n##### GENEL BILGI ##########")
print(person.info())


# Satırları getir

# İlk 5 satırı getir
print("\n##### HEAD ##########")
print(person.head())

# İlk 2 satırı getir
print("\n##### HEAD(2) ##########")
print(person.head(2))

# Son 5 satırı getir.
print("\n##### TAIL ##########")
print(person.tail())

#
print("\n##### SÜTUN ##########")
print(person.columns)

print("\n##### SÜTUN TÜRLERİ ##########")
print(person.dtypes)

print("\n##### SÜTUN-1 ##########")
print(person["Ad"])
print(person["Soyad"])
print(person["Yas"])

print("\n##### SÜTUN-2 ##########")
print(person[["Ad", "Soyad"]])
#print(person[["Ad", "Soyad","Yas"]])

print("\n##### SATIR-1 ##########")
print(person.iloc[0])

print("\n##### SATIR-2 ##########")
print(person.iloc[0:2])


print("\n##### FİLTRELEME ##########")
print(person[person["Yas"]>40])

print("\n##### YENİ SÜTUN EKLE ##########")
person["Maas"]=[100,200,300,400,500,600]
print(person)