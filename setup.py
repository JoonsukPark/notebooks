from setuptools import setup, Extension

setup(
    ext_modules=[Extension('mysum_c', ['mysum.c']),
                 Extension('mysum_cpp', ['mysum.cpp']),
                 ],
    install_requires=['numpy']
)