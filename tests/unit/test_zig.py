import pytest

from zig import Zig, CoreSection


class TestZig:

    # black-box: test section attacher is working
    def test_zig_section(self):
        app = Zig()
        test_section = []
        
        
        assert app.section == test_section
        assert isinstance(app.section_control, CoreSection)
