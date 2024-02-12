#!/usr/bin/env python
# coding: utf-8

# In[3]:


get_ipython().run_line_magic('matplotlib', 'inline')

import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0,10)
y = np.sin(x)
z = np.cos(x)

plt.plot(x,y,'b',x,z,'r')
plt.xlabel('Radians');
plt.ylabel('Value');
plt.title('Plotting Demonstration')
plt.legend(['sin','cos'])
plt.grid()


# In[20]:


harga_awal = 650000
harga_sekarang = 685000
berat_emas_awal = 25
keuntungan_awal = (harga_sekarang - harga_awal)*berat_emas_awal
persentase_keuntungan_awal = (keuntungan_awal/(harga_awal*berat_emas_awal))*100


print ("Rp.", keuntungan_awal)
print (round(persentase_keuntungan_awal), "%")


harga_setelah_pembelian_pertama = 685000
harga_setelah_pembelian_kedua = 715000
berat_emas_dibeli_kedua = 15
total_emas = berat_emas_awal + berat_emas_dibeli_ked
keuntungan_sekarang = keuntungan_awal + ((harga_setelah_pembelian_kedua - harga_setelah_pembelian_pertama) * total_emas)
persentase_keuntungan_kedua = (keuntungan_sekarang/(harga_awal*berat_emas_awal + 
                                                    harga_setelah_pembelian_pertama*berat_emas_dibeli_kedua))*100


print ("Rp.", keuntungan_sekarang)
print (round(persentase_keuntungan_kedua), "%")


# In[29]:


uang1 = 200000000
bunga = 0.1
uang_akhir = 400000000
tahun_awal = 0
n = 1
periode = 1
uang_akhir = int(uang1*(1+bunga/n)**(n*periode))
print("bunga tahun pertama : ", uang_akhir)


# In[30]:


uang1 = 200000000
bunga = 0.1
uang_akhir = 400000000
tahun_awal = 0
n = 1
periode = 2
uang_akhir =int( uang1*(1+bunga/n)**(n*periode))
print("bunga tahun kedua : ", uang_akhir)


# In[31]:


uang1 = 200000000
bunga = 0.1
uang_akhir = 400000000
tahun_awal = 0
n = 1
periode = 3
uang_akhir = int(uang1*(1+bunga/n)**(n*periode))
print("bunga tahun ketiga : ", uang_akhir)


# In[33]:


uang1 = 200000000
bunga = 0.1
uang_akhir = 400000000
tahun_awal = 0
n = 1
periode = 9
uang_akhir = int(uang1*(1+bunga/n)**(n*periode))
print("bunga tahun kesembian : ", uang_akhir)


# In[34]:


uang1 = 200000000
bunga = 0.1
uang_akhir = 400000000
tahun_awal = 0
n = 1
periode = 8
uang_akhir = int(uang1*(1+bunga/n)**(n*periode))
print("bunga tahun delapan : ", uang_akhir)


# In[35]:


uang1 = 200000000
bunga = 0.1
uang_akhir = 400000000
tahun_awal = 0
n = 1
periode = 7
uang_akhir = int(uang1*(1+bunga/n)**(n*periode))
print("bunga tahun ketuju : ", uang_akhir)


# In[ ]:




