#!/bin/bash

# Navigate to the Scrapy project directory
cd C:\Users\barat\OneDrive\Desktop\webdev\hirehub\backend\crawler


source $(poetry env info --path)/bin/activate
# Run the Scrapy spider
scrapy crawl ipospider -o output_$(date +\%Y\%m\%d\%H\%M\%S).csv