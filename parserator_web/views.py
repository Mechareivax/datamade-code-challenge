import usaddress
from django.views.generic import TemplateView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from rest_framework.exceptions import ParseError


class Home(TemplateView):
    template_name = 'parserator_web/index.html'


class AddressParse(APIView):
    renderer_classes = [JSONRenderer]

    errorMessage = "Unable to parse this value due to repeated labels."

    def get(self, request):
        # TODO: Flesh out this method to parse an address string using the
        # parse() method and return the parsed components to the frontend.

        input_dict = request.GET  # the querydict
        input_string = input_dict.get("address")  # the string the user entered
        address_components = self.parse(input_string)[0]
        address_type = self.parse(input_string)[1]

        if address_type == self.errorMessage:
            return Response({
                "error": self.errorMessage,
            })
        else:
            return Response({
                "input_string": input_string,
                "address_components": address_components,
                "address_type": address_type,
            })

    def parse(self, address):
        # TODO: Implement this method to return the parsed components of a
        # given address using usaddress: https://github.com/datamade/usaddress
        # COMPLETED: Returns a tuple containing 2 items: a list with the address
        # components and a string containing the address type -XM

        address_components = usaddress.parse(address)

        # Access the last item which will be the type of address - XM
        try:
            address_type = usaddress.tag(address)[-1]
        except usaddress.RepeatedLabelError as e:
            return e.original_string, self.errorMessage

        return address_components, address_type
