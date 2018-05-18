# -*- coding: utf-8 -*-
"""
A viewlet rendering a dsgvo information banner
"""

from plone import api
from plone.app.layout.viewlets import common as base

from kitconcept.dsgvo import _
from kitconcept.dsgvo.util import dsgvo_translate


class DsgvoViewlet(base.ViewletBase):
    '''
    A viewlet to render a dsgvo information banner
    '''

    def info(self):
        msg = _(
            u'dsgvo_info_banner',
            default=(
                u'Ihre Anfrage wird verschlüsselt per https an unseren '
                u'Server geschickt. Sie erklären sich damit einverstanden, '
                u'dass wir die Angaben zur Beantwortung Ihrer Anfrage '
                u'verwenden dürfen. Hier finden Sie unsere '
                u'<a href="${portal_url}/privacy">Datenschutzerklärung und '
                u'Widerrufhinweise</a>.'),
                )
        return dsgvo_translate(msg, self.request)

    def portal_url(self):
        return api.portal.get().absolute_url()

    def render(self):
        cookie = self.request.cookies.get('hide-dsgvo-banner', False)
        if cookie:
            return ''
        return super(DsgvoViewlet, self).render()
