Nama  : Ghaisan Luqyana Aqila
NPM   : 2206830460
Kelas : PBP A

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