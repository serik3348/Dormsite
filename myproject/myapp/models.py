from django.db import models


# Create your models here.


class Employee(models.Model):
    id = models.FloatField(primary_key=True)
    emp_name = models.CharField(max_length=50, blank=True, null=True)
    emp_email = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'employee'


class Abiandabla(models.Model):
    ab_id = models.FloatField(primary_key=True)
    first_name = models.CharField(max_length=50, blank=True, null=True)
    last_name = models.CharField(max_length=50, blank=True, null=True)
    phone_number = models.FloatField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'abiandabla'

    def __str__(self):
        return self.first_name + " " + self.last_name







class Faculties(models.Model):
    faculty_id = models.FloatField(primary_key=True)
    fac_title = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'faculties'

    def __str__(self):
        return self.fac_title


class StudentCities(models.Model):
    city_id = models.FloatField(primary_key=True)
    city_name = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'student_cities'

    def __str__(self):
        return self.city_name


class Dormstudents(models.Model):
    student_id = models.FloatField(primary_key=True)
    first_name = models.CharField(max_length=50, blank=True, null=True)
    last_name = models.CharField(max_length=50, blank=True, null=True)
    email = models.CharField(max_length=50, blank=True, null=True)
    gender = models.CharField(max_length=50, blank=True, null=True)
    student_phone = models.FloatField(blank=True, null=True)
    faculty = models.ForeignKey(Faculties, models.DO_NOTHING, blank=True, null=True)
    city = models.ForeignKey(StudentCities, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'dormstudents'

    def __str__(self):
        return self.first_name + " " + self.last_name


class Entryrecords(models.Model):
    entry_id = models.IntegerField(primary_key=True)
    student = models.ForeignKey(Dormstudents, models.DO_NOTHING, blank=True, null=True)
    day = models.DateField(max_length=50, blank=True, null=True)
    out_dorm = models.DateField(blank=True, null=True)
    in_dorm = models.DateField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'entryrecords'


class Dormrooms(models.Model):
    room_id = models.FloatField(primary_key=True)
    student = models.ForeignKey(Dormstudents, models.DO_NOTHING, blank=True, null=True)
    abiabla = models.ForeignKey(Abiandabla, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'dormrooms'

class Balance(models.Model):
    balance_id = models.FloatField(primary_key=True)
    student = models.ForeignKey(Dormstudents, models.DO_NOTHING, blank=True, null=True)
    year = models.FloatField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'balance'
