import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


local = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

mysql = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'bienestar',
        'USER': 'root',
        'PASSWORD': '',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}

heroku = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'd6s49obdnq004',
        'USER': 'ctchuysnckazuq',
        'PASSWORD': 'oQIvhlLn_OIKYYel_Ep_o8PREo',
        'HOST': 'ec2-54-243-249-173.compute-1.amazonaws.com',
        'PORT': '5432',
    }
}