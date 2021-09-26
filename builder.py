import sublime, sublime_plugin

from os.path import join as join_path, isdir
from os import mkdir

IS_WINDOWS = sublime.platform() == 'windows'
PATH_SEPARATOR = '\\' if IS_WINDOWS else '/'
EXTENSION = '.exe' if IS_WINDOWS else ''


class VlangBuilderCommand(sublime_plugin.WindowCommand):
    def run(self, **kwargs):
        self.flags = kwargs.pop('flags') if 'flags' in kwargs else []
        self.project = kwargs.pop('project') if 'project' in kwargs else False
        action = kwargs.pop('action') if 'action' in kwargs else 'guess'

        kwargs['shell_cmd'] = self.get_shell_cmd(action)
        # kwargs['shell_cmd'] = 'echo ' + kwargs.get('shell_cmd')
        self.window.run_command('exec', kwargs)


    def get_shell_cmd(self, action: str) -> str:
        parts = self.window.active_view().file_name().split(PATH_SEPARATOR)
        file = '.' if self.project else parts[-1]
        root = parts[-2]

        is_test = '_test.v' in file

        if not action and is_test:
            return disabled('file')

        settings = sublime.load_settings('V.sublime-settings')

        if not action:
            bin_name = file.split('.')[0] + EXTENSION

            if root in settings.get('magic_dirs') or []:
                base = PATH_SEPARATOR.join(parts[:-2])
                bin_dir = join_path(base, 'bin')
                if not isdir(bin_dir): mkdir(bin_dir)
                bin_name = join_path(bin_dir, bin_name)

            self.push_flags(False, ['-o', bin_name])

        elif action == 'guess':
            action = 'test' if is_test else 'run'

        extension = get_extension(file)

        for preset in settings.get('magic_if') or []:
            exts = preset.get('extensions', [])
            dirs = preset.get('directories', [])
            plat = preset.get('platform', '')
            flags = preset.get('flags', [])
            done = False

            [match_ext, excl_ext] = includes(extension, exts)
            [match_dir, excl_dir] = includes(root, dirs)

            if match_ext:
                if excl_ext:
                    return disabled('platform')

                elif match_dir or match_dir is None:
                    done = self.push_flags(done, flags)

            elif match_dir:
                if excl_dir:
                    return disabled('platform')

                if match_ext is None:
                    self.push_flags(done, flags)

        compiler = settings.get('compiler') or 'v'
        return ' '.join([compiler, *self.flags, action, file])


    def push_flags(self, done: bool, flags: list) -> bool:
        if not done:
            skip = False
            for f in flags:
                if skip:
                    skip = False
                elif f in self.flags:
                    if f == '-o':
                        skip = True
                else:
                    self.flags.append(f)
        return done or len(flags) > 0


def get_extension(file: str) -> str:
    """
    :examples:
        get_extension('some.win.prod.v')  -> 'win.prod'  # TODO
        get_extension('some.win.v')       -> 'win'
        get_extension('some.v')           -> ''
    """
    parts = file.split('.')[1:-1]
    return '.'.join(parts)


def includes(base: str, ary: list):
    if not ary: return [None, False]
    excl = '!' + base in ary
    return [base in ary or excl, excl]


def disabled(kind: str) -> str:
    return f'echo Disabled for the current {kind}.'
