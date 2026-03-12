import sqlite3
import pandas as pd
import streamlit as st

st.set_page_config(
    page_title="Food Delivery Analytics",
    layout="wide",
    initial_sidebar_state="collapsed"
)

@st.cache_data(ttl=300)
def load_data(db_path: str = "food_data.db") -> pd.DataFrame:
    """Mengambil data restoran dari database SQLite."""
    try:
        with sqlite3.connect(db_path) as conn:
            query = """
                SELECT name, rating, link, scraped_at 
                FROM restaurants 
                ORDER BY scraped_at DESC
            """
            df = pd.read_sql(query, conn)
        return df
    except sqlite3.Error as e:
        st.error(f"Database connection failed: {e}")
        return pd.DataFrame()

def render_metrics(df: pd.DataFrame) -> None:
    """Merender metrik KPI di bagian atas dashboard."""
    df_valid_rating = df[df['rating'] > 0]
    avg_rating = df_valid_rating['rating'].mean() if not df_valid_rating.empty else 0.0
    latest_scrape = df['scraped_at'].max().split()[0] if not df.empty else "N/A"

    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Total Restaurants Scraped", len(df))
    with col2:
        st.metric("Average Rating (Valid)", f"{avg_rating:.2f}")
    with col3:
        st.metric("Latest Data Update", latest_scrape)

def render_export_button(df: pd.DataFrame) -> None:
    """Menyediakan tombol unduh CSV."""
    csv = df.to_csv(index=False).encode('utf-8')
    st.download_button(
        label="Export Data to CSV",
        data=csv,
        file_name='restaurant_data_export.csv',
        mime='text/csv',
        use_container_width=True
    )

def main() -> None:
    """Fungsi orkestrator utama untuk merender dashboard."""
    st.title("Food Delivery Data Analytics")
    st.markdown("Real-time monitoring dashboard for restaurant data extraction pipeline.")
    st.divider()

    df = load_data()

    if df.empty:
        st.warning("No data available. Please run the scraping pipeline (main.py) first.")
        return

    render_metrics(df)
    st.divider()

    col_table, col_chart = st.columns([1.2, 1], gap="large")

    with col_table:
        st.subheader("Raw Data Overview")
        st.dataframe(
            df, 
            use_container_width=True, 
            height=400,
            hide_index=True
        )
        render_export_button(df)

    with col_chart:
        st.subheader("Rating Distribution (Valid Ratings)")
        df_valid = df[df['rating'] > 0].head(25)
        
        if not df_valid.empty:
            st.bar_chart(
                data=df_valid.set_index('name')['rating'],
                height=400
            )
        else:
            st.info("Not enough rated restaurants to display the chart.")

if __name__ == "__main__":
    main()