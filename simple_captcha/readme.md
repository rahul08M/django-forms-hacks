# Simple Cptcha using django
## Inplementation of [django-simple-captcha](https://django-simple-captcha.readthedocs.io/en/latest/usage.html)

### 1. Install django-simple-captcha 
```
pip install django-simple-captcha
```

### 2. Add ```captcha``` to the ```INSTALLED_APPS``` in your ```settings.py```
### 3. Migrate
```
python manange.py migrate
python manange.py migrate --settings app.settings # if you are using multiple settings
```

### 4. Add an entry to your root/base ```urls.py```

```
urlpatterns += [
    path('captcha/', include('captcha.urls')),
]
```
