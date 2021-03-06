# Password Wordlist Generator
#
# By: Nishant Kumar

#
#
##################

import itertools


ban = '''

                                                    '''

print('''\033[91m



 ███▄    █  ██▓  ██████  ██░ ██  ▄▄▄       ███▄    █ ▄▄▄█████▓    ██ ▄█▀ █    ██  ███▄ ▄███▓ ▄▄▄       ██▀███  
 ██ ▀█   █ ▓██▒▒██    ▒ ▓██░ ██▒▒████▄     ██ ▀█   █ ▓  ██▒ ▓▒    ██▄█▒  ██  ▓██▒▓██▒▀█▀ ██▒▒████▄    ▓██ ▒ ██▒
▓██  ▀█ ██▒▒██▒░ ▓██▄   ▒██▀▀██░▒██  ▀█▄  ▓██  ▀█ ██▒▒ ▓██░ ▒░   ▓███▄░ ▓██  ▒██░▓██    ▓██░▒██  ▀█▄  ▓██ ░▄█ ▒
▓██▒  ▐▌██▒░██░  ▒   ██▒░▓█ ░██ ░██▄▄▄▄██ ▓██▒  ▐▌██▒░ ▓██▓ ░    ▓██ █▄ ▓▓█  ░██░▒██    ▒██ ░██▄▄▄▄██ ▒██▀▀█▄  
▒██░   ▓██░░██░▒██████▒▒░▓█▒░██▓ ▓█   ▓██▒▒██░   ▓██░  ▒██▒ ░    ▒██▒ █▄▒▒█████▓ ▒██▒   ░██▒ ▓█   ▓██▒░██▓ ▒██▒
░ ▒░   ▒ ▒ ░▓  ▒ ▒▓▒ ▒ ░ ▒ ░░▒░▒ ▒▒   ▓▒█░░ ▒░   ▒ ▒   ▒ ░░      ▒ ▒▒ ▓▒░▒▓▒ ▒ ▒ ░ ▒░   ░  ░ ▒▒   ▓▒█░░ ▒▓ ░▒▓░
░ ░░   ░ ▒░ ▒ ░░ ░▒  ░ ░ ▒ ░▒░ ░  ▒   ▒▒ ░░ ░░   ░ ▒░    ░       ░ ░▒ ▒░░░▒░ ░ ░ ░  ░      ░  ▒   ▒▒ ░  ░▒ ░ ▒░
   ░   ░ ░  ▒ ░░  ░  ░   ░  ░░ ░  ░   ▒      ░   ░ ░   ░         ░ ░░ ░  ░░░ ░ ░ ░      ░     ░   ▒     ░░   ░ 
         ░  ░        ░   ░  ░  ░      ░  ░         ░             ░  ░      ░            ░         ░  ░   ░     
                                                                                                               
           		 
''')
                                                          		 
print('''\t\t\t\t\t\t\033[93mMINI \033[96mPROJECT\033[93m  \n\t\t\t\t\t\t    \033[93mO\033[96mN\033[93m ''')
print('''\033[92m
______  ___   _____ _____  _    _  _________________   _____  _____ _   _  ___________  ___ _____ ___________ 
| ___ \/ _ \ /  ___/  ___|| |  | ||  _  | ___ \  _  \ |  __ \|  ___| \ | ||  ___| ___ \/ _ \_   _|  _  | ___ \\
| |_/ / /_\ \\\ `--.\ `--. | |  | || | | | |_/ / | | | | |  \/| |__ |  \| || |__ | |_/ / /_\ \| | | | | | |_/ /
|  __/|  _  | `--. \`--. \| |/\| || | | |    /| | | | | | __ |  __|| . ` ||  __||    /|  _  || | | | | |    / 
| |   | | | |/\__/ /\__/ /\  /\  /\ \_/ / |\ \| |/ /  | |_\ \| |___| |\  || |___| |\ \| | | || | \ \_/ / |\ \ 
\_|   \_| |_/\____/\____/  \/  \/  \___/\_| \_|___/    \____/\____/\_| \_/\____/\_| \_\_| |_/\_/  \___/\_| \_|

''')

print('''\033[91m
        \033[91m [\033[96m*\033[91m] \033[97mGitHub  \033[91m=  \033[4m\033[1;97mhttps://github.com/unknowni8/password-generator \033[24m

''')

scale = input('\033[36m[!] provide a size scale [eg: "4 to 8" = 4:8 & For N letter = N:N] : ')
start = int(scale.split(':')[0])
final = int(scale.split(':')[1])

use_nouse = str(input("\n\033[36m[?] Do you want password acc. to personal data? [y/N]: "))
if use_nouse == 'y':
	first_name = str(input("\n\033[36m[*] Fist Name: "))
	last_name = str(input("\n\033[36m[*] Last Name: "))
	birthday = str(input("\n\033[36m[*] Birthday: "))
	month = str(input("\n\033[36m[*] Month: "))
	year = str(input("\n\033[36m[*] Year: "))
	chrs = first_name + last_name + birthday + month + year
else:
	chrs = input("\n\033[36m[!] Enter preffered alphabet for password: ")
	pass

chrs_up = chrs.upper()
# chrs_specials = '!\][/?.,~-=";:><@#$%&*()_+\' '
# chrs_numerics = '1234567890'

file_name = input('\n\033[36m[!] Insert a name for your wordlist file: ')
arq = open(file_name, 'w')
if input('\n\033[36m[?] Do you want to use uppercase characters? (y/n): ') == 'y':
	chrs = ''.join([chrs, chrs_up])
if(input('\n\033[36m[?] Do you want to use special characters? (y/n): ') == 'y'):
        chrs_specials = input('\033[36m[!]Enter the preffered special character: ')
        chrs = ''.join([chrs, chrs_specials])
if(input('\n\033[36m[?] Do you want to use numeric characters? (y/n): ') == 'y'):
        chrs_numerics = input('\033[36m[!]Enter the preffered number: ')
        chrs = ''.join([chrs, chrs_numerics])

for i in range(start, final+1):
	for j in itertools.product(chrs, repeat=i):
		temp = ''.join(j)
		print(temp)
		arq.write(temp + '\n')
arq.close()
