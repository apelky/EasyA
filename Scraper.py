'''
Scraper.py created by Angela Pelky on Thursday Feb 3, 2023.

Group 1:
Ethan Aasheim
Melodie Collins
Linnea Gilius
Timothy Nadeau
Angela Pelky

This is a part of the system that implements an update to the Emerald Grade Tracker (EGT).
The original EGT can be found here: 'https://emeraldmediagroup.github.io/grade-data'
The EGT displays the letter-grade distribuition across all professors in a particular department of the natural science at the University 
of Oregon. This system builds upon the original EGT by directly comparing professors in the same department on the same graph, and is only 
concerned with the extreme ends of the letter-grade spectrum.

----------------------------------------

Developer must provide a new url link in the main function if a different website to scrape is desired. 

EasyA.py uses Python 3.10
'''

import requests as r
from bs4 import BeautifulSoup as bs
import time as t 

def initalize_soup(url):
    '''
    Helper function that takes the url and initalizes it for processing 

    Parameters:
        url: string

    Returns:
        soup: parse tree for site data  
    '''
    site = r.get(url, timeout=20)
    soup = bs(site.content, 'html.parser')
    return soup

def get_link(html):
    '''
    Helper function that parses the tree looking for a link to the next relevant webpage

    Parameters:
        html: parse tree

    Returns:
        link: string
    '''
    # find the first instance of 'a' tag
    link = html.find('a')
    # split that instance to only get the desired link
    link = link['href']
    # add https://web.archive.org to inital part of link since not already included
    link = 'https://web.archive.org'+link
    #print(link)
    return link

def explore_catalog(url):
    '''
    Helper function that parses the course webpage and finds relevant schools to extract faculty data from

    Parameters:
        url: string

    Returns:
        school link: list of links (string) to specific school webpage 
    '''
    soup = initalize_soup(url)
    # list of schools 
    # ex: 'College of Arts and Sciences'
    school_link = []
    # optimize by looking through only the section we need
    div = soup.find('div', attrs={'id':'cl-menu'})
    cut_down = div.select('li', attrs={'class':'separator'}) 
    # find the schools, specifically 
    cut_down = cut_down[7:15]
    for school in cut_down:
        link = get_link(school)
        school_link.append(link)
    return school_link

def explore_school(url):
    '''
    Helper function that parses a specific school's webpage and finds relevant majors to extract faculty data from

    Parameters:
        url: string

    Returns:
        course_links: a list of links (string) to specific major webpage 
        faculty_list: a list of faculty (string)
    '''
    # first we want to scrape the school's homepage to find faculty
    faculty_list = scraper(url)
    course_links = []
    # if no faculty was found on the homepage, extract major webpage
    if faculty_list == None:
        soup = initalize_soup(url)
        faculty_list = []

        ul = soup.find('ul', attrs={'class': 'nav'})
        if ul != None:
            ul = ul.select('li')
            for url in ul:
                link = get_link(url)
                course_links.append(link)

    return course_links, faculty_list


def scraper(url):
    '''
    Helper function that scrapes a page to find faculty data

    Parameters:
        url: string

    Returns:
        faculty: a list of faculty (string)
    '''

    soup = initalize_soup(url)
    faculty = []

    # optimize by looking through only the container we need
    container = soup.find('div', attrs={'id':'facultytextcontainer'})
    if container != None:
        # for some reason the first faculty member is not part of the same class - this takes care of that
        first_faculty = container.find('p')
        # get all faculty
        faculty = container.find_all('p', attrs={'class':'facultylist'})
        faculty.extend(first_faculty)
    else:
        return None

    return faculty

def main():
    '''
    Main function that initalizes the program and writes scaped data to a file that needs to be parsed.

    Parameters:
        None

    Returns:
        None
    '''
    # the only link you need to provide is the course catalog page
    faculty_list = []
    school_links = explore_catalog('https://web.archive.org/web/20141124084353/http://catalog.uoregon.edu/')

    for school in school_links:
        courses, faculty = explore_school(school)
        if faculty != None:
            faculty_list.extend(faculty)
        for course in courses:
            # we want to continue trying to access the site until it is is successful 
            while True:
                try:
                    more_faculty = scraper(course)
                    if more_faculty != None:
                        faculty_list.extend(more_faculty)
                # list of potential exceptions that could be crashing the program
                except (r.exceptions.ConnectTimeout, r.exceptions.Timeout, r.exceptions.ConnectionError):
                    print("Timeout Occured")
                    continue
                break
    
    # write data to a .txt file so scraper doesn't have to run every time
    with open('Regular_Faculty.txt', 'w') as f:
        for line in faculty_list:
            f.write(f"{line}\n")

# This calls the 'main' function when this script is executed
if __name__ == "__main__":
    main()