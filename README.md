__Nama    : Ghaisan Luqyana Aqila__

__NPM     : 2206830460__

__Kelas   : PBP A__



Program ini didesain untuk membuat sebuah _Weapon Inventory_ untuk game Genshin Impact. 

Berikut adalah tautan menuju aplikasi Adaptable yang sudah di-deploy : https://gaelzen-io.adaptable.app/

Berikut adalah shortcut untuk tugas :

- [Tugas 2](#tugas-2)
- [Tugas 3](#tugas-3)
- [Tugas 4](#tugas-4)

# Tugas 2

## Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).

- Pada pembuatan project Django baru, saya membuat local directory dengan nama gi_wp_inventory dan melakukan inisiasi virtual environment (dengan command python -m venv env, kemudian env\Scripts\activate.bat untuk aktivasi) pada local directory tersebut. Kemudian setelah menjalankan virtual environment, saya membuat requirements.txt dengan beberapa dependencies dan melakukan instalasi Django (dengan command pip install -r requirements.txt) pada directory tersebut. Selanjutnya dibuat proyek Django bernama gi_wp_inventory (dengan command django-admin startproject gi_wp_inventory .). Pada ALLOWED_HOST di settings.py, ditambahkan nilai "*" untuk memberikan izin pada semua host. Setelah menjadikan gi_wp_inventory sebagai repositori Git, ditambahkan berkas .gitignore sebagai konfigurasi berkas dan directory yang diabaikan oleh Git. 
- Pada pembuatan main di project gi_wp_inventory, dijalankan command python manage.py startapp main, kemudian menambahkan 'main' pada INSTALLED_APPS di settings.py pada direktori proyek gi_wp_inventory. Setelah itu, saya menambahkan directory templates pada main yang berisi main.html dengan isi nama aplikasi, nama saya, npm, serta kelas PBP.
- Setelah pembuatan main, dilakukan routing pada proyek agar dapat menjalankan aplikasi main dengan menambahkan fungsi show_main pada path di urls.py di direktori main. Diberikan juga variabel app_name untuk memberikan nama unik pada pola URL dalam aplikasi.
- Pada pembuatan models di aplikasi main, dibuatlah sebuah class Item pada models.py. Pada class ini, saya membuat atribut-atribut yang diperlukan untuk mendeskripsikan atribut pada weapon, seperti name (type CharField), amount (type IntegerField), description (type TextField), base_atk (type IntegerField), substat (type CharField), weapon_passive (type TextField), weapon_type (type CharField), serta rarity (type CharField). Selanjutnya dijalankan migrasi model ke dalam basis data setelah membuat model.
- Pada views.py, ditambahkan function show_main dengan context berisi dictionary dengan isi name dan class untuk dikembalikan kepada template main.html yang akan menampilkan nama aplikasi, nama, serta kelas PBP. Pada template dilakukan modifikasi untuk main.html dengan mengubah menjadi {{ name }}, {{ npm }}, dan {{ class }} untuk menampilkan nilai dari variabel tersebut. Selain itu, main.html juga saya lakukan pencobaan untuk membuat gambaran tabel untuk tampilan aplikasi ke depannya. HTML ini juga akan disempurnakan nantinya supaya bisa lebih baik.
- Untuk membuat routing pada urls.py aplikasi main, ditambahkan path kosong ('') dan include dari aplikasi main ke berkas urls.py proyek (dengan include('main.urls')). Path diset kosong supaya ketika membuka aplikasi langsung menuju ke main.
- Setelah itu, dilakukan git add, commit, dan push ke dalam repository gi-wp-inventory yang berada di Github. Kemudian menuju ke website Adaptable dan dilakukan save settings and update deployment untuk melakukan deploy ke Adaptable.

## Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.

![bagan_request_client](./images/bagan-request-client.jpg)
- Pertama-tama, client akan melakukan request kepada project Django dengan mengakses suatu URL. Kemudian Django akan menerima request tersebut dan meneruskan request tersebut ke View yang sesuai.
- Setelah View menerima request dari URL, view akan menjalankan QuerySets yang akan dikirimkan kepada Models. Setelah menerima QuerySets, Models akan melakukan read/write pada database dan akan mengirimkan sebuah ResultSet yang akan dikirimkan kembali kepada View.
- Dengan ResultSet yang telah diberikan, View akan melakukan generate respons kepada Template berupa index.html yang berisi HTML, Javascript, CSS.

## Jelaskan mengapa kita menggunakan virtual environment? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?

Virtual Environment digunakan untuk mengisolasi lingkungan pada proyek supaya antara proyek satu dan lainnya tidak saling bertabrakan atau tidak saling terpengaruhi. Dengan menggunakan virtual environment, masing-masing proyek dapat memiliki version Django dan Python yang berbeda sesuai dengan keperluan dari masing-masing proyek itu sendiri. Selain itu, virtual environment dapat mempermudah pembuat proyek untuk mengelola dependency yang diperlukan untuk proyek tersebut.
Django sendiri bisa dibuat tanpa menggunakan virtual environment, namun hal ini sangat rentan karena dapat memicu terjadinya "dependency hell". Sebagai contoh apabila kita memiliki dua buah proyek, yaitu ProjectA dan ProjectB, dimana masing-masing proyek ini memiliki dependency di library yang sama, yaitu ProjectC. Misalkan ProjectA membutuhkan version 1.0.0, sementara ProjectB membutuhkan version 2.0.0. Python memiliki keterbatasan dimana tidak bisa membedakan antara versi satu dengan lainnya di dalam site-packages directory. Masing-masing dari version 1.0.0 dan 2.0.0 akan memiliki nama yang sama di dalam directory yang sama. Dengan demikian, tidak akan ada perbedaan antara dua versi tersebut dan akan dianggap sama oleh Python sehingga ProjectA dan ProjectB membutuhkan versi yang sama untuk bisa dijalankan.

## Jelaskan apakah itu MVC, MVT, MVVM dan perbedaan dari ketiganya.

MVC (Model-View-Controller), MVT (Model-View-Template), MVVM (Model-View-ViewModel) adalah tiga jenis arsitektur desain yang digunakan ketika akan melakukan pengembangan aplikasi berbasis website. Di antara ketiga jenis ini, bagian yang sama adalah di dua huruf pertamanya, yaitu M (Model) dan V (View). Model merepresentasikan data dan logika bisnis aplikasi yang bertanggung jawab untuk mengambil dan menyimpan data serta memprosesnya. View merepresentasikan antarmuka pengguna aplikasi yang bertanggung jawab untuk menampilkan data dari Model dan menyediakan antarmuka bagi pengguna untuk berinteraksi dengan aplikasi. Berikut ini adalah perbedaan antara MVC, MVT, dan MVVM :
- MVC (Model-View-Controller) :  Pada MVC, C (Controller) merepresentasikan sebagai perantara antara Model dan View. Controller menerima input dari pengguna, memprosesnya dengan Model, dan memperbarui View. MVC memberikan pemisahan aspek yang jelas antara komponen aplikasi. Namun, MVC memiliki keterbatasan seperti kesulitan dalam melakukan pengujian (testing) dan Controller dapat menjadi penuh dengan logika.
- MVT (Model-View-Template) : Pada MVT, T (Template) merepresentasikan sebagai pengatur tampilan atau presentasi data yang akan ditampilkan oleh View. MVT memiliki kemampuan pengujian yang lebih baik dibandingkan dengan MVC dengan adanya pemisahan yang lebih jelas, namun hal ini dapat menyebabkan duplikasi kode antara View dan Template.
- MVVM (Model-View-ViewModel) : Pada MVVM, VM (ViewModel) merepresentasikan sebagai perantara antara Model dan View. ViewModel memisahkan tampilan dari logika bisnis dengan cara yang lebih kuat dibandingkan dengan Controller dan Template. MVVM memungkinkan pengujian unit lebih mudah dan juga memungkinkan penggunaan data binding untuk memperbarui View secara otomatis saat ViewModel berubah. Namun, hal ini dapat menyebabkan peningkatan kompleksitas.


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
![show_html_postman](./images/show_html_postman.jpg)
![show_html](./images/show_html.jpg)
2. Show XML
![show_xml](./images/show_xml.jpg)
3. Show JSON
![show_xml](./images/show_json.jpg)
4. Show XML By ID
![show_xml](./images/show_xml_by_id.jpg)
5. Show JSON By ID
![show_xml](./images/show_json_by_id.jpg)


# Tugas 4

## Apa itu Django `UserCreationForm`, dan jelaskan apa kelebihan dan kekurangannya?

- `UserCreationForm` adalah salah satu dari banyak formulir bawaan yang disediakan oleh Django. Django `UserCreationForm` digunakan untuk membuat user baru yang dapat menggunakan aplikasi web kita. `UserCreationForm` memiliki 3 field: username, password1, password2 (yang pada dasarnya digunakan untuk konfirmasi password).
- Berikut ini adalah __kelebihan__ dari `UserCreationForm` :
1. __Mudah Digunakan__. `UserCreationForm` mudah untuk digunakan dan dapat disesuaikan dengan kebutuhan pembuat website / aplikasi.
2. __Integrasi dengan Model User Django__. Form ini dirancang untuk berintegrasi dengan baik dengan model user bawaan Django atau model custom user yang telah dibuat.
3. __Validasi Otomatis__. `UserCreationForm` melakukan validasi otomatis pada data yang dimasukkan oleh user, seperti memastikan bahwa password sesuai dengan persyaratan keamanan yang telah ditetapkan.
4. __Kustomisasi__. `UserCreationForm` bisa dilakukan kustomisasi secara bebas oleh pembuat website / aplikasi sesuai dengan kebutuhan masing-masing.
- Berikut ini adalah __kekurangan__ dari `UserCreationForm` :
1. __Pembatasan Fungsionalitas__. Fungsionalitas yang dimiliki oleh `UserCreationForm` sangatlah sederhana, sehingga pembuat harus menambahkan fitur-fitur tambahan jika ingin membuat sebuah form pendaftaran user yang lebih kompleks.
2. __Keterbatasan dalam Desain__. Tampilan dan desain form yang dimiliki oleh `UserCreationForm` sangat sederhana. Jika ingin membuat tampilan form yang lebih menarik atau responsif, maka kita perlu membuat tampilan formulir secara manual.
3. __Keamanan__. Meskipun `UserCreationForm` melakukan validasi otomatis terhadap password, masih perlu memastikan bahwa praktik keamanan yang tepat diterapkan dalam penggunaan form ini untuk menghindari adanya serangan yang tidak diinginkan seperti serangan _brute force_.

## Apa perbedaan antara autentikasi dan otorisasi dalam konteks Django, dan mengapa keduanya penting?

1. __Autentikasi__ adalah proses memverifikasi identitas user. Autentikasi umumnya melibatkan proses login dimana user harus memberikan kredensial seperti username dan password. Autentikasi bertujuan untuk memastikan bahwa hanya user yang sah yang memiliki izin untuk mengakses aplikasi kita. Dengan kata lain, autentikasi adalah proses memverifikasi identitas pengguna.
- Dalam konteks Django, Django menyediakan modul `django.contrib.auth` yang memiliki sistem autentikasi bawaan. Modul ini menyertakan views, forms, dan models yang membantu dalam proses autentikasi, seperti login, logout, dan pendaftaran user.
2. __Otorisasi__ proses menentukan perizinan user setelah mereka berhasil login ke dalam website / aplikasi. Otorisasi mengatur hak akses dan izin user berdasarkan peran atau peraturan tertentu. Otorisasi bertujuan untuk memastikan bahwa setelah autentikasi, user hanya memiliki akses ke bagian-bagian aplikasi / website yang sesuai dengan peran dan izin mereka.
- Dalam konteks Django, Django menyediakan sistem perizinan (_permissions_) yang memungkinkan pembuat website untuk mendefinisikan izin khusus pada objek (misalnya, apakah user tertentu dapat mengedit objek tertentu) atau tindakan (seperti menambah, mengubah, atau menghapus). Selain itu, dengan model Group, Django memungkinkan pengelompokan izin bersama-sama, sehingga memudahkan dalam pemberian izin.

## Apa itu _cookies_ dalam konteks aplikasi web, dan bagaimana Django menggunakan _cookies_ untuk mengelola data sesi pengguna?

- __Cookie HTTP__ (juga disebut cookie web, cookie Internet, cookie browser, atau cookie sederhana) adalah sepotong kecil data yang dikirim dari website dan disimpan di komputer user oleh website user saat user berselancar di dalam web. Teknologi ini dirancang untuk menjadi mekanisme bagi website untuk mengingat informasi _stateful_ (seperti barang yang ditambahkan dalam keranjang belanja di toko online) atau untuk merekam aktivitas penelusuran user. Cookies juga dapat digunakan untuk mengingat potongan informasi dan data yang sebelumnya dimasukkan user ke dalam form seperti nama, alamat, password.
- Dalam konteks Django, Django menggunakan _cookies_, khususnya cookie yang berisi identifikasi unik yang disebut "session ID", untuk mengidentifikasi _user session_. Ketika user terautentikasi, ID sesi disimpan di dalam cookie, yang kemudian digunakan untuk mengidentifikasi user saat melakukan login kembali ke server atau berpindah antar halaman.

## Apakah penggunaan _cookies_ aman secara default dalam pengembangan web, atau apakah ada risiko potensial yang harus diwaspadai?

Penggunaan cookies dalam pengembangan web dapat menjadi alat yang bermanfaat untuk menyimpan informasi di sisi klien (pada perangkat user) untuk berbagai keperluan, seperti autentikasi, user session, analisis, dan personalisasi. Namun, penggunaan cookies juga dapat memiliki potensi risiko keamanan seperti :
1. __Cross-Site Scripting (XSS)__. Ada potensi bahwa hacker dapat mencoba mencuri cookies user jika website yang menggunakan cookies vulnerable. Hal ini dapat menyebabkan hacker mendapatkan akses ke akun pengguna.
2. __Session Hijacking__. Jika cookies digunakan untuk mengelola user session, hacker dapat mencoba mencuri atau memodifikasi cookies session untuk mengambil alih user session.
3. __Cookie Theft__. Cookies yang tidak aman atau tidak terenkripsi dapat dicuri oleh hacker melalui berbagai teknik seperti _network sniffing_ atau serangan perantara.
4. __Privacy Concerns__. Penggunaan cookies untuk melacak perilaku user dapat menimbulkan masalah privasi dan dapat melibatkan persyaratan hukum tertentu seperti GDPR di Uni Eropa.

## Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).

### Membuat Fungsi dan Form Registrasi

1. Menambahkan import `redirect`, `UserCreationForm`, dan `messages` pada bagian `views.py` pada subdirektori `main`.
2. Membuat fungsi `register` pada `views.py` dengan menambahkan kode sebagai berikut :
```py
def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context)
```
3. Membuat berkas HTML baru dengan nama `register.html` pada folder `templates` pada direktori main dan menambahkan potongan kode sebagai berikut :
```html
{% extends 'base.html' %}

{% block meta %}
    <title>Register</title>
{% endblock meta %}

{% block content %}  

<div class = "login">
    
    <h1>Register</h1>  

        <form method="POST" >  
            {% csrf_token %}  
            <table>  
                {{ form.as_table }}  
                <tr>  
                    <td></td>
                    <td><input type="submit" name="submit" value="Daftar"/></td>  
                </tr>  
            </table>  
        </form>

    {% if messages %}  
        <ul>   
            {% for message in messages %}  
                <li>{{ message }}</li>  
                {% endfor %}  
        </ul>   
    {% endif %}

</div>  

{% endblock content %}
```
4. Menambahkan import fungsi `register` pada `urls.py` dan menambahkan path url ke dalam `urlpatterns` dengan kode sebagai berikut :
```py
...
path('register/', register, name='register'),
...
```

### Membuat Fungsi Login

5. Pada pembuatan fungsi login, pertama-tama, pada `views.py` di subdirektori `main`, menambahkan import `authenticate` dan `login` dari `django.contrib.auth`. Setelah itu, dibuatlah fungsi `login_user` dengan menambahkan kode sebagai berikut :
```py
def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('main:show_main')
        else:
            messages.info(request, 'Sorry, incorrect username or password. Please try again.')
    context = {}
    return render(request, 'login.html', context)
```
6. Setelah dibuat fungsi `login_user`, dibuatlah berkas HTML baru dengan nama `login.html` pada folder `templates` di direktori `main` yang berisi kode sebagai berikut :
```html
{% extends 'base.html' %}

{% block meta %}
    <title>Login</title>
{% endblock meta %}

{% block content %}

<div class = "login">

    <h1>Login</h1>

    <form method="POST" action="">
        {% csrf_token %}
        <table>
            <tr>
                <td>Username: </td>
                <td><input type="text" name="username" placeholder="Username" class="form-control"></td>
            </tr>
                    
            <tr>
                <td>Password: </td>
                <td><input type="password" name="password" placeholder="Password" class="form-control"></td>
            </tr>

            <tr>
                <td></td>
                <td><input class="btn login_btn" type="submit" value="Login"></td>
            </tr>
        </table>
    </form>

    {% if messages %}
        <ul>
            {% for message in messages %}
                <li>{{ message }}</li>
            {% endfor %}
        </ul>
    {% endif %}     
        
    Don't have an account yet? <a href="{% url 'main:register' %}">Register Now</a>

</div>

{% endblock content %}
```
7. Menambahkan import fungsi `login_user` pada `urls.py` dan menambahkan path url untuk fungsi tersebut dengan kode sebagai berikut :
```py
...
path('login/', login_user, name='login'),
...
```

### Membuat Fungsi Logout

8. Pada pembuatan fungsi logout, pertama-tama, pada `views.py` di subdirektori `main`, menambahkan import `logout` dari `django.contrib.auth`. Setelah itu, dibuatlah fungsi `logout_user` dengan menambahkan kode sebagai berikut :
```py
def logout_user(request):
    logout(request)
    return redirect('main:login')
```
9. Setelah dibuat fungsi logout, ditambahkan hyperlink tag untuk _Logout_ pada berkas `main.html` dengan kode sebagai berikut :
```html
...
<a href="{% url 'main:logout' %}">
    <button>
        Logout
    </button>
</a>
...
```
10. Setelah dibuat button logout, menambahkan import fungsi `logout_user` pada `urls.py` serta menambahkan path url untuk fungsi tersebut dengan kode sebagai berikut :
```py
...
path('logout/', logout_user, name='logout'),
...
```

### Merestriksi Akses Halaman Main

11. Ketika ingin membuat restriksi akses halaman `main`, menambahkan import `login_required` dari `django.contrib.auth.decorators` di `views.py`, kemudian menambahkan kode `@login_required(login_url='/login')` di atas fungsi `show_main` agar halaman `main` hanya dapat diakses oleh pengguna yang sudah login (terautentikasi).

### Menggunakan Data Dari Cookies

12. Untuk menggunakan data dari _Cookies_, tambahkan import `datetime`, `HttpResponseRedirect`, dan `reverse` pada `views.py`. Setelah itu, pada fungsi `login_user`, dilakukan penggantian kode yang ada pada blok `if user is not None` menjadi potongan kode berikut :
```py
...
if user is not None:
    login(request, user)
    response = HttpResponseRedirect(reverse("main:show_main")) 
    response.set_cookie('last_login', str(datetime.datetime.now()))
    return response
...
```
13. Pada fungsi `show_main`, ditambahkan kode `'last_login': request.COOKIES['last_login']` ke dalam variabel `context`.
14. Mengubah fungsi `logout_user` dengan kode sebagai berikut :
```py
def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response
```
15. Pada `main.html`, ditambahkan potongan kode sebagai berikut untuk menampilkan data _last login_ :
```html
...
<h5>Sesi terakhir login: {{ last_login }}</h5>
...
```

### Menghubungkan Model `Product` dengan `User`

16. Untuk menghubungkan model `Item` dengan `User`, pada `models.py` ditambahkan import `User` dari `django.contrib.auth.models`. Kemudian pada class `Item` ditambahkan potongan kode sebagai berikut :
```py
class Item(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ...
```
17. Pada `views.py`, mengubah fungsi `create_item` menjadi sebagai berikut :
```py
def create_item(request):
 form = ItemForm(request.POST or None)

 if form.is_valid() and request.method == "POST":
     item = form.save(commit=False)
     item.user = request.user
     item.save()
     return HttpResponseRedirect(reverse('main:show_main'))
 ...
 ```
 18. Setelah itu, dilakukan perubahan pada fungsi `show_main` menjadi sebagai berikut :
 ```py
 def show_main(request):
    items = Item.objects.filter(user=request.user)

    context = {
        'name': request.user.username,
    ...
...
```
Yang terakhir adalah dilakukan migrasi model dengan `python manage.py makemigrations` dan mengaplikasikan migrasi yang dilakukan pada poin sebelumnya dengan `python manage.py migrate`.