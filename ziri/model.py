import os


def filenotfounddecorator(func):
    def wrapper(*args):
        try:
            res = func(*args)
            return res
        except FileNotFoundError:
            print('Diary could not be found.')
        except Exception as e:
            print(f'Something went wrong: {e}')

    return wrapper


def add(date: str, text: str):

    filename = date + '.txt'
    if not os.path.exists(filename):
        # new entry
        with open(filename, 'w') as fp:
            fp.write(text)
            print('Diary for ', date, 'Added successfully!')
        read(date)
    else:
        # add another entry
        if not checkifentryexists(filename, text):
            with open(filename, 'a') as fp:
                fp.writelines(text+'\n')
            print('Diary for ', date, 'added on to successfully!')
            read(date)
        else:
            print(f'This entry: {text} already exists in the {date} diary')


def update(date: str, text: str):
    filename = date + '.txt'

    if not os.path.exists(filename):
        print('Diary for', date,
              'could not be found. Did you mean to add a new entry? Try add command instead')

    else:
        with open(filename, 'w') as fp:
            fp.write(text)
            print('Diary for ', date, ' updated successfully')
        read(date)


@filenotfounddecorator
def remove(date: str):
    filename = date + '.txt'
    os.remove(filename)
    print(f'Diary for {date} removed successfully!')


def clear(date: str):
    filename = date + '.txt'
    if os.path.exists(filename):
        with open(filename, 'w') as fp:
            fp.write('')
        print('Diary for ', date, ' cleared successfully')
    else:
        print(f'Diary for {date} could not be found')


def read(date: str):
    filename = date + '.txt'
    if os.path.exists(filename):
        with open(filename, 'r') as fp:
            diary = fp.readlines()
            print(f'--- {date} ---')
            if len(diary):
                for line in diary:
                    print(line, end='')
                print('--- The End ---')
            else:
                print('Nothing recorded here.')
    else:
        print(f'{date} diary does not exists.')


def list():
    current_directory = os.getcwd()
    text_files = [file for file in os.listdir(
        current_directory) if file.endswith('.txt')]

    if len(text_files) > 0:
        for f in text_files:
            print(f)
    else:
        print('You do not have any diary entries.')


@filenotfounddecorator
def checkifentryexists(filename: str, text: str):
    with open(filename, 'r') as fp:
        diary = fp.readlines()
    return text.lower() in str(diary).lower()
