import usaddress

# Modified version of views with just the function being tested -XM
errorMessage = "Unable to parse this value due to repeated labels."

def parse(address):
    # TODO: Implement this method to return the parsed components of a
    # given address using usaddress: https://github.com/datamade/usaddress
    # COMPLETED: Returns a tuple containing 2 items: a list with the address
    # components and a string containing the address type -XM

    address_components = usaddress.parse(address)

    # Access the last item which will be the type of address - XM
    try:
        address_type = usaddress.tag(address)[-1]
    except usaddress.RepeatedLabelError as e:
        return e.original_string, errorMessage

    return address_components, address_type
