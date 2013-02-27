##############################################################################
#
# Copyright (c) 2008 Zope Foundation and Contributors.
# All Rights Reserved.
#
# This software is subject to the provisions of the Zope Public License,
# Version 2.1 (ZPL).  A copy of the ZPL should accompany this distribution.
# THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL EXPRESS OR IMPLIED
# WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND FITNESS
# FOR A PARTICULAR PURPOSE.
#
##############################################################################
from z3c.authenticator import authentication
from z3c.authenticator import credential
from z3c.authenticator import group
from z3c.authenticator import interfaces
from z3c.authenticator import principal
from z3c.authenticator import testing
from z3c.authenticator import user
from z3c.testing import BaseTestIContainer
from z3c.testing import InterfaceBaseTest
from zope.component import testing import as placelesssetup
import doctest
import unittest


class AuthenticatorTest(BaseTestIContainer):

    def getTestInterface(self):
        return interfaces.IAuthenticator

    def getTestClass(self):
        return authentication.Authenticator


class UserContainerTest(InterfaceBaseTest):

    def getTestInterface(self):
        return interfaces.IUserContainer

    def getTestClass(self):
        return user.UserContainer


class UserTest(InterfaceBaseTest):

    def setUp(self):
        testing.setUpPasswordManager()

    def getTestInterface(self):
        return interfaces.IUser

    def getTestClass(self):
        return user.User

    def getTestPos(self):
        return (u'login', u'password', u'Title')


class AuthenticatedPrincipalTest(InterfaceBaseTest):

    def setUp(self):
        testing.setUpPasswordManager()

    def getTestInterface(self):
        return interfaces.IAuthenticatedPrincipal

    def getTestClass(self):
        return principal.AuthenticatedPrincipal

    def makeTestObject(self):
        usr =  user.User(u'login', u'password', u'Title')
        return principal.AuthenticatedPrincipal(usr)


class FoundPrincipalTest(InterfaceBaseTest):

    def setUp(self):
        testing.setUpPasswordManager()

    def getTestInterface(self):
        return interfaces.IFoundPrincipal

    def getTestClass(self):
        return principal.FoundPrincipal

    def makeTestObject(self):
        usr =  user.User(u'login', u'password', u'Title')
        return principal.FoundPrincipal(usr)


class GroupContainerTest(InterfaceBaseTest):

    def getTestInterface(self):
        return interfaces.IGroupContainer

    def getTestClass(self):
        return group.GroupContainer


class GroupTest(InterfaceBaseTest):

    def getTestInterface(self):
        return interfaces.IGroup

    def getTestClass(self):
        return group.Group


class SessionCredentialsTest(InterfaceBaseTest):

    def getTestInterface(self):
        return interfaces.ISessionCredentials

    def getTestClass(self):
        return credential.SessionCredentials

    def getTestPos(self):
        return (u'login', u'password')


class SessionCredentialsPluginTest(InterfaceBaseTest):

    def getTestInterface(self):
        return interfaces.ICredentialsPlugin

    def getTestClass(self):
        return credential.SessionCredentialsPlugin


class SessionCredentialsPluginFormTest(InterfaceBaseTest):

    def getTestInterface(self):
        return interfaces.IBrowserFormChallenger

    def getTestClass(self):
        return credential.SessionCredentialsPlugin

def placefulSetUp(test):
    zope.site.testing.siteSetUp(True)
    zope.traversing.testing.setUp()

def placefulTearDown(test):
    zope.site.testing.siteTearDown()

def test_suite():
    return unittest.TestSuite((
        doctest.DocFileSuite('README.txt',
            setUp=placefulSetUp, tearDown=placefulTearDown,
            optionflags=doctest.NORMALIZE_WHITESPACE|doctest.ELLIPSIS),
        doctest.DocFileSuite('group.txt',
            setUp=placefulSetUp, tearDown=placefulTearDown,
            optionflags=doctest.NORMALIZE_WHITESPACE|doctest.ELLIPSIS),
        doctest.DocTestSuite('z3c.authenticator.credential',
            setUp=placelesssetup.setUp, tearDown=placelesssetup.tearDown),
        doctest.DocTestSuite('z3c.authenticator.group',
            setUp=placelesssetup.setUp, tearDown=placelesssetup.tearDown),
        doctest.DocFileSuite('vocabulary.txt',
            setUp=placelesssetup.setUp, tearDown=placelesssetup.tearDown),
        unittest.makeSuite(AuthenticatorTest),
        unittest.makeSuite(UserContainerTest),
        unittest.makeSuite(UserTest),
        unittest.makeSuite(AuthenticatedPrincipalTest),
        unittest.makeSuite(FoundPrincipalTest),
        unittest.makeSuite(GroupContainerTest),
        unittest.makeSuite(GroupTest),
        unittest.makeSuite(SessionCredentialsTest),
        unittest.makeSuite(SessionCredentialsPluginTest),
        unittest.makeSuite(SessionCredentialsPluginFormTest),
        ))

if __name__ == '__main__':
    unittest.main(defaultTest='test_suite')
