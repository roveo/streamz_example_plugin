from setuptools import setup, find_packages

setup(
    name="streamz_example_plugin",
    version="0.0.1",
    install_requires=["streamz>=0.6.1"],
    packages=find_packages(),
    entry_points={
        "streamz.sources": [
            "from_iterable = streamz_example_plugin.sources:from_iterable"
        ],
        "streamz.nodes": ["repeat = streamz_example_plugin.nodes:repeat"],
    },
)
