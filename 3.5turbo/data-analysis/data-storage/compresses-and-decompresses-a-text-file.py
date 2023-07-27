Sure! Here is a Python script that compresses and decompresses a text file using the zlib library:

```python
import zlib

def compress_file(file_path):
    """
    Compresses a text file using zlib compression algorithm.
    
    :param file_path: path to the text file
    """
    try:
        with open(file_path, 'rb') as file:
            input_data = file.read()
            compressed_data = zlib.compress(input_data, level=zlib.Z_BEST_COMPRESSION)
        
        with open(file_path + '.compressed', 'wb') as file:
            file.write(compressed_data)
        
        print('Compression successful. Compressed file saved as', file_path + '.compressed')
    except FileNotFoundError:
        print('File not found.')
    except Exception as e:
        print('An error occurred during compression:', str(e))

def decompress_file(file_path):
    """
    Decompresses a compressed text file using zlib decompression algorithm.
    
    :param file_path: path to the compressed file
    """
    try:
        with open(file_path, 'rb') as file:
            compressed_data = file.read()
            decompressed_data = zlib.decompress(compressed_data)
        
        with open(file_path[:-10], 'wb') as file:
            file.write(decompressed_data)
        
        print('Decompression successful. Decompressed file saved as', file_path[:-10])
    except FileNotFoundError:
        print('File not found.')
    except Exception as e:
        print('An error occurred during decompression:', str(e))

# Ask the user for input
file_path = input('Enter the path to the text file: ')

# Compress the file
compress_file(file_path)

# Decompress the file
decompress_file(file_path + '.compressed')
```

To run this script, save it in a file named `task.py` and run `python task.py` in your command line. The script will prompt you to enter the path to the text file you want to compress. It will then compress the file using the zlib compression algorithm and save the compressed file with a `.compressed` extension. After that, it will decompress the same file and save the decompressed file without the `.compressed` extension.
