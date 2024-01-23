library(ggplot2)
library(dplyr)
library(tidyverse)

# Assuming data_S2 is your dataset
# Replace 'data_S2' with your actual dataset name

# Using data_S2, please produce a facet donut-plot showing the percentage of 
# Spanish-born and foreign-born population living in each region (COM) of Spain
# in 2016. 
# Save your plot as an image.
# Calculate the total population and the foreign-born population

# Order the regions
# Load the package
library(dplyr)

# Order the regions
data_donut <- data %>%
  filter(YEAR == 2016) %>%
  group_by(COM) %>%
  summarise(
    spanish_born = sum(POP_SPANISH),
    foreign_born = sum(POP_LATINAMERICA + POP_WESTERNEUROPE + POP_EASTERNEUROPE + POP_AFRICA + POP_ASIA + POP_OTHERS)
  ) %>%
  mutate(
    total = spanish_born + foreign_born,
    pct_spanish_born = spanish_born / total * 100,
    pct_foreign_born = (foreign_born / total) * 100
  ) %>%
  pivot_longer(c(pct_spanish_born,
                 pct_foreign_born),
               names_to = "GROUP",
               values_to = "SHARE") %>%
  mutate(PCT_FOREIGN_ORDER = row_number(),
         ORDER = ifelse(GROUP == "pct_foreign_born", PCT_FOREIGN_ORDER, NA)) %>%
  arrange(COM, desc(ORDER), SHARE) |>
  select(COM, GROUP, SHARE, PCT_FOREIGN_ORDER) |>
  group_by(COM) |>
  mutate(ymax = cumsum(SHARE),
         ymin = c(0, head(ymax, n = -1)),
         labelPosition = (ymax + ymin) / 2)

# Create the plot
data_donut <- data_donut %>%
  mutate(GROUP = case_when(
    GROUP == "pct_foreign_born" ~ "Foreign born",
    GROUP == "pct_spanish_born" ~ "Spanish born",
    TRUE ~ GROUP
  ))
data_donut_sum <- data_donut %>%
  dplyr::filter(GROUP == "foreign") %>%
  dplyr::group_by(COM) %>%
  dplyr::summarise(SHARE_sum = sum(SHARE, na.rm = TRUE))

# Arrange COM in data_donut by SHARE_sum in data_donut_sum
data_donut$COM <- factor(data_donut$COM, levels = data_donut_sum$COM[order(data_donut_sum$SHARE_sum)])

ggplot(data_donut, aes(ymax = ymax, 
                       ymin = ymin, 
                       xmax = 0.3, 
                       xmin = 1, 
                       fill = GROUP)) +
  geom_rect(color = "black") +
  coord_polar(theta = "y") +
  facet_wrap(~ COM) + 
  xlim(c(-2, 1)) +
  geom_text(x = 1.55, 
            aes(y = labelPosition, 
                label = round(SHARE, 2), 
                color = GROUP), 
            size = 4) +  # Increase font size for cities
  theme_void() +
  theme(strip.text = element_text(face = "bold", size = 14),  # Make font of cities larger
        legend.text = element_text(size = 12),  # Make font of legend larger
        legend.title = element_blank()) + 
  ggtitle("Population by place of birth (%), Spain yearofdata") +  # Add title
  theme(legend.position = c(0.8, 0.05),  # Adjust these values to place the legend
        legend.justification = c(1, 0))  # Adjust legend justification

ggsave("task(2).1donut_plot.png", width = 10, height = 8)
