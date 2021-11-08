from covergy.html_parser import HtmlParser
def main():
    name = input('Enter your name: ')
    # company_name = input('Enter the company name: ')
    # skills = input('Enter your skills separated by coma : ').split(',')
    parser = HtmlParser()
    print(parser.generate(name = name))
   

def generate_text(name, company_name, skills,position):
    text = f" Dear Sir/Madame , I was excited to learn about the {position} position with {company_name} posted on LinkedIn and would greatly appreciate your consideration of my placement in this role. Having reviewed the position requirements, which closely align with my qualifications, I believe that I will be a valuable contributor to your organisation's goals. While at university, I spent time building my {skills[0]} and {skills[1]}. I am focused and diligent when managing workloads and prioritising tasks to meet deadlines. I thrive in environments where I am able to make a direct impact using my web development   skills and complex problem solving to find solutions and achieve results. My academic experience has greatly contributed to the development of my critical thinking, teamwork and innovation skills. I excel at communicating both clearly and professionally with colleagues, management and customers. I look forward to speaking to you further and to providing you with details of my background and the qualities that I believe will be an asset to the company’s goals. Please take a moment to review the enclosed CV. Thank you for your time and consideration. Yours sincerely, Martin Yanchev "
    return text

if __name__ == "__main__":
    main()


