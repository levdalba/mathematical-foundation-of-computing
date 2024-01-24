world <- read_sf(".", "world")

st_crs(world)

world <- st_transform(world, 3857)

world <- world |>
  select(iso_n3, name,pop_est, gdp_md_est, continent, geometry)

ggplot(world) +
  geom_sf()

births <- read_csv("births.csv")
births$iso_n3 <- sprintf("%.3d", births$iso_n3)

combined_data <- merge(world, births, all = TRUE)
combined_data$Births[is.na(combined_data$Births)] <- 100
combined_data$gdp_md_est[is.na(combined_data$gdp_md_est)] <- 10


library(cartogram)

combined_data_births <- cartogram_cont(combined_data |> drop_na(),
                                       weight = "Births",itermax = 7)


combined_data_pop_est <- cartogram_cont(combined_data |> drop_na(),
                                        weight = "pop_est",itermax = 7)

combined_data_gdp_md_est <- cartogram_cont(combined_data |> drop_na(),
                                           weight = "gdp_md_est",itermax = 7)

world <- combined_data |> drop_na()


births_ <- combined_data_births |> select(continent, geometry) |>
  mutate(GROUP = "Births")

gdp_md_est_ <- combined_data_gdp_md_est |> select(continent, geometry) |>
  mutate(GROUP = "GDP")

pop_est_ <- combined_data_pop_est |> select(continent, geometry) |>
  mutate(GROUP = "Population")

world_ <- world |> select(continent, geometry) |>
  mutate(GROUP = "World")

data <- rbind(births_, gdp_md_est_, pop_est_, world_)

tableau_20 <- c("#3F88C5", "#F29F83", "#E18A90", "#86C0B3", "#6CB07E",
                "#EAC54F", "#C492B1", "#FFB7BD", "#B2978F", "#D0C4C4",
                "#FF7832", "#2DC897", "#FF8FA3", "#A98D6E", "#CFD9C3",
                "#A6A6A6", "#D3B7E8", "#E3E3E3", "#C6C6C6", "#ECECEC")


tableau_20[1:5]

theme_snow<-list(theme(plot.title = element_text(lineheight=1, size=22, face="bold",hjust = 0.5),
                       plot.subtitle = element_text(lineheight=1, size=8, face="bold",hjust = 0.5),
                       plot.caption = element_text(lineheight=1, size=15, hjust=0.5),
                       legend.title = element_blank (),
                       legend.text = element_text(colour="black", size = 13),
                       legend.position="bottom",
                       legend.background = element_rect(fill=NA, colour = NA),
                       legend.key.size = unit(1, 'lines'),
                       legend.key = element_rect(colour = NA, fill = NA),
                       axis.title.x = element_blank (),
                       axis.text.x  = element_blank (),
                       axis.title.y =  element_blank (),
                       axis.text.y  = element_blank (),
                       axis.ticks= element_blank (),
                       strip.text = element_text(size=15, face="bold",margin = margin(.1,0,.1,0, "cm")),
                       plot.background =  element_rect(fill = "white"),
                       panel.grid.major=element_line(colour="white",linewidth=.5),
                       panel.grid.minor=element_line(colour="white",linewidth=.15),
                       panel.border = element_rect(colour = "white", fill=NA, linewidth=.75),
                       panel.background =element_rect(fill ="#FFFFFF", colour = "#FFFFFF")))


ggplot() +
  geom_sf(data=world,
          fill="#BFBFBF",
          colour= "#BFBFBF")+
  geom_sf(data= data, # sf_object we want to plot
          aes(fill = continent), # variable to fill the polygons
          colour = "Black", #color of the border line
          size=.025)+
  scale_fill_manual(name="", # Name of the legend
                    values=tableau_20[1:6],
                    guide = guide_legend(direction = "horizontal",
                                         nrow = 1,
                                         keywidth=6,
                                         label.position = "bottom"))+ # color to use for plotting
  facet_wrap(~GROUP)+
  labs(x="",               # x-axis title
       y="",                    # y-axis title
       title="Cartograms: Births, GDP, and Population",    # title of the plot
       caption="\nLevan Dalbashvili | Harbour Space") +
  #theme_minimal()+ # theme for plotting
  theme(plot.title = element_text(lineheight=1, size=15, face="bold"),
        plot.caption = element_text(lineheight=1, size=8),
        legend.position="bottom",        
        legend.title = element_blank(),
        panel.background = element_rect(fill = "white", color  =  "white"),
        plot.background = element_rect(fill ="white", color  = "white"),
        panel.grid.major = element_line(color = "gray",
                                        linewidth = 0.15,
                                        linetype = 2)) +
  theme_light() +
  theme(legend.position = "bottom",
        legend.key.width = unit(5, "cm"))

