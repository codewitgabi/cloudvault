# Installation

Cloudvault is built off of the [Cloudinary](https://cloudinary.com/) platform. So before installing the package, it will be great to create an account and get the 'API CREDENTIALS'.

Click [here](https://cloudinary.com/users/register_free) to create an account and then get your credentials on login.

After that, you can proceed to `cloudvault` installation.

```
pip install cloudvault
```

Once `cloudvault` is installed, go to your project's settings.py and add the following lines

```
#!/usr/bin/python

# settings.py

INSTALLED_APPS = [
    # ... other apps
    "cloudvault" # can be omitted
]

CLOUDINARY = {
    "cloud_name": "your_cloud_name",
    "api_key": "your_api_key",
    "api_secret": "your_api_secret"
}

DEFAULT_FILE_STORAGE = "cloudvault.cloud_storage.CloudinaryStorage"

```

## Usage
Nothing changes when using `cloudvault` in your project.

```
#!/usr/bin/python

# models.py


class Picture(models.Model):
    image = models.ImageField()

    def __str__(self);
        return str(self.id)


```

When a `Picture` instance is saved, it saves it to cloudinary `self.image.url` returns a url that points to the image on `cloudinary`


## Installing the Project Locally

To install the project, simply clone the project to your system and then run

```
python -m pip install /path/to/project/cloudvault/cloudvault/dist/cloudvault-1.1.tar.gz
```

The project should install successfully.

### Author
Gabriel Michael Ojomakpene\
codewitgabi222@gmail.com\
09020617734
