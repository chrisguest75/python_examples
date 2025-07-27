# UV SCRIPT

The simplest way to write complex code with dependencies for scripting tools.  

## Running

```sh
./template.py
# or 
./example.py
```

## Create a template

```sh
uv init --script example.py --python 3.12
```

## Add shebang

```sh
#!/usr/bin/env -S uv run --script

chmod +x ./example.py 
```

## Dependencies

```sh
uv run --with rich example.py

uv add --script example.py 'requests<3' 'rich'
```

## Resources

* https://docs.astral.sh/uv/guides/scripts/#running-a-script-with-dependencies
