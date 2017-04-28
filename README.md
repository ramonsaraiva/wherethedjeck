# wherethedjeck

![Python 2.7](https://img.shields.io/badge/python-2.7-blue.svg)
![Python 3.6](https://img.shields.io/badge/python-3.6-blue.svg)

Quickly find where the heck things are in Django framework
> When reading the official Django documentation or developing your own things, there is a big chance you will forget from what module you should import the class `X`, the function `Y` or the decorator `Z`.

## Installing
```
pip install wherethedjeck
```

## Usage
The only requirement to use it, of course, is to have to Django package in your virtual-env or your python environment.
Besides that, in your terminal:
### Single queries

```
~$ wtd View
>> from django.views.generic.base import View
~$ wtd ModelForm
>> from django.forms.models import ModelForm
~$ wtd csrf_exempt
>> from django.views.decorators.csrf import csrf_exempt
```

### Multiple queries
```
~$ wtd Group Permission get_object_or_404 ContentType redirect reverse
from django.contrib.auth.models import Group
from django.contrib.auth.models import Permission
from django.shortcuts import get_object_or_404
from django.contrib.contenttypes.models import ContentType
from django.shortcuts import redirect
from django.urls.base import reverse
```

And that's it, no more wasted time on that.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details
