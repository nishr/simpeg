# -*- coding: utf-8 -*-
#
# SimPEG documentation build configuration file, created by
# sphinx-quickstart on Fri Aug 30 18:42:44 2013.
#
# This file is execfile()d with the current directory set to its containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

import sys
import os
from sphinx_gallery.sorting import FileNameSortKey

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#sys.path.insert(0, os.path.abspath('.'))

sys.path.append(os.path.abspath('..{}'.format(os.path.sep)))
sys.path.append(os.path.abspath('.{}_ext'.format(os.path.sep)))

# -- General configuration -----------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be extensions
# coming with Sphinx (named 'sphinx.ext.*') or your custom ones.
extensions = [
    'sphinx.ext.todo',
    'sphinx.ext.mathjax',
    'sphinx.ext.viewcode',
    'sphinx.ext.autodoc',
    'sphinx.ext.intersphinx',
    # 'sphinxcontrib.napoleon',
    'matplotlib.sphinxext.plot_directive',
    'sphinx_gallery.gen_gallery',
    'edit_on_github',
]

# numpydoc_show_class_members = False

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix of source filenames.
source_suffix = '.rst'

# The encoding of source files.
#source_encoding = 'utf-8-sig'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = u'SimPEG'
copyright = u'2013 - 2017, SimPEG Team, http://simpeg.xyz'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = '0.14.0b2'
# The full version, including alpha/beta/rc tags.
release = '0.14.0b2'

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#language = None

# There are two options for replacing |today|: either, you set today to some
# non-false value, then it is used:
#today = ''
# Else, today_fmt is used as the format for a strftime call.
#today_fmt = '%B %d, %Y'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
exclude_patterns = ['_build']

# linkcheck_ignore = [
#     'https://cnls.lanl.gov/~shashkov/papers/maxjcp.pdf',
#     'https://wiki.python.org/moin/NumericAndScientific',
#     'https://wiki.python.org/moin/PythonEditors',
#     'https://docs.scipy.org/doc/numpy/reference/generated/numpy.ndarray.html#numpy.ndarray',
#     'https://dx.doi.org/10.1016/j.cageo.2015.09.015',
#     'https://www-users.cs.umn.edu/~saad/PDF/umsi-2005-082.pdf',
#     'https://www.ngdc.noaa.gov/',
#     'https://discretize.simpeg.xyz/en/master/objects.inv'
# ]

linkcheck_retries = 3
linkcheck_timeout = 500

# The reST default role (used for this markup: `text`) to use for all documents.
#default_role = None

# If true, '()' will be appended to :func: etc. cross-reference text.
#add_function_parentheses = True

# If true, the current module name will be prepended to all description
# unit titles (such as .. function::).
#add_module_names = True

# If true, sectionauthor and moduleauthor directives will be shown in the
# output. They are ignored by default.
#show_authors = False

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# A list of ignored prefixes for module index sorting.
#modindex_common_prefix = []

# -- Edit on Github Extension ---------------------------------------------

edit_on_github_project = 'simpeg/simpeg'
edit_on_github_branch = 'master/docs'
check_meta = False

# -- Options for HTML output ---------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
try:
    import sphinx_rtd_theme
    html_theme = 'sphinx_rtd_theme'
    html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]
    pass
except Exception:
    html_theme = 'default'

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#html_theme_options = {}

# Add any paths that contain custom themes here, relative to this directory.
#html_theme_path = []

# The name for this set of Sphinx documents.  If None, it defaults to
# "<project> v<release> documentation".
#html_title = None

# A shorter title for the navigation bar.  Default is the same as html_title.
#html_short_title = None

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
#html_logo = None

# The name of an image file (within the static path) to use as favicon of the
# docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
html_favicon = os.path.sep.join(['.','images','logo-block.ico'])

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = []

# If not '', a 'Last updated on:' timestamp is inserted at every page bottom,
# using the given strftime format.
#html_last_updated_fmt = '%b %d, %Y'

# If true, SmartyPants will be used to convert quotes and dashes to
# typographically correct entities.
#html_use_smartypants = True

# Custom sidebar templates, maps document names to template names.
#html_sidebars = {}

# Additional templates that should be rendered to pages, maps page names to
# template names.
#html_additional_pages = {}

# If false, no module index is generated.
#html_domain_indices = True

# If false, no index is generated.
#html_use_index = True

# If true, the index is split into individual pages for each letter.
#html_split_index = False

# If true, links to the reST sources are added to the pages.
#html_show_sourcelink = True

# If true, "Created using Sphinx" is shown in the HTML footer. Default is True.
html_show_sphinx = False

# If true, "(C) Copyright ..." is shown in the HTML footer. Default is True.
html_show_copyright = False

# If true, an OpenSearch description file will be output, and all pages will
# contain a <link> tag referring to it.  The value of this option must be the
# base URL from which the finished HTML is served.
#html_use_opensearch = ''

# This is the file name suffix for HTML files (e.g. ".xhtml").
#html_file_suffix = None

# Output file base name for HTML help builder.
htmlhelp_basename = 'SimPEGdoc'


# -- Options for LaTeX output --------------------------------------------------

latex_elements = {
# The paper size ('letterpaper' or 'a4paper').
#'papersize': 'letterpaper',

# The font size ('10pt', '11pt' or '12pt').
#'pointsize': '10pt',

# Additional stuff for the LaTeX preamble.
#'preamble': '',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title, author, documentclass [howto/manual]).
latex_documents = [
  ('index', 'SimPEG.tex', u'SimPEG Documentation',
   u'SimPEG Team', 'manual'),
]

# The name of an image file (relative to this directory) to place at the top of
# the title page.
#latex_logo = None

# For "manual" documents, if this is true, then toplevel headings are parts,
# not chapters.
#latex_use_parts = False

# If true, show page references after internal links.
#latex_show_pagerefs = False

# If true, show URL addresses after external links.
#latex_show_urls = False

# Documents to append as an appendix to all manuals.
#latex_appendices = []

# If false, no module index is generated.
#latex_domain_indices = True


# -- Options for manual page output --------------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    ('index', 'simpeg', u'SimPEG Documentation', [u'SimPEG Team'], 1)
]

# If true, show URL addresses after external links.
#man_show_urls = False

# Intersphinx
intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'numpy': ('https://numpy.org/doc/stable/', None),
    'scipy': ('https://docs.scipy.org/doc/scipy/reference/', None),
    'matplotlib': ('http://matplotlib.org/', None),
    'properties': ('https://propertiespy.readthedocs.io/en/latest/', None),
    'discretize': ('http://discretize.simpeg.xyz/en/master/', None)
}


# -- Options for Texinfo output ------------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
  ('index', 'SimPEG', u'SimPEG Documentation',
   u'SimPEG Team', 'SimPEG', 'Simulation and parameter estimation in geophyiscs.',
   'Miscellaneous'),
]


# Sphinx Gallery
sphinx_gallery_conf = {
    # path to your examples scripts
    'examples_dirs' : ['../examples',
                       '../tutorials/models_mapping',
                       '../tutorials/forward_simulations',
                       '../tutorials/basic_inversions',
                       ],
    'gallery_dirs'  : ['content/examples',
                       'content/tutorials/models_mapping',
                       'content/tutorials/forward_simulations',
                       'content/tutorials/basic_inversions',
                       ],
    'within_subsection_order': FileNameSortKey,
    'backreferences_dir' : None
}


# Documents to append as an appendix to all manuals.
#texinfo_appendices = []

# If false, no module index is generated.
#texinfo_domain_indices = True

# How to display URL addresses: 'footnote', 'no', or 'inline'.
#texinfo_show_urls = 'footnote'

autodoc_member_order = 'bysource'


def supress_nonlocal_image_warn():
    import sphinx.environment
    sphinx.environment.BuildEnvironment.warn_node = _supress_nonlocal_image_warn


def _supress_nonlocal_image_warn(self, msg, node, **kwargs):
    from docutils.utils import get_source_line

    if not msg.startswith('nonlocal image URI found:'):
        self._warnfunc(msg, '{0!s}:{1!s}'.format(*get_source_line(node)))

supress_nonlocal_image_warn()

# http://stackoverflow.com/questions/11417221/sphinx-autodoc-gives-warning-pyclass-reference-target-not-found-type-warning

nitpick_ignore = [
    ('py:class', 'discretize.base.base_mesh.BaseMesh'),
    ('py:class', 'callable'),
    ('py:class', 'builtins.float'),
    ('py:class', 'builtins.complex')
    # ('py:class', 'IdentityMap'),
    # ('py:class', 'BaseSurvey'),
    # ('py:class', 'BaseSrc'),
    # ('py:class', 'BaseRx'),
    # ('py:class', 'Survey'),
    # ('py:class', 'FieldsFDEM'),
    # ('py:class', 'Fields3DElectricField'),
    # ('py:class', 'Fields3DMagneticFluxDensity'),
    # ('py:class', 'Fields3DCurrentDensity'),
    # ('py:class', 'Fields3DMagneticField'),
    # ('py:class', 'SurveyTDEM'),
    # ('py:class', 'SrcTDEM'),
    # ('py:class', 'FieldsTDEM'),
    # ('py:class', 'EMPropMap'),
    # ('py:class', 'Data'),
    # ('py:class', 'SurveyDC'),
    # ('py:class', 'BaseMTFields'),
    # ('py:class', 'SolverLU'),
    # ('py:class', 'BaseMagSurvey'),
    # ('py:class', 'BaseMagMap'),
    # ('py:class', 'Fields3DCellCentered'),
    # ('py:class', 'FieldsDC'),
    # ('py:class', 'Fields3DNodal'),
    # ('py:class', 'Survey_ky'),
    # ('py:class', 'Fields2D'),
    # ('py:class', 'Fields2DCellCentered'),
    # ('py:class', 'Fields2DNodal'),
    # ('py:class', 'BaseNSEMFields'),
    # ('py:class', 'Fields1DPrimarySecondary'),
    # ('py:class', 'Fields1D_eTotal'),
    # ('py:class', 'Fields3DPrimarySecondary'),
    # ('py:class', 'BaseNSEMSrc'),
    # ('py:class', 'SimPEG.electromagnetics.natural_source.utils.plot_utils.DataNSEMPlotMethods'),
    # ('py:class', 'DataNSEMPlotMethods'),
    # ('py:class', 'RichardsMap'),
    # ('py:class', 'SimPEG.props.HasModel'),
    # ('py:class', 'BaseFDEMSrc'),
    # ('py:class', 'BaseTDEMSrc'),
    # ('py:class', 'properties.Model'),
    # ('py:class', 'properties.PhysicalProperty'),
    # ('py:func', 'discretize.utils.mesh_utils.meshTensor'),
    # ('py:class', 'SimPEG.regularization.BaseRegularization'),
    # ('py:func', 'discretize.utils.mesh_utils.meshTensor'),
    # ('py:class', 'properties.base.HasProperties'),
    # ('py:class', 'properties.base.base.HasProperties'),
    # ('py:class', 'properties.Boolean'),
    # ('py:class', 'FieldsDerivativesEB'),
    # ('py:class', 'FieldsDerivativesHJ'),
    # ('py:class', 'SimPEG.electromagnetics.viscous_remanent_magnetization.simulation.BaseVRMSimulation'),
    # ('py:class', 'SimPEG.electromagnetics.viscous_remanent_magnetization.simulation.Simulation3DLinear'),
    # ('py:class', 'SimPEG.electromagnetics.viscous_remanent_magnetization.simulation.Simulation3DLogUniform'),
    # ('py:class', 'SimPEG.electromagnetics.viscous_remanent_magnetization.receivers.BaseRxVRM'),
    # ('py:class', 'SimPEG.electromagnetics.viscous_remanent_magnetization.receivers.PointMagneticField'),
    # ('py:class', 'SimPEG.electromagnetics.viscous_remanent_magnetization.receivers.PointMagneticFieldTimeDerivative'),
    # ('py:class', 'SimPEG.electromagnetics.viscous_remanent_magnetization.receivers.PointMagneticFluxDensity'),
    # ('py:class', 'SimPEG.electromagnetics.viscous_remanent_magnetization.receivers.PointMagneticFluxTimeDerivative'),
    # ('py:class', 'SimPEG.electromagnetics.viscous_remanent_magnetization.sources.BaseSrcVRM'),
    # ('py:class', 'SimPEG.electromagnetics.viscous_remanent_magnetization.sources.MagDipole'),
    # ('py:class', 'SimPEG.electromagnetics.viscous_remanent_magnetization.sources.CircLoop'),
    # ('py:class', 'SimPEG.electromagnetics.viscous_remanent_magnetization.sources.LineCurrent'),
    # ('py:class', 'SimPEG.electromagnetics.viscous_remanent_magnetization.survey.SurveyVRM'),
    # ('py:class', 'SimPEG.electromagnetics.viscous_remanent_magnetization.waveforms.StepOff'),
    # ('py:class', 'SimPEG.electromagnetics.viscous_remanent_magnetization.waveforms.SquarePulse'),
    # ('py:class', 'SimPEG.electromagnetics.viscous_remanent_magnetization.waveforms.ArbitraryDiscrete'),
    # ('py:class', 'SimPEG.electromagnetics.viscous_remanent_magnetization.waveforms.ArbitraryPiecewise'),
    # ('py:class', 'SimPEG.electromagnetics.viscous_remanent_magnetization.waveforms.Custom'),
    # ('py:class', 'SimPEG.props.LocationVector'),
    # ('py:class', 'SurveyVRM'),
]
