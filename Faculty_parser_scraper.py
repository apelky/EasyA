'''
Faculty_Parser.py created by Angela Pelky on Tue Jan 17, 2023.

Group 1:
Ethan Aasheim
Melodie Collins
Linnea Gilius
Timothy Nadeau
Angela Pelky

This is a part of the system that implements an update to the Emerald Grade Tracker (EGT).
The original EGT can be found here: 'https://emeraldmediagroup.github.io/grade-data'
The EGT displays the letter-grade distribuition across all professors in a particular department of the natural science at the University of Oregon.
This system builds upon the original EGT by directly comparing professors in the same department on the same graph, and is only concerned with the extreme ends of the letter-grade spectrum.

----------------------------------------

Developer must provide "Regular_Faculty.txt" if any updates/changes have been made to the Natural Sciences faculty.

EasyA.py uses Python 3.10
'''

import requests as r
from bs4 import BeautifulSoup as bs

def scraper(url):

    site = r.get(url)
    soup = bs(site.content, 'html.parser')

    # optimize by looking through only the container we need
    container = soup.find('div', attrs={'id':'facultytextcontainer'})
    # for some reason the first faculty member is not part of the same class
    first_faculty = container.find('p')
    # get all faculty
    faculty = container.find_all('p', attrs={'class':'facultylist'})
    faculty.append(first_faculty)

    return faculty

def get_name(faculty):
    names_list = []

    for name in faculty:
        line_to_parse = name.string
        # Find the first instance of a comma
        name_position = line_to_parse.find(",")
        if name_position != -1:
            # Grab everything before the comma
            name = line_to_parse[:name_position]
            # Append the name into the list
            names_list.append(name)

    # Remove duplicates
    without_dups = list(set(names_list))
    return without_dups

def name_parser(names):
    new_names_list = []

    for name in names:
        # Find the last instance of a space
        last_index = name.rfind(" ")
        # Grab everything after that space
        last = name[last_index+1:]
        # Grab everything before that space
        first = name[:last_index]
        # Concatenate the string into the desired format
        l_comma_f = last + ", " + first
        # Append the formatted name to a list
        new_names_list.append(l_comma_f)

    return new_names_list


def main():
    faculty = scraper('https://web.archive.org/web/20141107201347/http://catalog.uoregon.edu/arts_sciences/africanstudies/')
    names = get_name(faculty)
    ready_to_compare = name_parser(names)
    print(ready_to_compare)
    return ready_to_compare

# This calls the 'main' function when this script is executed
if __name__ == "__main__":
    main()