from models.LinkedList import LinkedList


def make_empty_list():
    return LinkedList()


def list_all_elements(countries_linked_list):
    countries_linked_list.traverse_list()
    return
    

def register_element(country, index, countries_linked_list):
    countries_linked_list.insert_at_index(int(index), country)
    return


def register_at_start(country, countries_linked_list):
    countries_linked_list.insert_at_start(country)
    return

def register_at_end(country, countries_linked_list):
    countries_linked_list.insert_at_end(country)


def register_after(country, after_country, countries_linked_list):
    countries_linked_list.insert_after_item(after_country, country)
    return


def register_before(country, before_country, countries_linked_list):
    countries_linked_list.insert_before_item(before_country, country)
    return


def verify_list_length(countries_linked_list):
    length = countries_linked_list.get_count()
    return length


def verify_country_in_list(country, countries_linked_list):
    return countries_linked_list.search_item(country)


def remove_element(country, countries_linked_list):
    countries_linked_list.delete_element_by_value(country)
    return


def remove_first_element(countries_linked_list):
    country = countries_linked_list.start_node.item
    countries_linked_list.delete_at_start()
    return country


def remove_last_element(countries_linked_list):
    country = countries_linked_list.get_last_node()
    countries_linked_list.delete_at_end()
    return country
