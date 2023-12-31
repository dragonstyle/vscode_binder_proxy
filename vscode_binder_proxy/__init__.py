"""
Return config on servers to start for quarto_vscode_binder

See https://jupyter-server-proxy.readthedocs.io/en/latest/server-process.html
for more information.
"""
import os
import shutil


def setup_quarto_vscode_binder():

    executable = "code-server"
    if not shutil.which(executable):
        raise FileNotFoundError("Can not find code-server in PATH")
    
    # Start vscode in CODE_WORKINGDIR env variable if set
    # If not, start in 'current directory', which is $REPO_DIR in mybinder
    # but /home/jovyan (or equivalent) in JupyterHubs
    working_dir = os.getenv("CODE_WORKINGDIR", ".")
    extensions_dir = os.getenv("CODE_EXTENSIONSDIR", None)

    cmd = [
            executable,
            "--auth",
            "none",
            "--disable-telemetry",
            "--port=" + str(port),
        ]

    if extensions_dir:
        cmd += ["--extensions-dir", extensions_dir]
    cmd.append(working_dir)

    return {
        'command': cmd,
        "timeout": 300,
         "new_browser_tab": True,
        'environment': {},
        'launcher_entry': {
            'title': 'VS Code',
            'icon_path': os.path.join(os.path.dirname(os.path.abspath(__file__)), 'icons', 'vscode.svg')
        }
    }
