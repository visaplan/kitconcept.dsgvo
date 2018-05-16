from plone.app.users.browser.account import AccountPanelSchemaAdapter
from plone.app.users.browser.register import RegistrationForm, AddUserForm
from plone.app.users.browser.userdatapanel import UserDataPanel
from plone.supermodel import model
from plone.z3cform.fieldsets import extensible

from z3c.form import field

from zope import schema
from zope.component import adapts
from zope.interface import Interface

from kitconcept.dsgvo import _
from kitconcept.dsgvo.interfaces import IKitconceptDsgvoLayer
from kitconcept.dsgvo.widget import DsgvoSingleCheckBoxBoolFieldWidget


def validateAccept(value):
    return value is True


class IDsgvoUserDataSchema(model.Schema):

    dsgvo_accept = schema.Bool(
        title=_(u'label_dsgvo_accept',
                default=(
                    u'I Accept the <a href="${portal_url}/privacy">'
                    u'${site_title} privacy policy</a>.')),
        description=_(
            u'help_dsgvo_accept',
            default=u''),
        required=True,
        constraint=validateAccept,
    )


class DsgvoUserDataSchemaAdapter(AccountPanelSchemaAdapter):
    schema = IDsgvoUserDataSchema


class UserDataPanelExtender(extensible.FormExtender):
    adapts(Interface, IKitconceptDsgvoLayer, UserDataPanel)

    def update(self):
        fields = field.Fields(IDsgvoUserDataSchema)
        # Users have already accepted.
        fields = fields.omit('dsgvo_accept')
        self.add(fields)


class RegistrationPanelExtender(extensible.FormExtender):
    adapts(Interface, IKitconceptDsgvoLayer, RegistrationForm)

    def update(self):
        fields = field.Fields(IDsgvoUserDataSchema)
        fields['dsgvo_accept'].widgetFactory = \
            DsgvoSingleCheckBoxBoolFieldWidget
        self.add(fields)


class AddUserFormExtender(extensible.FormExtender):
    adapts(Interface, IKitconceptDsgvoLayer, AddUserForm)

    def update(self):
        fields = field.Fields(IDsgvoUserDataSchema)
        # management form doesn't need this field
        fields = fields.omit('dsgvo_accept')
        self.add(fields)
