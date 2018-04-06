from django.db import models
from djrichtextfield.models import RichTextField
# Create your models here.
class Category(models.Model):
    SHOP_CATEGORY_CHOICES = (
        (
            ('아우터', (
                ('셔츠', '셔츠'),
                ('가디건', '가디건'),
                ('코트', '코트'),
                ('점퍼', '점퍼'),
                ('패딩', '패딩'),
            )
            )
        ),
        ('티셔츠', (
            ('맨투맨', '맨투맨'),
            ('후드', '후드'),
            ('긴팔티/7부', '긴팔티/7부'),
            ('스트라이프', '스트라이프'),
            ('반팔', '반팔'),
            ('나시', '나시'),
        )
        ),
        ('셔츠', (
            ('베이직/기본', '베이직/기본'),
            ('체크/패턴', '체크/패턴'),
            ('스프라이프', '스프라이프'),
            ('헨리넥/차이나', '헨라넥/차이나'),
            ('데님', '데님'),
        )
        ),
        ('니트/가디건', (
            ('니트', '니트'),
            ('가디건', '가디건'),
            ('폴라&터틀', '폴라&터틀'),
        )
        ),
    )
    chop_category_name = models.CharField('상품-카테고리이름',max_length=20,choices=SHOP_CATEGORY_CHOICES,null=True,blank=True,default='')

class Item(models.Model):
    category=models.ForeignKey(Category,on_delete=models.CASCADE,default='',verbose_name='카테고리')
    item_code=models.CharField(max_length=100,default='',verbose_name='상품코드')
    price=models.PositiveIntegerField('가격',default=0)
    max_stock = models.PositiveIntegerField(default=1000, verbose_name='판매 재고(전체)')
    description = RichTextField(verbose_name='상품설명',default='')
