import requests
from bs4 import BeautifulSoup

def scrape_wikipedia(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    name_element = soup.find('span', {'class': 'mw-page-title-main'})
    if name_element is not None:
        name = name_element.string
    else:
        name = None

    mother_name_th_element = soup.find('th', class_='infobox-label', string="Mother")
    mother_name_th_element2 = soup.find('th', class_='infobox-label', string="Parents")
    if mother_name_th_element is not None:
        print("1 is not none")
        next_sibling = mother_name_th_element.find_next_sibling()
        print(next_sibling.name)
        if next_sibling.name == 'a':
            mother_name = next_sibling.string
        elif next_sibling.name == 'td':
            print("td it is")
            mother_name = next_sibling.string
    elif mother_name_th_element2 is not None:
        print("2 is not none")
        mother_name = None
        if mother_name_th_element2:
            mother_list = mother_name_th_element2.find_next('ul')
            mother_list_items = mother_list.find_all('li')

            for item in mother_list_items:
                if "(mother)" in item.text:
                    anchor_tag = item.find('a')
                    if anchor_tag:
                        mother_name = anchor_tag.string
                    else:
                        mother_name = item.string
                else:
                    mother_name_element = mother_name_th_element2.find_next_sibling('td')
                    if mother_name_element is not None:
                        mother_name_element_br = mother_name_element.find_next_sibling('br')
                        if mother_name_element_br is not None:
                            mother_name = mother_name_element_br.strip()
                            
                    else:
                        print("no td_element")
        else:
            mother_name = "Mother Not Listed"


        
    
    mother_link_th_element = soup.find('th', class_='infobox-label', string="Mother")
    if mother_link_th_element is not None:
        mother_link_td_element = mother_link_th_element.find_next_sibling('td')
        if mother_link_td_element: 
            mother_link_a_element = mother_link_td_element.find_next('a')
            if mother_link_a_element:
                mother_link_text = mother_link_a_element['href']  # Get the href attribute
                mother_link = "https://www.wikipedia.org" + mother_link_text
            else:
                print("Mother does no wiki")    
        else:
            mother_link = "No Valid Link"
    else:
        mother_link_th_element = soup.find('th', class_='infobox-label', string="Parents")
        mother_link = None
        if mother_link_th_element:
            mother_list = mother_link_th_element.find_next('ul')
            mother_list_items = mother_list.find_all('li')
            
            for item in mother_list_items:
                if "(mother)" in item.text:
                    print("it found mother")
                    anchor_tag = item.find('a')
                    if anchor_tag:
                        print("it found mother anchor tag")
                        mother_link_text = item.find('a')['href']
                        if mother_link_text is not None:
                            print("mother link not none")
                            mother_link = "https://www.wikipedia.org" + mother_link_text
                            print(mother_link)
                            break
                    else:
                        print("Mother has no Wikipedia page.")
                else:
                    print("its not finding mother")
        else:
            print("Mother has no Wikipedia page")
    


    
    father_link_th_element = soup.find('th', class_='infobox-label', string="Father")
    if father_link_th_element is not None:
        father_link_td_element = father_link_th_element.find_next_sibling('td')
        if father_link_td_element: 
            father_link_a_element = father_link_td_element.find_next('a')
            if father_link_a_element:
                father_link_text = father_link_a_element['href']  
                father_link = "https://www.wikipedia.org" + father_link_text
            else:
                print("Father has no Wikipedia page.")    
        else:
            father_link = "No Valid Link"
    else:
        
        father_link_th_element = soup.find('th', class_='infobox-label', string="Parents")
        father_link = None
        if father_link_th_element:
            
            father_list = father_link_th_element.find_next('ul')
            father_list_items = father_list.find_all('li')
            
            for item in father_list_items:
                if "(father)" in item.text:
                    print("it found father")
                    anchor_tag = item.find('a')
                    if anchor_tag:
                        father_link_text = item.find('a')['href']
                        father_link = "https://www.wikipedia.org" + father_link_text
                        break
                    else:
                        print("Father has no Wikipedia page.")
                        break
        else:
            print("Father Not Listed")

    father_name_th_element = soup.find('th', class_='infobox-label', string="Father")
    if father_name_th_element is not None:
        
        next_sibling = father_name_th_element.find_next_sibling()
        if next_sibling.name == 'a':
            father_name = next_sibling.string.strip()
        else:
            father_name_element = father_name_th_element.find_next_sibling('td')
            if father_name_element is not None:
                father_name = father_name_element.string.strip()
    else:
        father_name_th_element = soup.find('th', class_='infobox-label', string="Parents")
        father_name = None
        if father_name_th_element:
            father_list = father_name_th_element.find_next('ul')
            father_list_items = father_list.find_all('li')
            
            for item in father_list_items:
                if "(father)" in item.text:
                    father_name = item.find('a').text.strip()
                    break
        else:
            father_name = "Father Not Listed"
        

    birth_date_element = soup.find('span', {'class': 'bday'})
    if birth_date_element is not None:
        birth_date = birth_date_element.string
        
    else:
        birth_date = "Not Listed" 


    died_th_element = soup.find('th', class_='infobox-label', string='Died')
    if died_th_element:
        death_date_element = died_th_element.find_next_sibling('td', class_='infobox-data')
        if death_date_element:
            death_date_text = death_date_element.text.strip().split('\n')[0]
            opening_parenthesis = death_date_text.find('(')
            closing_parenthesis = death_date_text.find(')')

        if opening_parenthesis != -1 and closing_parenthesis != -1:
            # Extract the text between parentheses
            death_date = death_date_text[opening_parenthesis + 1: closing_parenthesis]
        else:
            death_date = None
    else:
        death_date = None


    death_age_th_element = soup.find('th', class_='infobox-label', string='Died')
    if death_age_th_element:
        death_age_td_element = death_age_th_element.find_next_sibling('td', class_='infobox-data')
        if death_age_td_element:
            death_age_text = death_age_td_element.text.strip().split('\n')[0]
            
            if death_age_text.find('(aged)') is not None:
                
                opening_and_aged = death_age_text.find('(aged')
                if opening_and_aged is not None:
                    if opening_and_aged != -1:
                        char1 = death_age_text[opening_and_aged + 6]
                        char2 = death_age_text[opening_and_aged + 7]
                        char3 = death_age_text[opening_and_aged + 8]
                        if char3 == ')':
                            age_two_char = char1 + char2
                            death_age = age_two_char
                        else:
                            age_three_char = char1 + char2 + char3
                            death_age = age_three_char 
                    else:
                        death_age = "Unknown"
            else:
                death_age = "Unknown"
    else: 
        death_age = None

    
    return {
        'Name': name,
        'Date of Birth': birth_date,
        'Date of Death': death_date,
        'Age at Death': death_age,
        'Mother': mother_name,
        'Father': father_name,
        'Mother Link': mother_link,
        'Father Link': father_link
        
        
    }

def scrape_parent_info(parent_link):
    return scrape_wikipedia(parent_link)




def main():
    while True:
        
        starting_url = input("Enter a Wikipedia URL (or 'quit' to exit): ")
        
        if starting_url.lower() == 'quit':
            print("Exiting program.")
            return
            
        data = scrape_wikipedia(starting_url)
        
        
        while True:
            print({key: value for key, value in data.items() if key not in ['Mother Link', 'Father Link']})

            scrape_parents = input("\nDo you want to look at the mother or father's information? (mother/father): \n" )
            

            if scrape_parents.lower() == 'quit':
                break
            elif scrape_parents.lower() == 'mother':
                mother_link = data.get('Mother Link')
                if mother_link:
                    mother_data = scrape_wikipedia(mother_link)
                    #print({key: value for key, value in mother_data.items() if key not in ['Mother Link', 'Father Link']})
                    data = mother_data
                else:
                    print("Mother info not available. :(")
            elif scrape_parents.lower() == 'father':
                father_link = data.get('Father Link')
                if father_link:
                    father_data = scrape_wikipedia(father_link)
                    #print({key: value for key, value in father_data.items() if key not in ['Father Link', 'Mother Link']})
                    data = father_data
                else:
                    print("Father info not available :(")
            else:
                print("Invalid Input")


 

if __name__ == "__main__":

    main()