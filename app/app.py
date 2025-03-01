from shiny import App, ui, render
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Define UI
app_ui = ui.page_fluid(
    ui.h1("My Shiny Python App"),
    ui.layout_sidebar(
        ui.panel_sidebar(
            ui.input_slider("n", "N", 0, 100, 20),
            ui.input_select(
                "dataset", "Dataset", choices=["Dataset 1", "Dataset 2", "Dataset 3"]
            ),
            ui.input_checkbox_group(
                "options", "Options", choices=["Option 1", "Option 2", "Option 3"]
            ),
        ),
        ui.panel_main(ui.output_plot("plot"), ui.output_table("table")),
    ),
)


# Define server
def server(input, output, session):
    @render.plot
    def plot():
        np.random.seed(input.n())
        data = np.random.randn(input.n())
        fig, ax = plt.subplots()
        ax.hist(data, bins=15)
        ax.set_title(f"Selected: {input.dataset()}")
        return fig

    @render.table
    def table():
        np.random.seed(input.n())
        data = np.random.randn(min(10, input.n()), 4)
        return pd.DataFrame(data, columns=["A", "B", "C", "D"])


# Create app
app = App(app_ui, server)
