# -*- coding: utf-8 -*-

from zope.interface import implements
from plone.app.workflow.interfaces import ISharingPageRole
from plone.app.workflow.permissions import DelegateRoles 

class SuperRevisoreRole(object):
    implements(ISharingPageRole)
    
    title = u"Può super-revisionare"
    required_permission = DelegateRoles