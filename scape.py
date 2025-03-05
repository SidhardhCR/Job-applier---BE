from fastapi import FastAPI
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

app = FastAPI()


def scrape_jobs():
    # Configure Selenium WebDriver
    options = Options()
    options.add_argument("--headless")  # Run in headless mode
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)

    url = "http://localhost:5173/"
    driver.get(url)

    jobs = []
    job_elements = driver.find_elements(By.CLASS_NAME, "job-card")

    if not job_elements:
        print("No job elements found!")
        driver.quit()
        return []

    print("job", job_elements)

    for job in job_elements:
        print("Extracting job:", job.text)
        print("------------------------------")

        title = job.find_element(By.TAG_NAME, "h2").text

        p_tags = job.find_elements(By.TAG_NAME, "p")
        company = p_tags[0].text if len(p_tags) > 0 else ""
        skills = p_tags[1].text if len(p_tags) > 1 else ""
        description = p_tags[2].text if len(p_tags) > 2 else ""

        jobs.append({
            "title": title,
            "company": company,
            "skills": skills,
            "description": description
        })

    driver.quit()
    return jobs


@app.get("/scrape-jobs")
def get_scraped_jobs():
    return {"jobs": scrape_jobs()}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
