# DEPRECATION NOTICE

This repository has been deprecated. Use https://github.com/sirosen/texthooks instead.

A newer version of `alphabetize-codeowners` is maintained there.

# alphabetize-codeowners

For teams with lists of users attached to different paths, comparison of
codeowners lines quickly becomes difficult.

Alphabetize the lists of path owners so that they are always normalized to the
same form.

## Usage

Use via `pre-commit`:

```yaml
- repo: https://github.com/sirosen/alphabetize-codeowners
  rev: 0.0.1
  hooks:
    - id: alphabetize-codeowners
```

Use it as a python script by installing with `pipx`:

```
pipx install alphabetize-codeowners
```

Then run with

```
alphabetize-codeowners -v
```

## Sorting and Normalization Behaviors

### Sorts Owners, Not Lines

`alphabetize-codeowners` alphabetizes the lists of *owners* per path.
It does not alphabetize the lines in the file or otherwise sort them.

### Ignores Comments and Empty Lines

Any comment lines or empty lines should be left unmodified by the hook.

### Normalizes Whitespace

On the lines which are modified, the hook will normalize the line to have no
leading whitespace, and to separate codeowner names with a single space
character.
