# RMBG

RMBG is a Python-based tool for demonstrating the removal of the background from images. This repository accompanies a YouTube video tutorial which can be found [here](https://youtu.be/t24aCY6mvHw).

## Installation

First, you need to install the required libraries listed in `requirements.txt`. You can do this by running the following command:

```bash
pip install -U --upgrade -r requirements.txt > install_log.out
```

This command will upgrade and install all the necessary libraries and log the installation process in `install_log.out`.

## Usage

To remove the background from an image, simply run the following command:

```bash
python bg_remover.py
```

The script will prompt you for the input file path. Once the process is complete, it will save the background-removed image in the same directory as the input file, with the filename formatted as `{input_file_name}_rmbg.png`.

## Support

If you find this tool useful, please consider starring the repository. Share it with your friends and fellow developers!

Happy coding!
