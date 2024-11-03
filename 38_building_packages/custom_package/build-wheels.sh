#!/bin/bash
set -e -u -x

function repair_wheel {
    wheel="$1"
    if ! auditwheel show "$wheel"; then
        echo "Skipping non-platform wheel $wheel"
    else
        auditwheel repair "$wheel" --plat "$PLAT" -w ./wheelhouse/
    fi
}

# Compile wheels
#for PYBIN in /opt/python/*/bin; do
    "${PYBIN}/pip" install -r ./dev-requirements.txt
    "${PYBIN}/python" setup.py sdist bdist_wheel
    #"${PYBIN}/pip" wheel ./ --no-deps -w ./wheelhouse/
#done

# Bundle external shared libraries into the wheels
for whl in wheelhouse/*.whl; do
    repair_wheel "$whl"
done

# Install packages and test
#for PYBIN in /opt/python/*/bin/; do
    "${PYBIN}/pip" install python-manylinux-demo --no-index -f ./wheelhouse
    (cd "$HOME"; "${PYBIN}/nosetests" pymanylinuxdemo)
#done
