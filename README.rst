.. This README is meant for consumption by humans and pypi. Pypi can render rst files so please do not use Sphinx features.
   If you want to learn more about writing documentation, please check out: http://docs.plone.org/about/documentation_styleguide.html
   This text does not appear on pypi or github. It is a comment.

==============================================================================
kitconcept.dsgvo
==============================================================================

.. image:: https://travis-ci.org/kitconcept/kitconcept.dsgvo.svg?branch=master
    :target: https://travis-ci.org/kitconcept/kitconcept.dsgvo

.. image:: https://img.shields.io/pypi/status/kitconcept.dsgvo.svg
    :target: https://pypi.python.org/pypi/kitconcept.dsgvo/
    :alt: Egg Status

.. image:: https://img.shields.io/pypi/v/kitconcept.dsgvo.svg
    :target: https://pypi.python.org/pypi/kitconcept.dsgvo
    :alt: Latest Version

.. image:: https://img.shields.io/pypi/l/kitconcept.dsgvo.svg
    :target: https://pypi.python.org/pypi/kitconcept.dsgvo
    :alt: License

|

.. image:: https://raw.githubusercontent.com/kitconcept/kitconcept.dsgvo/master/kitconcept.png
   :alt: kitconcept
   :target: https://kitconcept.com/

The General Data Protection Regulation ("GDPR" or "DSGVO" in German) is a regulation in EU law on data protection and privacy for all individuals within the European Union.

kitconcept.dsgvo implements the technical requirements that are necessary to be compliant with this regulation.

Please keep in mind that this add-on covers only the technical aspects of the regulation.
We highly recommend to consult a laywer to properly implement the regulation.

Features
--------

- [ ] Store username, date, time and IP address of the user on registration
- [ ] Opt-out for storing cookies
- [ ] Extensible registration form with user confirmation
- [ ] Export user data

Examples
--------

This add-on can be seen in action at the following sites:

- VHS-Ehrenamtsportal.de


Documentation
-------------

Full documentation for end users can be found in the "docs" folder, and is also available online at http://docs.plone.org/foo/bar


Translations
------------

This product has been translated into

- German


Installation
------------

Install kitconcept.dsgvo by adding it to your buildout::

    [buildout]

    ...

    eggs =
        kitconcept.dsgvo


and then running ``bin/buildout``


Contribute
----------

- Issue Tracker: https://github.com/kitconcept/kitconcept.dsgvo/issues
- Source Code: https://github.com/kitconcept/kitconcept.dsgvo
- Documentation: https://docs.plone.org/foo/bar


Support
-------

If you are having issues, please let us know.
We have a mailing list located at: project@example.com


License
-------

The project is licensed under the GPLv2.
