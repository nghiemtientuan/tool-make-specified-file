import sys
from core.text import create_file_text
from core.const import output_path, convert_bytes, file_size


def create_file(filename, type='txt', size=0):
    """
        Create file by type extension

        Parameters:
        filename (string): file name
        type     (string): file extension
        size     (string): file size by byte

        Returns: null
    """

    size = int(size)
    if size <= 0:
        size = 1
    file_types = {
        # text
        'txt': create_file_text(filename, size),

        # shel run
        'exe': False,

        # image
        'jpg': False,
        'png': False,
        'jpeg': False,

        # excel
        'xls': False,
        'xlsx': False,

        # word
        'doc': False,
        'docx': False,

        # pdf
        'pdf': False,

        # PowerPoint
        'ppt': False,
        'pptx': False,
    }

    status = file_types.get(type, 'extension_not_support')
    if status is True:
        file_path = output_path(filename, type)
        size = file_size(file_path)
        print('Create file success!!')
        print('File path: {}'.format(file_path))
        print('File size: {} ({} bytes)'.format(
            convert_bytes(size),
            size
        ))
    elif status == 'extension_not_support':
        print('[Notify] error: File extension is not support')
    else:
        print('[Notify] error: Create file error')


if __name__ == "__main__":
    params = sys.argv
    if len(params) <= 1:
        print('[Notify] error: Please enter file name')
    else:
        file_name = sys.argv[1]
        if len(params) > 3:
            create_file(file_name, sys.argv[2], sys.argv[3])
        elif len(params) > 2:
            create_file(file_name, sys.argv[2])
        else:
            create_file(file_name)
