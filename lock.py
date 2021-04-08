from lib.main import Main
import os


if __name__ == '__main__':
    print('\n\n')
    print('[ P R O F I L E  -  L O C K E D ]'.center(os.get_terminal_size().columns))
    a = Main()
    print('\n\n\n[!] Put your cookie')
    a.set_cookie = input('[?] >>> ')

    # Check cookie
    print('[!] Please waitt!')
    id = a.validate_cookie
    if id:
        print('[!] Cookie valid')
        # Change language to burma
        b = a.change_lang("my_MM").text
        if 'lang="my"' in b[:200]:

            # and lock profile with id
            a.lock_profile(id)
            print('[!] Profile success locked')

            # and change language to indonesian
            a.change_lang('id_ID')
            exit('[!] Exit')
        else:
            print('[!] Failed to change language')
            exit('[!] Exit')
    else:
        print('[!] Cookie invalid')
        exit('[!] Exit')
