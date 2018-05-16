from Products.CMFPlone.utils import safe_unicode
from cgi import escape
from plone import api
from plone.app.z3cform.widget import SingleCheckBoxBoolWidget
from z3c.form.interfaces import IFieldWidget
from z3c.form.widget import FieldWidget
from zope.component import adapter
from zope.component import getMultiAdapter
from zope.i18n import translate
from zope.i18nmessageid import Message
from zope.interface import implementer
from zope.interface import implementer_only
from zope.schema.interfaces import IBool

from kitconcept.dsgvo.interfaces import IDsgvoSingleCheckBoxBoolWidget
from kitconcept.dsgvo.interfaces import IKitconceptDsgvoLayer


@implementer_only(IDsgvoSingleCheckBoxBoolWidget)
class DsgvoSingleCheckBoxBoolWidget(SingleCheckBoxBoolWidget):
    """
    Single Input type checkbox widget implementation that renders
    html in the label and help and interpolates the portal url and
    site name
    """

    klass = u'single-checkbox-bool-widget'

    def _translate(self, message):
        portal = api.portal.get()
        portal_state = getMultiAdapter((portal, self.request),
                                       name=u'plone_portal_state')
        site_title = escape(safe_unicode(portal_state.navigation_root_title()))
        portal_url = portal_state.portal_url()

        # interpolation does not work if we pass the mapping to
        # translate(). We have to construct a new message with
        # a mapping.
        # See https://github.com/zopefoundation/zope.i18n/issues/9
        translation = translate(
            Message(
                message,
                mapping={
                    'portal_url': portal_url,
                    'site_title': site_title,
                    }
                ),
            context=self.request)
        return translation

    @SingleCheckBoxBoolWidget.label.setter
    def label(self, value):
        self._label = self._translate(value)

    @SingleCheckBoxBoolWidget.description.setter
    def description(self, value):
        self._description = self._translate(value)


@adapter(IBool, IKitconceptDsgvoLayer)
@implementer(IFieldWidget)
def DsgvoSingleCheckBoxBoolFieldWidget(field, request):
    """IFieldWidget factory for CheckBoxWidget."""
    return FieldWidget(field, DsgvoSingleCheckBoxBoolWidget(request))
