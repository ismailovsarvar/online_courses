from django.urls import path

from courses.views import (
    CourseView,
CourseDetailView,
    WebDesignView,
    DevelopmentView,
    GameDesignView,
    AppsDesignView,
    MarketingView,
    ResearchView,
    ContentView,
    SeoView,
)

urlpatterns = [
    path('course/', CourseView.as_view(), name='courses'),
    # Courses link:
    path('course/<slug:slug>/', CourseDetailView.as_view(), name='course_detail'),
    path('web-design/', WebDesignView.as_view(), name='web_design'),
    path('development/', DevelopmentView.as_view(), name='development'),
    path('game-design/', GameDesignView.as_view(), name='game_design'),
    path('app-design/', AppsDesignView.as_view(), name='apps_design'),
    path('marketing/', MarketingView.as_view(), name='marketing'),
    path('research/', ResearchView.as_view(), name='research'),
    path('content/', ContentView.as_view(), name='content'),
    path('seo/', SeoView.as_view(), name='seo'),
]
