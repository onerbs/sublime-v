import sublime, sublime_plugin

is_windows = sublime.platform() == 'windows'
path_separator = '\\' if is_windows else '/'


def get_bin_output(binary):
    return path_separator.join(['..', 'bin', binary])


def get_binary_name(file):
    if not file: return ''
    parts = file.split('.')
    base_name = parts[0] if len(parts) < 3 else '.'.join(parts[:-1])
    return '%s.exe' % base_name if is_windows else base_name


def is_compiling(shell_cmd, file):
    compile_commands = ['v %s' % file, 'v -prod %s' % file]
    return shell_cmd in compile_commands


class VlangBuilderCommand(sublime_plugin.WindowCommand):
    def run(self, **kwargs):
        shell_cmd = kwargs.get('shell_cmd')
        file_name = self.window.active_view().file_name()
        path_parts = file_name.split(path_separator)
        settings = sublime.load_settings('V.sublime-settings')
        magic_dirs = settings.get('magic_dirs') or []

        file = path_parts[-1]
        parent = path_parts[-2]

        if parent in magic_dirs and is_compiling(shell_cmd, file):
            shell_cmd += ' -o %s' % get_bin_output(get_binary_name(file))

        if not shell_cmd:
            action = 'test' if '_test.v' in file else 'run'
            shell_cmd = 'v %s %s' % (action, file)

        kwargs['shell_cmd'] = shell_cmd
        self.window.run_command('exec', kwargs)
