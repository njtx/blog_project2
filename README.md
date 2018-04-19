# blog_project2
### python3+django2.0.4 简单版博客-阶段一
##### 1 创建项目
##### 2 选用sqlite3数据库，后期改用mysql
##### 3 创建app blog
##### 4 写User模块类,作为映射数据库表user
## 5 遇到的问题
### 5.1 图片上传
#### 5.1.1 利用ImageField字段需要安装Pillow
####5.1.2 配置setting.py以及urls.py


setting.py:


  MEDIA_ROOT = os.path.join(BASE_DIR,'media_cdn')
  MEDIA_URL ='/media/'


urls.py:


  from django.conf import settings
  from django.views.static import serve

  if settings.DEBUG:
      urlpatterns += [
          re_path(r'^media/(?P<path>.*)$', serve, {
              'document_root': settings.MEDIA_ROOT,
          }),
      ]
   
   
   ### 5.1 django2中urls.py配置有改变
    1.把url函数换成path
    2.不在使用^、$作为路由
    3.如果想要使用正则，需要 import django.urls.re_path,然后把path换成re_path
