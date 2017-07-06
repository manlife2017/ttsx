from django.db import models


# Create your models here.
class GoodsType(models.Model):
    typename = models.CharField(max_length=30)

    def __str__(self):
        return self.typename

    class Meta(object):
        db_table = 'goodstype'


class GoodsInfoManager(models.Manager):

    def create(self, b):
        for i in range(1, 22):
            g = GoodsInfo()
            g.gname = b.typename + str(i)
            g.gtype = b
            g.gprice = 22.39 + i
            g.gintro = g.gname + '浆果柔软多汁，味美爽口，适合速冻保鲜贮藏。草莓速冻后，可以保持原有的色、香、味，既便于贮藏，又便于外销。'
            g.gdescription = '草莓采摘园位于北京大兴区 庞各庄镇四各庄村 ，每年1月-6月面向北京以及周围城市提供新鲜草莓采摘和精品礼盒装草莓，草莓品种多样丰富，个大香甜。所有草莓均严格按照有机标准培育，不使用任何化肥和农药。草莓在采摘期间免洗可以直接食用。欢迎喜欢草莓的市民前来采摘，也欢迎各大单位选购精品有机草莓礼盒，有机草莓礼盒是亲朋馈赠、福利送礼的最佳选择。'
            if i < 10:
                 g.gimg = 'goods/goods00'+str(i)+'.jpg'
                 g.gbidimg = 'goods/goods00'+str(i)+'.jpg'
            else:
                g.gimg = 'goods/goods0'+str(i)+'.jpg'
                g.gbidimg = 'goods/goods0'+str(i)+'.jpg'
            g.save()


class GoodsInfo(models.Model):
    gname = models.CharField(max_length=30)
    gtype = models.ForeignKey('GoodsType')
    gprice = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    gunti = models.CharField(max_length=20, default='500g')
    gmoods = models.IntegerField(default=0)
    gsurplus = models.IntegerField(default=1000)
    gintro = models.CharField(max_length=100)
    gdescription = models.TextField()
    gimg = models.ImageField(upload_to='goods/')
    gbigimg = models.ImageField(upload_to='goods/')
    goods = GoodsInfoManager()

    class Meta(object):
        db_table = 'goodsinfo'


