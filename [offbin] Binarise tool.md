offbin
======

## Purpose
Single command to run any of the commands that were previously in the directory.

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
$ /tmp/multi hello
# Extracting with tar
# Running 'package.json' with `npm run-script hello`
# <output from ^>
# Running 'Cargo.toml' with `cargo hello`
# <output from ^>
# Running 'Rakefile' with `rake hello`
# <output from ^>
# Running 'Makefile' with `make hello`
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

## Consider
- Only supporting Makefile, `cargo make`, `mage`, `package.json` &etc., rather than making offbin a generic self-extracting format

## CLI arguments

 - `--version`
 - `--help`
 - `--dry-run`: don't execute, just show what will be executed
 - `--no-cleanup`: don't remove extracted files after run
 - `--arg`, `-A`: argument. This argument will go at the end of every run command. Expected to be used when you want the default runner with extra arguments provided. Can be specified multiple times.
 - `--no-ignore-vcs`: rather than ignoring everything in .gitignore, will compress entire folder into the output binary.
 - `--no-defaults`: no default entrypoints. Handy for using offbin as a simple self-extracting archive format, and for when `--entrypoint` are specified explicitly but not exhaustively.
 - `--entrypoint`: explicit command to run, rather than default. Can be specified multiple times.
 - All positional arguments are appended, e.g.: `cargo run <args>`, instead of `cargo run`
 
## Implementation detail
 
Because many different language formats will be supported, create a mapping in a language-independent format, like:
```json
{
  "Makefile*": "make $@",
  "Gruntfile": "grunt $@",
  "makers": "makers $@",
  "package.json": "npm run-script build",
  "Makefile.toml": "cargo make $@",
  "Cargo.toml": "cargo run"
}
```

Also environment variables MUST be inherited from base process.