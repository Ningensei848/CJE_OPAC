from django import forms


class SearchForm(forms.Form):
    # form <input type="text" name="keywords" required id="id_keywords">
    # before <input id="search" type="text" name="search" class="validate" required>
    keywords = forms.CharField(
        widget=forms.TextInput(attrs={
            'id': 'search',
            'class': 'validate',
        })
    )

