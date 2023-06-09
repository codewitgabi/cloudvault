from django.core.files.storage import Storage
from django.conf import settings
import cloudinary
from cloudinary.uploader import upload
from cloudinary import CloudinaryResource


class CloudinaryStorage(Storage):
    """
    Custom storage class to handle uploaded images.
    """
    def __init__(self) -> None:
        self.cloud_name = settings.CLOUDINARY.get("cloud_name")
        self.api_key = settings.CLOUDINARY.get("api_key")
        self.api_secret = settings.CLOUDINARY.get("api_secret")

    def _save(self, name, content):
        # upload file to cloudinary
        response = upload(content, overwrite=False, resource_type="auto")

        # return cloudinary secure url
        url = response["secure_url"]

        return url;

    def url(self, name) -> str:
        """
        return the url of the uploaded file
        """
        return name;

    def exists(self, name) -> bool:
        """
        Checks if a file already exists at location.
        """
        try:
            response = cloudinary.api.resource(name)

            return response["exists"]
        except:
            return False


