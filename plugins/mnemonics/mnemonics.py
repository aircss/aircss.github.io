import os
import pathlib

from pelican import signals
from pelican.readers import RstReader


from docutils import nodes
from docutils.parsers.rst import directives
from docutils.parsers.rst import Directive
from docutils.statemachine import StringList


TEMPLATE = """
    <div class="cf pb4">
        <div class="db w-third fl tc b">Bases</div>
        <div class="db w-third fl tc b">Modifiers</div>
        <div class="db w-third fl tc b">Optional extensions</div>
    </div>
    <div class="flex justify-around items-center code f7">
        <div class="db w-third tc">
            {bases}
        </div>

        <div class="db w-third tc">
            {modifiers}
        </div>

        <div class="db w-third tc">
            {options}
        </div>
    </div>
"""


class Mnemonics(Directive):

    required_arguments = 1
    has_content = False

    def run(self):
        target = pathlib.Path(os.getcwd())

        content_node = nodes.Element()
        content_node.tagname = 'div'
        content_node['class'] = 'mnemonics'

        kind = None
        tokens = {
            'bases': [],
            'modifiers': [],
            'options': [],
        }

        with open(target / self.arguments[0]) as f:
            for line in f:

                if line.strip() ==  'Bases:':
                    kind = 'bases'
                    continue

                if line.strip() ==  'Modifiers:':
                    kind = 'modifiers'
                    continue

                if line.strip() == 'Optional extensions:':
                    kind = 'options'
                    continue

                if not kind:
                    continue

                if line.startswith('*/'):
                    break

                if line and f'  {line.lstrip()}'.startswith(line):
                    break

                tokens[kind].append(line.strip())

        bases = []
        if tokens['bases']:
            for token in tokens['bases']:
                bases.append(f'<span class="red">{token}</span><br>')
        else:
            bases.append('<span class="i noir-50">none</span>')

        modifiers = []
        if tokens['modifiers']:
            for token in tokens['modifiers']:
                modifiers.append(f'<span class="red">{token}</span><br>')
        else:
            modifiers.append('<span class="i noir-50">none</span>')

        options = []
        if tokens['options']:
            for token in tokens['options']:
                options.append(f'<span class="red">{token}</span><br>')
        else:
            options.append('<span class="i noir-50">none</span>')

        content_node += nodes.Text(TEMPLATE.format(
            bases='\n'.join(bases),
            modifiers='\n'.join(modifiers),
            options='\n'.join(options),
        ))

        return [nodes.raw('', content_node, format='html')]



def register():
    """Register the plugin to Pelican."""
    directives.register_directive('mnemonics', Mnemonics)
