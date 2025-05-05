<h2>SPARKFUN TINY GPS</h2>

<h3>GPS Verisinin Bilgisayara Transferi ve Gerçek-Zamanlı Görüntülenmesi</h3>
<p align="justify">Bu projede <a href="https://www.sparkfun.com/products/retired/13199">SparkFun GPS Module</a> GPS modülünü kullanıyoruz [1]. Arduino Shield ile geldiğinden direk üstten Arduino Uno'ya bağlanabiliyor. <b>TinyGPS</b> kütüphanesi <a href="https://github.com/mikalhart/TinyGPS">Mikal Hart TinyGPS github repo</a> kullanarak Arduino'ya transfer edilen enlem ve boylam verisini bilgisayara ilk önce MATLAB ile okuduk [2]. Gümüşhane Üniversitesi Stadyumu'nda yapılan bir yürüyüşün verisinin gerçek zamanda MATLAB'da görselleştirilmesini izlemek için aşağıdaki resme tıklayın.</p>

[![IMAGE ALT TEXT HERE](figure/enes-muratcan-stadium-walk-1by2-thumbnail.jpg)](https://www.youtube.com/watch?v=dK4XJg6-qIM)

<p align="justify">Python'da bu işi yapabilmek için aşağıdaki paketleri <b>Anaconda</b> ortamında oluşturacağımız <b>gps</b> isimli sanal ortama kuralım.</p>

```
conda install pip
pip install numpy
pip install matplotlib
pip install pandas
pip install keyboard
pip install pyserial
```

<p align="justify">Ardından Arduino ve TinyGPS modülü bağlantılarını yaptıktan sonra <b>gps</b> isimli sanal ortamı aktif hâle getirip <b>sparkfun_tiny_gps.py</b> ve <b>plot_trajectory.py</b> kodlarını sırasıyla çalıştırarak veri toplayıp grafik çizdirebiliriz. Sparkfun Tiny GPS modül ile ilgili bütün bilgileri ve resimleri yukarıdaki <b>document</b> klasörünün içindeki örnek raporda bulabilirsiniz.</p>

<h3>Referanslar</h3>
<ol>
    <li align="justify">SparkFun GPS Modülü - https://www.sparkfun.com/products/retired/13199</li>
    <li align="justify">Mikal Hart tarafından gelişitirilen TinyGPS 13 kütüphanesi - http://arduiniana.org/2013/09/greater-accuracy-with-tinygps-13/</li>
</ol>