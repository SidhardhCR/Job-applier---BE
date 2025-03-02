from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


def scrape_jobs():
    # # Configure Selenium WebDriver
    # options = Options()
    # options.add_argument("--headless")  # Run in headless mode
    # options.add_argument("--disable-gpu")
    # options.add_argument("--no-sandbox")

    # service = Service(ChromeDriverManager().install())
    # driver = webdriver.Chrome(service=service, options=options)

    # url = "http://localhost:5174/"
    # driver.get(url)

    # jobs = []
    # job_elements = driver.find_elements(By.CLASS_NAME, "job-card")

    # if not job_elements:
    #     print("No job elements found!")
    #     driver.quit()
    #     return []

    # print("job", job_elements)

    # for job in job_elements:
    #     print("Extracting job:", job.text)
    #     print("------------------------------")

    #     title = job.find_element(By.TAG_NAME, "h2").text

    #     p_tags = job.find_elements(By.TAG_NAME, "p")
    #     company = p_tags[0].text if len(p_tags) > 0 else ""
    #     skills = p_tags[1].text if len(p_tags) > 1 else ""
    #     description = p_tags[2].text if len(p_tags) > 2 else ""

    #     jobs.append({
    #         "title": title,
    #         "company": company,
    #         "skills": skills,
    #         "description": description
    #     })

    # driver.quit()
    testdata  = {"jobs":[
        {"jobId":"FE121","title":"Frontend Developer","company":"TechCorp - Remote","skills":"React, Tailwind CSS","description":"Looking for a React and Tailwind CSS developer."},
        {"jobId":"FE122","title":"Backend Developer","company":"InnovateX - New York, USA","skills":"Node.js, MongoDB","description":"Node.js and MongoDB experience required."},
        {"jobId":"FE123","title":"Full Stack Developer","company":"CodeWorks - San Francisco, USA","skills":"React, Node.js, AWS","description":"React, Node.js, and AWS knowledge preferred."},
        {"jobId":"FE124","title":"UI/UX Designer","company":"DesignStudio - London, UK","skills":"Figma, Adobe XD","description":"Figma and Adobe XD experience required."},
        {"jobId":"FE125","title":"Product Manager","company":"TechSoft - Berlin, Germany","skills":"Product Management, Agile","description":"Product Management and Agile experience required."},
        {"jobId":"FE126","title":"DevOps Engineer","company":"DevOpsPro - Paris, France","skills":"Docker, Kubernetes","description":"Docker and Kubernetes experience required."}]}
    return testdata