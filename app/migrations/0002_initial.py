# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Industry'
        db.create_table(u'app_industry', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=60)),
        ))
        db.send_create_signal('app', ['Industry'])

        # Adding model 'Invite'
        db.create_table(u'app_invite', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('invite_to', self.gf('django.db.models.fields.related.ForeignKey')(related_name='recipient', to=orm['app.User'])),
            ('date', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal('app', ['Invite'])

        # Adding model 'Location'
        db.create_table(u'app_location', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=64)),
        ))
        db.send_create_signal('app', ['Location'])

        # Adding model 'User'
        db.create_table(u'app_user', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('linkedin', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('headline', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('picture_url', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('join_date', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('profile_url', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('industry', self.gf('django.db.models.fields.related.ForeignKey')(related_name='industry', to=orm['app.Industry'])),
            ('location', self.gf('django.db.models.fields.related.ForeignKey')(related_name='location', to=orm['app.Location'])),
            ('invites', self.gf('django.db.models.fields.related.ForeignKey')(related_name='invites', to=orm['app.Invite'])),
            ('latitude', self.gf('django.db.models.fields.CharField')(default=0, max_length=64)),
            ('longitude', self.gf('django.db.models.fields.CharField')(default=0, max_length=64)),
            ('age', self.gf('django.db.models.fields.PositiveSmallIntegerField')(max_length=3)),
            ('experience', self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=0, max_length=2)),
            ('availability', self.gf('django.db.models.fields.CharField')(default=1, max_length=64)),
        ))
        db.send_create_signal('app', ['User'])


    def backwards(self, orm):
        # Deleting model 'Industry'
        db.delete_table(u'app_industry')

        # Deleting model 'Invite'
        db.delete_table(u'app_invite')

        # Deleting model 'Location'
        db.delete_table(u'app_location')

        # Deleting model 'User'
        db.delete_table(u'app_user')


    models = {
        'app.industry': {
            'Meta': {'object_name': 'Industry'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '60'})
        },
        'app.invite': {
            'Meta': {'object_name': 'Invite'},
            'date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'invite_to': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'recipient'", 'to': "orm['app.User']"})
        },
        'app.location': {
            'Meta': {'object_name': 'Location'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '64'})
        },
        'app.user': {
            'Meta': {'object_name': 'User'},
            'age': ('django.db.models.fields.PositiveSmallIntegerField', [], {'max_length': '3'}),
            'availability': ('django.db.models.fields.CharField', [], {'default': '1', 'max_length': '64'}),
            'experience': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0', 'max_length': '2'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'headline': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'industry': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'industry'", 'to': "orm['app.Industry']"}),
            'invites': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'invites'", 'to': "orm['app.Invite']"}),
            'join_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'latitude': ('django.db.models.fields.CharField', [], {'default': '0', 'max_length': '64'}),
            'linkedin': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'location': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'location'", 'to': "orm['app.Location']"}),
            'longitude': ('django.db.models.fields.CharField', [], {'default': '0', 'max_length': '64'}),
            'picture_url': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'profile_url': ('django.db.models.fields.CharField', [], {'max_length': '128'})
        }
    }

    complete_apps = ['app']