# Import forms to override
from allauth.account.forms import SignupForm, LoginForm, ResetPasswordForm


class CustomSingupForm(SignupForm):
    """
    Overrides all-auth form to add custom classes for UI interpolation.
    """

    def __init__(self, *args, **kwargs):
        print("I REACHED *#*#" * 10)
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            print(visible.field)
            visible.field.widget.attrs["class"] = "contactinput"
