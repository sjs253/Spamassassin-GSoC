import codecs
from glob import glob


def get_labelled_data_count():
    path = '/home/shreyansh/Downloads/KAM-500Ham+500Spam'

    cnt = 0
    with codecs.open(path, 'r', encoding='utf-8', errors='ignore') as file_stream:
        lines = file_stream.readlines()

        for line in lines:
            line = line.strip()
            if line.startswith("X-Spam-Status"):
                cnt += 1
    print(cnt)


def mbox_to_dicts():
    path = '/home/shreyansh/Desktop/Formail/*'
    # path= '/home/shreyansh/Downloads/KAM-500Ham+500Spam'

    file_paths = glob(path)

    mbox_dict = {}
    for file_path in file_paths:
        with codecs.open(file_path, 'r', encoding='utf-8', errors='ignore') as file_stream:
            lines = file_stream.readlines()
            mbox_dict[file_path] = lines

    return mbox_dict


def get_useful_mbox(mbox_dict):
    useful_mbox_dict = {}
    for file_path, lines in mbox_dict.items():

        is_useful = False
        for line in lines:
            line = line.strip()
            if line.startswith("X-Spam-Status"):
                is_useful = True
                break

        if is_useful:
            useful_mbox_dict[file_path] = lines

    return useful_mbox_dict


headers = {
    'body_header': "Content-Type: text/plain;",
    'html_header': "Content-Type: text/html;",
    'attachment_header': "Content-Type: application/octet-stream;",
    'subject_header': "Subject:",
    'spam_header': "X-Spam-Status:"
}


def split_single_mbox(lines):
    spam_content = []
    subject_content = []
    body_content = []

    headers_idx = {}

    for idx, line in enumerate(lines):
        line = line.strip()
        for header_type, header in headers.items():
            if line.startswith(header):
                headers_idx[header_type] = idx
    return headers_idx


def split_mbox_dict_to_headers(mbox_dict):
    mobx_with_headers = {}

    cnt = 0
    for file_path, lines in mbox_dict.items():
        # spam, subject, body = split_single_mbox(lines)

        headers_idx = split_single_mbox(lines)
        print(headers_idx['spam_header'])
        if headers_idx['spam_header'] == 0:

            cnt += 1
        # mobx_with_headers[file_path] = {'spam': spam, 'subject': subject, 'body': body}

    # return mobx_with_headers
    return cnt


def convertor():
    all_mbox = mbox_to_dicts()

    useful_mbox = get_useful_mbox(all_mbox)

    print(split_mbox_dict_to_headers(useful_mbox))
    print(len(all_mbox))
    print(len(useful_mbox))


if __name__ == "__main__":
    convertor()
