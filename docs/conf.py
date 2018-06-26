# -*- coding: utf-8 -*-

import os
import sys
import inspect
import shutil

__location__ = os.path.join(os.getcwd(), os.path.dirname(
    inspect.getfile(inspect.currentframe())))

sys.path.insert(0, os.path.join(__location__, '../src'))


try:  # for Sphinx >= 1.7
    from sphinx.ext import apidoc
except ImportError:
    from sphinx import apidoc

output_dir = os.path.join(__location__, "api")
module_dir = os.path.join(__location__, "../src/termux")
try:
    shutil.rmtree(output_dir)
except FileNotFoundError:
    pass

try:
    import sphinx
    from distutils.version import LooseVersion

    cmd_line_template = "sphinx-apidoc -f -o {outputdir} {moduledir}"
    cmd_line = cmd_line_template.format(outputdir=output_dir, moduledir=module_dir)

    args = cmd_line.split(" ")
    if LooseVersion(sphinx.__version__) >= LooseVersion('1.7'):
        args = args[1:]

    apidoc.main(args)
except Exception as e:
    print("Running `sphinx-apidoc` failed!\n{}".format(e))

extensions = ['sphinx.ext.autodoc', 'sphinx.ext.intersphinx', 'sphinx.ext.todo',
              'sphinx.ext.autosummary', 'sphinx.ext.viewcode', 'sphinx.ext.coverage',
              'sphinx.ext.doctest', 'sphinx.ext.ifconfig', 'sphinx.ext.mathjax',
              'sphinx.ext.napoleon']

templates_path = ['_templates']

source_suffix = '.rst'

# source_encoding = 'utf-8-sig'
source_encoding = 'utf-8'

master_doc = 'index'

project = u'termux'
copyright = u'2018, Ublim'

version = ''  # Is set by calling `setup.py docs`
release = ''  # Is set by calling `setup.py docs`

exclude_patterns = ['_build']

pygments_style = 'sphinx'

html_theme = 'sphinx_rtd_theme'

try:
    from termux import __version__ as version
except ImportError:
    pass
else:
    release = version

# html_logo = ""

# html_favicon = None

html_static_path = ['_static']

htmlhelp_basename = 'termux-doc'


latex_elements = {
}

latex_documents = [
  ('index', 'user_guide.tex', u'termux Documentation',
   u'Ublim', 'manual'),
]


python_version = '.'.join(map(str, sys.version_info[0:2]))
# intersphinx_mapping = {
#     'sphinx': ('http://www.sphinx-doc.org/en/stable', None),
#     'python': ('https://docs.python.org/' + python_version, None),
#     'matplotlib': ('https://matplotlib.org', None),
#     'numpy': ('https://docs.scipy.org/doc/numpy', None),
#     'sklearn': ('http://scikit-learn.org/stable', None),
#     'pandas': ('http://pandas.pydata.org/pandas-docs/stable', None),
#     'scipy': ('https://docs.scipy.org/doc/scipy/reference', None),
# }
