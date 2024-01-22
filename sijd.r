codb_nds <- read_csv("CoDB_NDS.csv")

# Create a new data frame with selected columns and conditions
new_data <- codb_nds %>%
  select(C0, C1, C2, C3, C4, T1, S2, HS01:HS11) %>%
  filter(C3 == "LATIN-AMERICA" & S2 == "IPUMS")

# Convert to long format
new_data_long <- new_data %>%
  pivot_longer(cols = starts_with("HS"), names_to = "Household_Size", values_to = "Proportion")

# Plot smoothed dot plot
# Plot smoothed dot plot with smaller points, confidence interval band, and color scale
ggplot(new_data_long, aes(x = T1, y = Proportion, color = Household_Size)) +
  geom_point(size = 1, alpha = 0.5) +
  geom_smooth(method = "loess", se = TRUE, span = 0.85, aes(fill = Household_Size), alpha = 0.1) +
  scale_x_continuous(breaks = seq(1960, 2030, by= 10))+
  labs(x = NULL,
       y = "Value") +
  #title = "Smoothed Dot Plot of Household Sizes Over Time in LATIN-AMERICA (IPUMS)",
  #subtitle = "Your subtitle here",
  #(caption = "gio kurtanidze") +
  facet_wrap(~C4) +
  theme_minimal() +
  theme(legend.direction = "horizontal",
        plot.background = element_rect(fill = "white"),# Display legend items in a horizontal line
        legend.position = "bottom") +  # Position the legend at the bottom +
  guides(colour = guide_legend(nrow = 1))
