![The project's banner](https://github.com/LucasGoncSilva/lipsum/blob/main/readme_banner.svg?raw=true)


<h1 align='center'>:notebook: LIPSUM :notebook:</h1>


<h4 align='justify'>Made with Django as MVC framework, this project works as a real, useful online password manager. It uses cryptography to store the secrets in DB, so a DB leak of information will presents only encrypted data instead of raw sensitive information.</h4>


![GitHub last commit](https://img.shields.io/github/last-commit/LucasGoncSilva/lipsum?label=last%20main%20commit&style=for-the-badge)
![GitHub last commit (branch)](https://img.shields.io/github/last-commit/LucasGoncSilva/lipsum/dev?label=last%20dev%20commit&style=for-the-badge)
![Lines of code](https://img.shields.io/tokei/lines/github/LucasGoncSilva/lipsum?label=project%27s%20total%20lines&style=for-the-badge)
![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/LucasGoncSilva/lipsum?color=4717f6&style=for-the-badge)


<br>


![GitHub language count](https://img.shields.io/github/languages/count/LucasGoncSilva/lipsum?color=a903fc&style=for-the-badge)
![GitHub top language](https://img.shields.io/github/languages/top/LucasGoncSilva/lipsum?style=for-the-badge)


<br>
<hr>


<h2 align='center'>:chart_with_upwards_trend: Project's Status :chart_with_upwards_trend:</h2>

<img src='https://img.shields.io/badge/-Successfully%20done-0b0?style=for-the-badge'/>
<img src='https://img.shields.io/badge/-also%20work%20in%20progress...-fb0?style=for-the-badge'/>

:link: Check here: <https://lipsum.herokuapp.com> :link:


<br>
<hr>


<h2 align='center'>:floppy_disk: Applied Technologies :cloud:</h2>


![HTML logo](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)
![CSS logo](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white)
![Sass logo](https://img.shields.io/badge/Sass-CC6699?style=for-the-badge&logo=sass&logoColor=white)
![JavaScript logo](https://img.shields.io/badge/JavaScript-323330?style=for-the-badge&logo=javascript&logoColor=F7DF1E)
![Bootstrap logo](https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white)
<hr>


![Django logo](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=green)
<hr>


![PostgreSQL logo](https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white)
<hr>


![Heroku logo](https://img.shields.io/badge/Heroku-430098?style=for-the-badge&logo=heroku&logoColor=white)


<br>
<hr>


<h2 align='center'>:star: Features :star:</h2>


- [x] Save different services, even more than one save per services (e.g. two Instagram's accounts)
- [x] Save login's info for each saved service, such as email, username and password
- [x] Edit saved secrets once they get altered on the respective service
- [ ] Export your secrets to your email (the same used for login in this app)
- [ ] Generate locally pseudo-random passwords as platform suggestion


```mermaid
flowchart RL

subgraph CLOUD
    subgraph SYSTEM/APP
        View((View)):::Arch
        Template{Template}:::Arch
        Model{{Model}}:::Arch
    end

    Cover[/"cover()"/]
    Uncover[/"uncover()"/]

    subgraph DB-INSTANCE
        Database[(Database)]:::Arch
    end
end

User((User))


User -- CreateView:POST ----> View
View --> Model -- insert --> Cover --> Database
Model -- select --> Database
Database --> Uncover --> Model
Model --> View --> Template
Template -- DetailView --> User


click Cover "https://github.com/LucasGoncSilva/lipsum/blob/main/secret/encript_db.py"
click Uncover "https://github.com/LucasGoncSilva/lipsum/blob/main/secret/encript_db.py"


style CLOUD fill:#f0f0ff;
style SYSTEM/APP fill:#fff;
style DB-INSTANCE fill:#fff;
style User fill:#aaf,color:#fff,stroke:#008;
style Cover fill:#afa,color:#070,stroke:#070;
style Uncover fill:#afa,color:#070,stroke:#070;

classDef Arch fill:#f0f0ff,color:#008,stroke:#6f6fff;
```
<h5 align='center'>Lipsum's current architecture</h5>


<br>
<hr>


<h2 align='center'>:compass: Using :crystal_ball:</h2>

### Creating an Account

To start, if do not having an account, create one by going ate `/conta/registrar`, fill and submit the presented form. Then, insert your `username` and `password` you filled the creation form. Already have an account? Log in directly at `/conta/entrar` or clicking "Entrar" button.

<hr>

### Undestanding the Interface

After log in, at every moment, there wil be a navbar at the top of the page. You can use it to navegate through the system and get some actions like:

* Create and overview your credentials
* Create and overview your cards
* Create and overview your notes
* Log out of your account


#### Index Page

This page shows the total of each secret (credentials, cards, notes) and a little history of your last secrets registration. Also gives you access to create and overview more secret.


#### Creation Page

Using navbar (clicking in a dropdown menu) or clicking an "Adicionar" button on index page, you access a creation page. As the page's form get filled, the `slug` (readonly) field gets that secret's reference; You can use it later to access that secret from url (e.g. `/segredo/cartao/:slug:`).

Properly filling the page's form and submitting it, you create a new secret with the information filled in that creation form and get redirected to a page that shows all of your registered secrets of that type (credential - credencial; card - cartao/cartão; note - anotação).


#### List Page

This page shows all secret you registered, one type at once. You can access it after create a new secret or using navbar. By clicking a secret displayed here, the new page rendered is a detailed view of that secret. If there is no secret of a type registered, the page shows a text message. The green button gets you to the creation page.


#### Detail page

Here you get a detailed view of the choosen secret, showing every information of that one. Besides that, there are 3 buttons at the top: the blue one (for editting the current secret), the red (delete the current secret) and the gray one (for adding a new secret).


<br>
<hr>


<h2 align='center'>:warning: WARNINGS :warning:</h2>

* This project is already online, but also under development. Use it knowing that some bugs might happen, so keep, at least for now, your secrets that you have another way to access besides Lipsum.
* Due to it's gratuity, Lipsum supports a limited number of users, requests/online time and secrets stored on it's database. At some point this system will no longer offers registration for new users, preventing the database to colapse.
