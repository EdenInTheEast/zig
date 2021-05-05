import pytest


from zig.main_components import Graph 


class TestDomElements:

    #test passing of attributes to DomElement works
    def test_div_creation(self):
        test_id = "123" 
        test_figure = "figure"
        test_section = []

        # HOW TO TEST ALL attributes efficiently?
        graph = Graph(test_figure, id=test_id)

        assert graph.figure == test_figure
        assert graph.id == test_id
        # check for section
        assert graph.section == test_section

