import sublime, sublime_plugin

class VlangBuilderCommand(sublime_plugin.WindowCommand):
    def parse(self, **kwargs):
        if kwargs.get('shell_cmd'): return kwargs
        file = self.window.active_view().file_name().split('/')[-1]
        flag = 'test' if '_test.v' in file else 'run'
        kwargs['shell_cmd'] = 'v %s %s' % (flag, file)
        return kwargs

    def run(self, **kwargs):
        self.window.run_command('exec', self.parse(**kwargs))
