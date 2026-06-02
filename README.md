# PyTreefy

[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE) ![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white) [![Buy Me a Coffee](https://img.shields.io/badge/Buy%20Me%20a%20Coffee-ffdd00?style=flat&logo=buy-me-a-coffee&logoColor=black)](https://buymeacoffee.com/infinition)

![IMG_0846](https://github.com/infinition/PyTreefy/assets/37984399/ecadbdee-8218-45e3-8f5e-88bb22a10126)

PyTreefy is a Python utility that scans a directory, generates its file structure diagram, and concatenates the contents of all discovered Python files into a single consolidated file. This is useful for code auditing, documentation, or bundling context for language models.

## Features

- **Directory Tree Generation**: Creates an ASCII visual representation of the directory and subdirectory tree structure.
- **Source Code Aggregation**: Collects and appends the source code of all Python scripts (*.py) found inside the target directory.
- **Consolidated Output**: Combines both the tree diagram and the source files into a single, clean text file.

## Setup

Requires Python 3.x.

Clone the repository and navigate into it:
```bash
git clone https://github.com/infinition/PyTreefy.git
cd PyTreefy
```

## Usage

Run the script and enter the path of the directory you want to analyze when prompted:
```bash
python PyTreefy.py
```

### Example

Running the script:
```
Entrez le chemin du répertoire à explorer: /home/user/projects
```

The script generates `output.txt` in the target directory with the following structure:
```
Arborescence des fichiers:

directory/
    subdirectory1/
        file1.py
        file2.txt
    subdirectory2/
        file3.py
    file4.py

# File: file1.py
# Path: /path/to/directory/subdirectory1/file1.py
<contents of file1.py>

# File: file3.py
# Path: /path/to/directory/subdirectory2/file3.py
<contents of file3.py>

# File: file4.py
# Path: /path/to/directory/file4.py
<contents of file4.py>
```

## Script Details

- `generate_directory_tree(root_dir)`: Generates the visual representation of the folder structure.
- `collect_python_scripts(directory)`: Recurses the directory to find and merge `.py` files.
- `write_to_output_file(output_file, text)`: Writes the final string to the output path.

## Star History

<a href="https://www.star-history.com/?repos=infinition%2FPyTreefy&type=date&legend=top-left">
 <picture>
   <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=infinition/PyTreefy&type=date&theme=dark&legend=top-left" />
   <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=infinition/PyTreefy&type=date&legend=top-left" />
   <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=infinition/PyTreefy&type=date&legend=top-left" />
 </picture>
</a>

## License

MIT. See [LICENSE](LICENSE).
