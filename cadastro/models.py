from django.db import models

class inscricao (models.model):
      nome = models.CharField(max_length=100)
      cpf = models.CharField('CPF', max_length=11, unique=True)
      idade = models.IntegerField()
      email = models.EmailField()
      telefone = models.CharField(max_length=20, blank=True)
      criado_em = models.DateTimeField('criado em', auto_now_add =True)
      
      class Meta:
              ordering = ['criado em']
              verbose_name = (u'nome')
              verbose_name_plural = (u'nome')
              
      def __unicode__(self):
              return self.nome