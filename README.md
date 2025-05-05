<h2>SPARKFUN TINY GPS</h2>
<h3>Mutlak Konumlama Sistemleri</h3>
<p align="justify">Algılama (sensör) teknolojilerindeki ilerleme, bilgisayar işlemci hızlarında artış ve bu alanlarda kullanılan donanımların boyutlarının iyice küçülmesiyle beraber Konum Tabanlı Hizmetler (Location Based Services - LBS) hayatlarımızın değişilmez bir parçası hâline geldi. Günümüzde durmadan büyüyerek kompleksleşen ve teknolojideki gelişmelerle global bir köye dönüşen dünyamızda özellikle navigasyon hizmetleri hem yayalar hem taşıtlar için neredeyse zorunluluk oldu. Kullanıcıların dış mekanlarda bulunduğu durumlarda konum bilgisini elde etmenin standart yolu Küresel Navigasyon Uydu Sistemleri (Global Navigation Satellite Systems - GNSS) kullanmaktır. Açık havada en az üç uydu sinyaline erişilebildiği durumlarda alıcının iki boyutlu koordinatlarını (enlem (latitude) ve boylam (longitude)), Şekil 1'de görüldüğü gibi en az dört uydu yakalandığı durumda ise alıcının üç boyutlu koordinatlarını (enlem-boylam ve yükseklik (altitude) bilgilerini) elde edebilen GNSS teknolojisi, bu hesaplarda laterasyon (lateration) denilen bir teknik kullanmaktadır. Yakalanan uydu sinyali sayısı arttıkça elde edilen pozisyon tahmini hatasının azaldığı GNSS çözümünde, üç uydudan az uydu yakalanması durumunda kesin bir pozisyon elde edilemez.</p>

<figure>
    <img src=figure/GPS.png alt="GPS" width=50% height=auto>
    <caption>Şekil 1. Küresel Navigasyon Uydu Sistemleri (GNSS) ile lokalizasyon</caption>
</figure>

<p align="justify">Küresel bir kapsama alanı ve uzun süreli bir çözüm sağlamasına rağmen, özellikle yüksek binaların olduğu alanlarda sinyallerin yansıması sonucu oluşan çoklu yol (multipath), ormanlık alanlar gibi yerlerde gözlemlenen sinyal zayıflama (attenuation) ve iç mekanlarda ve tünellerde karşılaşılan sinyal engellenmesi (blockage) gibi problemlerden dolayı GPS teknolojisi yetersiz kalmaktadır. Bu gibi durumlarda ortama uyduların yerini alacak sinyal vericiler (beacon) yerleştirilirse, Şekil 2'de görüldüğü gibi GPS benzeri bir Yerel Konumlama Sistemi (Local Positioning System - LPS) kurulabilir. Burada sinyal vericilerden gönderilen Radyo Frekansı (Radio Frequency - RF) sinyali olarak genellikle Wireless-Fidelity (Wi-Fi), UltraWide-Band (UWB), Bluetooth Low Energy (BLE) kullanılırken, alıcı-vericilerin geometrisinden veya sinyallerin verici ile alıcı arasında harcadığı yolculuk zamanından (e.g., time of flight – ToF, time difference of arrival - TDoA) faydalanarak Triangulation, Trilateration veya Multilateration isimli metotlarla pozisyon tahmini yapılmaktadır [1].</p>

<figure>
    <img src=figure/indoor-localization-with-trilateration.png alt="LPS" width=50% height=auto>
    <caption>Şekil 2. Yerel Konumlama Sistemi (LPS) ile lokalizasyon</caption>
</figure>

<p align="justify">Yukarıda sayılan metotlara ek olarak, kullanıcı tarafında, alınan sinyal kuvveti (received signal strength - RSS) kullanılarak yol kaybı modelleri (path loss models) oluşturulup konumlama yapılabilir. Şu ana kadar ismi geçen tekniklerin hepsi Non-Line-of-Sight (NLoS) denilen (verici ile alıcı arasında yer alan engellerden dolayı görüş kaybı olarak tercüme edilebilecek) problemden mustariptirler. Bu durumun gözlendiği ortamlarda Şekil 3'te gösterilen parmak izi (fingerprinting) metodu kullanılabilir. Konumlama yapılacak mekânda (konumlama yapmadan önce mekânı tarayarak) RSS değerlerinden bir veri tabanı oluşturulan Fingerprinting  tekniğinde, gerçek zamanda ölçülen RSS değerleri oluşturulmuş veri tabanıyla kıyaslanır (mesela bir makine öğrenmesi metoduyla [2]) ve böylece konum tahmini yapılır. Pozisyon tahminlerinin kesinliği yapılan RSS ölçüm sayısıyla doğru orantılı olacağından dolayı çok ölçüm pozisyon tahmini kesinliğini artırır, ancak bu oldukça fazla zaman alacağından bu işi zahmetli hâle getirir. Buna ek olarak, ortamda yapılan değişiklerde, veri tabanı güncellenmesi yapılması gerektiğinden Fingerprinting pratik bir yöntem değildir. Veri tabanı oluştururken SLAM, inter/ekstrapolasyon veya crowdsourcing kullanılarak vakitten ve emekten tasarruf edilebilir ama aynı performans beklenmemelidir [3].</p>

<figure>
    <img src=figure/wifi-fingerprinting-ips.jpg alt="fingerprinting" width=50% height=auto>
    <caption>Şekil 3. Yerel Konumlama Sistemi (LPS) ile lokalizasyon</caption>
</figure>

<p align="justify">Fingerprinting metodundan daha düşük performanslı ama daha pratik başka bir konumlama tekniği ise yakınlık tabanlı lokalizasyondur (proximity-based localization). Bu metot çoğunlukla Radio Frequency IDentification (RFID) ve bazen BLE teknolojilerinden faydalanmaktadır. Özellikle pasif RFID etiket (tag) kullanan çözümler, geniş iç mekânlarda ucuza konumlama yapabilme olanağı sağlamaktadır [4].</p>

<h3>Göreceli Konumlama Sistemleri</h3>
<p align="justify">Bahsi geçen tüm mutlak konumlama sistemleri pozisyon tahmini yaparken geçmiş tahminlerden bağımsız olduğundan uzun soluklu çözümler sağlayabilmektedir. Buna rağmen altyapı (infrastructure) kurulumu ve bakımı pahalı ve meşakkatli olduğundan, altyapı gerektirmeyen (infrastructure-free) daha ucuz ve pratik çözümler tercih edilmektedir. Dış sinyallere bağlı olmayan bu sistemler, başlangıç koşulları sağlandığında kendi kendilerine konum bilgisini hesaplayabilmektedirler. En çok kullanılan göreceli konumlama sistemi kamera geometrisinden faydalanmaktadır: Eş-zamanlı haritalama ve konumlama (Simultaneous Localization and Mapping - SLAM) olarak bilinen robotik bilim dalında mono, stereo ve RGB-D kameralarla gerçek-zamanda oldukça yüksek performansla pozisyon tahmini yapılabilmektedir [5]. Otonom araba ve robot uygulamalarında SLAM için tercih edilen bir başka popüler teknoloji, laser sensörlerle ortamı görünmez ışıkla  tarayarak çalışan LIDAR’dır [6]. Kamera tabanlı SLAM'e göre daha pahalı olmasına rağmen, daha yüksek performans sağlayan LIDAR tabanlı SLAM [7], aynı zamanda mahremiyet konusunda kullanıcıları memnun etmektedir [8].</p>

<p align="justify">Altyapı gerektirmeyen ve kendi kendine pozisyonlama yapabilen bir başka göreceli konumlama sistemi atâlet sensörleri ile kurulabilir. İvmemetre (accelerometer) ve ciroskopdan (gyroscope) meydana gelen Atâletsel Ölçüm Birimi (AÖB) veya daha yaygın olan İngilizcesi ile Inertial Measurement Unit (IMU), son yirmi senede Mikro-Elektro-Mekanik-Sistemler (Micro-Electro-Mechanical-Systems - MEMS) teknolojisindeki gelişmelerle son derece yaygın hâle geldi. Hafif, ucuz, küçük ebatlı, düşük güç gereksinimli ve giyilebilir olan MEMS IMU, hareketli uygulamalarda (e.g., motion capture - MoCap) kendisinden çok daha pahalı olan alternatif kamera takip sistemlerine (e.g., VICON) tercih edilir oldu. Ayrıca tespit edilemeyecek şekilde pasif olması ve kullanıcı mahremiyetine tehdit oluşturmaması IMU teknolojisinin ekstra avantajlarından. Bütün bu olumlu özelliklerine rağmen, tüketici sınıfı IMU (consumer grade IMU) verisinde gözlenen zamanla-değişen (time-variant) sensör yanlılığı (bias) ve ölçek faktörü (scale factor) parametrelerinin tahminleri çok zor ve sinyallerde gözlemlenen sensör gürültüsü (noise) ise çok şiddetli. Bu problemlere ek olarak, bir de ölü-hesaplama (dead-reckoning - DR) metoduyla elde edilen Ataletsel Navigasyon Sistemi (Inertial Navigation System - INS) çözümünde biriken hatalar, "zamanla kayma" diye tercüme edebileceğimiz "drift" fenomenine dönüşerek navigasyon çözümünü çok kısa bir zaman için bile işe yaramaz hâle getirmekte. Bu sorunu engellemek için INS hatalarının büyümesine izin vermeden periyodik bir şekilde en az bir mutlak (e.g., WiFi [9]) veya göreceli (e.g., camera [10]) bir konumlama sistemini tamamlayıcı (complementary) olarak kullanan bir sensör füzyonu algoritması (e.g., Kalman Filtresi) ile konum tahmini güncellenebilir.</p>

<h3>GPS Verisinin Bilgisayara Kablosuz Transferi ve Gerçek-Zamanlı Görüntülenmesi</h3>
<p align="justify">Bu projede <a href="https://www.sparkfun.com/products/retired/13199">SparkFun GPS Module</a> GPS modülünü kullanıyoruz [11]. Arduino Shield ile geldiğinden direk üstten Arduino Uno'ya bağlanabiliyor. <b>TinyGPS</b> kütüphanesi <a href="https://github.com/mikalhart/TinyGPS">Mikal Hart TinyGPS github repo</a> kullanarak Arduino'ya transfer edilen enlem ve boylam verisini bilgisayara ilk önce MATLAB ile okuduk [12]. Gümüşhane Üniversitesi Stadyumu'nda yapılan bir yürüyüşün verisinin gerçek zamanda MATLAB'da görselleştirilmesini izlemek için aşağıdaki resme tıklayın.</p>

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
    <li align="justify"><a href="https://ieeexplore.ieee.org/abstract/document/6843307" target="_blank">J. Lategahn, M. Müller and C. Röhrig, <i>"Extended Kalman Filter for a Low Cost TDoA/IMU Pedestrian Localization System,"</i> 2014 11<sup>th</sup> Workshop on Positioning, Navigation and Communication (WPNC), Dresden, Germany, 2014, pp. 1-6.</a></li>
    <li align="justify"><a href="https://ieeexplore.ieee.org/document/9138275" target="_blank">M. D'Aloia et al., <i>"IoT Indoor Localization with AI Technique,"</i> 2020 IEEE International Workshop on Metrology for Industry 4.0 & IoT, Roma, Italy, 2020, pp. 654-658.</a></li>
    <li align="justify"><a href="https://ieeexplore.ieee.org/document/8451859" target="_blank">B. Jang and H. Kim, <i>"Indoor Positioning Technologies without Offline Fingerprinting Map: A Survey,"</i> in IEEE Communications Surveys & Tutorials, vol. 21, no. 1, pp. 508-525, Firstquarter 2019.</a></li>
    <li align="justify">M. Bolic, M. Rostamian and P. M. Djuric, <i>"Proximity Detection with RFID: A Step Toward the Internet of Things,"</i> in IEEE Pervasive Computing, vol. 14, no. 2, pp. 70-76, Apr.-June 2015.</li>
    <li align="justify">R. Mur-Artal and J. D. Tardós, <i>"ORB-SLAM2: An Open-Source SLAM System for Monocular, Stereo, and RGB-D Cameras,"</i> in IEEE Transactions on Robotics, vol. 33, no. 5, pp. 1255-1262, Oct. 2017.</li>
    <li align="justify">W. Hess, D. Kohler, H. Rapp and D. Andor, <i>"Real-time loop closure in 2D LIDAR SLAM,"</i> 2016 IEEE International Conference on Robotics and Automation (ICRA), Stockholm, Sweden, 2016, pp. 1271-1278.</li>
    <li align="justify">M. H. Sharif, <i>"Laser-Based Algorithms Meeting Privacy in Surveillance: A Survey,"</i> in IEEE Access, vol. 9, pp. 92394-92419, 2021.</li>
    <li align="justify">E. Guo, <i>"A Roomba recorded a woman on the toilet. How did screenshots end up on Facebook?,"</i> [MIT Technology Review]. Available: https://www.technologyreview.com/2022/12/19/1065306/roomba-irobot-robot-vacuums-artificial-intelligence-training-data-privacy/, Accessed: Mar. 29, 2023.</li>
    <li align="justify">V. Guimarães et al., <i>"A motion tracking solution for indoor localization using smartphones,"</i> 2016 International Conference on Indoor Positioning and Indoor Navigation (IPIN), Alcala de Henares, Spain, 2016, pp. 1-8.</li>
    <li align="justify">G. Huang, "Visual-Inertial Navigation: A Concise Review," 2019 International Conf. on Robotics and Automation (ICRA), Montreal, QC, Canada, 2019, pp. 9572-9582.</li>
    <li align="justify">SparkFun GPS Modülü - https://www.sparkfun.com/products/retired/13199</li>
    <li align="justify">Mikal Hart tarafından gelişitirilen TinyGPS 13 kütüphanesi - http://arduiniana.org/2013/09/greater-accuracy-with-tinygps-13/</li>
    <li align="justify"><b>pyserial</b> kütüphanesi - https://pyserial.readthedocs.io/en/latest/</li>
</ol>