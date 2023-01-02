from django.db import models

class Card(models.Model):
    Category= models.CharField(max_length=500)
    url= models.URLField(blank=True)
    Tweet_Text=models.CharField(max_length=500)
    Trend_score=models.FloatField()
    IMAGE_URL=models.URLField(max_length=5000,blank=True)
    # hashtags_Tweet_Text": [],
    video_img_url= models.URLField(max_length=5000,blank=True)
    item_id=models.IntegerField()
    Brand=models.CharField(max_length=500)
    Sub_Category=models.CharField(max_length=500)
    Flipkart_url=models.URLField(max_length=5000,blank=True)
    product_image_link=models.URLField(blank=True)
    product_title=models.CharField(max_length=500)


# hash_tag : list of strings ------ one to many relation
# class Hash_tag_list(models.Model):
#     item_id= models.IntegerField()
#     hash_tag=models.CharField(max_length=500)
#     tag=models.ForeignKey(Card,on_delete=models.CASCADE)
