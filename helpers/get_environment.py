import os
import sys, getopt
from dotenv import load_dotenv


load_dotenv()


def get_url():
    argument_list = sys.argv[1:]

    options = "hmo:"

    long_options = ["ENV="]
    try:
        arguments, values = getopt.getopt(argument_list, options, long_options)
        for current_argument, current_value in arguments:
            if current_argument in ("--ENV", "--env"):
                match current_value:
                    case 'local':
                        print(f"{os.getenv('LOCAL_URL')}:{os.getenv('PORT')}")
                    case 'remote':
                        print("Remote")
            elif current_argument:
                print(f"{os.getenv('LOCAL_URL')}:{os.getenv('PORT')}")

    except getopt.error as err:
        print(str(err))

