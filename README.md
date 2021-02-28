# Sublime V

> Sublime Text 3 support for [The V Programming Language](https://vlang.io)


## Features

- Syntax highlighting
- Build system
	- `Run` (default action for `*.v` files)
	- `Test` (default action for `*_test.v` files)
	- `Compile`
	- `Compile (production)`
	- `Format file`
	- `Format project`
	- `Test project`
	- `Profile`


### Magic directories

This is a list of special directory names that have a particular behavior when
you compile source files directly inside them, i.e. the output binary file
will be placed inside a folder named `bin` at the same level as the magic dir.


Imagine you have `src` in the list, and the following project:

	src/
	 └─ some.v

When you compile `some.v`, you will end up with the resulting tree:

	src/
	 └─ some.v
	bin/
	 └─ some

> You may have to create the `bin` folder manually


Edit the list as you prefer under:

	Preferences > Package Settings > V > Settings


## Installation

	# Windows
	git clone https://github.com/onerbs/sublime-v ^
		"%AppData%\Sublime Text 3\Packages\V"

	# Linux
	git clone https://github.com/onerbs/sublime-v \
		"~/.config/sublime-text-3/Packages/V"

	# macOS
	git clone https://github.com/onerbs/sublime-v \
		"~/Library/Application Support/Sublime Text 3/Packages/V"
