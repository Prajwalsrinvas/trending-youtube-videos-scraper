# Trending YouTube Videos Scraper
Scrape trending videos on YouTube using Selenium and AWS Lambda!

- Web scraping is a great way to extract public information from websites and create datasets for data analysis and machine learning. 
- Through [this workshop](https://www.youtube.com/watch?v=FcW-AXsirBE), I understood the process of building and deploying a web scraping project from scratch using Python, Selenium, and AWS Lambda. 

# Objective
1. Scrape top 10 trending videos on YouTube using Selenium
2. Set up a recurring job on AWS Lambda to scrape every 30 minutes
3. Send the results as a CSV attachment over email (or to a spreadsheet)

# Topics Covered
* GitHub
* Replit
* Selenium
* AWS Lambda
* SMTP

# Steps

## Step 1 - Create a GitHub repository
* Create a repository at https://github.com/new
* Add README, gitignore (Python) and license 
* (Optional) Clone the repository locally
* References:
    * Introduction to GitHub: https://lab.github.com/githubtraining/introduction-to-github 
    * Git & GitHub tutorial: https://www.youtube.com/watch?v=RGOj5yH7evk 


## Step 2 - Launch the repository on Replit
* Connect Replit with your GitHub account
* Launch the repository as a Replit project
* Set up the language and run command
* Create and execute a Python script
* Attempt to scrape the page using requests & Beautiful Soup
* References:
    * Introduction to Replit: https://docs.replit.com/tutorials/01-introduction-to-the-repl-it-ide 
    * Replit + GitHub: https://docs.replit.com/tutorials/06-github-and-run-button 
    * YouTube trending feed: https://www.youtube.com/feed/trending 
    * Beautiful soup tutorial: https://blog.jovian.ai/web-scraping-using-python-and-beautifulsoup-adf43cbdb816 


## Step 3 - Extract information using Selenium
* Install selenium and create a browser driver
* Load the page and extract information
* Create a CSV of results using Pandas
* References:
    * Selenium tutorial: https://www.browserstack.com/guide/python-selenium-to-run-web-automation-test
    * Pandas tutorial: https://jovian.ai/learn/data-analysis-with-python-zero-to-pandas/lesson/lesson-4-analyzing-tabular-data-with-pandas


## Step 4 - Set up a recurring job on AWS Lambda
* Create an AWS Lambda Python function
* Deploy a sample script and observe the output
* Add layers for Selenium and Chromium
* Set up recurring job using AWS CloudWatch
* References:
    * Python on AWS Lambda tutorial: https://stackify.com/aws-lambda-with-python-a-complete-getting-started-guide 
    * Chromium & Selenium on AWS Lambda: https://dev.to/awscommunity-asean/creating-an-api-that-runs-selenium-via-aws-lambda-3ck3
    * Recurring AWS Lambda functions: https://docs.aws.amazon.com/lambda/latest/dg/services-cloudwatchevents-expressions.html 

## Step 5 - Send results over email using SMTP
* Create email client using smtplib
* Set up SSL, TLS and authenticate with password
* Send a sample email with just text
* Send an email with text and attachment
* References:
    * Sending Email with Python: https://stackabuse.com/how-to-send-emails-with-gmail-using-python/
    * Send email using Python: https://www.geeksforgeeks.org/send-mail-attachment-gmail-account-using-python/
    * Environment variables on Replit: https://docs.replit.com/programming-ide/storing-sensitive-information-environment-variables
    * https://docs.aws.amazon.com/lambda/latest/dg/configuration-envvars.html 
    * Update Google sheets using Python: https://www.analyticsvidhya.com/blog/2020/07/read-and-update-google-spreadsheets-with-python/


## Step 6 - Selenium Lambda Layers:
- https://github.com/aakashns/selenium-aws-lambda-layers
- Reference code: https://gist.github.com/aakashns/5393587e21cff67d399e949b77e008af

# References:
- [Web Scraping from Scratch with Python, Selenium and AWS Lambda](https://www.youtube.com/watch?v=FcW-AXsirBE)  
- [Selenium YouTube Scraper Live](https://github.com/aakashns/selenium-youtube-scraper-live)
