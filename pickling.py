import pickle

# Имя файла в котором мы сохраняем обьекст
shoplistfile = 'shoplist.data'
# Список покупок
shoplist = ['яблоки', 'манго', 'морковь']

# Запись в файл
f = open(shoplistfile, 'wb')
pickle.dump(shoplist, f) # помещаем обьект в файл
f.close()

del shoplist # Уничтожаем переменную shoplist

# Считываем из хранилища
f = open(shoplistfile, 'rb')
storedlist = pickle.load(f) # Загружаем обьект из файла
print(storedlist)