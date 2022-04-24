from controllers import controller as ctlr


def main():
    #  Session data
    countries_linked_list = ctlr.make_empty_list()

    while True:
        commands = input().split(" ")
        command = commands[0].upper()
        arguments = commands[1:]

        #  Registar País no Início da Lista (RPI):
        if command == "RPI":
            if len(arguments) == 2:
                register_element(*arguments, countries_linked_list)
                continue
            register_at_start(*arguments, countries_linked_list)

        # Registar País no Fim da Lista (RPF):
        elif command == "RPF":
            register_at_end(*arguments, countries_linked_list)

        #  Registar País Depois de outro Elemento já Registado (RPDE):
        elif command == "RPDE":
            register_after(*arguments, countries_linked_list)

        # Registar País Antes de outro elemento já registado (RPAE)
        elif command == "RPAE":
            register_before(*arguments, countries_linked_list)

        # Verificar Número de elementos da lista (VNE)
        elif command == "VNE":
            verify_list_length(*arguments, countries_linked_list)

        # Verificar se um País se encontra na lista (VP)
        elif command == "VP":
            verify_country_in_list(*arguments, countries_linked_list)

        # Eliminar o primeiro elemento da lista (EPE)
        elif command == "EPE":
            remove_first_element(*arguments, countries_linked_list)
        
        # Eliminar o último elemento da lista (EUE)
        elif command == "EUE":
            remove_last_element(*arguments, countries_linked_list)

        # Eliminar um determinado país da lista (EP)
        elif command == "EP":
            remove_element(*arguments, countries_linked_list)


def register_element(country, index, countries_linked_list):
    ctlr.register_element(country, index, countries_linked_list)
    ctlr.list_all_elements(countries_linked_list)
    return


def register_at_start(country, countries_linked_list):
    ctlr.register_at_start(country, countries_linked_list)
    ctlr.list_all_elements(countries_linked_list)
    return


def register_at_end(country, countries_linked_list):
    ctlr.register_at_end(country, countries_linked_list)
    ctlr.list_all_elements(countries_linked_list)
    return


def register_after(country, after_country, countries_linked_list):
    ctlr.register_after(country, after_country, countries_linked_list)
    ctlr.list_all_elements(countries_linked_list)
    return


def register_before(country, before_country, countries_linked_list):
    ctlr.register_before(country, before_country, countries_linked_list)
    ctlr.list_all_elements(countries_linked_list)
    return


def verify_list_length(countries_linked_list):
    length = ctlr.verify_list_length(countries_linked_list)
    print(f"O número de elementos são {length}.")
    return


def verify_country_in_list(country, countries_linked_list):
    found = ctlr.verify_country_in_list(country, countries_linked_list)
    if found:
        print(f"O país {country} encontra-se na lista.")
        return
    print(f"O país {country} não se encontra na lista.")
    return


def remove_element(country, countries_linked_list):
    ctlr.remove_element(country, countries_linked_list)
    print(f"O país {country} foi eliminado da lista.")
    return


def remove_first_element(countries_linked_list):
    country = ctlr.remove_first_element(countries_linked_list)
    print(f"O país {country} foi eliminado da lista.")
    return


def remove_last_element(countries_linked_list):
    country = ctlr.remove_last_element(countries_linked_list)
    print(f"O país {country} foi eliminado da lista.")
    return