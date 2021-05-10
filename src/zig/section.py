from typing import Union, Tuple, List, TYPE_CHECKING
from abc import ABC, abstractmethod

from .defaults import DEFAULT_SECTION_CONFIG


class Section:
    """ Interface for section object
    includes methods that are specific to section
    like __iter__ 

    """


    def __init__(self):
        # need to implement your own section
        self.section = None

        # type of object that can be added to section
        self.supported_type = None

    def add(self):
        raise NotImplementedError

    def __iter__(self):
        raise NotImplementedError




class BaseSectionAttacher:
    # interface with methods that will be added 
    # directly to main object.
    # 
    def __init__(self, section_type: str = None):
        self.section = None
        self.section_control = None

    def section_controller_factory(self):
        raise NotImplementedError

    def section_factory(self):
        raise NotImplementedError

    def add(self):
        raise NotImplementedError


class SectionAttacher(Section, BaseSectionAttacher):
    """
    Abstract Factory Pattern

    SectionAttacher is both of type Section and SectionAttacher class.

    Allows child to attach or change to different Section types dynamically
    without knowing the name of New Section type.
    By default, all related classes will use the same Section type

    Classes using Section and SectionAttacher: Zig, DomElement, HtmlElement


    :param section_type: allows different object to choose
                        different implementation of Section.
    """

    def __init__(self, *args, section_type: str = DEFAULT_SECTION_CONFIG, **kwargs):

        if not hasattr(self, "section_control"):
            self.section = self.section_controller_factory(section_type)

        """
        if not hasattr(self, "section") and self.section_control:
            # creates section object
            self.section = self.section_factory(self.section_control)
            print(self.section)
        """

    def section_controller_factory(self, section_type: str):
        if SECTION_OPTIONS.get(section_type):
            return SECTION_OPTIONS[section_type]()

        raise Exception(f"Section Type {section_type} does not exist!")

    def section_factory(self, controller: Section):
        if controller:
            if hasattr(controller, "section"):
                return controller.section
            else:
                raise Exception(f"Controller doesn't have section")
        raise Exception(f"Requires Controller. {controller} is invalid")

    # Note: SectionAttacher needs to implement same method as Section
    # It works as a Factory and also an interface for the product

    def add(self, component: Section) -> None:
        if hasattr(self, "section"):
            self.section.add(component)
        else:
            raise Exception(f"Requires Section object")
        # so that it can be chained
        return self


    def insert(self):
        pass

    def show(self):
        if hasattr(self, "section"):
            self.section.show(self.section, *args, **kwargs)
        else:
            raise Exception(f"Requires Section object") 


    def get(self, *args, **kwargs):
        if hasattr(self, "section"):
            self.section.get(self.section, *args, **kwargs)
        else:
            raise Exception(f"Requires Section object")







# only for typing
from .element import Element


class CoreSection(Section):
    """ Backbone of all html element component that allows nesting.
    Main purpose of this class is to implement quick lookup and insert of component

    Section is used to contain other Section objects and non-section objects


    zig.section itself uses Section

    components are stored in dictionary with name/index as key
    components'name are stored in list to depict the order
    """

    def __init__(self):

        self.supported_type = (Element)

        # dictionary for fast retrievel
        self.__section_dict = {}

        # list to keep order; implementation of section and section_order need not be the same
        self.__section = self.__section_order = []
        self.order = 0

    @property
    def section(self):
        return self.__section

    @section.setter
    def section(self, var):
        # Section needs to maintain both hashmap and ordered list. Cannot be set manually.
        raise TypeError("Not able to set section manaully. Use section.add instead.")

    def add(self, component: Union[Element, List[Element]]):
        """
        add other components
        able to add one, or a list of components

        automate adding to dict, and list
        add(Div())
        add([Div(), Graph(), Div()])
        """
        if isinstance(component, list):
            for comp in component:
                self.__section_order, self.__section_dict = self.__add(
                    comp, self.__section_order, self.__section_dict
                )
        else:
            self.__add(component)


    def __add(
        self, component: Element, section_list: list, section_dict: dict
    ) -> Tuple[list, dict]:
        try:
            # try recording in hashtable first
            section_dict = self.__add_dict(component, section_dict)
        except Exception:
            raise
        else:
            try:
                # then try adding to order
                section_list = self.__add_to_order(component, section_list)
            except Exception:
                raise e

        ## HOW TO MAKE SURE BOTH ARE UPDATED TOGETHER?
        return section_list, section_dict

    def __add_dict(self, component: Element, section_dict: dict) -> dict:
        if isinstance(component, self.supported_type):
            if section_dict.get(component.id):
                # id already exist
                raise Exception(f"id {component.id} is already in use")
            else:
                # if given id, use it as key
                if getattr(component, "id", None):
                    section_dict[component.id] = component
                # else generate.
                else:
                    # use order number as key
                    section_dict[self.order] = component
                    ## WHAT IF WE GENERATE SOMETHING THAT CLASHES WITH AN EXISTING ID?

                self.order += 1

                return section_dict
        else:
            raise TypeError(
                f"Component {type(component)} need to be of type {self.supported_type}"
            )

    def __add_to_order(self, component: Element, section_list: list) -> list:
        if isinstance(component, self.supported_type):
            section_list.append(component)
            return section_list
        else:
            raise TypeError(
                f"Component {type(component)} need to be of type {self.supported_type}"
            )

    def __iter__(self):
        for x in self.section:
            yield x

    def insert(self, index):
        # insert at index
        pass

    def show(self):
        # show all components in order
        return self.__section.dict

    def get(self, component_id):
        # return the specific component in the section
        return __section_dict.get(component_id, None)


# this needs to be cleaner
SECTION_OPTIONS = {"CoreSection": CoreSection}
