# Load necessary library
library(sf)

setwd("C:\\Users\\levan\\OneDrive\\Documents\\Final project r")

# Define the file paths
birth <- "C:/Users/levan/OneDrive/Documents/Final project r/crude-birth-rate.csv"
life_expectancy <- "C:/Users/levan/OneDrive/Documents/Final project r/life-expectancy.csv"

# Read the CSV files
birth_data <- read.csv(birth)

life_expectancy_data <- read.csv(life_expectancy)
birth_data$Entity <- trimws(birth_data$Entity)

# Remove '(UN)' and any additional spaces from 'Entity' column in 'birth_data'
birth_data$Entity <- gsub("\\s*\\(UN\\)\\s*", "", birth_data$Entity)






birth_data <- subset(birth_data, select = -Code)

# Remove 'Code' column from 'life_expectancy_data' data frame
life_expectancy_data <- subset(life_expectancy_data, select = -Code)

# Now you can merge the data frames
# Now you can merge the data frames
merged_data <- merge(birth_data, life_expectancy_data, by = c("Entity", "Year"), all = TRUE)

merged_data <- subset(merged_data, Year >= 1950 & Year <= 2021)

# Define the entities to keep
entities_to_keep <- c("Africa", "Asia", "Europe", "Latin America and the Caribbean", "Northern America", "Oceania","High-income countries", "Low-income countries",  "Less developed regions", "More developed regions")

# Keep only the specified entities in 'merged_data'
merged_data <- subset(merged_data, Entity %in% entities_to_keep)

# Load necessary libraries
library(reshape2)
library(ggplot2)

# Reshape the data to a long format
long_data <- melt(merged_data, id.vars = c("Entity", "Year"), variable.name = "Variable", value.name = "Value")

# Create line graph for both variables
# Load necessary library
library(sf)

setwd("C:\\Users\\levan\\OneDrive\\Documents\\Final project r")

# Define the file paths
birth <- "C:/Users/levan/OneDrive/Documents/Final project r/crude-birth-rate.csv"
life_expectancy <- "C:/Users/levan/OneDrive/Documents/Final project r/life-expectancy.csv"

# Read the CSV files
birth_data <- read.csv(birth)

life_expectancy_data <- read.csv(life_expectancy)
birth_data$Entity <- trimws(birth_data$Entity)

# Remove '(UN)' and any additional spaces from 'Entity' column in 'birth_data'
birth_data$Entity <- gsub("\\s*\\(UN\\)\\s*", "", birth_data$Entity)






birth_data <- subset(birth_data, select = -Code)

# Remove 'Code' column from 'life_expectancy_data' data frame
life_expectancy_data <- subset(life_expectancy_data, select = -Code)

# Now you can merge the data frames
# Now you can merge the data frames
merged_data <- merge(birth_data, life_expectancy_data, by = c("Entity", "Year"), all = TRUE)

merged_data <- subset(merged_data, Year >= 1950 & Year <= 2021)

# Define the entities to keep
entities_to_keep <- c("Africa", "Asia", "Europe", "Latin America and the Caribbean", "Northern America", "Oceania","High-income countries", "Low-income countries",  "Less developed regions", "More developed regions")

# Keep only the specified entities in 'merged_data'
merged_data <- subset(merged_data, Entity %in% entities_to_keep)

# Load necessary libraries
library(reshape2)
library(ggplot2)

# Reshape the data to a long format
long_data <- melt(merged_data, id.vars = c("Entity", "Year"), variable.name = "Variable", value.name = "Value")

# Create line graph for both variables
# Define the new labels for the facets
facet_labels <- c("Birth.rate...Sex..all...Age..all...Variant..estimates" = "Birth Rate",
                  "Period.life.expectancy.at.birth...Sex..all...Age..0" = "Period Life Expectancy")

# Create line graph for both variables with new facet labels, centered and larger, bolder title
ggplot(long_data, aes(x = Year, y = Value, color = Entity)) +
  geom_line() +
  facet_wrap(~ Variable, scales = "free_y", labeller = as_labeller(facet_labels)) +
  labs(title = "Life Expectancy and Birth Rate Over Time", x = "Year") +
  theme_minimal() +
  theme(plot.title = element_text(hjust = 0.5, size = 14, face = "bold"),
        axis.title = element_text(size = 12, face = "bold"),
        axis.text = element_text(size = 10, face = "bold"),
        strip.text = element_text(size = 12, face = "bold")) +
  scale_x_continuous(breaks = seq(min(long_data$Year), max(long_data$Year), by = 10))
