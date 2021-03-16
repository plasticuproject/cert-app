# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django import forms


class Certs(models.Model):
    id = models.TextField(primary_key=True, blank=True)
    date_added = models.TextField(blank=True, null=True)
    applied = models.IntegerField(blank=True, null=True)
    date_applied = models.TextField(blank=True, null=True, max_length=200)
    banned = models.IntegerField(blank=True, null=True)
    banned_date = models.TextField(blank=True, null=True, max_length=200)
    required_activation = models.IntegerField(blank=True, null=True)
    currently_used = models.IntegerField(blank=True, null=True)

    class Meta:
        # managed = False
        db_table = 'certs'
