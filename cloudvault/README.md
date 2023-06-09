# Project Description
**cloudvault** 

cloudvault is a django package for file upload similar to using AWS S3-Bucket. It uses the **Cloudinary** Platform which is cheaper and easier to integrate.

Quickly deploy or test your django application using `cloudvault`.

## Installation

```
pip install cloudvault
```

## Quick Start

1. Add "cloudvault" to your `INSTALLED_APPS` in settings.py

```
INSTALLED_APPS = [
    # other apps
    "cloudvault",
]
```

2. Configure your `Cloudinary settings`

```
CLOUDINARY = [
    "cloud_name": "",
    "api_key": "",
    "api_secret": ""
]
```

3. Change `DEFAULT_FILE_STORAGE` in your settings.py

```
DEFAULT_FILE_STORAGE = "cloudvault.cloud_storage.CloudinaryStorage"
```

4. You can now upload image, videos from here.

