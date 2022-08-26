from django.db import models

#データベース的な
#python manage.py makemigrationsを実行
#python manage.py migrateを実行

#python manage.py shellでコンソールを開き
#from myapp.models import Personでクラスを読み込み
#p = Person(last_name="Python", first_name="Taro")でインスタンスを作成
#p.last_nameでインスタンスのフィールドを確認できる
class Person(models.Model):
    last_name = models.CharField(max_length=20)
    first_name = models.CharField(max_length=20)
    created = models.DateTimeField(auto_now_add=True)
    saved = models.DateTimeField(auto_now=True)
    age = models.IntegerField()
