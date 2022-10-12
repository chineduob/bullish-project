""" The behave before_scenario method is called before all tests or any test is run to read the config ini file"""

import configparser


def before_scenario(context, scenario):
    """ Reads the config files before tests are run"""
    context.data_config = configparser.ConfigParser()

    context.data_config.read('utilities/{env}.ini'.format(env=context.config.userdata["env"]))