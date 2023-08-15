import setuptools

setuptools.setup(
    name="vscode_binder_proxy",
    version='1.0',
    url="https://github.com/dragonstyle/vscode_binder_proxy/",
    author="Charles Teague",
    description="charles@posit.co",
    packages=setuptools.find_packages(),
	keywords=['Jupyter'],
	classifiers=['Framework :: Jupyter'],
    install_requires=[
        'jupyter-server-proxy'
    ],
    entry_points={
        'jupyter_serverproxy_servers': [
            'vscode = vscode_binder_proxy:setup_quarto_vscode_binder',
        ]
    },
    package_data={
        'vscode_binder_proxy': ['icons/*'],
    },
)
