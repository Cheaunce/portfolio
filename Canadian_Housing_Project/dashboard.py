"""
Rent vs. Crime Severity Dashboard
----------------------------------
Interactive companion to notebooks 01-04. Reads the same processed CSVs
those notebooks produce, without recomputing anything.

Styled to match notebooks 04/05 -- foam (#55d5ec) and
love (#f56761) as the two accent colors, matching ../styles/chance.mplstyle,
and the same dark background palette.

Run from the project root using:
    streamlit run dashboard.py
"""

import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st

st.set_page_config(page_title="Canadian Rent vs. Crime Severity", layout="centered")

# matching chance.mplstyle
BG = "#191724"
GRID = "#26233a"
TEXT = "#e0def4"
FOAM = "#55d5ec"
LOVE = "#f56761"

PLOTLY_TEMPLATE = go.layout.Template(
    layout=go.Layout(
        paper_bgcolor=BG,
        plot_bgcolor=BG,
        font=dict(color=TEXT),
        xaxis=dict(gridcolor=GRID, zerolinecolor=GRID),
        yaxis=dict(gridcolor=GRID, zerolinecolor=GRID),
        legend=dict(bgcolor=BG),
    )
)

# make Streamlit's own chrome match the dark theme, not just the charts
st.markdown(
    f"""
    <style>
    .stApp {{ background-color: {BG}; color: {TEXT}; }}
    </style>
    """,
    unsafe_allow_html=True,
)


# ----------------------------------------------------------------------
# Load data (cached so it doesn't re-read the CSV on every widget click)
# ----------------------------------------------------------------------
@st.cache_data
def load_data():
    df = pd.read_csv("data/processed/housing_csi_merged_2020_2024.csv")
    per_centre_corr = pd.read_csv("data/processed/per_centre_corr_2020_2024.csv")
    return df, per_centre_corr


df, per_centre_corr = load_data()

CSI_METRICS = {
    "Overall crime severity": "csi_total",
    "Violent crime severity": "csi_violent",
    "Non-violent crime severity": "csi_nonviolent",
    "Weighted clearance rate": "clearance_rate",
}

st.title("Canadian Rent vs. Crime Severity, 2020-2024")
st.caption(
    "Rental data from CMHC's Rental Market Survey; crime data from StatCan's "
    "Crime Severity Index (table 35-10-0026-01), 17 Census Metropolitan Areas."
)

# ----------------------------------------------------------------------
# Sidebar controls
# ----------------------------------------------------------------------
st.sidebar.header("Filters")

all_cities = sorted(df["centre"].unique())
selected_city = st.sidebar.selectbox(
    "Focus city (for the trend and detail views below)",
    options=["All cities"] + all_cities,
)

selected_year = st.sidebar.select_slider(
    "Year (for the cross-city comparison)",
    options=sorted(df["year"].unique()),
    value=df["year"].max(),
)

csi_label = st.sidebar.selectbox("Crime metric", options=list(CSI_METRICS.keys()))
csi_col = CSI_METRICS[csi_label]

st.sidebar.markdown("---")
st.sidebar.caption(
    "Reads the merged dataset already produced: "
    "`housing_csi_merged_2020_2024.csv`."
)


# ----------------------------------------------------------------------
# Row 1: National trend (or single-city trend if one is selected)
# ----------------------------------------------------------------------
st.subheader("Rent vs. crime severity over time")

if selected_city == "All cities":
    trend_df = df.groupby("year")[["rent_rms", csi_col]].mean().reset_index()
    trend_title = "National average"
else:
    trend_df = df[df["centre"] == selected_city][["year", "rent_rms", csi_col]]
    trend_title = selected_city

fig_trend = go.Figure()
fig_trend.add_trace(
    go.Scatter(
        x=trend_df["year"], y=trend_df["rent_rms"],
        name="Avg. rent ($)", yaxis="y1", mode="lines+markers",
        line=dict(color=FOAM), marker=dict(color=FOAM),
    )
)
fig_trend.add_trace(
    go.Scatter(
        x=trend_df["year"], y=trend_df[csi_col],
        name=csi_label, yaxis="y2", mode="lines+markers",
        line=dict(color=LOVE), marker=dict(color=LOVE),
    )
)
fig_trend.update_layout(
    template=PLOTLY_TEMPLATE,
    title=f"{trend_title}: rent vs. {csi_label.lower()}",
    xaxis=dict(title="Year", dtick=1),
    yaxis=dict(title="Average rent ($)", side="left"),
    yaxis2=dict(title=csi_label, overlaying="y", side="right", gridcolor=GRID),
    legend=dict(orientation="h", yanchor="bottom", y=1.02, x=0),
    height=420,
)
st.plotly_chart(fig_trend, use_container_width=True)


# ----------------------------------------------------------------------
# Row 2: Cross-city comparison for the selected year
# ----------------------------------------------------------------------
st.subheader(f"Cities compared, {selected_year}")

year_df = df[df["year"] == selected_year].copy()
year_df["highlight"] = year_df["centre"] == selected_city

fig_scatter = px.scatter(
    year_df,
    x=csi_col,
    y="rent_rms",
    color="highlight",
    color_discrete_map={True: FOAM, False: LOVE},
    hover_name="centre",
    labels={csi_col: csi_label, "rent_rms": "Average rent ($)"},
    text=year_df["centre"].str.replace(" CMA", "", regex=False),
)
fig_scatter.update_traces(textposition="top center", showlegend=False)
fig_scatter.update_layout(template=PLOTLY_TEMPLATE, height=500)
st.plotly_chart(fig_scatter, use_container_width=True)


# ----------------------------------------------------------------------
# Row 3: Within-city correlation, all cities, selected one highlighted
# ----------------------------------------------------------------------
st.subheader("Within-city correlation: rent vs. overall crime severity (2020-2024)")

corr_df = per_centre_corr.copy()
corr_df = corr_df.sort_values("rent_csi_correlation")
# color by sign (matches notebook 4: pine = negative, rose = positive),
# selected city gets full opacity, everyone else fades back
corr_df["color"] = corr_df["rent_csi_correlation"].apply(lambda v: LOVE if v < 0 else FOAM)
corr_df["opacity"] = corr_df["centre"].apply(lambda c: 1.0 if c == selected_city else 0.45)

fig_corr = go.Figure(
    go.Bar(
        x=corr_df["rent_csi_correlation"],
        y=corr_df["centre"],
        orientation="h",
        marker=dict(color=corr_df["color"], opacity=corr_df["opacity"]),
    )
)
fig_corr.update_layout(
    template=PLOTLY_TEMPLATE,
    xaxis_title="Correlation (rent vs. csi_total)",
    height=550,
    showlegend=False,
)
fig_corr.add_vline(x=0, line_width=1, line_color=TEXT)
st.plotly_chart(fig_corr, use_container_width=True)

st.caption(
    "Each bar uses only that city's own 5 yearly values. Correlations are "
    "fragile with this few points. Treat them as a starting point for "
    "further digging, not a firm conclusion."
)
