from django.conf.urls import url, patterns

urlpatterns = patterns('django_model.views'
        url(r'^$', 'employee_index', name='employees_list'),
        )
