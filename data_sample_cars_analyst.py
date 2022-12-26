# -*- coding: utf-8 -*-
"""Data Sample Cars Analyst.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Ktef9nAGW7idTvpSc3zq4hBQIrhPZD4o

# **1. Bacalah file csv ‘cars_sampled.csv’**

Ditampilkan sebagai berikut:
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv('cars_sampled.csv')
data

"""#**2. Buatlah diagram batang yang menampilkan proporsi (dalam persen) dari gearbox yang digunakan untuk masing-masing jenis mobil. Sebagai contoh tampilan adalah sebagai gambar dibawah ini. Lengkapi grafik sesuai dengan keterangan-keterangan yang memadai. Anda juga bisa memodifikasi warna, tampilan sesuai dengan keinginan anda.**

Ditampilkan sebagai berikut:
"""

data_diagram=pd.crosstab(data.vehicleType, data.gearbox)
data_diagram['pct_automatic']=(data_diagram['automatic']/data_diagram.sum(axis=1))*100
data_diagram['pct_manual']=(data_diagram['manual']/data_diagram.sum(axis=1))*100
data_diagram

data_diagram_fix=data_diagram.plot.bar(y=['pct_automatic','pct_manual'], figsize=(15,5), colormap='prism')
for p in data_diagram_fix.patches:
    width, height = p.get_width(), p.get_height()
    x, y = p.get_xy() 
    data_diagram_fix.text(x+width/2,
            y+height+3, 
            '{:.0f} %'.format(height), 
            horizontalalignment='center', 
            verticalalignment='center')
plt.title('Persentase Gearbox')    
plt.show()

"""# **3. Buatlah diagram boxplot yang menampilkan harga mobil jenis mobil kecil (‘small car’) pada masing-masing tahun. Filter data dengan ketentuan berikut: Harga lebih dari 0 dan kurang dari 35000, tahunnya antara 2007 sampai 2016. Lengkapi grafik sesuai dengan keterangan-keterangan yang memadai. Anda juga bisa memodifikasi warna, tampilan sesuai dengan keinginan anda.**

Ditampilkan sebagai berikut:
"""

data_boxplot=data[data['vehicleType']=='small car']
data_boxplot1=data_boxplot[data['yearOfRegistration']>=2007][data['yearOfRegistration']<=2016]
data_boxplot2=data_boxplot1[data['price']>0][data['price']<35000]
data_boxplot_fix=data_boxplot2[['vehicleType', 'yearOfRegistration','price']]
data_boxplot_fix

sns.boxplot(x="yearOfRegistration", y="price", data=data_boxplot_fix)
plt.title('Harga dan Tahun Registrasi Mobil Jenis Small Car')
sns.set(rc={'figure.figsize':(8,5)}, font_scale=1.5, style='whitegrid')
plt.show()

"""# **4. Buatlah 2 plot bersampingan dengan ketentuan sebagai berikut: Filter data dengan ketentuan harga lebih dari 0 dan kurang dari 50000 , powerPS lebih dari 0 dan kurang dari 600, dan jenis mobil adalah suv . Kedua plot memiliki sumbu tegak berupa harga, sedangkan pada plot pertama sumbu mendatarnya adalah powerPS, sedangkan sumbu kedua menampilkan tahun registrasi mobil. Lengkapi grafik sesuai dengan keterangan-keterangan yang memadai. Anda juga bisa memodifikasi warna, tampilan sesuai dengan keinginan anda.**

Ditampilkan sebagai berikut:
"""

df = data
pd.DataFrame(df, columns=['powerPS', 'price', 'vehicleType', 'yearOfRegistration'])

suv = df.iloc[:, :19][df.vehicleType == 'suv'][(df['price'] > 0) & (df['price']  < 50000)][(df['powerPS'] > 0) & (df['powerPS']  < 600)]
suv

suv1 = pd.DataFrame(suv, columns=['powerPS', 'price', 'vehicleType', 'yearOfRegistration'])
suv1

fig, axes = plt.subplots(1, 2, figsize = (15,5))
axes[0].scatter(suv1['powerPS'], suv1['price'])
axes[0].set_xlabel('powerPS')
axes[0].set_ylabel('price')
axes[0].grid()
plt.xlim(0, 500)
plt.ylim(0, 50000)

axes[1].scatter(suv1['yearOfRegistration'], suv1['price'])
axes[1].set_xlabel('yearOfRegistration')
axes[1].set_ylabel('price')
axes[1].grid()
plt.xlim(2002, 2016)
plt.ylim(0, 50000)

"""# **5. Buatlah satu plot pengolahan data dengan ketentuan (1) Bukan grafik seperti nomor 2,3,dan 4. (2) Menggunakan variabel yang menurut anda memiliki korelasi/keterkaitan dengan harga mobil. (3) Dilengkapi dengan keterangan grafik yang memadai.**

Ditampilkan sebagai berikut:
"""

dataframe = data
baru1 = pd.DataFrame(dataframe, columns=['seller', 'price', 'fuelType'])
baru1

"""data menampilkan harga, jenis bensin dan penjualnya (secara komersial atau privat), kemudian akan dicari korelasinya dengan harga mobil"""

baru2 = baru1.groupby(['seller', 'fuelType']).mean()
baru2

"""data menampilkan rata-rata harga setiap jenis bensin yang dijual secara komersial atau privat"""

baru2.plot(kind="barh", fontsize=10, colormap='Paired')

"""dibentuk grafik yang menampilkan jenis bensin dan penjualannya, dimana korelasinya dengan harga mobil disini adalah ketika ada yang ingin membeli suatu mobil dengan jenis bensin petrol, diesel, hybrid, dll maka dapat dilihat perbandingan harganya, jika ingin yang murah tinggal dicek saja antara komersial atau privat."""