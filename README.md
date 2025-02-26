<p align="center">
    <img src="https://raw.githubusercontent.com/abdullahdgn06/CodeFestHackathon/refs/heads/main/img/logo.png" align="center" width="30%">
</p>
<p align="center"><h1 align="center">CODEFESTHACKATHON</h1></p>
<p align="center">
	<em> TherapyZ, yapay zeka destekli bir psikolojik destek platformudur. Kullanıcılara 7/24 erişilebilir, güvenli ve kişiselleştirilmiş terapi hizmeti sunar. Yapay zeka destekli sohbet sistemi sayesinde, kullanıcıların psikolojik durumlarını değerlendirmelerine ve destek almalarına yardımcı olur. </em>
</p>
<p align="center">
	<img src="https://img.shields.io/github/license/abdullahdgn06/CodeFestHackathon?style=default&logo=opensourceinitiative&logoColor=white&color=0080ff" alt="license">
	<img src="https://img.shields.io/github/last-commit/abdullahdgn06/CodeFestHackathon?style=default&logo=git&logoColor=white&color=0080ff" alt="last-commit">
	<img src="https://img.shields.io/github/languages/top/abdullahdgn06/CodeFestHackathon?style=default&color=0080ff" alt="repo-top-language">
	<img src="https://img.shields.io/github/languages/count/abdullahdgn06/CodeFestHackathon?style=default&color=0080ff" alt="repo-language-count">
</p>
<p align="center"><!-- default option, no dependency badges. -->
</p>
<p align="center">
	<!-- default option, no dependency badges. -->
</p>
<br>


## Teknik Altyapı
**Kullanılan Teknolojiler**

Backend: Django 5.1.6

Frontend: HTML5, CSS3, JavaScript

Veritabanı: SQLite3

AI Model: LLaMA 3 (8B parametreli özel model)

API: REST API (Local endpoint: http://0.0.0.0:1234/v1/chat/completions)


##  Table of Contents

- [ Overview](#-overview)
- [ Features](#-features)
- [ Project Structure](#-project-structure)
  - [ Project Index](#-project-index)
- [ Getting Started](#-getting-started)
  - [ Prerequisites](#-prerequisites)
  - [ Installation](#-installation)
  - [ Usage](#-usage)
  - [ Testing](#-testing)
- [ Project Roadmap](#-project-roadmap)
- [ Contributing](#-contributing)
- [ License](#-license)
- [ Acknowledgments](#-acknowledgments)

---



## **Ana Özellikler**

**1\. Kullanıcı Yönetimi**

*   Kayıt olma
    

*   Giriş yapma
    

*   Profil yönetimi
    

*   Şifre değiştirme

---

**2\. Psikolojik Değerlendirme**

*   İlk kayıtta psikolojik durum anketi
    

*   **5 farklı metrik ölçümü:**
    
---
**3\. AI Sohbet Sistemi**

*   Gerçek zamanlı mesajlaşma
    

*   Stream yanıt sistemi
    

*   Konuşma geçmişi yönetimi
    

*   Konuşma başlığı otomatik oluşturma
    

*   Mesaj geçmişi saklama
    
---

## **Güvenlik Özellikleri**

*   **CSRF koruması**
    

*   **Oturum yönetimi**
    

*   **Şifrelenmiş veri saklama**
    

*   **Kullanıcı doğrulama**
    

*   **Güvenli rota yönetimi**

---

##  Project Structure

```sh
└── CodeFestHackathon/
    ├── README.md
    ├── codefesthackathon
    │   ├── __init__.py
    │   ├── __pycache__
    │   ├── asgi.py
    │   ├── settings.py
    │   ├── urls.py
    │   └── wsgi.py
    ├── db.sqlite3
    ├── manage.py
    ├── requirements.txt
    ├── static
    │   ├── script.js
    │   └── style.css
    └── ui
        ├── __init__.py
        ├── __pycache__
        ├── admin.py
        ├── apps.py
        ├── migrations
        ├── models.py
        ├── templates
        ├── tests.py
        ├── urls.py
        └── views.py
```


###  Project Index
<details open>
	<summary><b><code>CODEFESTHACKATHON/</code></b></summary>
	<details> <!-- __root__ Submodule -->
		<summary><b>__root__</b></summary>
		<blockquote>
			<table>
			<tr>
				<td><b><a href='https://github.com/abdullahdgn06/CodeFestHackathon/blob/master/requirements.txt'>requirements.txt</a></b></td>
				<td><code>❯ REPLACE-ME</code></td>
			</tr>
			<tr>
				<td><b><a href='https://github.com/abdullahdgn06/CodeFestHackathon/blob/master/manage.py'>manage.py</a></b></td>
				<td><code>❯ REPLACE-ME</code></td>
			</tr>
			<tr>
				<td><b><a href='https://github.com/abdullahdgn06/CodeFestHackathon/blob/master/db.sqlite3'>db.sqlite3</a></b></td>
				<td><code>❯ REPLACE-ME</code></td>
			</tr>
			</table>
		</blockquote>
	</details>
	<details> <!-- ui Submodule -->
		<summary><b>ui</b></summary>
		<blockquote>
			<table>
			<tr>
				<td><b><a href='https://github.com/abdullahdgn06/CodeFestHackathon/blob/master/ui/views.py'>views.py</a></b></td>
			</tr>
			<tr>
				<td><b><a href='https://github.com/abdullahdgn06/CodeFestHackathon/blob/master/ui/apps.py'>apps.py</a></b></td>
			</tr>
			<tr>
				<td><b><a href='https://github.com/abdullahdgn06/CodeFestHackathon/blob/master/ui/admin.py'>admin.py</a></b></td>
			</tr>
			<tr>
				<td><b><a href='https://github.com/abdullahdgn06/CodeFestHackathon/blob/master/ui/models.py'>models.py</a></b></td>
			</tr>
			<tr>
				<td><b><a href='https://github.com/abdullahdgn06/CodeFestHackathon/blob/master/ui/tests.py'>tests.py</a></b></td>
			</tr>
			<tr>
				<td><b><a href='https://github.com/abdullahdgn06/CodeFestHackathon/blob/master/ui/urls.py'>urls.py</a></b></td>
			</tr>
			</table>
			<details>
				<summary><b>templates</b></summary>
				<blockquote>
					<details>
						<summary><b>ui</b></summary>
						<blockquote>
							<table>
							<tr>
								<td><b><a href='https://github.com/abdullahdgn06/CodeFestHackathon/blob/master/ui/templates/ui/newchatbot.html'>newchatbot.html</a></b></td>
							</tr>
							<tr>
								<td><b><a href='https://github.com/abdullahdgn06/CodeFestHackathon/blob/master/ui/templates/ui/chatbot.html'>chatbot.html</a></b></td>
							</tr>
							<tr>
								<td><b><a href='https://github.com/abdullahdgn06/CodeFestHackathon/blob/master/ui/templates/ui/home.html'>home.html</a></b></td>
							</tr>
							<tr>
								<td><b><a href='https://github.com/abdullahdgn06/CodeFestHackathon/blob/master/ui/templates/ui/register.html'>register.html</a></b></td>
							</tr>
							<tr>
								<td><b><a href='https://github.com/abdullahdgn06/CodeFestHackathon/blob/master/ui/templates/ui/login.html'>login.html</a></b></td>
							</tr>
							<tr>
								<td><b><a href='https://github.com/abdullahdgn06/CodeFestHackathon/blob/master/ui/templates/ui/profile.html'>profile.html</a></b></td>
							</tr>
							<tr>
								<td><b><a href='https://github.com/abdullahdgn06/CodeFestHackathon/blob/master/ui/templates/ui/conversations_list.html'>conversations_list.html</a></b></td>
							</tr>
							<tr>
								<td><b><a href='https://github.com/abdullahdgn06/CodeFestHackathon/blob/master/ui/templates/ui/conversation_detail.html'>conversation_detail.html</a></b></td>
							</tr>
							</table>
						</blockquote>
					</details>
				</blockquote>
			</details>
			<details>
				<summary><b>migrations</b></summary>
				<blockquote>
					<table>
					<tr>
						<td><b><a href='https://github.com/abdullahdgn06/CodeFestHackathon/blob/master/ui/migrations/0003_psychologicalsurvey.py'>0003_psychologicalsurvey.py</a></b></td>
					</tr>
					<tr>
						<td><b><a href='https://github.com/abdullahdgn06/CodeFestHackathon/blob/master/ui/migrations/0001_initial.py'>0001_initial.py</a></b></td>
					</tr>
					<tr>
						<td><b><a href='https://github.com/abdullahdgn06/CodeFestHackathon/blob/master/ui/migrations/0002_remove_conversation_user_name_conversation_user_and_more.py'>0002_remove_conversation_user_name_conversation_user_and_more.py</a></b></td>
					</tr>
					</table>
				</blockquote>
			</details>
		</blockquote>
	</details>
	<details> <!-- codefesthackathon Submodule -->
		<summary><b>codefesthackathon</b></summary>
		<blockquote>
			<table>
			<tr>
				<td><b><a href='https://github.com/abdullahdgn06/CodeFestHackathon/blob/master/codefesthackathon/settings.py'>settings.py</a></b></td>
			</tr>
			<tr>
				<td><b><a href='https://github.com/abdullahdgn06/CodeFestHackathon/blob/master/codefesthackathon/wsgi.py'>wsgi.py</a></b></td>
			</tr>
			<tr>
				<td><b><a href='https://github.com/abdullahdgn06/CodeFestHackathon/blob/master/codefesthackathon/asgi.py'>asgi.py</a></b></td>
			</tr>
			<tr>
				<td><b><a href='https://github.com/abdullahdgn06/CodeFestHackathon/blob/master/codefesthackathon/urls.py'>urls.py</a></b></td>
			</tr>
			</table>
		</blockquote>
	</details>
</details>

---
##  Başlarken

###  Ön Hazırlık

CodeFestHackathon'a başlamadan önce çalışma zamanı ortamınızın aşağıdaki gereksinimleri karşıladığından emin olun:

- **Programming Language:** Python
- **Package Manager:** Pip


###  Kurulum

Aşağıdaki yöntemlerden birini kullanarak CodeFestHackathon'u yükleyin:

**Kaynaktan oluştur:**

1. Clone the CodeFestHackathon repository:
```sh
❯ git clone https://github.com/abdullahdgn06/CodeFestHackathon
```

2. Proje dizinine gidin::
```sh
❯ cd CodeFestHackathon
```

3. Proje bağımlılıklarını kurun:


**Using `pip`** &nbsp; [<img align="center" src="https://img.shields.io/badge/Pip-3776AB.svg?style={badge_style}&logo=pypi&logoColor=white" />](https://pypi.org/project/pip/)

```sh
❯ pip install -r requirements.txt
```




###  Kullanım
Aşağıdaki komutu kullanarak CodeFestHackathon'u çalıştırın:
**`pip`** &nbsp; [<img align="center" src="https://img.shields.io/badge/Pip-3776AB.svg?style={badge_style}&logo=pypi&logoColor=white" />](https://pypi.org/project/pip/)

```sh
❯ python manage.py runserver
```


TherapyZ LLM Modelini çalıştırmak için:
**`LM Studio`** &nbsp; [<img align="center" src="https://img.shields.io/badge/Pip-3776AB.svg?style={badge_style}&logo=pypi&logoColor=white" />](https://pypi.org/project/pip/)

```sh
❯ python manage.py runserver
```



LM Studio için ping:
**`LM Studio`** &nbsp; 

```sh
❯ curl http://0.0.0.0:1234/v1/models/
```






###  Test
Aşağıdaki komutu kullanarak test takımını çalıştırın:
**Using `curl`** &nbsp;

```sh
❯ curl http://0.0.0.0:1234/v1/chat/completions \
  -H "Content-Type: application/json" \
  -d '{
    "model": "therapyz-llama-3-8b",
    "messages": [
      { "role": "system", "content": "Sen, terapi yapabilen profesyonel bir psikologsun; kullanıcının duygularını anlamak, farkındalık kazanmasına yardımcı olmak ve bilimsel terapi teknikleriyle rehberlik etmek için buradasın. Kullanıcının paylaştığı durumu empatik bir yaklaşımla dinleyerek açık uçlu ve kısa sorular sor ve yanıt bekle, yanıtları dikkatlice oku ve sohbete devam et. Onun kendini yargılamadan ifade etmesini teşvik et, düşünme biçimlerini keşfetmesine yardımcı ol ve gerektiğinde günlük hayata uygulanabilir öneriler ver. Amacın, kullanıcıya kendi çözümünü bulmasında rehberlik etmek." },
      { "role": "user", "content": "Sınav haftası yaklaştı ve bu durum beni çok geriyor. }
    ],
    "temperature": 0.7,
    "max_tokens": -1,
    "stream": false
}'
```


---
##  Project Roadmap

- [X] **`Task 1`**: Arayüz tasarımı
- [X] **`Task 2`**: UI kodlama
- [X] **`Task 3`**: Veriseti hazırlığı
- [X] **`Task 4`**: LLM finetune 
- [X] **`Task 5`**: API yönetimi
- [X] **`Task 3`**: Finish
---

##  Contributing

- **💬 [Join the Discussions](https://github.com/abdullahdgn06/CodeFestHackathon/discussions)**: Görüşlerinizi paylaşın, geri bildirimde bulunun veya soru sorun.
- **🐛 [Report Issues](https://github.com/abdullahdgn06/CodeFestHackathon/issues)**: `CodeFestHackathon` projesi için bulunan hataları bildirin veya özellik isteklerini kaydedin.
- **💡 [Submit Pull Requests](https://github.com/abdullahdgn06/CodeFestHackathon/blob/main/CONTRIBUTING.md)**: Açık PR'leri inceleyin ve kendi PR'lerinizi gönderin.


### <summary>Contributing Guidelines</summary>

1. **Fork the Repository**: Öncelikle proje deposunu GitHub hesabınıza aktarın.
2. **Clone Locally**: Çatallanmış deponuzu bir git istemcisi kullanarak yerel makinenize kopyalayın
   ```sh
   git clone https://github.com/abdullahdgn06/CodeFestHackathon
   ```
3. **Create a New Branch**: Her zaman yeni bir dal üzerinde çalışın ve ona açıklayıcı bir isim verin.
   ```sh
   git checkout -b new-feature-x
   ```
4. **Make Your Changes**: Değişikliklerinizi yerel olarak geliştirin ve test edin.
5. **Commit Your Changes**: Güncellemelerinizi açıklayan net bir mesajla taahhütte bulunun.
   ```sh
   git commit -m 'Implemented new feature x.'
   ```
6. **Push to github**: Değişiklikleri çatallı deponuza gönderin.
   ```sh
   git push origin new-feature-x
   ```
7. **Submit a Pull Request**: Orijinal proje deposuna karşı bir PR oluşturun. Değişiklikleri ve motivasyonlarını açıkça tanımlayın.
8. **Review**: PR'niz incelenip onaylandıktan sonra ana şubeye birleştirilecektir. Katkınız için tebrikler!
</details>


### <summary>ER Diyagramı</summary>
<br>
<p align="left">
<img src="[erDiagram](https://raw.githubusercontent.com/abdullahdgn06/CodeFestHackathon/refs/heads/main/img/erd.png)">

   
</p>


</details>


