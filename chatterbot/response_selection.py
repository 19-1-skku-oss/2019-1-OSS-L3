"""
Response selection methods determines which response should be used in
the event that multiple responses are generated within a logic adapter.
"""
import logging


def get_most_frequent_response(input_statement, response_list, storage=None):
    """
    :param input_statement: A statement, that closely matches an input to the chat bot.
    :type input_statement: Statement

    :param response_list: A list of statement options to choose a response from.
    :type response_list: list

    :param storage: An instance of a storage adapter to allow the response selection
                    method to access other statements if needed.
    :type storage: StorageAdapter

    :return: The response statement with the greatest number of occurrences.
    :rtype: Statement
    """
    matching_response = None
    occurrence_count = -1

    logger = logging.getLogger(__name__)
    logger.info('Selecting response with greatest number of occurrences.')

    for statement in response_list:
        count = len(list(storage.filter(
            text=statement.text,
            in_response_to=input_statement.text)
        ))

        # Keep the more common statement
        if count >= occurrence_count:
            matching_response = statement
            occurrence_count = count

    # Choose the most commonly occuring matching response
    return matching_response


def get_first_response(input_statement, response_list, storage=None):
    """
    :param input_statement: A statement, that closely matches an input to the chat bot.
    :type input_statement: Statement

    :param response_list: A list of statement options to choose a response from.
    :type response_list: list

    :param storage: An instance of a storage adapter to allow the response selection
                    method to access other statements if needed.
    :type storage: StorageAdapter

    :return: Return the first statement in the response list.
    :rtype: Statement
    """
    logger = logging.getLogger(__name__)
    logger.info('Selecting first response from list of {} options.'.format(
        len(response_list)
    ))
    return response_list[0]


def get_random_response(input_statement, response_list, storage=None):
    """
    :param input_statement: A statement, that closely matches an input to the chat bot.
    :type input_statement: Statement

    :param response_list: A list of statement options to choose a response from.
    :type response_list: list

    :param storage: An instance of a storage adapter to allow the response selection
                    method to access other statements if needed.
    :type storage: StorageAdapter

    :return: Choose a random response from the selection.
    :rtype: Statement
    """
    from random import choice
    logger = logging.getLogger(__name__)
    logger.info('Selecting a response from list of {} options.'.format(
        len(response_list)
    ))
    return choice(response_list)


def get_wikipedia_response(input_statement, response_list, storage=None):

    first_data = get_first_response(input_statement, response_list, storage)
    match_data = get_most_frequent_response(input_statement, response_list, storage)

    if first_data.text == match_data.text:
        return match_data

    input_search_text = input_statement.search_text \
                                if input_statement.search_text else \
                                storage.tagger.get_text_index_string(input_statement.text)
    
    to_find = ''

    for props in input_search_text.split(' '):
        props_list = props.split(':')
        if props_list[0] == "VERB":
            to_find = props_list[1]
            break

    if not to_find:
        return first_data

    from requests import get

    lang_code = 'en'
    url = 'https://'+ lang_code + '.wikipedia.org/w/api.php'
    query = 'wehaveto' + to_find +'&redirects=true'

    response = get(url=(url + query)).json()
    
    pages = response['query']['pages']

    if '-1' in pages.keys():
        return first_data
    else:
        key = next(iter(pages.keys()))
        respond = pages[key]['extract']

        from .conversation import Statement

        output_search_text = storage.tagger.get_text_index_string(respond)

        rtn_data = Statement(
            text=respond,
            in_response_to=input_statement.text,
            search_text=output_search_text,
            search_in_respond_to=input_search_text
        )

        return rtn_data