from zope.i18nmessageid import MessageFactory
from Products.CMFCore.permissions import setDefaultRoles

PloneMessageFactory = MessageFactory('plone')

setDefaultRoles('firebaseplonedemo.portlet: Add FireBasePloneDemo portlet',
                ('Manager', 'Site Administrator', 'Owner', ))
