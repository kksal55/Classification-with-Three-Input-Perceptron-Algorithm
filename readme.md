# Perceptron Modeli İle Sınıflandırma

Bu proje, bir Perceptron modelini eğitmek ve test verilerinde tahminlerde bulunmak için kullanılır.

## Projenin İşlevselliği

Bu kod, Perceptron öğrenme algoritmasını uygular ve verilen bir veri setini kullanarak bir model eğitir. Ayrıca, verilen test verileri üzerinde tahminlerde bulunur ve doğru tahmin yüzdesini hesaplar.

## Kullanım

Bu projeyi kullanmak için öncelikle bir veri setine ihtiyacınız olacaktır. Bu veri seti, bir CSV dosyası veya benzeri bir formatta olabilir.

```python
txt_yukle(dosya): 
    """
    Bu fonksiyon, bir CSV dosyasını yükler ve dosyanın içindeki tüm verileri float tipine dönüştürür.
    """
    ...

tahmin_et(satir, agirliklar):
    """
    Bu fonksiyon, her veri noktası için bir tahmin yapar.
    """
    ...

agirliklari_egit(egitim_verisi, ogrenme_hizi, epoch_sayisi, agirliklar):
    """
    Bu fonksiyon, eğitim verilerini kullanarak modelin ağırlıklarını günceller.
    """
    ...

test_verisini_test_et(test_verisi, agirliklar):
    """
    Bu fonksiyon, test verisini alır ve her veri noktası için bir tahmin yapar.
    """
    ...

test_dataset(test_verisi, weights):
    """
    Bu fonksiyon, doğru tahminlerin yüzdesini hesaplar.
    """
    ...

k_fold_cross_validation(dataset, k, ogrenme_hizi, n_epoch,agirliklar):
    """
    Bu fonksiyon, k-fold cross validation kullanarak modelin doğruluğunu değerlendirir.
    """
    ...

kullanıcıdan_agirlik_al():
    """
    Bu fonksiyon, kullanıcıdan bias değerini ve başlangıç ağırlıklarını alır.
    """
    ...

perceptron_veri_dogrulama(ogrenme_hizi, epoch_sayisi, agirliklar):
    """
    Bu ana fonksiyon, yukarıdaki tüm fonksiyonları kullanarak Perceptron modelini eğitir ve test eder.
    """
    ...


