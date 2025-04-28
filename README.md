# BMI Hesaplama Uygulaması

Bu proje, kullanıcının **boy ve kilo** bilgilerini girerek **BMI (Body Mass Index)** değerini hesaplamasına olanak tanır. Uygulama, kullanıcının verdiği verilere göre BMI'yi hesaplar ve sonucu ilgili kategorilere ayırarak ekranda gösterir.

### Özellikler:
- **Kilo** ve **Boy** girildikten sonra BMI hesaplanır.
- BMI sonucu şu kategorilere ayrılır:
  - **Zayıf**: BMI < 18.5
  - **Normal**: 18.5 ≤ BMI < 25
  - **Fazla Kilolu**: 25 ≤ BMI < 30
  - **Obez**: BMI ≥ 30
- Kullanıcı hatalı giriş yaptığında hata mesajı gösterilir.
- Uygulama, boy ve kilo için **geçerli** aralıkları kontrol eder.
- Kullanıcı dostu bir arayüze sahip.

### Teknolojiler:
- **Python**: Uygulama **Python 3.x** ile yazılmıştır.
- **Tkinter**: Grafiksel kullanıcı arayüzü için **Tkinter** kütüphanesi kullanılmıştır.

### Başlangıç

Projenin çalışabilmesi için sadece Python yüklü olmalıdır. Eğer bilgisayarınızda **Tkinter** yüklü değilse, aşağıdaki adımları takip ederek kurulum yapabilirsiniz:

1. Python yüklü değilse, [Python'un resmi web sitesinden](https://www.python.org/downloads/) Python'u indirip kurun.
2. Tkinter, Python ile birlikte gelir. Eğer yüklü değilse, terminal veya komut satırında şu komutu çalıştırarak kurabilirsiniz:
   ```bash
   pip install tk
