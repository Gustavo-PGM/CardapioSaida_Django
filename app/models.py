from django.db import models

class Segunda(models.Model):
    merenda_manha = models.TextField(max_length=255)
    almoco = models.TextField(max_length=255)
    merenda_tarde = models.TextField(max_length=255)

    class Meta:
        verbose_name_plural = "Segunda"

    def __str__(self):
        return f"Segunda - Merenda Manhã: {self.merenda_manha}, Almoço: {self.almoco}, Merenda Tarde: {self.merenda_tarde}"

class Terca(models.Model):
    merenda_manha = models.TextField(max_length=255)
    almoco = models.TextField(max_length=255)
    merenda_tarde = models.TextField(max_length=255)

    class Meta:
        verbose_name_plural = "Terça"

    def __str__(self):
        return f"Terça - Merenda Manhã: {self.merenda_manha}, Almoço: {self.almoco}, Merenda Tarde: {self.merenda_tarde}"

class Quarta(models.Model):
    merenda_manha = models.TextField(max_length=255)
    almoco = models.TextField(max_length=255)
    merenda_tarde = models.TextField(max_length=255)

    class Meta:
        verbose_name_plural = "Quarta"

    def __str__(self):
        return f"Quarta - Merenda Manhã: {self.merenda_manha}, Almoço: {self.almoco}, Merenda Tarde: {self.merenda_tarde}"

class Quinta(models.Model):
    merenda_manha = models.TextField(max_length=255)
    almoco = models.TextField(max_length=255)
    merenda_tarde = models.TextField(max_length=255)

    class Meta:
        verbose_name_plural = "Quinta"

    def __str__(self):
        return f"Quinta - Merenda Manhã: {self.merenda_manha}, Almoço: {self.almoco}, Merenda Tarde: {self.merenda_tarde}"

class Sexta(models.Model):
    merenda_manha = models.TextField(max_length=255)
    almoco = models.TextField(max_length=255)
    merenda_tarde = models.TextField(max_length=255)

    class Meta:
        verbose_name_plural = "Sexta"

    def __str__(self):
        return f"Sexta - Merenda Manhã: {self.merenda_manha}, Almoço: {self.almoco}, Merenda Tarde: {self.merenda_tarde}"

from django.db import models

class Primeiro(models.Model):
    saida = models.TextField(max_length=255)

    class Meta:
        verbose_name_plural = "Primeiro"

    def __str__(self):
        return f"Primeiro: {self.saida}"

class Segundo(models.Model):
    saida = models.TextField(max_length=255)

    class Meta:
        verbose_name_plural = "Segundo"

    def __str__(self):
        return f"Segundo: {self.saida}"

class Terceiro(models.Model):
    saida = models.TextField(max_length=255)

    class Meta:
        verbose_name_plural = "Terceiro"

    def __str__(self):
        return f"Terceiro: {self.saida}"

class Quarto(models.Model):
    saida = models.TextField(max_length=255)

    class Meta:
        verbose_name_plural = "Quarto"

    def __str__(self):
        return f"Quarto: {self.saida}"

class Quinto(models.Model):
    saida = models.TextField(max_length=255)

    class Meta:
        verbose_name_plural = "Quinto"

    def __str__(self):
        return f"Quinto: {self.saida}"

class Sexto(models.Model):
    saida = models.TextField(max_length=255)

    class Meta:
        verbose_name_plural = "Sexto"

    def __str__(self):
        return f"Sexto: {self.saida}"

class Setimo(models.Model):
    saida = models.TextField(max_length=255)

    class Meta:
        verbose_name_plural = "Setimo"

    def __str__(self):
        return f"Setimo: {self.saida}"

class Oitavo(models.Model):
    saida = models.TextField(max_length=255)

    class Meta:
        verbose_name_plural = "Oitavo"

    def __str__(self):
        return f"Oitavo: {self.saida}"

class Nono(models.Model):
    saida = models.TextField(max_length=255)

    class Meta:
        verbose_name_plural = "Nono"

    def __str__(self):
        return f"Nono: {self.saida}"

class Decimo(models.Model):
    saida = models.TextField(max_length=255)

    class Meta:
        verbose_name_plural = "Decimo"

    def __str__(self):
        return f"Decimo: {self.saida}"

class DecimoPrimeiro(models.Model):
    saida = models.TextField(max_length=255)

    class Meta:
        verbose_name_plural = "DecimoPrimeiro"

    def __str__(self):
        return f"DecimoPrimeiro: {self.saida}"

class DecimoSegundo(models.Model):
    saida = models.TextField(max_length=255)

    class Meta:
        verbose_name_plural = "DecimoSegundo"

    def __str__(self):
        return f"DecimoSegundo: {self.saida}"