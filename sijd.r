# Assuming 'data' is your data frame
# Set working directory
setwd("C:\\Users\\levan\\OneDrive\\Documents\\Final project r\\stack-overflow-developer-survey-2023")

# Read the dataset
data <- read.csv("survey_results_public.csv")

# Convert 'YearsCode' and 'ConvertedCompYearly' to numeric
data$YearsCode <- as.numeric(as.character(data$YearsCode))
data$ConvertedCompYearly <- as.numeric(as.character(data$ConvertedCompYearly))

# Remove rows with missing or non-numeric values in either column
data <- data[!is.na(data$YearsCode) & !is.na(data$ConvertedCompYearly), ]

# Remove rows with ConvertedCompYearly after 15000000
data <- data[data$ConvertedCompYearly <= 1000000, ]

# Create scatter plot
scatter_plot <- ggplot(data, aes(x = YearsCode, y = ConvertedCompYearly, color = MainBranch, size = WorkExp)) +
  geom_point(alpha = 0.7) +
  labs(title = 'Scatter Plot of Salary vs. Years of Coding Experience',
       x = 'Years of Coding Experience',
       y = 'Converted Compensation Yearly') +
  theme_minimal() +
  scale_color_manual(values = c("#4C72B0", "#55A868", "#C44E52", "#8172B2", "#CCB974", "#64B5CD", "#EAEAF2")) +
  scale_size_continuous(range = c(1, 5)) +
  scale_y_continuous(labels = scales::comma, limits = c(0, 1000000), breaks = seq(0, 1000000, by = 100000))

print(scatter_plot)
unique_currencies <- unique(data$Currency)

# Print unique currencies
print(unique_currencies)
