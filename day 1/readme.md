# Day 1

Day 1 focuses on ChatGPT for data analytics use cases that can be done with or inside the ChatGPT app. No technical knowledge required!

The whole day will cover this case study: [Case Study Elegant Homes UK](https://github.com/tobiaszwingmann/chatgpt-for-data-analytics-bootcamp/blob/main/day%201/Case%20Study%20Elegant%20Homes%20UK.pdf)

**BIG WARNING!** None of these use cases will always give 100% accurate results. In fact, for some use cases, a 100% accurate result doesn't even exist. That's why we call these scenarios **Augmented AI Use Cases**. AI helps you, but you have to make the final decision. We'll talk more about this in the course.

---

## Data Analysis Frameworks
### Use Case 1: Problem Statements
- [Smart Problem GPT](https://chatgpt.com/g/g-tHZOlUaYD-smart-problem-gpt)
- [GPT Config](https://github.com/tobiaszwingmann/chatgpt-for-data-analytics-bootcamp/blob/main/day%201/gpt-configs/01_smart-problem-gpt.md)
- [Chat example](https://chatgpt.com/share/68a04842-8f28-800b-b1b8-47fe2ba648bc)

### Use Case 2: Issue Trees
- [Issue Tree GPT](https://chatgpt.com/g/g-qaKT45vrL-issue-tree-gpt)
- [GPT Config](https://github.com/tobiaszwingmann/chatgpt-for-data-analytics-bootcamp/blob/main/day%201/gpt-configs/02_issue-tree-gpt.md)
- [Chat example](https://chatgpt.com/share/6a324610-abdc-83eb-b8a8-65081d96a9d0)

### Use Case 3: Root Cause Analysis
- [RCA GPT](https://chatgpt.com/g/g-68a595214cdc8191885d097cdd8243d2-rca-gpt)
- [GPT Config](https://github.com/tobiaszwingmann/chatgpt-for-data-analytics-bootcamp/blob/main/day%201/gpt-configs/03_rca-gpt.md)
- [Chat example](https://chatgpt.com/share/68a59710-69e0-800b-8428-847b2ad415f0)

### Use Case 4: Data Storytelling
- [Data Story GPT](https://chatgpt.com/g/g-68a5979657f88191bf8edb5aa6c632e4-data-storytelling-gpt)
- [GPT Config](https://github.com/tobiaszwingmann/chatgpt-for-data-analytics-bootcamp/blob/main/day%201/gpt-configs/04_data-storytelling-gpt.md)
- [Chat example](https://chatgpt.com/share/68a59c59-2820-800b-9c7b-bc4f69a3da26)
- Artifacts: [PowerPoint](https://github.com/tobiaszwingmann/chatgpt-for-data-analytics-bootcamp/blob/main/day%201/artifacts/Elegant_Homes_Segmentation_Presentation.pptx)

---

## Fast Data Analysis inside ChatGPT

### Use Case 5: Tidy data analysis

#### Naive data analysis
- [Data](https://github.com/tobiaszwingmann/chatgpt-for-data-analytics-bootcamp/blob/main/data/consolidated_customer_report.xlsx)
- [Chat example: Naive analysis](https://chatgpt.com/share/6a32688b-5c90-83eb-82ec-0645ebc88e63)
  - **Prompt**: `Compare revenue by quarter national vs. international in a table`
  - **Check**: National/International? Hidden columns? Currency?
  - How much code was written for this?
 
#### Tidy data preparation
- [Data](https://github.com/tobiaszwingmann/chatgpt-for-data-analytics-bootcamp/blob/main/data/consolidated_customer_report.xlsx)
- [Tidy Data GPT](https://chatgpt.com/g/g-69b7fd4c7d08819199164820f9c4e867-tidy-data-gpt)
- [GPT Config](https://github.com/tobiaszwingmann/chatgpt-for-data-analytics-bootcamp/blob/main/day%201/gpt-configs/05_tidy_data_gpt.md)
  - Artifacts: [Python script](https://github.com/tobiaszwingmann/chatgpt-for-data-analytics-bootcamp/blob/main/day%201/artifacts/create_customer_quarterly_tidy.py)
  - Chat example: [Tidy data prep](https://chatgpt.com/share/6a327256-d670-83eb-843e-0ae28ad94170)
- **Bonus:** [Multiple files chat examples](https://chatgpt.com/share/69b80eea-d5e0-800b-8845-c2eff6992636)

#### Tidy data analysis
- [Tidy Data](https://github.com/tobiaszwingmann/chatgpt-for-data-analytics-bootcamp/blob/main/data/customer_quarterly_tidy.csv)
  - **Prompt**: `Compare revenue by quarter national vs. international in a table`
  - **Check**: National/International? Hidden columns? Currency?
  - How much code was written for this?
- Chat example: [Tidy data analysis](https://chatgpt.com/share/6a326921-7d28-83eb-903a-c774b34f1b1c)
- **Bonus:**
  - [Visual Data Analysis GPT](https://chatgpt.com/g/g-69b8055886088191a795e914c9345204-visual-data-analysis-gpt) | [Config](https://github.com/tobiaszwingmann/chatgpt-for-data-analytics-bootcamp/blob/main/day%201/gpt-configs/05_visual_data_analysis_gpt.md)
  - [Chat example](https://chatgpt.com/share/69b807e7-cd5c-800b-8520-ee4e2c35e7ab)

### Transactional Data

### Use Case 6: Data Quality
- [Transactional Data](https://github.com/tobiaszwingmann/chatgpt-for-data-analytics-bootcamp/blob/main/data/tidy_invoice_lines.csv)
- [Data Quality GPT](https://chatgpt.com/g/g-69b80a23cfcc8191ae2b92f3bdceac13-data-quality-gpt) | [Config](https://github.com/tobiaszwingmann/chatgpt-for-data-analytics-bootcamp/blob/main/day%201/gpt-configs/06_data_quality_gpt.md)
- [Chat example](https://chatgpt.com/share/69b813b7-72f8-800b-ad50-5f13cfd56f94)

### Use Case 7: Advanced Data Analysis
- Data: [Cleaned Transactional Data](https://github.com/tobiaszwingmann/chatgpt-for-data-analytics-bootcamp/blob/main/data/tidy_invoice_lines.csv)
- [Advanced Data Analysis GPT](https://chatgpt.com/g/g-69b817d7ee388191849934eb899abd4c-advanced-data-analysis-gpt) | [GPT Config](https://github.com/tobiaszwingmann/chatgpt-for-data-analytics-bootcamp/blob/main/day%201/gpt-configs/07_advanced_data_analysis_gpt.md)
- [Chat example](https://chatgpt.com/share/69b81ba5-0724-800b-85ba-ac2e956271ef)

### Use Case 8: Forecasting
- [B2B/B2C Data](https://github.com/tobiaszwingmann/chatgpt-for-data-analytics-bootcamp/blob/main/data/customer_b2b_b2c_proxy_segments.csv) and [Cleaned Transactional Data](https://github.com/tobiaszwingmann/chatgpt-for-data-analytics-bootcamp/blob/main/data/tidy_invoice_lines.csv) 
- [Forecasting GPT](https://chatgpt.com/g/g-68a4c571de948191949d40f3b67cbcc8-forecasting-gpt) | [GPT Config](https://github.com/tobiaszwingmann/chatgpt-for-data-analytics-bootcamp/blob/main/day%201/gpt-configs/08_forecasting_gpt.md)
- [Chat example](https://chatgpt.com/share/69b821d9-7be4-800b-a684-1dbbbc395c81)

