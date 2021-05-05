from typing import Union, List, Callable, Any, Iterable
from collections import OrderedDict

from .interact_in import InteractIn
from .interact_out import InteractOut
from ..defaults import INTERACT_SUBDOMAIN


class BaseInteract:
    def __init__(self):
        self.id = None
        self.inputs_args = None
        self.inputs_kwargs = None
        self.output_dict = None
        self.api_point = None
        self.processor = None


class Interact:
    """Interact class stores, reports, and chains interaction functions

    :example:

    Interact(InteractIn(html_input_element),
             InteractOut(dom_output_element),
             update_ouput_div
            )


    Interact(InteractIn(inp.id, "value", key="key_word_name"),
             InteractOut(ouput.id, "content"),
             update_ouput_div
            )

    def update_output_div(key_word_name=None):
        pass



    DESIGN QUESTION:
        - ABLE TO CHAIN INTERACT OBJECT?
        - POSSIBLE TO DO CHANGE-SENSITIVE INPUTS?
                - update chains and objects before receiving from api


    """

    # keep track of all ids
    interact_ids = set()

    def __init__(
        self,
        input: Union[InteractIn, List[InteractIn]],
        output: Union[InteractOut, List[InteractOut]],
        func: Callable[..., Any],
    ):

        # Interaction ID
        # Make it easy for the client to refer and retrieve
        self.id = self.generate_id(interact_ids=self.interact_ids)

        # Store all input items. For rendering.
        self.inputs = []

        # COMPILED UNPON REQUEST
        # This is will compiled upon request from inputs_args_name
        # lazy loading: pass to function
        # :Example: func(*inputs_args)
        self.inputs_args = []

        # Store the func arg names in order
        # this method is preferred as intropsection allows easier debugging
        # arg name's convention : id_attribute-name
        # :Example: [id1_attr1, id2_attr2]
        self.inputs_args_names = []

        # dictionary of argname-value pair for fast update
        # :Example: {id1_attr1: value, id2_attr2: value}
        self.values_dict = {}

        # COMPILED UNPON REQUEST
        # dictionary of kwargs that will be compiled upon request
        # pass to function
        # func(**inputs_kwargs)
        self.inputs_kwargs = {}

        # dictionary of kwargs-arg-name pair
        # :Example: {kwarg_name: arg_name}
        self.inputs_kwargs_names = {}

        # INPUT VARIABLES
        # input will take either a list or an input object
        # from each input element, need to get id, attribute and value

        # :namespace: id_html-attribute
        self.__input_name_space = "{identity}_{attribute}"

        # convert it into a list to make code cleaner
        # don't need to separate method of handling single obj or list
        input = [input] if not isinstance(input, list) else input

        # TODO: use builder pattern for this
        if isinstance(input, list):
            for i in input:
                if isinstance(i, InteractIn):
                    # Interact_In should be in charge of making sure
                    # that id, attribute and value are ready to be used
                    if i.identity and i.attribute:
                        name_space = self.__input_name_space.format(
                            identity=i.identity, attribute=i.attribute
                        )

                        self.inputs.append(i)

                        if hasattr(i, "value"):
                            if not i.key:
                                # store in order
                                self.inputs_args_names.append(name_space)
                            else:
                                # store with keyword
                                self.inputs_kwargs_names[i.key] = name_space

                            self.values_dict[name_space] = i.value

                else:
                    raise TypeError(f"{i} {type(i)} need to be of type: InteractIn")

        # OUTPUT VARIABLES
        # Store all output elements. For rendering.
        self.outputs = []

        # Output information
        # :Example: ouput = {"id_123": {attribute:"figure", type:"Graph", data:{} }, ...}
        # output should also be in order
        # output should also support dictionary mapping to id

        self.output_dict = OrderedDict()
        self.output_format = ["attribute", "dom_type", "data"]

        # PROCESS OUTPUT
        output = [output] if not isinstance(output, list) else output

        if isinstance(output, list):
            for j in output:
                if isinstance(j, InteractOut):
                    # NOTE: Should we generate initial output value from the current input values?
                    # Option to trigger process later after function is collected
                    if j.identity and j.attribute:
                        self.output_dict[j.identity] = {
                            self.output_format[0]: j.attribute,
                            self.output_format[1]: j.dom_type,
                            self.output_format[2]: None,
                        }

                        self.outputs.append(j)
                else:
                    raise TypeError(f"{j} {type(j)} need to be of type: InteractOut")

        # CALLBACK
        # function chain should be in order
        # NOTE FUTURE: Able to use class and not just function?
        self.function_chain = []

        if callable(func):
            self.processor = func

            # should check if input matches output
            self.function_chain.append(func)

        # GENERATE API
        # api name format will be used a api url
        # it must be unique, and should be informative

        # NOTE: comply with url naming convention ?
        # TO LET USERS CHANGE THIS IN DEFAULT
        self.api_subdomain = INTERACT_SUBDOMAIN
        __api_name_format = "{id}"
        __required_names = {"id": self.id}

        self.api_point = self._generate_api_point(
            __api_name_format,
            self.api_subdomain,
            additional_parameters=__required_names,
        )

    """ ID METHODS
    """

    def generate_id(self, 
                    *, 
                    curr_tries: int = 1, 
                    max_tries: int = 10, 
                    interact_ids: set = None) -> int:
        # id generator for Interact Object
        # uses cls.interact_ids to keep track
        interact_ids = interact_ids if interact_ids else self.interact_ids

        if curr_tries > max_tries:
            raise Exception("Unable to generate id for Interact object.")
        if len(interact_ids) == 0:
            return 0

        new_id = list(interact_ids)[:-1] + curr_tries

        if new_id not in interact_ids:
            interact_ids.add(new_id)
            return new_id
        elif curr_tries <= max_tries:
            curr_tries += 1
            self.generate_id(curr_tries=curr_tries, interact_ids=interact_ids)



    """ API METHODS
    """

    def _generate_api_point(
        self, name_format: str, subdomain: str, additional_parameters: list = None
    ):
        api_point = (
            "/" + subdomain + "/" + name_format.format(id=additional_parameters["id"])
        )

        return api_point

    """ CHAIN METHODS 
    """

    def chain_calls(self, function_chain: list):
        # TODO: Given a list of functions, pass output to input
        # for x in function_chain:
        pass

    """ PROPERTY METHODS
    """

    @property
    def inputs_args(self):
        return self.__compile_args(self.inputs_args_names, self.values_dict)

    @inputs_args.setter
    def inputs_args(self, values: list):
        if isinstance(values, list):
            return values

    @property
    def inputs_kwargs(self):
        return self.__compile_kwargs(self.inputs_kwargs_names, self.values_dict)

    @inputs_kwargs.setter
    def inputs_kwargs(self, values: dict):
        if isinstance(values, dict):
            return values

    def __compile_args(self, inputs_args_names: list, values_dict: dict):
        # lazy loading of arguments
        # NOTE: how to keep track of changes? Possible?
        compiled_list = []

        for name in inputs_args_names:
            compiled_list.append(values_dict[name])

        return compiled_list

    def __compile_kwargs(self, inputs_kwargs_names: dict, values_dict: dict):
        # lazy loading of keyword arguments
        # NOTE: how to keep track of changes? Possible?

        compiled_dict = {}

        for key, name in inputs_kwargs_names.items():
            compiled_dict[key] = values_dict[name]

        return compiled_dict

    """ UPDATE METHODS
    """

    def _update_single_input(self, id, attribute, new_value, values_dict=None):
        i = {"identity": id, "attribute": attribute}

        search_key = self.__input_name_space.format(
            identity=i["identity"], attribute=i["attribute"]
        )

        values_dict = values_dict if values_dict else self.values_dict

        if self.values_dict.get(search_key, None):
            self.values_dict[search_key] = new_value

            return True
        else:
            raise KeyError(
                f"{search_key} cannot be found in Interact input values vault"
            )

    def update(self, request_data: dict):
        # Template method
        # propose update prodcess
        # json_data will be a dictionary or list of htmlelement information

        # NOTE: request data should be in dict form.
        # Container should be in charge of compiling it into a generic format
        # 1. get json put request data

        # NOTE FORMAT should be in dict form
        # :Example: {index: {"id":id, "attribute":attr, "value":val}}

        for o in request_data.values():
            self._update_single_input(o["id"], o["attribute"], o["value"])

        return True

    """ OUTPUT METHODS
    """

    def process(self):
        # NOTE: main function that the client will be using

        arg_list = self.inputs_args
        kwargs_dict = self.inputs_kwargs
        processor = self.processor
        outputs_dict = self.output_dict

        outputs_dict = self._process(arg_list, kwargs_dict, outputs_dict, processor)

        return outputs_dict

    def _process_inputs(self, inputs_args: Iterable, inputs_kwargs: dict, processor):
        # NOTE: this is the main processing method
        # compile

        if len(inputs_args) or len(inputs_kwargs):
            result = processor(*inputs_args, **inputs_kwargs)

            # TODO: how do I handle multiple outputs of diff. type?
            # it should be able to accept list or tuple
            # what about dictonary?

            if isinstance(result, (list, tuple, set, dict)):
                return result
            else:
                return [result]

    def _update_outputs(self, results, outputs: List[dict]) -> List[dict]:
        # UPDATE
        # update each output in the order of specification
        for id, idx in zip(outputs, range(len(outputs))):
            outputs[id]["data"] = results[idx]

        return outputs

    def _process(
        self,
        arg_list: list,
        kwargs_dict: dict,
        outputs: List[dict],
        processor: Callable,
    ):
        # NOTE: main process controller
        # process inputs with function and updates output datas

        # PROCESSS
        if self.processor:
            results = self._process_inputs(arg_list, kwargs_dict, processor)

            # TODO: where should i check that function
            # return the same no. of outputs?
            if results and len(results) == len(outputs):
                # UPDATE
                return self._update_outputs(results, outputs)
            else:
                raise Exception(
                    f"No. of outputs {len(outputs)} doesn't match the return of {len(results)} results"
                )
        else:
            raise Exception("Requires a processing function.")

    """ HTTP METHODS
    """

    def http_response(self, request_method, request_data):
        if request_method == "POST":
            response = self._post_response(request_data)
        elif request_method == "PUT":
            response = self._put_response(request_data)
        elif request_method == "GET":
            response = self._get_response(request_data)
        else:
            raise Exception("Invalid HTTP request")

        return response

    def _post_response(self, request_data):
        # should be the same as put
        self._put_response(request_data)

    def _put_response(self, request_data):
        # 1. Update values
        if self.update(request_data):
            # if update successfully, process and return output vales
            response_dict = self.process()
            return response_dict
        else:
            # TODO: flask need to implement error handler
            raise Exception("Unable to update data")

    def _get_response(self, request_data):
        response_dict = self.process()
        if response_dict:
            return response_dict

        raise Exception("Unable to get output results")

    """ JSON METHODS
    """

    def render(self):
        # NOTE: non-functional; uses global variables
        # this is only used for setting up the interaction on client-side
        inputs_dict = {}
        outputs_dict = {}

        for i, element in enumerate(self.inputs):
            # NOTE: right now we are getting it from InteractIn objects
            # shouldn't we get it from interact storage instead?
            inputs_dict[i] = {
                "id": element.identity,
                "dom_type": element.dom_type,
                "attribute": element.attribute,
            }

        for i, element in enumerate(self.outputs):
            outputs_dict[i] = {
                "id": element.identity,
                "dom_type": element.dom_type,
                "attribute": element.attribute,
            }

        render_format = {
            "input": inputs_dict,
            "output": outputs_dict,
            "api_point": self.api_point,
        }

        return render_format
