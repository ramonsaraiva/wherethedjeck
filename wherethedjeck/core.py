import re
import subprocess
import django


class DjangoGrep(object):

    DJANGO_PATH = django.__path__[0]

    def __init__(self, query):
        self.query = query

    @property
    def pattern(self):
        return '^(def|class) {0}\(.*'.format(self.query)

    def execute_grep(self):
        command = '{0} "{1}" {2}'.format(
            'grep -Ero', self.pattern, self.DJANGO_PATH)
        return subprocess.check_output(command, shell=True)

    def normalize_module_from_output(self, output):
        pattern = '.*/(django\/.*)\.py.*'
        return re.match(pattern, output).group(1).replace('/', '.')

    def get_result(self):
        try:
            output = self.execute_grep().decode('utf-8')
            return self.normalize_module_from_output(output)
        except subprocess.CalledProcessError:
            return None
