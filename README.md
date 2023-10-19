#  TextClassificationAndSearching
 
<h2> 1) Projenin Geliştirilme Aşamaları </h2>

Projenin geliştirilmesinde ilk olarak girilen metinleri konularına göre sınıflandıracak yapay zekâ modelinin eğitimi için bir veri seti araştırılması yapılmıştır. Projede Kaggle [1] sitesindeki 7 farklı kategoriden ('Dünya', 'Ekonomi', 'Kültür - Tarih', 'Sağlık', 'Siyaset', 'Spor', 'Teknoloji') oluşan veri seti kullanılmıştır. Yapay zekâ modelinin eğitimi için ücretsiz GPU desteği sağlayan Google Colaboratory ortamı tercih edilmiştir. Veri setinde gerekli ön işlemeler yapılmıştır. Veri, noktalama işaretleri, sayılardan ve bağlaçlardan arındırılmıştır.  Model eğitimi için “Logistic Regression” algoritması tercih edilmiştir. Veri seti boyutu çok büyük olmadığından dolayı yaklaşık olarak %83 doğruluk elde edilebilmiştir.
Eğitim tamamlandıktan sonra kaydedilen model dosyası kullanıcıdan alınan metinler üzerinde sınıflandırma yapılarak test edilmiştir. Metin içerisindeki en çok frekansa sahip kelimeler alt başlıklar olarak kabul edilmiştir. Elde edilen bu alt başlıklar ile Wikipedia sitesinde araştırma yapılmıştır ve kullanıcıya bilgi verilmiştir. Wikipedia sitesinde araştırma yapılmasının sebebi Google’da bulunan web sitelerinin yapılarının birbirinden farklı olmasıdır. Farklı yapılardaki sitelerden verileri çekmek için verinin bulunduğu etiketleri değiştirmek gerekmektedir. Bu nedenle tek bir site üzerinden araştırma sonuçlarının alınmasına karar verilmiştir. Son olarak elde edilen tüm bilgiler Microsoft SQL Server veri tabanında tablolara kayıt edilmiştir.

<h2> 2) Projede Elde Edile Çıktılar </h2>

Kullanıcıya sunulan menü ekranı Şekil 1’de görülmektedir.
<div align="center">
    <img src="https://github.com/hediyeorhan/TextClassificationAndSearching/assets/59260491/20286365-5054-46ab-b06e-9f1079057222" alt="Şekil 1: Kullanıcıya sunulan menü ekranı">
</div>

<h5> Şekil 1: Kullanıcıya sunulan menü ekranı </h5>
<div align="center">
    <p>Bu metin ortalı olarak gösteriliyor.</p>
</div>

Girilen metnin konusu Şekil 2, Şekil 3, Şekil 4 ve Şekil 5’te görüldüğü gibi tahmin edilmektedir.

![image](https://github.com/hediyeorhan/TextClassificationAndSearching/assets/59260491/92e7876d-37b7-4dfc-9ba7-38ea59751e27)
<h5> Şekil 2: Girilen metnin konusunun belirlenmesi </h5>

![image](https://github.com/hediyeorhan/TextClassificationAndSearching/assets/59260491/5a695ff3-b181-430e-9219-af9c5964a87e)

Şekil 3: Girilen metnin konusunun belirlenmesi

![image](https://github.com/hediyeorhan/TextClassificationAndSearching/assets/59260491/1be40f91-3d6d-4010-99a7-ab406c10ee36)

Şekil 4: Girilen metnin konusunun belirlenmesi

![image](https://github.com/hediyeorhan/TextClassificationAndSearching/assets/59260491/955824df-7420-434b-9592-2fed741edde8)

Şekil 5: Girilen metnin konusunun belirlenmesi

Şekil 6’da metinlerin alt başlıkları belirlenerek bunlar ile ilgili Wikipedia sitesinde yapılan arama sonuçlarının elde edilmesi görülmektedir. Burada ‘Ebru Sanatı’ ile ilgili girilen bir metnin ve ‘Tarih’ ile ilgili girilen bir metnin alt başlıkları belirlenerek ‘Ebru Tarihi’ ile ilgili bir araştırma yapılmıştır.

![image](https://github.com/hediyeorhan/TextClassificationAndSearching/assets/59260491/ef2ebd5a-f8a8-4882-bed9-d05e60df4090)

Şekil 6: Alt başlıklara göre arama yapılması

Şekil 7’de metinlerin alt başlıkları belirlenerek bunlar ile ilgili Wikipedia sitesinde yapılan arama sonuçlarının elde edilmesi görülmektedir.

![image](https://github.com/hediyeorhan/TextClassificationAndSearching/assets/59260491/cd4b1a95-0ecc-4baf-8e90-ee6012499b72)

Şekil 7: Alt başlıklara göre arama yapılması

Şekil 8’ de metinlerin sınıflarının kayıt edildiği veri tabanı tablosu, Şekil 9’da arama sonuçlarının kayıt edildiği veri tabanı tablosu görülmektedir.

![image](https://github.com/hediyeorhan/TextClassificationAndSearching/assets/59260491/6c43e7fc-fff9-440c-9b0f-257869ad221a)

Şekil 8: Metinlerin sınıflarının ve alt başlıklarının bulunduğu veri tabanı tablosu

![image](https://github.com/hediyeorhan/TextClassificationAndSearching/assets/59260491/c194ee9b-6e88-43e2-8d7a-8de33453048c)

Şekil 9: Arama sonuçlarının bulunduğu veri tabanı tablosu

KAYNAKÇA
[1] Kaggle Veri Seti. Available: https://www.kaggle.com/code/erdal002/turkish-text-classification/input

 
