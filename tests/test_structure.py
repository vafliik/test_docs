from tests.base_test import BaseTest


class TestStructure(BaseTest):

    def test_structure_matches_added_elements(self):

        self.message_panel.type('Add FlatButton')
        self.message_panel.wait_for_number_of_replies_to_be(1)

        self.message_panel.type('Add FlatButton called Sheldon')
        self.message_panel.wait_for_number_of_replies_to_be(2)

        self.message_panel.type('Add Divider')
        self.message_panel.wait_for_number_of_replies_to_be(3)

        self.message_panel.type('Add RadioButton')
        self.message_panel.wait_for_number_of_replies_to_be(4)

        self.message_panel.type('Add Checkbox')
        self.message_panel.wait_for_number_of_replies_to_be(5)

        self.message_panel.type('Add Checkbox called Penny')
        self.message_panel.wait_for_number_of_replies_to_be(6)

        self.view_panel.expand_card()

        expected_structure = [
            ('Button', 'BUTTON'),
            ('Button', 'SHELDON'),
            ('Divider', None),
            ('RadioButton', 'Radio 2'),
            ('Checkbox', 'Checkbox'),
            ('Checkbox', 'Penny'),
        ]

        real_structure = self.view_panel.card_content_structure()

        assert real_structure == expected_structure