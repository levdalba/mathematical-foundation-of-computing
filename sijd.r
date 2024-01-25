library(ggplot2)
library(dplyr)
library(stringr)
library(tidyr)
library(forcats)

# Set working directory
setwd("C:\\Users\\levan\\OneDrive\\Documents\\Final project r\\stack-overflow-developer-survey-2023")

data <- read.csv("survey_results_public.csv")

# Remove rows with NA values in the 'LanguageHaveWorkedWith' column
data <- data[!is.na(data$LanguageHaveWorkedWith), ]

# Count occurrences of each programming language
lang_counts <- data %>%
  mutate(LanguageHaveWorkedWith = str_split(LanguageHaveWorkedWith, ";")) %>%
  unnest(c(LanguageHaveWorkedWith)) %>%
  count(LanguageHaveWorkedWith) %>%
  arrange(desc(n))

# Create the bar plot
ggplot(lang_counts, aes(x = n, y = fct_reorder(LanguageHaveWorkedWith, n))) +
  geom_col(fill = 'lightcoral') +
  scale_x_continuous(limits = c(0, 60000), breaks = seq(0, 60000, by = 5000)) +  # Set x-axis range and breaks
  labs(title = 'Top Programming Languages Used by Developers',
       x = 'Number of Developers',
       y = 'Programming Language')