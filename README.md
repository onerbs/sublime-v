# Sublime V

Sublime Text support for [The V Programming Language](https://vlang.io)


## Features

- Syntax highlighting
- Build system
	- `Run` (default action for `*.v` files)
	- `Test` (default action for `*_test.v` files)
	- `Compile`
	- `Compile (production)`
	- `Compile (skip unused)`
	- `Test project`
	- `Format file`
	- `Format project`
	- `Vet file`
	- `Vet project`
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


Edit the list as you prefer under:

	Preferences > Package Settings > V > Settings


## Installation

Navigate into the Sublime Text `Packages` directory and clone the repository:

	git clone https://github.com/onerbs/sublime-v V


> Open the packages folder using `Preferences: Browse Packages` from the command palette.
