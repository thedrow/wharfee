from __future__ import unicode_literals

from optparse import OptionParser
from .option import CommandOption


COMMAND_OPTIONS = {
    'ps': [
        CommandOption(CommandOption.TYPE_BOOLEAN, '-a', '--all',
                      action='store_true',
                      dest='all',
                      help='Show all containers. '
                           'Only running containers are shown by default.'),
        CommandOption(CommandOption.TYPE_CONTAINER, None, '--before',
                      action='store',
                      dest='before',
                      help='Show only container created before Id or Name, '
                           'include non-running ones.'),
        CommandOption(CommandOption.TYPE_BOOLEAN, '-h', '--help',
                      action='store_true',
                      dest='help',
                      help='Display help for this command.'),
        CommandOption(CommandOption.TYPE_BOOLEAN, '-l', '--latest',
                      action='store_true',
                      dest='latest',
                      help='Show only the latest created container, '
                           'include non-running ones.'),
        CommandOption(CommandOption.TYPE_NUMERIC, '-n', None,
                      action='store',
                      dest='limit',
                      help='Show n last created containers, include '
                           'non-running ones.'),
        CommandOption(CommandOption.TYPE_NUMERIC, '--no-trunc', None,
                      action='store_false',
                      dest='trunc',
                      help='Don\'t truncate output.'),
        CommandOption(CommandOption.TYPE_BOOLEAN, '-q', '--quiet',
                      action='store_true',
                      dest='quiet',
                      help='Only display numeric IDs.'),
        CommandOption(CommandOption.TYPE_BOOLEAN, '-s', '--size',
                      action='store_true',
                      dest='latest',
                      help='Display total file sizes.'),
        CommandOption(CommandOption.TYPE_CONTAINER, None, '--since',
                      action='store',
                      dest='since',
                      help='Show only containers created since Id or Name, '
                           'include non-running ones.')
    ]
}


def parse_command_options(cmd, params):
    """
    Parse options for a given command.
    :param cmd: string: command name
    :param params: list: all tokens after command name
    :return: parser, args, opts
    """
    parser = OptionParser(prog=cmd, add_help_option=False)
    for opt in COMMAND_OPTIONS[cmd]:
        parser.add_option(opt.get_option())
    popts, pargs = parser.parse_args(params)
    popts = vars(popts)
    return parser, pargs, popts