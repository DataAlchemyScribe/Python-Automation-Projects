# This is a website automator python project, 
# which helps to combine various webpages which I need at a particular time for certain tasks

import sys
import webbrowser

url_links = {
    "START2024" : ["https://eclass.iirs.gov.in/login", "https://www.youtube.com/@iirsoutreachdehradun/streams"],
    "ARMeta" : ["https://spark.meta.com/", "https://docs.google.com/document/d/1Elwe-ZKJ_hFQN40Xmvhrc6ED2B7Pmo_bzfwE_dtVp9g/edit", "https://flaunch.io/index"],
    "Learn" : ["https://www.coursera.org/", "https://www.edx.org/", "https://www.khanacademy.org/", "https://chatgpt.com/"],
    "Clothing" : ["https://www.amazon.in/", "https://www.flipkart.com/", "https://www.myntra.com/", "https://www.ajio.com/", "https://www.shoppersstop.com/", "https://www.thesouledstore.com/men"]
}


# function to call that key-link which contains all the value-links
def start_opening_webpages(url_links):
    for link in url_links:
        webbrowser.open(link)



# this code is written in order to execute" only if this file is run/execute independently, 
# not if it is imported as a module into another file
if __name__ == "__main__":
    key_link = sys.argv[1]
    if key_link in url_links:
        start_opening_webpages(url_links[key_link])
    else:
        print("Invalid key-link or Incorrect command!\nPlease re-type the command!\n")


