from django.test import TestCase

# Create your tests here.
class PostTestClass(TestCase):
 
    # testing instance
    def test_instance(self):
        self.assertTrue(isinstance(self.post,Image))

    # Test Saving
    def test_save_method(self):
        self.post.save_image()
        post = Post.objects.all()
        self.assertTrue(len(images)>0)

    # Test deleting
    def test_delete_method(self):
        self.image.delete_image()
        post = Post.objects.all()
        self.assertTrue(len(images)<1)

    # Tests whether the image caption is updated
    def test_update_image_caption(self):
        
        self.image.save_image()
        self.image.update_image_caption(self.image.id,'city')
        new_update = Image.objects.get(name = "image")
        self.assertEqual(new_update.caption, 'city')


