#  TextClassificationAndSearching
 
<h2> 1) Projenin Geliştirilme Aşamaları </h2>

Projenin geliştirilmesinde ilk olarak girilen metinleri konularına göre sınıflandıracak yapay zekâ modelinin eğitimi için bir veri seti araştırılması yapılmıştır. Projede Kaggle [1] sitesindeki 7 farklı kategoriden ('Dünya', 'Ekonomi', 'Kültür - Tarih', 'Sağlık', 'Siyaset', 'Spor', 'Teknoloji') oluşan veri seti kullanılmıştır. Yapay zekâ modelinin eğitimi için ücretsiz GPU desteği sağlayan Google Colaboratory ortamı tercih edilmiştir. Veri setinde gerekli ön işlemeler yapılmıştır. Veri, noktalama işaretleri, sayılardan ve bağlaçlardan arındırılmıştır.  Model eğitimi için “Logistic Regression” algoritması tercih edilmiştir. Veri seti boyutu çok büyük olmadığından dolayı yaklaşık olarak %83 doğruluk elde edilebilmiştir.
Eğitim tamamlandıktan sonra kaydedilen model dosyası kullanıcıdan alınan metinler üzerinde sınıflandırma yapılarak test edilmiştir. Metin içerisindeki en çok frekansa sahip kelimeler alt başlıklar olarak kabul edilmiştir. Elde edilen bu alt başlıklar ile Wikipedia sitesinde araştırma yapılmıştır ve kullanıcıya bilgi verilmiştir. Wikipedia sitesinde araştırma yapılmasının sebebi Google’da bulunan web sitelerinin yapılarının birbirinden farklı olmasıdır. Farklı yapılardaki sitelerden verileri çekmek için verinin bulunduğu etiketleri değiştirmek gerekmektedir. Bu nedenle tek bir site üzerinden araştırma sonuçlarının alınmasına karar verilmiştir. Son olarak elde edilen tüm bilgiler Microsoft SQL Server veri tabanında tablolara kayıt edilmiştir.

<h2> 2) Projede Elde Edilen Çıktılar </h2>

Kullanıcıya sunulan menü ekranı Şekil 1’de görülmektedir.
<div align="center">
    <img src="https://github.com/hediyeorhan/TextClassificationAndSearching/assets/59260491/c0564213-7297-4c79-9987-7d456f2389ba" alt="Şekil 1: Kullanıcıya sunulan menü ekranı">
</div>
<div align="center">
    <p>Şekil 1: Kullanıcıya sunulan menü ekranı</p>
</div>

Girilen metnin konusu Şekil 2, Şekil 3, Şekil 4 ve Şekil 5’te görüldüğü gibi tahmin edilmektedir.

<div align="center">
    <img src="https://github.com/hediyeorhan/TextClassificationAndSearching/assets/59260491/3c850587-678b-42e7-9869-6fcb640ada82" alt="Şekil 2: Girilen metnin konusunun belirlenmesi">
</div>
<div align="center">
    <p>Şekil 2: Girilen metnin konusunun belirlenmesi</p>
</div>

<div align="center">
    <img src="https://github.com/hediyeorhan/TextClassificationAndSearching/assets/59260491/479a794a-8ba3-4e43-8c06-98363f45ce6f" alt="Şekil 3: Girilen metnin konusunun belirlenmesi">
</div>
<div align="center">
    <p>Şekil 3: Girilen metnin konusunun belirlenmesi</p>
</div>

<div align="center">
    <img src="https://github.com/hediyeorhan/TextClassificationAndSearching/assets/59260491/a7282353-a6ad-47e5-8155-2eddf076f47b" alt="Şekil 4: Girilen metnin konusunun belirlenmesi">
</div>
<div align="center">
    <p>Şekil 4: Girilen metnin konusunun belirlenmesi</p>
</div>

<div align="center">
    <img src="https://github.com/hediyeorhan/TextClassificationAndSearching/assets/59260491/41aacbe3-9bc7-45c6-8a3e-a35cf929fcd9" alt="Şekil 5: Girilen metnin konusunun belirlenmesi">
</div>
<div align="center">
    <p>Şekil 5: Girilen metnin konusunun belirlenmesi</p>
</div>

Şekil 6’da metinlerin alt başlıkları belirlenerek bunlar ile ilgili Wikipedia sitesinde yapılan arama sonuçlarının elde edilmesi görülmektedir. Burada ‘Ebru Sanatı’ ile ilgili girilen bir metnin ve ‘Tarih’ ile ilgili girilen bir metnin alt başlıkları belirlenerek ‘Ebru Tarihi’ ile ilgili bir araştırma yapılmıştır.

<div align="center">
    <img src="https://github.com/hediyeorhan/TextClassificationAndSearching/assets/59260491/a4abe9c0-a232-4b7c-8a77-2219caca60b6" alt="Şekil 6: Alt başlıklara göre arama yapılması">
</div>
<div align="center">
    <p>Şekil 6: Alt başlıklara göre arama yapılması</p>
</div>


Şekil 7’de metinlerin alt başlıkları belirlenerek bunlar ile ilgili Wikipedia sitesinde yapılan arama sonuçlarının elde edilmesi görülmektedir.

<div align="center">
    <img src="https://github.com/hediyeorhan/TextClassificationAndSearching/assets/59260491/7941ff0d-7215-4321-b6d3-44671c33379e" alt="Şekil 7: Alt başlıklara göre arama yapılması">
</div>
<div align="center">
    <p>Şekil 7: Alt başlıklara göre arama yapılması</p>
</div>


Şekil 8’ de metinlerin sınıflarının kayıt edildiği veri tabanı tablosu, Şekil 9’da arama sonuçlarının kayıt edildiği veri tabanı tablosu görülmektedir.

<div align="center">
    <img src="https://github.com/hediyeorhan/TextClassificationAndSearching/assets/59260491/a447cc76-a29c-426f-b19f-03f0522c7ac9" alt="Şekil 8: Metinlerin sınıflarının ve alt başlıklarının bulunduğu veri tabanı tablosu">
</div>
<div align="center">
    <p>Şekil 8: Metinlerin sınıflarının ve alt başlıklarının bulunduğu veri tabanı tablosu</p>
</div>

<div align="center">
    <img src="https://github.com/hediyeorhan/TextClassificationAndSearching/assets/59260491/91ce13e6-aac0-486e-877e-a8b9dae6290b" alt="Şekil 9: Arama sonuçlarının bulunduğu veri tabanı tablosu">
</div>
<div align="center">
    <p>Şekil 9: Arama sonuçlarının bulunduğu veri tabanı tablosu</p>
</div>


<h2> KAYNAKÇA </h2>
[1] Kaggle Veri Seti. Available: https://www.kaggle.com/code/erdal002/turkish-text-classification/input

 
