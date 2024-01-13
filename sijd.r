# Load necessary libraries
library(ggplot2)
library(dplyr)

# Read the data

setwd("C:\\Users\\levan\\Downloads\\data_ass4.xlsx")

# Read the Excel file
# You mentioned the file is an Excel file, so use read_excel instead of read.csv
data <- read.csv("data_ass4.csv")
colors <- c("Canada" = "red", "France" = "blue", "Germany" = "green", "Italy" = "purple", 
            "Japan" = "orange", "United Kingdom" = "brown", "United States" = "black")
# Filter data for G7 countries and the years 1947 to 2007
g7_countries <- c("Canada", "France", "Germany", "Italy", "Japan", "United Kingdom", "United States")
data_g7 <- data %>%
  filter(Entity %in% g7_countries & Year >= 1947 & Year <= 2007)
plot <- ggplot(data_g7, aes(x = Year, y = life_expectancy, color = Entity)) +
  geom_line(size = 1) +
  scale_color_manual(values = colors, name = "Country") +
  labs(title = "Life Expectancy in G7 Countries (1947-2007)",
       x = "Year",
       y = "Life Expectancy") +
  scale_x_continuous(breaks = seq(min(data_g7$Year), max(data_g7$Year), by = 10)) +
  scale_y_continuous(breaks = seq(floor(min(data_g7$life_expectancy)), ceiling(max(data_g7$life_expectancy)), by = 2)) +
  theme_minimal() +
  theme(
    plot.title = element_text(hjust = 0.5, face = "bold"),
    legend.position = "bottom",
    legend.box = "horizontal",
    panel.background = element_rect(fill = "white"),
    plot.background = element_rect(fill = "white"),
    axis.text.x = element_text(face = "bold", size = 12),
    axis.text.y = element_text(size = 12)
  ) +
  facet_wrap(~ Entity, scales = "free_y")  # Add this line to create a separate plot for each country

print(plot)
ggsave("life_expectancy_plot7.png", plot = plot, width = 10, height = 6, dpi = 600)
