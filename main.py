import os
import sys


# This function runs the trading bot
def f_run_bot():
    print('Trading bot started!')
    config = f_check_for_config()


# This function is used to check for a config file and return data inside of it
def f_check_for_config():
    print('Checking for config file!')
    config_path = 'Config/config.cfg'
    if os.path.isfile(config_path):
        print('Config file found!')
        return f_load_config_file(config_path)
    else:
        sys.exit('Config file not found!')
        

# This function is used to get and return the data of the config file
def f_load_config_file(p_path):
    print('Loading the config file!')
    config_path = p_path
    try:
        with open(config_path) as file:
            print(file.readlines())
    except IOError:
        sys.exit('Config file could not be accessed!')






# This function calls the function to run the trading bot
def main():
    f_run_bot()


if __name__ == "__main__":
    main()
