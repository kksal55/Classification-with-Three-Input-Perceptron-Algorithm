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

rwerrfsdfsdfsdfsdfsdfsdfsdfsd




This project trains a Perceptron model and makes predictions on test data.

## Project Functionality

This code implements the Perceptron learning algorithm and trains a model using a given dataset. It also makes predictions on test data and calculates the accuracy of the predictions.

## Usage

To use this project, you will need a dataset. The dataset can be in CSV format or a similar format.

```python
txt_yukle(file): 
    """
    This function loads a CSV file and converts all the data into floating-point numbers.
    """
    ...

tahmin_et(row, weights):
    """
    This function makes predictions for each data point.
    """
    ...

agirliklari_egit(training_data, learning_rate, epoch_count, weights):
    """
    This function updates the weights of the model using the training data.
    """
    ...

test_verisini_test_et(test_data, weights):
    """
    This function makes predictions on the test data.
    """
    ...

test_dataset(test_data, weights):
    """
    This function calculates the accuracy of the predictions.
    """
    ...

k_fold_cross_validation(dataset, k, learning_rate, n_epoch, weights):
    """
    This function evaluates the accuracy of the model using k-fold cross validation.
    """
    ...

kullanıcıdan_agirlik_al():
    """
    This function prompts the user to enter the bias value and initial weights.
    """
    ...

perceptron_veri_dogrulama(learning_rate, epoch_count, weights):
    """
    This main function trains and tests the Perceptron model using the provided functions.
    """
    ...
