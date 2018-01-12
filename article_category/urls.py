from django.conf.urls import url


from article_category.views import manage_category
from article_category.views import get_all_articles_by_category
from article_category.views import get_all_category
from article_category.views import add_category
from article_category.views import edit_category
from article_category.views import delete_category

app_name = 'category'

urlpatterns = [
    url(r'^all/$', get_all_category, name='all_category'),
    url(r'^(?P<category_id>[\d]+)/$',
        get_all_articles_by_category,
        name='all_article'),
]


# urlpatterns used by backend
urlpatterns += [
    url(r'management/$', manage_category, name='manage'),
    url(r'add/$', add_category, name='add'),
    url(r'edit/(?P<category_id>[\d]+)/$', edit_category, name='edit'),
    url(r'category/(?P<category_id>[\d]+)/delete$',
        delete_category,
        name='delete'),
]

