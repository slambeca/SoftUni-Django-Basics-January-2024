from django.urls import path, include

from Petstagram.accounts.views import signup_user, signin_user, details_profile, edit_profile, delete_profile, \
    signout_user

urlpatterns = (
    path("signup/", signup_user, name="signup user"),
    path("signin/", signin_user, name="signin user"),
    path("signout/", signout_user, name="signout user"),

    path(
        "profile/<int:pk>/", include([
                path("", details_profile, name="details profile"),
                path("edit/", edit_profile, name="edit profile"),
                path("delete/", delete_profile, name="delete profile")
        ]),
    )
)
