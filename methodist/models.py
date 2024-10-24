from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Post(models.Model):  
    title = models.CharField(max_length=200)  
    content = models.TextField()  
    created_at = models.DateTimeField(auto_now_add=True) 

    def __str__(self):
        return (f"{self.title} {self.content}") 

class Comment(models.Model):  
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)  
    user = models.ForeignKey(User, on_delete=models.CASCADE)  
    text = models.TextField()  
    created_at = models.DateTimeField(auto_now_add=True)  

    def __str__(self):  
        return f"{self.user.username}: {self.text[:20]}"  

class Record(models.Model):
	created_at = models.DateTimeField(auto_now_add=True)
	first_name = models.CharField(max_length=50)
	last_name =  models.CharField(max_length=50)
	email =  models.CharField(max_length=100)
	phone = models.CharField(max_length=15)
	address =  models.CharField(max_length=100)
	city =  models.CharField(max_length=50)
	state =  models.CharField(max_length=50)
	zipcode =  models.CharField(max_length=20)

	def __str__(self):
		return(f"{self.first_name} {self.last_name}")


class Category(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True) 
    title = models.CharField(max_length=255)
    author = models.CharField(null=True, max_length=50)
    date = models.DateField(null=True)
    description = models.CharField(max_length=255, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True) 
    category_image = models.ImageField(upload_to='media/upload')
    thumbnail = models.ImageField(upload_to='media/uploads/', blank=True, null=True)

 
    def __str__(self):
        return self.title

    
    def get_thumbnail(self):
        if self.thumbnail:
            return self.thumbnail.url
        else:
            if self.image:
                self.thumbnail = self.make_thumbnail(self.image)
                self.save()
                return self.thumbnail.url
            
            else:
                # Default Image
                return 'https://via.placeholder.com/240x180.jpg'
    
    # Generating Thumbnail - Thumbnail is created when get_thumbnail is called
    def make_thumbnail(self, image, size=(300, 200)):
        img = Image.open(image)
        img.convert('RGB')
        img.thumbnail(size)

        thumb_io = BytesIO()
        img.save(thumb_io, 'JPEG', quality=85)

        thumbnail = File(thumb_io, name=image.name)

        return thumbnail    
    
    
class Staff(models.Model):  
    first_name = models.CharField(max_length=50)  
    last_name = models.CharField(max_length=50)  
    position = models.CharField(max_length=100)  
    image = models.ImageField(upload_to="media/upload", null=True)
    address = models.CharField(max_length=255, null=True)
    email = models.EmailField(null=True)
    phone = models.CharField(null=True, max_length=20)

    def __str__(self):  
        return f"{self.first_name} {self.last_name} - {self.position}"    