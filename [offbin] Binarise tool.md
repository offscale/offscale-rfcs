offbin
======

## Purpose
Single command to run any of the commands that were previously in the directory.

## Idea
```cmd
> dir /b
foo.exe foo.toml can.exe can.toml runner.toml
> type runner.toml
[runner]
foo --makefile foo.toml
can --makefile can.toml
> offbin --compression=upx -o ../cool.exe
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

## Consider
- Only supporting Makefile, `cargo make`, `mage`, `package.json` &etc., rather than making offbin a generic self-extracting format

## CLI arguments

 - `--version`
 - `--help`
 - `--dry-run`: don't execute, just show what will be executed
 - `--no-cleanup`: don't remove extracted files after run
 - All other arguments are put to the end of the command, e.g.: `npm run-script <args>`, instead of running the default
 - `--entrypoint`: explicit command to run at the end, rather than default (as ^). Can be specified multiple times.
 - `--arg`, `-A`: argument. Can be specified multiple times. This argument will go at the end of every run command. Expected to be used when you want the default runner with extra arguments provided.
 - `--cache`: rather than ignoring everything in .gitignore, will cache entire folder
 
## Implementation detail
 
Because many different language formats will be supported, create a mapping in a language-independent format, like:
```json
{
  "Makefile*": "make $@",
  "Gruntfile": "grunt $@",
  "makers": "makers $@",
  "Makefile.toml": "cargo make $@"
}
```

Also environment variables MUST be inherited from base process.