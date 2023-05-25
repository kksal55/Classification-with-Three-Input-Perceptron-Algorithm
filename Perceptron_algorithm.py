from csv import reader
from math import sqrt
import random
from collections import Counter 
from statistics import mean

""" Toplam değer(x1,x2,x3) 1.5 ten küçükse 0, büyükse 1 değeri çıkar"""

# CSV dosyasını yükleyip, içerisindeki verileri float tipine dönüştüren fonksiyon
def txt_yukle(dosya):
    veri = list()
    with open(dosya, 'r') as dosya:
        csv_okuyucu = reader(dosya)
        for satir in csv_okuyucu:
            if not satir:
                continue
            veri.append(satir)
    for satir in veri:
        for i in range(len(veri[0])):
            satir[i] = float(satir[i])
    return veri

# Her veri noktası için tahmin yapan fonksiyon
def tahmin_et(satir, agirliklar):
    aktivasyon = 0
    if(len(satir) == 5):
        for i in range(len(satir)-1):
            aktivasyon += agirliklar[i] * satir[i]  # ağırlık * veri satırındaki sütun
    else:
        for i in range(len(satir)):
            aktivasyon += agirliklar[i] * satir[i]  # ağırlık * veri satırındaki sütun
    if aktivasyon > 0.0:
        return 1.0
    else:
        return 0

# Ağırlıkları güncellemek için kullanılan fonksiyon
def agirliklari_egit(egitim_verisi, ogrenme_hizi, epoch_sayisi, agirliklar):
    epoch = 0
    toplam_hata = float('inf')
    while toplam_hata != 0 and epoch < epoch_sayisi:  # toplam hata 0 olana veya maksimum epoch sayısına ulaşana kadar hesapla
        toplam_hata = 0.0
        for satir in egitim_verisi:
            tahmin = tahmin_et(satir, agirliklar)
            hata = satir[-1] - tahmin
            #print("satir:", satir)
            #print("satir beklenen:", satir[-1], "tahmin:", tahmin, "=>> hata =", hata)

            if hata != 0:
                toplam_hata += 0.5 * hata**2
                for i in range(len(satir)-1):
                    agirliklar[i] = agirliklar[i] + ogrenme_hizi * hata * satir[i]  
                #print("Ağırlıklar", ["%.4f" % agirlik for agirlik in agirliklar]) #agirlik guncellemesi sonrası yeni ağırlıkları yazıdr

        print('>epoch=%d, ogrenme_hizi=%.3f, toplam_hata=%.3f' % (epoch, ogrenme_hizi, toplam_hata)) #her epoch sonrasi değerleri yazdır
        print("Ağırlıklar", ["%.4f" % agirlik for agirlik in agirliklar])
        epoch += 1
    return agirliklar

# Test verisini test edip, tahminleride ekrana yazan fonk.
def test_verisini_test_et(test_verisi, agirliklar):
    for satir in test_verisi:
        tahmin = tahmin_et(satir, agirliklar)
        print(satir, "DEĞER:", tahmin, "==> değerler toplamı", f"{sum(satir)-1:.2f}")

# Doğru tahminlerin yüzdesini hesaplayan fonk.
def test_dataset(test_verisi, weights):
    dogru_tahmin = 0
    total_tahmin = len(test_verisi)
    for row in test_verisi:
        tahmin = tahmin_et(row, weights)
        if tahmin == row[-1]:
            dogru_tahmin += 1
    ortalama = dogru_tahmin / total_tahmin
    return ortalama

# K-fold cross validation yaparak modelin doğruluğunu değerlendiren fonksiyon
def k_fold_cross_validation(dataset, k, ogrenme_hizi, n_epoch,agirliklar):
    random.shuffle(dataset)
    satir_Sayisi = len(dataset) // k
    dogru_orani = []
    for i in range(k):
        test_edilecek_data = dataset[i * satir_Sayisi: (i+1) * satir_Sayisi]
        egitilecek_data = dataset[:i * satir_Sayisi] + dataset[(i+1) * satir_Sayisi:]
        #agirliklar = [random.uniform(-1, 1) for _ in range(len(egitilecek_data[0]))]
        agirliklar = agirliklari_egit(egitilecek_data, ogrenme_hizi, n_epoch, agirliklar)
        accuracy = test_dataset(test_edilecek_data, agirliklar)
        dogru_orani.append(accuracy)
    genelOrtalama = mean(dogru_orani)
    return genelOrtalama

# Kullanıcıdan  bias değerini ve başlangıç ağırlıklarını alacak olan fonksiyon
def kullanıcıdan_agirlik_al():
    agirliklar_input = input("Lütfen virgülle ayrılmış şekilde bias değerini ve başlangıç ağırlıklarını girin (örneğin: 1.0,1.0,1.0,1.0): ")
    agirliklar = [1.0, 1.0, 1.0, 1.0]  # Varsayılan ağırlık değerleri
    if agirliklar_input:
        input_degerleri = agirliklar_input.split(",")
        if len(input_degerleri) == 4:
            try:
                agirliklar = [float(w) for w in input_degerleri]
            except ValueError:
                pass  # Geçersiz sayısal değerler olduğunda varsayılan değerleri kullanmaya devam et
                print("Geçersiz değerler girildi. Varsayılan ağırlık değerleri atandı")
    return agirliklar

# def random_data_olustur(veri_sayisi):
#         data = []
#         for _ in range(veri_sayisi):
#             x1 = random.uniform(0.1, 1.0)
#             x2 = random.uniform(0.1, 1.0)
#             x3 = random.uniform(0.1, 1.0)
#             total = x1 + x2 + x3
#             if total < 1.5:
#                 label = 0
#             else:
#                 label = 1
#             data.append([1, f"{x1:.1f}", f"{x2:.1f}", f"{x3:.1f}", label])
#         return data
    

# Main fonksiyon, yukarıdaki tüm fonksiyonları kullanarak perceptron modelini eğitir ve test eder
def perceptron_veri_dogrulama(ogrenme_hizi, epoch_sayisi, agirliklar):


    # random_data = random_data_olustur(100)
    # for row in random_data:
    #     print(','.join(str(value) for value in row))
    
    egitim_verisi = list()
    egitim_verisi = txt_yukle("egitim_verisi.txt")
    test_verisi = list()
    test_verisi = txt_yukle("test_verisi.txt")
    for j in test_verisi:
        del j[4]
    print(test_verisi)
    agirliklar = agirliklari_egit(egitim_verisi, ogrenme_hizi, epoch_sayisi, agirliklar)
    test_verisini_test_et(test_verisi, agirliklar)

ogrenme_hizi = 0.01
epoch_sayisi = 200
agirliklar = kullanıcıdan_agirlik_al()  # agirliklar[0] bias olarak kullanılır



dataset = txt_yukle("egitim_verisi.txt")
# ortalama_dogru_orani = k_fold_cross_validation(dataset, 5, ogrenme_hizi, epoch_sayisi,agirliklar)
# print("Ortalama Doğruluk:",  f"{ortalama_dogru_orani:.2f}")

perceptron_veri_dogrulama(ogrenme_hizi, epoch_sayisi, agirliklar)

