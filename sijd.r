setwd("C:\\Users\\levan\\OneDrive\\Documents\\Final project r\\stack-overflow-developer-survey-2023")

data <- read.csv("survey_results_public.csv")

# Load necessary libraries
library(dplyr)
library(readr)

# Read the data from a CSV file
df <- data

# Calculate the number and percentage of respondents who used each learning resource
df_summary <- df %>%
  group_by(LearningResource) %>%
  summarise(Responses = n(), .groups = 'drop') %>%
  mutate(Percentage = Responses / sum(Responses) * 100)

# Print the summary
print(df_summary)