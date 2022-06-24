import coinbasepro as cbp
import json
import os
import sys


# This function runs the trading bot
def f_run_bot():
    print('Trading bot started!')
    config = f_check_for_config()
    auth_client = f_authenticate_client(config[0]['Key'], config[0]['Secret'], config[0]['Passphrase'])
    try:
        print(auth_client.get_accounts())
    except:
        sys.exit('Could not get account info!')


# This function is used to check for a config file and return data inside of it
def f_check_for_config():
    print('Checking for config file!')
    config_path = 'Config/config.json'
    if os.path.isfile(config_path):
        print('Config file found!')
        return f_load_config_file(config_path)
    else:
        sys.exit('Config file not found!')
        

# This function is used to get and return the data of the config file
def f_load_config_file(path):
    print('Loading the config file!')
    config_path = path
    try:
        with open(config_path) as file:
               return json.load(file)
    except IOError:
        sys.exit('Config file could not be accessed!')

# This function is used to authenticate a client
def f_authenticate_client(key, secret, passphrase):
    return cbp.AuthenticatedClient(key=key, secret=secret, passphrase=passphrase)



# This function calls the function to run the trading bot
def main():
    f_run_bot()


if __name__ == "__main__":
    main()
