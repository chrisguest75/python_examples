from codeartifact_test_package import metadata

#from importlib import metadata
#version = metadata.version("codeartifact_test_package")


if __name__ == '__main__':
    md = metadata.get_metadata()
    print(md.get('name'))
    print(md)




