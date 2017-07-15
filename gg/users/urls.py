from django.conf.urls import url

from . import views

urlpatterns = [
    url(
        regex=r'^profile/pricelist/$',
        view=views.PriceListListView.as_view(),
        name='pricelist_list'
    ),
    url(
        regex=r'^profile/~pricelist/$',
        view=views.PriceListUpdateView.as_view(),
        name='pricelist_update'
    ),
    url(
        regex=r'^profile/pricelist/(?P<pk>[\w.@+-]+)/$',
        view=views.PriceListDetailView.as_view(),
        name='pricelist_detail'
    ),

    url(
        regex=r'^$',
        view=views.UserListView.as_view(),
        name='list'
    ),
    url(
        regex=r'^~redirect/$',
        view=views.UserRedirectView.as_view(),
        name='redirect'
    ),
    url(
        regex=r'^(?P<username>[\w.@+-]+)/$',
        view=views.UserDetailView.as_view(),
        name='detail'
    ),
    url(
        regex=r'^~update/$',
        view=views.UserUpdateView.as_view(),
        name='update'
    ),
]
