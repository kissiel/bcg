# bcg - Boilerplate Code Generator
###BCG creates a file with boilerplate content already in it.
###Type of content can be specified or inferred from the file extension.

Usage:
`$ bcg FILE TYPE`
`FILE` is the filename to be geneareted,
`TYPE` is optional template name to use
e.g.:
* `$ bcg foo.py` - create `foo.py` using `py` template
* `$ bcg bar cpp` - create `bar` file using `cpp` template

bcg will look for templates in following directories (in order of importance):

	1. `types` in the directory containing `bcg.py`
	2. `$XDG_CONFIG_HOME/bcg` or `$HOME/.config/bcg` if `$XDG_CONFIG_HOME`
		is not specified
	3. `bcg` in each of directories specified in `$XDG_CONFIG_DIRS`
