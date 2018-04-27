from static import *

from random import randint, seed
from datetime import date

def start_horoscopy():
    aujourdhui = str(date.today())
    aujourdhui = aujourdhui[0:4] + aujourdhui[5:7] + aujourdhui[8:10]

    my_seed = seed(int(aujourdhui))

    x = randint(1,10)

    user_input = input("\nTa date de naissance sous la forme jj/mm/aaaa\n")

    if check_date(user_input):

        signe = check_signes(user_input)

        pt(c_green("ton signe c'est de la merde"))
        pt(c_green("aujourdhui tu vas en chier\n"))


def check_date(user_input):
    is_user_input_ok = True

    """
	if (month>12 || month<1){
		date_is_ok = false;
	}

	else if (month==2){
		bool is_bissextile = false;

		if ((year%4==0 && year%100!=0)||(year%400==0)){
			is_bissextile = true;
		}

		if ((not is_bissextile) && (day<1 || day>29)){
			date_is_ok = false;
		}
		else if ((is_bissextile)&&(day<1 || day>28)){
			date_is_ok = false;
		}
	}

	else if ((month==4 || month==6 || month==9 || month==11)&&(day<1 || day>30)){
		date_is_ok = false;
	}

	else if (day<1 || day>31){ // other months
			date_is_ok = false;
	}

	return date_is_ok;
    """

    return is_user_input_ok



def check_signes(user_input):
    pass
