import os

def generate_directory_tree(root_dir):
    tree = []
    for root, dirs, files in os.walk(root_dir):
        level = root.replace(root_dir, '').count(os.sep)
        indent = ' ' * 4 * (level)
        tree.append(f"{indent}{os.path.basename(root)}/")
        subindent = ' ' * 4 * (level + 1)
        for file in files:
            tree.append(f"{subindent}{file}")
    return '\n'.join(tree)

def collect_python_scripts(directory):
    collected_text = ""
    # Collect files only in the main directory
    for file in os.listdir(directory):
        if file.endswith(".py"):
            file_path = os.path.join(directory, file)
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            header = f"# File: {file}\n# Path: {file_path}\n"
            collected_text += header + "\n" + content + "\n\n\n"

    return collected_text

def write_to_output_file(output_file, text):
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(text)

if __name__ == "__main__":
    input_directory = input("Entrez le chemin du répertoire à explorer: ")  # Chemin du répertoire à explorer
    output_file = input_directory + "/output.txt"  # Fichier de sortie

    # Generate directory tree
    directory_tree = generate_directory_tree(input_directory)
    
    # Collect Python scripts
    collected_text = collect_python_scripts(input_directory)
    
    # Combine directory tree and collected scripts
    final_output = f"Arborescence des fichiers:\n\n{directory_tree}\n\n\n{collected_text}"

    # Write to output file
    write_to_output_file(output_file, final_output)

    print(f"Les scripts ont été collectés et écrits dans {output_file}")
