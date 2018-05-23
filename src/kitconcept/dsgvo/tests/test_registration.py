from Products.CMFPlone.interfaces import ISecuritySchema
from Products.SiteErrorLog.SiteErrorLog import SiteErrorLog

from plone import api
from plone.registry.interfaces import IRegistry
from zope.component import getMultiAdapter
from zope.component import getUtility
from plone.testing.z2 import Browser

import lxml
import unittest
import transaction

from kitconcept.dsgvo.testing import KITCONCEPT_DSGVO_FUNCTIONAL_TESTING


def raising(self, info):
    import traceback
    traceback.print_tb(info[2])
    print info[1]


ACCEPT_WIDGET_XPATH = '//input[@name="form.widgets.dsgvo_accept:list"]'


class TestRegistration(unittest.TestCase):
    """Test that kitconcept.dsgvo is properly installed."""

    layer = KITCONCEPT_DSGVO_FUNCTIONAL_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.portal_url = self.portal.absolute_url()
        self.app = self.layer['app']
        self.request = self.layer['request']

        # prepare browser and error handling
        self.browser = Browser(self.app)
        self.browser.handleErrors = False  # Don't get HTTP 500 pages
        self.browser.mech_browser.set_handle_robots(False)  # Ignore robots.txt
        self.portal.error_log._ignored_exceptions = ()
        self.old_raising = SiteErrorLog.raising
        SiteErrorLog.raising = raising

        # enable self registration
        registry = getUtility(IRegistry)
        security_settings = registry.forInterface(
            ISecuritySchema, prefix="plone")
        security_settings.enable_self_reg = True
        security_settings.enable_user_pwd_choice = True
        transaction.commit()

        self.registration_url = '%s/@@register' % self.portal_url

    def _call_view(self, view_name):
        view = getMultiAdapter((self.portal, self.request), name=view_name)
        html = view()
        tree = lxml.html.fromstring(html)
        return html, tree
        
    def tearDown(self):
        SiteErrorLog.raising = self.old_raising

    def test_registration_form(self):
        self.browser.open(self.registration_url)
        import pdb; pdb.set_trace()

    # def test_submit_without_accept(self):
    #     self.request.form.update({
    #         'form.widgets.dsgvo_accept-0': 'selected',
    #         })
    #     html, tree = self._call_view('register')
    #     import pdb; pdb.set_trace()

