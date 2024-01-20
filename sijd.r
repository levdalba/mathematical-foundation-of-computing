# Read countries.csv and e0M.csv into R
# Use the countries in countries.csv to filter e0M
# Produce a joy plot (ridges) setting the time interval on the y-axis and the 
# values on the x-axis. Maybe you want to take a look:
# https://cran.r-project.org/web/packages/ggridges/vignettes/introduction.html
# Save your plot as an image.


library(ggridges)
library(dplyr)
library(tidyr)

## EX 2: JOYPLOTS ########
# Read countries.csv and e0M.csv into R
# Use the countries in countries.csv to filter e0M
# Produce a joy plot (ridges) setting the time interval on the y-axis and the 
# values on the x-axis. Maybe you want to take a look:
# https://cran.r-project.org/web/packages/ggridges/vignettes/introduction.html
# Save your plot as an image.

countries <- read_csv("countries.csv")
eom <- read_csv("e0m.csv")

# Install and load necessary packages if not already installed
if (!requireNamespace("tidyverse", quietly = TRUE)) {
  install.packages("tidyverse")
}

if (!requireNamespace("viridis", quietly = TRUE)) {
  install.packages("viridis")
}

# Load the required packages
library(tidyverse)
library(viridis)

# Read data
countries <- read_csv("countries.csv")
eom <- read_csv("e0m.csv")

# Match countries between the two datasets
merged_data <- merge(countries, eom, by.x = "x", by.y = "country")

# Reshape the data for ggridges
melted_data <- reshape2::melt(merged_data, id.vars = c("x", "country_code"), measure.vars = colnames(eom)[3:(ncol(eom)-1)])
library(ggridges)
melted_data$variable <- factor(melted_data$variable, levels = rev(unique(melted_data$variable)))

# Plot the joy plot with the same style and aesthetics
ggplot(melted_data, aes(x = value, y = variable, fill = after_stat(x))) +
  geom_density_ridges_gradient(scale = 2, 
                               rel_min_height = 0.01,
                               alpha = 0.5, # Adjust alpha to a valid value
                               jittered_points = FALSE) +
  scale_fill_viridis_c(name = "Temp. [C]", option = "B", alpha = 0.5, begin = 0.2, end = 0.8, direction = -1) + # Adjust color scale
  labs(title = 'Global convergence in male life expectancy at birth since 1950',
       subtitle = 'UNPD World Population Prospects 2015 Revision, via wpp2015',
       x = "\n Value",
       y = "Period\n",
       caption = "Levan Dalbashvili") +
  theme_minimal() +
  theme(legend.position = "bottom",
        legend.key.width = unit(6, "cm"))