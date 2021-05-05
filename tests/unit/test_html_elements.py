import pytest

from zig.html_components import Div 


class TestHtmlElements:

    # black-box: test passing of attributes to HTMLElement works
    def test_div_creation(self):
        test_id = "123" 
        test_content = "test"
        test_section = []

        # HOW TO TEST ALL attributes efficiently?
        div = Div(test_content, id=test_id)

        assert div.content == test_content
        assert div.id == test_id

        assert div.section == test_section 


