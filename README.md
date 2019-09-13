# ComicBook
Web crawler that scraps comicbook data from another website.
# Description
- This script will create folders and subfolders by following Comicbooks and its chapters
# Requirments
- Python 3.x
# Instructions
- Installing libraries

    >pip install requests

    >pip install BeautifulSoup4

    >pip install selenium

- Download ChromeDriver - https://chromedriver.chromium.org/
- Replace your ChromeDriver path in 5th line.
    >driver = webdriver.Chrome(r'C:\Users\iis.B201-55\Desktop\chromedriver')
- Relace your local path in 36th line.

    >os.mkdir('E:/temp/' + folder_name)
