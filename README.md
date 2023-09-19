# Tugas 3

## Apa perbedaan antara form `POST` dan form `GET` dalam Django?

Form `POST` dan form `GET` memiliki fungsi yang sama yaitu mengirimkan nilai (value) dari variabel ke sebuah file yang lain. Namun, keduanya memiliki perbedaan dalam hal pengiriman data tersebut.
1. `POST` merupakan method dalam pembuatan form dimana nilai variabel tidak ditampilkan ke dalam URL ketika data dipindahkan. `POST` ini biasa digunakan untuk melakukan input data melalui form dan digunakan untuk mengirim data-data penting seperti password, nama, alamat tempat tinggal, dan lainnya yang bersifat privasi. Karena hal ini, `POST` lebih aman dibandingkan dengan `GET`. Selain itu, pada `POST`, input data tidak dibatasi panjang string sehingga bisa dimasukkan data dengan panjang apapun. Untuk pengambilan variabel pada `POST` dilakukan dengan `request.POST.get`.
2. `GET` merupakan method dalam pembuatan form dimana nilai variabel ditampilkan ke dalam URL sehingga user dapat dengan mudah memasukkan nilai variabel baru. `GET` ini biasa digunakan untuk melakukan input data melalui link  dan digunakan untuk mengirim data-data yang tidak terlalu penting. Hal ini dikarenakan ketika user melakukan input data, nilai variabel yang dimasukkan akan terlihat di URL. Karena ini, `GET` kurang aman dibandingkan dengan `POST`. Selain itu, pada `GET`, input data dibatasi panjang string sampai 2047 karakter, sehingga data yang diinput tidak bisa sampai melebihi 2047 karakter. Untuk pengambilan variabel pada `GET` dilakukan dengan `request.GET.get`.

Sumber : [Penjelasan Singkat tentang POST & GET Django](https://gist.github.com/rririanto/442f0590578ca3f8648aeba1e25f8762), [Perbedaan Method POST dan GET Beserta Fungsinya](https://makinrajin.com/blog/perbedaan-post-dan-get/)

## Apa perbedaan utama antara XML, JSON, dan HTML dalam konteks pengiriman data?

1. **XML** adalah bahasa markah yang menyediakan aturan untuk menentukan data apa pun. Data dalam XML disimpan dalam bentuk elemen yang terdiri dari tag yang dapat menyimpan data dalam hierarki yang dalam dan rumit. XML digunakan untuk menyimpan dan melakukan transfer data secara umum. XML sering digunakan dalam berbagai konteks seperti konfigurasi aplikasi, pertukaran data antara sistem, dan penyimpanan data terstruktur.
2. **JSON** adalah format pertukaran data terbuka yang dapat dibaca baik oleh manusia maupun mesin. JSON bersifat independen dari bahasa pemrograman dan merupakan output API umum dalam berbagai aplikasi. Data dalam JSON disimpan dalam bentuk pasangan key-value dan dapat dibentuk menjadi sebuah array. JSON digunakan untuk pertukaran data antara server dan client dalam format yang mudah dipahami oleh JavaScript, meskipun juga digunakan dalam banyak bahasa pemrograman lainnya. JSON sendiri sangat populer dalam pengembangan aplikasi web dan API.
3. **HTML** adalah singkatan dari _Hypertext Markup Language_, yaitu bahasa markup standar untuk membuat dan menyusun halaman dan aplikasi web. HTML digunakan untuk membuat struktur dan tampilan halaman web. Masing-masing halaman web tersebut terdiri atas serangkaian tags yang tersusun untuk membentuk sebuah halaman website. Tag tersebut membuat hierarki yang menyusun konten hingga menjadi bagian, paragraf, heading, dan _block_ konten lainnya. 

Sumber : [JSON vs XML - Perbedaan Antara Berbagai Representasi Data](https://aws.amazon.com/id/compare/the-difference-between-json-xml/), [Apa Itu HTML? Fungsi dan Cara Kerja HTML](https://www.hostinger.co.id/tutorial/apa-itu-html)

## Mengapa JSON sering digunakan dalam pertukaran data antara aplikasi web modern?

- **_Simplicity_ dan _Readability_**
Dalam penulisannya, JSON menggunakan format pasangan key-value dan array sehingga lebih mudah untuk dibaca. Selain itu, JSON tidak membutuhkan special tag, atribut, ataupun skema seperti XML. JSON juga support untuk common data type seperti strings, numbers, booleans, nulls, objects, dan arrays.
- **_Compatibility_ dan _Interoperability_**
JSON kompatibel dengan berbagai macam platform, language, serta framework. Hal ini yang membuat JSON menjadi fleksibel untuk digunakan. JSON juga support untuk berbagai macam modern browser, web server, dan web API, sehingga memudahkan untuk melakukan pertukaran data antar sistem dan environment yang berbeda.
- **_Performance_ dan _Efficiency_**
JSON lebih cepat dan lebih ringan dibandingkan dengan XML karena JSON memiliki ukuran file yang lebih kecil dan struktur yang lebih sederhana. JSON tidak memerlukan closing tag, namespace, ataupun deklarasi, dimana hal ini dimiliki oleh XML sehingga XML terkesan lebih kompleks. Selain itu, JSON memiliki syntax yang lebih konsisten sehingga memudahkan untuk dilakukan _parse_ dan _generate_ oleh manusia ataupun mesin. JSON juga bisa meningkatkan kecepatan dan responsivitas sebuah aplikasi web karena mengurangi _bandwith_ dan waktu process yang diperlukan untuk transfer dan manipulasi data.

Sumber : [JSON untuk Aplikasi Web: Kelebihan dan Kekurangan](https://www.linkedin.com/advice/3/what-benefits-drawbacks-using-json-data)

## Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).

1. Sebelum membuat input form untuk menambahkan objek model, saya membuat `base.html` pada folder `templates` di root folder sebagai template dasar dari html yang dibuat dan dibuat juga beberapa penyesuaian untuk CSS nya. Setelah itu, pada `DIRS` di `settings.py` di subdirektori `gi_wp_inventory`, ditambahkan `'templates'` sebagai base dir. Pada `main.html` dilakukan beberapa perubahan untuk `block content` dengan penyesuaian untuk isi dari body.
Untuk pembuatan form input data untuk menambahkan objek model, pertama dibuat `forms.py` untuk membuat struktur form yang dapat menerima data item baru. Setelah itu, diimport `ModelForm` dan `Item` dan dibuat class `ItemForm`. Deklarasi `model = Item` sehingga data dari form akan disimpan menjadi sebuah objek `Item`. Fields diisi dengan `["name", "amount", "description", "base_atk", "substat", "weapon_passive", "weapon_type", "rarity"]` sebagai atribut-atribut yang diminta inputnya untuk _weapon_ dalam inventory tersebut.
2. Pada pembuatan views, pada file `views.py` ditambahkan import `HttpResponseRedirect`, `ItemForm`, dan `reverse`. Setelah itu, dibuat fungsi baru `create_item` untuk menghasilkan formulir yang dapat menambahkan data item secara otomatis ketika data disubmit dari form. Pada `show_main`, ditambahkan `items = Item.objects.all()` dan `'items': items`. Setelah itu, pada `urls.py` di `main`, pada bagian `urlpatterns` ditambahkan path url untuk mengakses fungsi `create_item` yang sudah diimport sebelumnya. Selanjutnya dibuat file html baru dengan nama `create_item.html` pada direktori `main/templates` dimana ini akan menjadi pembuat item baru. Setelah itu, pada `main.html`, dilakukan beberapa penyesuaian pada `block content` untuk dilakukan looping setiap kali ada penambahan data item untuk dimasukkan ke dalam tabel, dan ditambahkan juga button untuk menambahkan item baru.
3. Untuk mengembalikan data dalam bentuk XML, selanjutnya diimport `HttpResponse` dan `serializers` serta dibuat fungsi `show_xml` pada `views.py`, dan dibuat variabel data di dalam fungsi tersebut untuk menyimpan hasil _query_ dari seluruh data dalam `Item`. Selanjutnya dibuat _return function_ berupa `HttpResponse` dengan parameter data hasil _query_ dalam format _xml_. Kemudian pada `urls.py` ditambahkan import fungsi `show_xml` dari yang telah dibuat dan tambahkan path url ke dalam `urlpatterns` sehingga fungsi yang sudah diimport dapat diakses.
4. Untuk mengembalikan data dalam bentuk JSON, diimport `HttpResponse` dan `serializers` serta dibuat fungsi `show_json` pada `views.py`, dan dibuat variabel data di dalam fungsi tersebut untuk menyimpan hasil _query_ dari seluruh data dalam `Item`. Selanjutnya dibuat _return function_ berupa `HttpResponse` dengan parameter data hasil _query_ dalam format _json_. Kemudian pada `urls.py` ditambahkan import fungsi `show_json` dari yang telah dibuat dan tambahkan path url ke dalam `urlpatterns` sehingga fungsi yang sudah diimport dapat diakses.
5. Untuk mengembalikan data berdasarkan ID dalam bentuk XML dan JSON, pada `views.py` ditambahkan fungsi `show_xml_by_id` dan `show_json_by_id`, kemudian masing-masing fungsi ditambahkan variabel `data` untuk menyimpan hasil query dari data dengan id tertentu yang ada pada `Item`. Setelah itu pada `urls.py` ditambahkan import `show_xml_by_id` dan `show_json_by_id`, kemudian tambahkan path url ke dalam `urlpatterns` sehingga fungsi yang sudah diimport dapat diakses.

## Screenshot Hasil Akses URL pada Postman

1. Show HTML
![show_html](./images/show_html.jpg)
2. Show XML
![show_xml](./images/show_xml.jpg)
3. Show JSON
![show_xml](./images/show_json.jpg)
4. Show XML By ID
![show_xml](./images/show_xml_by_id.jpg)
5. Show JSON By ID
![show_xml](./images/show_json_by_id.jpg)

===========================================================================

# Tugas 2

Pada tugas kedua ini, saya membuat sebuah Weapon Inventory untuk game Genshin Impact. Berikut adalah tautan menuju aplikasi Adaptable yang sudah di-deploy :
https://gaelzen-io.adaptable.app/

1. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).

- Pada pembuatan project Django baru, saya membuat local directory dengan nama gi_wp_inventory dan melakukan inisiasi virtual environment (dengan command python -m venv env, kemudian env\Scripts\activate.bat untuk aktivasi) pada local directory tersebut. Kemudian setelah menjalankan virtual environment, saya membuat requirements.txt dengan beberapa dependencies dan melakukan instalasi Django (dengan command pip install -r requirements.txt) pada directory tersebut. Selanjutnya dibuat proyek Django bernama gi_wp_inventory (dengan command django-admin startproject gi_wp_inventory .). Pada ALLOWED_HOST di settings.py, ditambahkan nilai "*" untuk memberikan izin pada semua host. Setelah menjadikan gi_wp_inventory sebagai repositori Git, ditambahkan berkas .gitignore sebagai konfigurasi berkas dan directory yang diabaikan oleh Git. 
- Pada pembuatan main di project gi_wp_inventory, dijalankan command python manage.py startapp main, kemudian menambahkan 'main' pada INSTALLED_APPS di settings.py pada direktori proyek gi_wp_inventory. Setelah itu, saya menambahkan directory templates pada main yang berisi main.html dengan isi nama aplikasi, nama saya, npm, serta kelas PBP.
- Setelah pembuatan main, dilakukan routing pada proyek agar dapat menjalankan aplikasi main dengan menambahkan fungsi show_main pada path di urls.py di direktori main. Diberikan juga variabel app_name untuk memberikan nama unik pada pola URL dalam aplikasi.
- Pada pembuatan models di aplikasi main, dibuatlah sebuah class Item pada models.py. Pada class ini, saya membuat atribut-atribut yang diperlukan untuk mendeskripsikan atribut pada weapon, seperti name (type CharField), amount (type IntegerField), description (type TextField), base_atk (type IntegerField), substat (type CharField), weapon_passive (type TextField), weapon_type (type CharField), serta rarity (type CharField). Selanjutnya dijalankan migrasi model ke dalam basis data setelah membuat model.
- Pada views.py, ditambahkan function show_main dengan context berisi dictionary dengan isi name dan class untuk dikembalikan kepada template main.html yang akan menampilkan nama aplikasi, nama, serta kelas PBP. Pada template dilakukan modifikasi untuk main.html dengan mengubah menjadi {{ name }}, {{ npm }}, dan {{ class }} untuk menampilkan nilai dari variabel tersebut. Selain itu, main.html juga saya lakukan pencobaan untuk membuat gambaran tabel untuk tampilan aplikasi ke depannya. HTML ini juga akan disempurnakan nantinya supaya bisa lebih baik.
- Untuk membuat routing pada urls.py aplikasi main, ditambahkan path kosong ('') dan include dari aplikasi main ke berkas urls.py proyek (dengan include('main.urls')). Path diset kosong supaya ketika membuka aplikasi langsung menuju ke main.
- Setelah itu, dilakukan git add, commit, dan push ke dalam repository gi-wp-inventory yang berada di Github. Kemudian menuju ke website Adaptable dan dilakukan save settings and update deployment untuk melakukan deploy ke Adaptable.

2. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.

![bagan_request_client](./images/bagan-request-client.jpg)
- Pertama-tama, client akan melakukan request kepada project Django dengan mengakses suatu URL. Kemudian Django akan menerima request tersebut dan meneruskan request tersebut ke View yang sesuai.
- Setelah View menerima request dari URL, view akan menjalankan QuerySets yang akan dikirimkan kepada Models. Setelah menerima QuerySets, Models akan melakukan read/write pada database dan akan mengirimkan sebuah ResultSet yang akan dikirimkan kembali kepada View.
- Dengan ResultSet yang telah diberikan, View akan melakukan generate respons kepada Template berupa index.html yang berisi HTML, Javascript, CSS.

3. Jelaskan mengapa kita menggunakan virtual environment? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?

Virtual Environment digunakan untuk mengisolasi lingkungan pada proyek supaya antara proyek satu dan lainnya tidak saling bertabrakan atau tidak saling terpengaruhi. Dengan menggunakan virtual environment, masing-masing proyek dapat memiliki version Django dan Python yang berbeda sesuai dengan keperluan dari masing-masing proyek itu sendiri. Selain itu, virtual environment dapat mempermudah pembuat proyek untuk mengelola dependency yang diperlukan untuk proyek tersebut.
Django sendiri bisa dibuat tanpa menggunakan virtual environment, namun hal ini sangat rentan karena dapat memicu terjadinya "dependency hell". Sebagai contoh apabila kita memiliki dua buah proyek, yaitu ProjectA dan ProjectB, dimana masing-masing proyek ini memiliki dependency di library yang sama, yaitu ProjectC. Misalkan ProjectA membutuhkan version 1.0.0, sementara ProjectB membutuhkan version 2.0.0. Python memiliki keterbatasan dimana tidak bisa membedakan antara versi satu dengan lainnya di dalam site-packages directory. Masing-masing dari version 1.0.0 dan 2.0.0 akan memiliki nama yang sama di dalam directory yang sama. Dengan demikian, tidak akan ada perbedaan antara dua versi tersebut dan akan dianggap sama oleh Python sehingga ProjectA dan ProjectB membutuhkan versi yang sama untuk bisa dijalankan.

4. Jelaskan apakah itu MVC, MVT, MVVM dan perbedaan dari ketiganya.

MVC (Model-View-Controller), MVT (Model-View-Template), MVVM (Model-View-ViewModel) adalah tiga jenis arsitektur desain yang digunakan ketika akan melakukan pengembangan aplikasi berbasis website. Di antara ketiga jenis ini, bagian yang sama adalah di dua huruf pertamanya, yaitu M (Model) dan V (View). Model merepresentasikan data dan logika bisnis aplikasi yang bertanggung jawab untuk mengambil dan menyimpan data serta memprosesnya. View merepresentasikan antarmuka pengguna aplikasi yang bertanggung jawab untuk menampilkan data dari Model dan menyediakan antarmuka bagi pengguna untuk berinteraksi dengan aplikasi. Berikut ini adalah perbedaan antara MVC, MVT, dan MVVM :
- MVC (Model-View-Controller) :  Pada MVC, C (Controller) merepresentasikan sebagai perantara antara Model dan View. Controller menerima input dari pengguna, memprosesnya dengan Model, dan memperbarui View. MVC memberikan pemisahan aspek yang jelas antara komponen aplikasi. Namun, MVC memiliki keterbatasan seperti kesulitan dalam melakukan pengujian (testing) dan Controller dapat menjadi penuh dengan logika.
- MVT (Model-View-Template) : Pada MVT, T (Template) merepresentasikan sebagai pengatur tampilan atau presentasi data yang akan ditampilkan oleh View. MVT memiliki kemampuan pengujian yang lebih baik dibandingkan dengan MVC dengan adanya pemisahan yang lebih jelas, namun hal ini dapat menyebabkan duplikasi kode antara View dan Template.
- MVVM (Model-View-ViewModel) : Pada MVVM, VM (ViewModel) merepresentasikan sebagai perantara antara Model dan View. ViewModel memisahkan tampilan dari logika bisnis dengan cara yang lebih kuat dibandingkan dengan Controller dan Template. MVVM memungkinkan pengujian unit lebih mudah dan juga memungkinkan penggunaan data binding untuk memperbarui View secara otomatis saat ViewModel berubah. Namun, hal ini dapat menyebabkan peningkatan kompleksitas.