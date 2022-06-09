from django.urls import include, path

from api.views import GuessView

app_name = 'api'

guess_pattern = [path('guess/', GuessView.as_view(), name='guess')]


urlpatterns = [
    path('v1.0/', include(guess_pattern)),
]
