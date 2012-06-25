from django.conf.urls.defaults import *
from fileupload.views import PictureCreateView, PictureDeleteView, multiple_uploader


urlpatterns = patterns('',
    (r'^new/$', PictureCreateView.as_view(), {}, 'upload-new'),
    (r'^new/add/$', multiple_uploader, {}, 'upload-add'),
    (r'^delete/(?P<pk>\d+)$', PictureDeleteView.as_view(), {}, 'upload-delete'),
)

