# -*- coding: utf-8 -*-
from interlegis.portalmodelo.policy.testing import INTEGRATION_TESTING

import unittest


class SitePropertiesTestCase(unittest.TestCase):

    layer = INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.properties = self.portal['portal_properties'].site_properties
        self.languages = self.portal['portal_languages']
        self.types = self.portal['portal_types']
        self.maxDiff = None

    def test_title(self):
        self.assertEqual(self.portal.title, 'Portal Modelo')

    def test_description(self):
        self.assertEqual(
            self.portal.description, 'O portal das casas legislativas')

    def test_validate_email_is_enabled(self):
        self.assertTrue(self.portal.validate_email)

    def test_allowAnonymousViewAbout_is_enabled(self):
        self.assertTrue(self.properties.allowAnonymousViewAbout)

    def test_displayPublicationDateInByline_is_enabled(self):
        self.assertTrue(self.properties.displayPublicationDateInByline)

    def test_localTimeFormat(self):
        self.assertEqual(self.properties.localTimeFormat, '%d/%m/%Y')

    def test_localLongTimeFormat(self):
        self.assertEqual(self.properties.localLongTimeFormat, '%d/%m/%Y %H:%M')

    def test_enable_link_integrity_checks_is_enabled(self):
        self.assertTrue(self.properties.enable_link_integrity_checks)

    def test_livesearch_is_disabled(self):
        self.assertFalse(self.properties.enable_livesearch)

    def test_brasilian_portuguese_is_default_language(self):
        self.assertTrue(self.languages.use_combined_language_codes)
        self.assertEqual(self.properties.default_language, 'pt-br')

    def test_utf8_is_default_charset(self):
        self.assertEqual(self.properties.default_charset, 'utf-8')
        self.assertEqual(self.portal.email_charset, 'utf-8')

    def test_types_searched(self):
        all_types = set(self.types.listContentTypes())
        types_not_searched = set(self.properties.types_not_searched)
        types_searched = all_types - types_not_searched
        expected = [
            'Blog',
            'Claim',
            'Collection',
            'collective.cover.content',
            'collective.polls.poll',
            'CSVData',
            'Document',
            'EasyNewsletter',
            'ENLIssue',
            'ENLSubscriber',
            'ENLTemplate',
            'Event',
            'File',
            'Folder',
            'FormFolder',
            'Image',
            'Link',
            'News Item',
            'OmbudsOffice',
            'Parliamentarian',
            'Ploneboard',
            'PloneboardComment',
            'PloneboardForum',
            'sc.embedder',
            'Topic',
            'Window',
        ]
        self.assertItemsEqual(types_searched, expected)

    def test_icons_are_visible_to_authenticated_users_only(self):
        self.assertEqual(self.properties.icon_visibility, 'authenticated')


class NavtreePropertiesTestCase(unittest.TestCase):

    layer = INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.navtree = self.portal['portal_properties'].navtree_properties
        self.types = self.portal['portal_types']
        self.maxDiff = None

    def test_content_types_displayed_on_navigation(self):
        all_types = set(self.types.listContentTypes())
        metaTypesNotToList = set(self.navtree.metaTypesNotToList)
        content_types_displayed = all_types - metaTypesNotToList
        expected = [
            'Blog',
            'Collection',
            'EasyNewsletter',
            'Folder',
            'FormFolder',
            'OmbudsOffice',
            'Ploneboard',
            'PloneboardForum',
        ]
        self.assertItemsEqual(content_types_displayed, expected)
