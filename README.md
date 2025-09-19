# overview 

The dataset contains **785,741 job postings** with **17 columns** covering job titles, locations, posting dates, company names, skills, and limited salary information. It includes categorical variables (e.g., job title, location, company), boolean flags (remote work, degree requirement, health insurance), numeric fields (average annual and hourly salaries), and a datetime column for posting dates.

Most columns are nearly complete, but some have significant missing values: salary information is sparse (`salary_rate` \~4%, `salary_year_avg` \~2.8%, `salary_hour_avg` \~1.3%), and skills are available for \~85% of postings.

The dataset is well suited for analyzing **job market trends, in-demand skills, geographic distribution, and remote work patterns**, but less reliable for detailed salary benchmarking due to missing data.

# The Questions 

Below are the questions I will answer in my project.

1.  What are the most demanded skills for the top 3 most popular data roles?
2.  How are in-demand skills trending for Data Analysts?
3.  How well do jobs and skills pay for Data Analysts?
4.  What is the most optimal skill to learn for Data Analysts? (High Demand & High Paying)

# The Tools I used  

- python: Is the main tool I used to clean, filter, analyze, visualize the data provided 
  - pandas: The library I used to analyze the data.
  - marplotlib: The library I used to visualize the data provided.
  - seaborn: The library that provides more advanced visuals.

- jupyter notebook: The notebook I used to run my codes easily.
- VS code: My go-to for executing my python scripts
- Git and Githup: Essintial in sharing my analysis, insuring collaboration.

# Data preparation and clean up 

 - Import data and clean up
   - Here I have cleand and filterd my data 

### Cleanup:

```
import ast 
import numpy as np
import pandas as pd
from datasets import load_dataset
import matplotlib.pyplot as plt
import seaborn as sns

# Loading Data
dataset = load_dataset('lukebarousse/data_jobs')
df = dataset['train'].to_pandas()

# data cleanup
df['job_posted_date']=pd.to_datetime(df['job_posted_date'])
df['job_skills']=df['job_skills'].apply(lambda x: ast.literal_eval(x) if pd.notna(x) else x)
```
### Filtering:
Here I have filtered only the data taken from Egypt only.

```df_Egy= df[df['job_country']=='Egypt']```

# The Analysis
## 1.What are the most demanded skills for the top 3 most popular data roles?

The analysis focused on job postings in Egypt extracted from the larger global dataset. The data was filtered to include only Egyptian postings and the skills associated with each role were expanded so that individual skills could be counted. The dataset was then grouped by job title and skill to identify the most frequently requested skills for different positions. For visualization, the top three job titles—Data Analyst, Data Engineer, and Data Scientist—were selected, and the top five skills within each category were plotted to highlight both absolute counts and relative percentages.

View my notebook in details here:
[2_skills_count.ipynb](3_project/2_skills_count.ipynb)

### Visualize data 
```
fig, ax= plt.subplots(len(job_titles),1)



for i, job_title in enumerate(job_titles):
    df_plot=df_skills_count[df_skills_count['job_title_short'] == job_title].head()
    sns.barplot(data=df_plot, x='skills_count',y='job_skills',palette='mako',ax=ax[i])
    ax[i].set_ylabel(job_title)
    ax[i].set_xlim(0, 250)
     
     # Calculate percentages
    total = df_plot['skills_count'].sum()
    df_plot['percentage'] = df_plot['skills_count'] / total * 100

        # Annotate each bar with percentage
    for p, perc in zip(ax[i].patches, df_plot['percentage']):
        width = p.get_width()
        ax[i].text(
            width + 0.5,                      # position (a bit to the right of bar)
            p.get_y() + p.get_height() / 2,   # center of the bar
            f'{perc:.1f}%',                   # format the percentage
            va='center'
        )

plt.tight_layout()
sns.despine()
```

### Results
![visualization](3_project/outputs/2_skills_count_output.png)

### Insights

The results show that Python and SQL are the two most consistently demanded skills across all three roles, forming the foundation of data-related jobs in Egypt.

- Data Analysts primarily rely on SQL, Excel, and visualization tools (Tableau, Power BI), with Python also playing a significant role.

- Data Engineers emphasize Python and SQL, but also require big data tools (Spark, Kafka) and cloud technologies (AWS).

- Data Scientists demonstrate the strongest reliance on Python and SQL, with Tableau and R adding value for statistical and visualization tasks, and Spark appearing for large-scale data processing.

Overall, the Egyptian job market highlights a strong demand for core programming and database skills while differentiating between roles through specialized requirements: visualization and business tools for Analysts, big data and cloud infrastructure for Engineers, and a combination of statistical methods and large-scale processing for Scientists.

## 2.How are in-demand skills trending for Data Analysts?

I transformed the data by breaking job skills into separate rows, counting how often each skill appeared per month, ranking them by total demand, and converting month numbers to names. Then I calculated the percentage demand of each skill per month and visualized the top 3 skills (SQL, Python, Excel) in a line chart with markers, percentages on the y-axis, and clear labels to show their monthly trends.

View my notebook in details here:
[3_skills_trend.ipynb](3_project/3_skills_trend.ipynb)

### Visualize data 

```
df_plot= df_DA_Egy_persent.iloc[:, :3]

sns.lineplot(data=df_plot, dashes=False, palette='mako',marker='o', markersize=6)
sns.despine()

plt.title('Trending job skills in Egypt per month')
plt.xlabel('2023')
plt.ylabel('Demanded persentage skills')
plt.legend().remove()

from matplotlib.ticker import PercentFormatter
ax= plt.gca()
ax.yaxis.set_major_formatter(PercentFormatter(decimals=0))

for i in range(3):
    plt.text(11.25, df_plot.iloc[-1, i], df_plot.columns[i])
```

### Results
![visualization](3_project/outputs/3_skills_trend_output.png)

### Insights

* **SQL**
  SQL is consistently the **most in-demand skill** for Data Analysts in Egypt. It peaks above **45% in April and July**, showing strong reliance on database querying skills. Despite fluctuations, SQL remains the top requirement across the year.

* **Python**
  Python demand shows more **volatility** but nearly **matches SQL in July and December**. This suggests Python is increasingly critical for analytical and automation tasks, and employers are seeking candidates with advanced programming capabilities alongside SQL.

* **Excel**
  Excel demonstrates **steady but lower demand** compared to SQL and Python, averaging **20–35%**. Its dip around September followed by recovery toward the year’s end shows it is still a **foundational tool**, but less central than SQL and Python for analyst roles.

