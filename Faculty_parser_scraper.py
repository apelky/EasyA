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

def initalize_soup(url):
    site = r.get(url)
    soup = bs(site.content, 'html.parser')
    return soup

def get_link(html):
    link = html.find('a')
    #print(link)
    link = link['href']
    link = 'https://web.archive.org'+link
    return link

def explore_catalog(url):
    soup = initalize_soup(url)
    school_link = []
    # optimize by looking through only the section we need
    div = soup.find('div', attrs={'id':'cl-menu'})
    cut_down = div.select('li', attrs={'class':'separator'}) 
    cut_down = cut_down[7:15]
    for school in cut_down:
        link = get_link(school)
        #print(link)
        school_link.append(link)
    return school_link

def explore_school(url):
    soup = initalize_soup(url)
    course_links = []
    faculty_list = []
    
    ul = soup.find('ul', attrs={'class': 'nav'})
    #print(ul)
    if ul != None:
        ul = ul.select('li')
        #print(ul)
        for url in ul:
            #print(url)
            link = get_link(url)
            course_links.append(link)
    else:
        # send ul straight to scraper
        faculty = scraper(soup)
        faculty.append(faculty_list)

    return course_links, faculty_list


def scraper(url):

    soup = initalize_soup(url)

    #print(soup)
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
    # the only link you need to provide is the course catalog page
    faculty_list = []
    school_links = explore_catalog('https://web.archive.org/web/20141124084353/http://catalog.uoregon.edu/')
    courses, faculty = explore_school(school_links[0])
    print(courses)

    '''for school in school_links:
        print(school)
        courses, faculty = explore_school(school)
        faculty_list.extend(faculty)
        #for course in courses:
            #more_faculty = scraper(course)
            #faculty_list.extend(more_faculty)
    print(courses)
    print('------------------------------------------------------------------------')
    print(faculty_list)
    #print(school_links)

    '''
    #names = get_name(faculty)
    #ready_to_compare = name_parser(names)
    #print(ready_to_compare)
    #return ready_to_compare

# This calls the 'main' function when this script is executed
if __name__ == "__main__":
    main()