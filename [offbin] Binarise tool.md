offbin
======

## Purpose
Single command to run any of the commands that were previously in the directory.

## Consider
- Only supporting Makefile, `cargo make`, `mage`, `package.json` &etc., rather than making offbin a generic self-extracting format

## CLI arguments for `offbin`
 - `--version`
 - `--help`
 - `-v`, specify multiple times for greater verbosity (log levels)
 - `--pipe`, specify default for all: `--pipe '*:stdout:file:///dev/stdout' --pipe '*:stderr:file:///dev/stderr'`, and specialisation: `package.json:stdout:'file://$name.stdout'`
 - `--dry-run`: don't execute, just show what will be executed
 - `--arg`, `-A`: argument. Added to the end of every default/specialised entrypoint. Can be specified multiple times.
 - `--no-ignore-vcs`: rather than ignoring everything in .gitignore, will compress entire folder into the output binary.
 - `--no-defaults`: no default entrypoints. Handy for using offbin as a simple self-extracting archive format, and for when `--entrypoint` are specified explicitly but not exhaustively.
 - `--entrypoint`: explicit command to run, rather than default. Can be specified multiple times.
 - All positional refer to tasks, `<binary> task0 task1` will run tasks: task0 and task1 sequentially

## CLI arguments for `offbin`ifed binary
 - `--version`
 - `--help`
 - `-v`, specify multiple times for greater verbosity (log levels)
 - `--pipe`, specify default for all: `--pipe '*:stdout:file:///dev/stdout' --pipe '*:stderr:file:///dev/stderr'`, and specialisation: `package.json:stdout:'file://$name.stdout'`
 - `--dry-run`: don't execute, just show what will be executed
 - `--no-cleanup`: don't remove extracted files after run
 - `--arg`, `-A`: argument. Added to the end of every default/specialised entrypoint. Can be specified multiple times.
 - `--no-defaults`: no default entrypoints. Handy for using offbin as a simple self-extracting archive format, and for when `--entrypoint` are specified explicitly but not exhaustively.
 - `--entrypoint`: explicit command to run, rather than default. Can be specified multiple times.
 - All positional refer to tasks, `<binary> task0 task1` will run tasks: task0 and task1 sequentially

## Idea

### Example 0
```cmd
> dir /b
foo.exe foo.toml can.exe can.toml runner.toml
> type runner.toml
[runner]
foo --makefile foo.toml
can --makefile can.toml
> offbin --compression=upx -o ..\cool.exe
> cd ..\tmp_dir
> ..\cool.exe
# Extracting with UPX
# Running foo with arg "foo.toml"
# Running can with arg "can.toml"
# Removing all extracted files
> ..\cool.exe foo
# Extracting with UPX
# Running foo with arg "foo.toml"
# Removing all extracted files
```

### Example 1

#### Setup
```bash
$ ls
package.json  Cargo.toml  Rakefile  Makefile
index.js      main.rs     cli.rb    main.c
> offbin --compression=lzma -o /tmp/multi
```

#### 0
```bash
$ cd "$(mktemp -d)"
$ /tmp/multi
# Extracting with tar
# Running 'package.json' with default `npm run-script build`
# <output from ^>
# Running 'Cargo.toml' with default `cargo run`
# <output from ^>
# Running 'Rakefile' with default `rake`
# <output from ^>
# Running 'Makefile' with default `make`
# <output from ^>
# Removing all extracted files
```

#### 1
```bash
$ cd "$(mktemp -d)"
$ /tmp/multi package.json
# Extracting with tar
# Running 'package.json' with `npm run-script hello`
# <output from ^>
# Removing all extracted files
```

#### 2
```bash
$ cd "$(mktemp -d)"
$ /tmp/multi --entrypoint 'Cargo.toml:ls'
# Extracting with tar
# Running 'package.json' with default `npm run-script build`
# <output from ^>
# Running 'Cargo.toml' with `ls`
package.json  Cargo.toml  Rakefile  Makefile
index.js      main.rs     cli.rb    main.c
# Running 'Rakefile' with default `rake`
# <output from ^>
# Running 'Makefile' with default `make`
# <output from ^>
# Removing all extracted files
```

#### 3
```bash
$ cd "$(mktemp -d)"
$ /tmp/multi --entrypoint 'Cargo.toml:ls' --no-defaults
# Extracting with tar
# Running 'Cargo.toml' with `ls`
package.json  Cargo.toml  Rakefile  Makefile
index.js      main.rs     cli.rb    main.c
# Removing all extracted files
```
 
## Implementation detail
 
Because many different language formats will be supported, create a mapping in a language-independent format, like:
```json
{
  "Makefile*": {
    "command": "make $@",
    "name": {"$ref": "#/README.md/name"}
  },
  "Gruntfile": {
    "command": "grunt $@"
  },
  "makers": {
    "command": "makers $@"
  },
  "package.json": {
    "command": "npm run-script build",
    "name": ".name"
  },
  "Makefile.toml": {
    "command": "cargo make $@",
    "name": {"$ref": "#/Cargo.toml/name"}
  },
  "Cargo.toml": {
    "command": "cargo run",
    "name": ".name"
  },
  "README.md": {
    "command": null,
    "name": "get_name_from_README()"
  }
}
```

Also environment variables MUST be inherited from base process.