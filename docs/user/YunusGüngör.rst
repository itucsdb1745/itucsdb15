Yunus Güngör tarafından tamamlanan parçalar
===========================================

Ana Sayfa
=========

  Misafir Kullanıcı
  -----------------

  Misafir kullanıcı giriş yapmak için sağ üst köşede bulunan "Login" butonunu kullanabilir. Kullanıcın giriş yapması ile, misafir kullanıcı normal kullanıcı haline gelir.

  .. figure:: /docs/pictures/homePageNotLogin.png
     :scale: 50 %
     :alt: Ana Sayfa Ekranı

     Misafir kullanıcı ana sayfada mesajları ve cevapları görüntüleyebilir veya giriş yapabilir.

  Herhangi mesaja ait cevaplar görüntülenmek istendiğinde "Answers" butonuna basılarak o mesaja ait mesajlar ve o mesajların oyları ekranda görüntülenebilir.

  .. figure:: /docs/pictures/answersNotLogin.png
     :scale: 50 %
     :alt: Ana Sayfa Ekranı ve cevaplar

     "Answers" butonuna basıldıktan sonra cevaplar mesajın altında görüntülenebilir hale gelir.

  Cevapların sol tarafında cevabı yazan kullanıcının adı ve resmi bulunmaktadır.

  Cevap yazmak için kullanıcıların giriş yaparak normal kullanıcı olması gerekmektedir. Giriş yapmak için login sayfası kullanılabilir.

  .. figure:: /docs/pictures/loginPage.png
     :scale: 50 %
     :alt: Giriş sayfası

     Daha önce kaydolunan kullanıcı adı ve şifre login sayfasındaki forma girilerek ve "Log in/Sign Up" butonuna basılarak giriş yapılabilir.

  Eğer misafir kullanıcı daha önce hesabını kaydetmediyse, başka bir kullanıcı tarafından kullanılmayan bir kullanıcı adı ve daha sonra hatırlayabileceği bir şifreyi login sayfasındaki forma girip, "Log in/Sign Up" tuşuna bastıktan sonra, kullanıcının şifreyi tekrar girmesi istenecektir.

  .. figure:: /docs/pictures/signUp.png
     :scale: 50 %
     :alt: Üye olma işlemi

     Verilen ekstra mesajlar ile sistemin nasıl kullanılabileceği ile ilgili ipuçları veya geri bildirimler yapılmaktadır. Login sayfasında sistemde bulunmayan bir kullanıcı adı girildiğinde login sayfası otamatik olarak üye ekleme moduna geçer. Kullanıcının şifresini tekrar girmesi ile yeni kullanıcı sistemde oluştulabilir. Bu durumda kullanıcı adı değiştirilemez. Eğer kullanıcı yanlış kullanıcı adı girdiğini düşünüyorsa tarayıcıdaki geri tuşunu kullanarak geri dönebilir ve tekrar deneyebilir.

  Oluşturulan hesabın şifresi veya profil fotosu profil sayfasından değiştirilebilir ancak kullanıcı adının değiştirilmesine izin verilmez.

  Normal Kullanıcı
  ----------------

  Kullanıcı giriş yaptıktan veya sistem otamatik olarak tanıdıktan sonra ana sayfa ekranı "Profile" butonu, "Add Message" sekmesi, her mesajda "Reply" butonu ve her cevapta "Up" butonu ile birlikte görüntülenir.

  .. figure:: /docs/pictures/homePage.png
     :scale: 50 %
     :alt: Ana Sayfa Ekranı

     Ana sayfa ekranından "Profile" butonu kullanılarak profil sayfasına erişilebilir. Kullanıcı ansayfada bulunan "Add Message" sekmesini kullanarak yeni bir mesaj ekleyebilir.

  "Add Message" sekmesine tıklandığında mesaj eklemek için gerekli olan form ekranda görünür olacaktır. Bu formda başlık ve mesaj bilgileri doldurulduktan sonra "add message" butonuna basarak yeni mesaj sisteme eklenebilir.

  .. figure:: /docs/pictures/addMessage.png
     :scale: 50 %
     :alt: Mesaj Ekleme sekmesi

     Mesaj eklemek için doldurulması gereken form.

  Herhangi bir cevap eklemek için, cevap eklenmek istenen mesajın üstünde bulunan "Reply" tuşu kullanılabilir.

  .. figure:: /docs/pictures/reply.png
     :scale: 50 %
     :alt: Mesaja cevap vermek için kullanılan bölüm

     "Reply" tuşuna basıldığında görüntülenen form doldurularak ve "Add New Answer to the Message" butonu kullanılarak, mesaja cevap eklenebilir. Tekrar "Reply" tuşuna basıldığında veya butona basıldığında form tekrar gizlenir.

 Herhangi bir cevaba oy vermek için oy verilmek istenen cevabın üstünde bulunan "Up" butonu kullanılabilir. Oy verildikten sonra ana sayfa yenilenir ve cevaplar oy sayısına göre tekrar sıralanır. Kullanıcıların oy verme sınırı bulunmamaktadır. Herhangi bir cevabın daha yukarda görüntülenmesi verilen oyların sayısına bağlıdır. Daha çok oy alan cevap daha yukarda görüntülenir.

 .. figure:: /docs/pictures/up.png
    :scale: 50 %
    :alt: Cevabı oylamak için kullanılabilecek buton

    "Up" butonun görüntülenebilmesi için kullanıcının giriş yapmış olması ve herhangi bir mesaja ait olan cevapları görüntülüyor olması gerekmektedir.

  Admin Kullanıcı
  ---------------

  Admin kullanıcılar normal kullanıcıların yapabildiği tüm işlemleri normal kullanıcı gibi yerine getirebilir. Bu işlemler: Mesaj ekleme, cevap ekleme, profil sayfasına erişebilme ve cevapları oylayabilmektir. Bu işlemlerin yanında ana sayfada mesaj ve cevapları düzenleyebilirler.

  .. figure:: /docs/pictures/mainPageAdmin.png
     :scale: 50 %
     :alt: Admin hesabı ile görüntülenen ana sayfa

     Admin kullanıcı ana sayfada bulunan mesajların üzerindeki "Delete" ve "Edit" butonlarına erişim sağlayabilir.

  Admin kullanıcılar eklenen herhangi bir mesaj veya cevabı silebilir veya düzenleyebilir. Mesaj veya cevapların üzerinde bulunan "Delete" butonuna basıldığında o mesaj veya cevap silinir. Silinen mesaja ait olan tüm cevaplar da mesajla birlikte silinir.
  "Edit" butonuna basıldığında ise yeni bir sayfada düzenleme formu daha önce bulunan mesaj veya cevap verisiyle birlikte görüntülenir. İstenilen düzenlemeler yapıldıktan sonra "Summit Message" butonu ile yapılan değişiklikler kaydedilir.

  .. figure:: /docs/pictures/answerEdit.png
     :scale: 50 %
     :alt: Cevap Düzenleme ekranı

     Cevap Düzenleme ekranı

   .. figure:: /docs/pictures/messageEdit.png
      :scale: 50 %
      :alt: Mesaj Düzenleme ekranı

      Mesaj Düzenleme ekranı

Profil Sayfası
==============


  Misafir Kullanıcı
  -----------------

  Normal Kullanıcı
  ----------------

  Admin Kullanıcı
  ---------------
